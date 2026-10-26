"""Lernlage der Woche für `/weekly-review`: Ist-Minuten, Abrufquote, Rückstau, nächster Abschnitt.

Reine Rechnung, das Modell rechnet nichts nach. Alle Zahlen sind Stand, kein
Soll-Ist-Vorwurf (Grundsatz 5 in `01_kompass/lerngrundsaetze.md`,
kein Schuldaufbau).

Quellen
- Ist-Minuten Deep Dive: Spalte Minuten der `lernlog.md` aller Lernprojekte
  unter `03_projekte/`. Wiederholung läuft über `/heute` und hat kein Zeitlog,
  ihre Minuten sind aus den Abrufen geschätzt (`heute.KOSTEN`).
- Budget: `lernen.deep_dive_h_woche` in `00_kern/einstellungen.json`, ohne
  Eintrag 5 Stunden.
- Abrufquote: Anteil richtiger Antworten (Note ab 3) an Abrufen im Fenster.
  Der erste Kontakt einer Karte zählt nicht, er wird großzügig bewertet und
  misst nichts (siehe `/heute`).
- Rückstau: Zeit der heute fälligen Karten gegen das Standardtagesbudget.
  Der Verlauf braucht Messpunkte, `--merken` schreibt einen in `rueckstau.json`.
- Nächster Abschnitt: erster Abschnitt in Lesepfad-Reihenfolge mit gesperrten Karten.

Aufruf (aus dem Hub):
    python 04_gedaechtnis/wochenlage.py [--tage N] [--merken]
"""
import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))
import engine  # noqa: E402
import heute as tagesplan  # noqa: E402

HUB = HIER.parent
PROJEKTE = HUB / "03_projekte"
VERLAUF = HIER / "rueckstau.json"

VORGABE_DEEP_DIVE_H = 5        # Wochenbudget Deep Dive, falls die Einstellungen keins nennen
KORRIDOR = (0.60, 0.70)        # Zielkorridor Trefferquote, Setzung, siehe methodik.md
MESSABSTAND_TAGE = 6           # Rückstau-Trend gegen einen Messpunkt dieses Alters


def _datum(text):
    text = text.strip()
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", text):
        return date.fromisoformat(text)
    m = re.fullmatch(r"(\d{1,2})\.(\d{1,2})\.(\d{4})", text)
    return date(int(m[3]), int(m[2]), int(m[1])) if m else None


def lernlog_minuten(pfad):
    """(Datum, Minuten) je Zeile einer lernlog.md. Zeilen ohne lesbares Datum oder ohne Zahl fallen weg."""
    zeilen = Path(pfad).read_text(encoding="utf-8").splitlines()
    spalten, out = None, []
    for z in zeilen:
        if not z.strip().startswith("|"):
            continue
        zellen = [c.strip() for c in z.strip().strip("|").split("|")]
        if spalten is None:
            if "Datum" in zellen and "Minuten" in zellen:
                spalten = (zellen.index("Datum"), zellen.index("Minuten"))
            continue
        d_i, m_i = spalten
        if len(zellen) <= max(d_i, m_i):
            continue
        d, m = _datum(zellen[d_i]), zellen[m_i]
        if d and m.isdigit():
            out.append((d, int(m)))
    return out


def deep_dive_min(daten=None):
    """Wochenbudget Deep Dive in Minuten aus den Einstellungen."""
    try:
        stunden = float(tagesplan.lernen(daten).get("deep_dive_h_woche") or VORGABE_DEEP_DIVE_H)
    except (TypeError, ValueError):
        stunden = VORGABE_DEEP_DIVE_H
    return int(round(stunden * 60))


def ist_minuten(projekte=PROJEKTE, heute=None, tage=7):
    """Minuten Deep Dive im Fenster, gesamt und je Projekt."""
    heute = heute or date.today()
    ab = heute - timedelta(days=tage - 1)
    je_projekt = {}
    for lernlog in sorted(Path(projekte).glob("*/lernlog.md")):
        zeilen = lernlog_minuten(lernlog)
        je_projekt[lernlog.parent.name] = sum(m for d, m in zeilen if ab <= d <= heute)
    return {"fenster_tage": tage, "ab": ab.isoformat(), "bis": heute.isoformat(),
            "minuten": sum(je_projekt.values()), "je_projekt": je_projekt}


def abrufe(ordner=None, heute=None, tage=7):
    """Abrufe im Fenster ohne den ersten Kontakt einer Karte. Gibt (Note, Zuversicht, Kostenklasse) zurück."""
    heute = heute or date.today()
    ab = heute - timedelta(days=tage - 1)
    out = []
    for _, karte in engine.alle_karten(ordner):
        for i, e in enumerate(karte["lernzustand"].get("review_history", [])):
            if i == 0:
                continue
            if ab <= date.fromisoformat(e["date"]) <= heute:
                out.append((e["quality"], e.get("zuversicht"), karte["typ"]))
    return out


def abrufquote(ordner=None, heute=None, tage=7):
    a = abrufe(ordner, heute, tage)
    richtig = sum(1 for q, _, _ in a if q >= 3)
    quote = richtig / len(a) if a else None
    mit_z = [(q, z) for q, z, _ in a if z is not None]
    kalibrierung = None
    if len(mit_z) >= 5:
        kalibrierung = {"zuversicht": round(sum(z for _, z in mit_z) / len(mit_z), 1),
                        "trefferquote": round(100 * sum(1 for q, _ in mit_z if q >= 3) / len(mit_z), 1),
                        "karten": len(mit_z)}
    if quote is None:
        lage = "keine Abrufe"
    elif quote < KORRIDOR[0]:
        lage = "unter dem Korridor"
    elif quote > KORRIDOR[1]:
        lage = "über dem Korridor"
    else:
        lage = "im Korridor"
    return {"abrufe": len(a), "richtig": richtig,
            "quote_prozent": None if quote is None else round(100 * quote, 1),
            "lage": lage, "kalibrierung": kalibrierung,
            "wiederholung_min_geschaetzt": round(sum(tagesplan.KOSTEN[t] for _, _, t in a) / 60, 1)}


def rueckstau(ordner=None, heute=None, verlauf=VERLAUF):
    """Last der fälligen Karten in Tagesbudgets, mit Trend gegen einen älteren Messpunkt."""
    heute = heute or date.today()
    faellig = engine.faellige(ordner, heute=heute)
    last = sum(tagesplan.kosten(k) for k in faellig)
    standard = tagesplan.STANDARD_MINUTEN * 60
    punkte = json.loads(Path(verlauf).read_text(encoding="utf-8")) if Path(verlauf).exists() else []
    alt = [p for p in punkte if (heute - date.fromisoformat(p["datum"])).days >= MESSABSTAND_TAGE]
    trend = None
    if alt:
        ref = alt[-1]
        diff = last - ref["last_sek"]
        trend = {"gegen": ref["datum"], "last_sek_vorher": ref["last_sek"],
                 "richtung": "waechst" if diff > 0 else "schrumpft" if diff < 0 else "gleich"}
    return {"faellig": len(faellig), "last_sek": last,
            "last_tagesbudgets": round(last / standard, 2),
            "bremse": last > tagesplan.STAU_FAKTOR * standard, "trend": trend}


def merken(ordner=None, heute=None, verlauf=VERLAUF):
    """Schreibt den Messpunkt des Tages (ein Punkt je Datum, ein zweiter Lauf überschreibt)."""
    heute = heute or date.today()
    punkt = {"datum": heute.isoformat(),
             "last_sek": rueckstau(ordner, heute, verlauf)["last_sek"]}
    punkte = json.loads(Path(verlauf).read_text(encoding="utf-8")) if Path(verlauf).exists() else []
    punkte = [p for p in punkte if p["datum"] != punkt["datum"]] + [punkt]
    Path(verlauf).write_text(json.dumps(punkte, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return punkt


def naechster_abschnitt(ordner=None):
    """Erster Abschnitt mit gesperrten Karten und die aktiven Abschnitte (kürzlich freigeschaltet)."""
    gesperrt = sorted({k["abschnitt"] for _, k in engine.alle_karten(ordner) if k["gesperrt"]})
    heute = date.today()
    aktiv = sorted({k["abschnitt"] for _, k in engine.alle_karten(ordner) if tagesplan.ist_aktiv(k, heute)})
    return {"naechster": gesperrt[0] if gesperrt else None, "aktiv": aktiv}


def lage(ordner=None, projekte=PROJEKTE, heute=None, tage=7, verlauf=VERLAUF):
    ist = ist_minuten(projekte, heute, tage)
    ist["budget_min"] = deep_dive_min() * tage // 7
    return {"ist_minuten": ist, "abrufquote": abrufquote(ordner, heute, tage),
            "rueckstau": rueckstau(ordner, heute, verlauf), "abschnitte": naechster_abschnitt(ordner)}


def main(argv=None):
    args = list(sys.argv[1:] if argv is None else argv)
    tage = 7
    if "--tage" in args:
        try:
            tage = int(args[args.index("--tage") + 1])
        except (IndexError, ValueError):
            print("Fehler: --tage braucht eine ganze Zahl", file=sys.stderr)
            return 1
    ergebnis = lage(tage=tage)
    if "--merken" in args:
        ergebnis["gemerkt"] = merken()
    print(json.dumps(ergebnis, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
