"""Gedächtnis-Engine für die Lernprojekte des Hub.

Verallgemeinerter SM-2-Scheduler. Intervalle und Fälligkeit sind reine
Arithmetik und werden bewusst in Python gerechnet, nicht vom Sprachmodell.

Karten liegen als JSON je Projekt unter `04_gedaechtnis/karten/<projekt>.json`.
Jede Karte trägt `id`, `projekt`, `abschnitt` (Abschnitt des Lesepfads oder
Modulblock, etwa XY2-K00 für Modul XY2, Kern-Abschnitt 00), `typ` (Begriff, Anwendung, Rechnung), `frage`,
`antwort`, `quelle` (Werk und Kapitel aus der Bibliothek), `gesperrt`,
`freigeschaltet` und den `lernzustand`. Eine Karte ohne Quelle wird nicht
angelegt, weil Karten ihr Werk und Kapitel nennen müssen.

Eine Karte hat drei Zustände wie in einem Karteikasten:

- gesperrt: angelegt, der Stoff ist noch nicht gelesen. Sie erscheint nie.
  Freigeschaltet wird je Abschnitt, sobald der Abschnitt gelesen ist. Abruf
  auf ungelesenem Stoff misst nichts.
- bereit: freigeschaltet, aber nie abgerufen. Der Vorrat, aus dem der Zufluss
  neuer Karten schöpft. Er ist kein Rückstand.
- im Kasten: mindestens einmal abgerufen. SM-2 schiebt die Karte mit jeder
  richtigen Antwort ein Fach weiter nach hinten, eine falsche Antwort holt sie
  ins erste Fach zurück. Ab `SITZT_AB_TAGEN` Intervall gilt sie als sitzend.

Zu jedem Abruf lässt sich die Zuversicht vor der Antwort (0 bis 100 Prozent)
festhalten. Der Vergleich von Zuversicht und Ergebnis zeigt, wie gut das
eigene Wissen eingeschätzt wird (Brown, Roediger, McDaniel, Make It Stick,
Kap. 5).

Aufruf (aus dem Hub):
    python 04_gedaechtnis/engine.py add --projekt P --abschnitt A --typ T --frage F
                                        --antwort A --quelle Q [--id ID] [--schwer] [--frei]
    python 04_gedaechtnis/engine.py freischalten ABSCHNITT
    python 04_gedaechtnis/engine.py due    [--projekt P] [--limit N]
    python 04_gedaechtnis/engine.py neu    [--projekt P] [--limit N]
    python 04_gedaechtnis/engine.py zeige  ID ...
    python 04_gedaechtnis/engine.py review ID:Q[:Z] ...      Q 0 bis 5, Z 0 bis 100
    python 04_gedaechtnis/engine.py stats
    python 04_gedaechtnis/engine.py zahl                     fällige Karten insgesamt
"""
import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path

WURZEL = Path(__file__).resolve().parent
KARTEN = WURZEL / "karten"

TYPEN = ("Begriff", "Anwendung", "Rechnung")

EF_START = 2.5
# Karten, die erwartbar verwechselt werden, starten mit engeren Intervallen.
EF_START_SCHWER = 2.1
EF_MIN = 1.3

# Ab diesem Verhältnis (vergangene Tage zu geplantem Intervall) gilt eine Karte
# als verspätet: richtig beantwortet, aber das Intervall wächst nur von einer
# gekürzten Basis.
VERSPAETUNG_AB = 2.0

# Drei Wochen Intervall gelten als gefestigt. Setzung, siehe methodik.md.
SITZT_AB_TAGEN = 21


def laden(pfad):
    # utf-8-sig verdaut ein BOM aus Dateien, die unter Windows entstanden sind
    with open(pfad, encoding="utf-8-sig") as fh:
        return json.load(fh)


def speichern(pfad, obj):
    pfad.parent.mkdir(parents=True, exist_ok=True)
    with open(pfad, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


def tage_seit_letzter(zustand, heute):
    """Tage seit der letzten Wiederholung, None wenn nie abgerufen."""
    letzte = zustand.get("last_reviewed")
    if not letzte and zustand.get("review_history"):
        letzte = zustand["review_history"][-1].get("date")
    if not letzte:
        return None
    return (heute - date.fromisoformat(letzte)).days


def neuer_zustand(schwer=False):
    return {
        "easiness_factor": EF_START_SCHWER if schwer else EF_START,
        "repetitions": 0,
        "interval_days": 0,
        "last_reviewed": None,
        "due_date": None,
        "review_history": [],
    }


def sm2_step(zustand, qualitaet, heute=None, zuversicht=None):
    """Ein SM-2-Schritt auf dem Lernzustand. Gibt den Zustand zurück.

    qualitaet: 0 = falsch bis 5 = perfekt. Ab 3 gilt die Antwort als richtig.

    Abweichung vom Lehrbuch-SM-2: Standard rechnet, als wäre jede Karte
    pünktlich gekommen. Eine Karte, die nach 40 Tagen statt nach 15
    beantwortet wird, ist aber nicht so sicher wie eine pünktliche. Ist sie
    mehr als doppelt so spät (VERSPAETUNG_AB), wächst das Intervall deshalb
    nur von einer gekürzten Basis: basis = geplant * VERSPAETUNG_AB / verhältnis.
    """
    if not 0 <= qualitaet <= 5:
        raise ValueError("Qualität muss zwischen 0 und 5 liegen")
    if zuversicht is not None and not 0 <= zuversicht <= 100:
        raise ValueError("Zuversicht muss zwischen 0 und 100 liegen")
    heute = heute or date.today()
    ef = zustand.get("easiness_factor", EF_START)
    reps = zustand.get("repetitions", 0)
    intervall = zustand.get("interval_days", 0)
    vergangen = tage_seit_letzter(zustand, heute)

    ef = ef + (0.1 - (5 - qualitaet) * (0.08 + (5 - qualitaet) * 0.02))
    ef = max(EF_MIN, round(ef, 4))

    if qualitaet < 3:
        reps = 0
        intervall = 1
    else:
        reps += 1
        if reps == 1:
            intervall = 1
        elif reps == 2:
            intervall = 6
        else:
            basis = intervall
            if vergangen and intervall and vergangen / intervall > VERSPAETUNG_AB:
                basis = max(1, intervall * VERSPAETUNG_AB / (vergangen / intervall))
            intervall = max(1, int(round(basis * ef)))

    eintrag = {"date": heute.isoformat(), "quality": qualitaet,
               "interval": intervall, "vergangen": vergangen}
    if zuversicht is not None:
        eintrag["zuversicht"] = zuversicht

    zustand["easiness_factor"] = ef
    zustand["repetitions"] = reps
    zustand["interval_days"] = intervall
    zustand["last_reviewed"] = heute.isoformat()
    zustand["due_date"] = (heute + timedelta(days=intervall)).isoformat()
    zustand.setdefault("review_history", []).append(eintrag)
    return zustand


def zustand(karte):
    """gesperrt, bereit oder im_kasten."""
    if karte["gesperrt"]:
        return "gesperrt"
    z = karte["lernzustand"]
    if not z.get("review_history") and z.get("repetitions", 0) == 0:
        return "bereit"
    return "im_kasten"


def ist_neu(karte):
    """Neu heißt freigeschaltet und nie abgerufen. Eine einmal verfehlte Karte ist bekannt."""
    return zustand(karte) == "bereit"


def ist_faellig(karte, heute=None):
    if zustand(karte) != "im_kasten":
        return False
    heute = heute or date.today()
    return date.fromisoformat(karte["lernzustand"]["due_date"]) <= heute


def sitzt(karte):
    return zustand(karte) == "im_kasten" and karte["lernzustand"]["interval_days"] >= SITZT_AB_TAGEN


def alle_karten(ordner=None):
    """Alle Karten aller Projekte als Liste von (Projekt, Karte)."""
    out = []
    for pfad in sorted(Path(ordner or KARTEN).glob("*.json")):
        for karte in laden(pfad)["karten"]:
            out.append((pfad.stem, karte))
    return out


def faellige(ordner=None, projekt=None, heute=None, limit=None):
    """Fällige Karten über alle Projekte, die am längsten überfälligen zuerst."""
    heute = heute or date.today()
    treffer = [k for p, k in alle_karten(ordner)
               if (projekt is None or p == projekt) and ist_faellig(k, heute)]
    treffer.sort(key=lambda k: (k["lernzustand"]["due_date"], k["id"]))
    return treffer[:limit] if limit else treffer


def neue(ordner=None, projekt=None, limit=None):
    """Bereite Karten in Reihenfolge des Lesepfads (Abschnitt, dann Anlage)."""
    treffer = [k for p, k in alle_karten(ordner)
               if (projekt is None or p == projekt) and ist_neu(k)]
    treffer.sort(key=lambda k: k["abschnitt"])     # stabil, Anlagereihenfolge bleibt
    return treffer[:limit] if limit else treffer


def anlegen(ordner, projekt, abschnitt, typ, frage, antwort, quelle,
            karten_id=None, schwer=False, frei=False, heute=None):
    if typ not in TYPEN:
        raise ValueError(f"Typ muss einer von {', '.join(TYPEN)} sein")
    if not re.fullmatch(r"[a-z0-9_]+", projekt or ""):
        raise ValueError("Projekt darf nur a bis z, Ziffern und Unterstrich enthalten")
    for name, wert in (("abschnitt", abschnitt), ("frage", frage),
                       ("antwort", antwort), ("quelle", quelle)):
        if not wert or not wert.strip():
            raise ValueError(f"{name} darf nicht leer sein")
    pfad = Path(ordner) / f"{projekt}.json"
    datei = laden(pfad) if pfad.exists() else {"projekt": projekt, "karten": []}
    vorhandene = {k["id"] for _, k in alle_karten(ordner)}
    if karten_id is None:
        nummer = len(datei["karten"]) + 1
        karten_id = f"{projekt}-{nummer:03d}"
        while karten_id in vorhandene:
            nummer += 1
            karten_id = f"{projekt}-{nummer:03d}"
    elif karten_id in vorhandene:
        raise ValueError(f"id {karten_id} gibt es schon")
    heute = heute or date.today()
    karte = {"id": karten_id, "projekt": projekt, "abschnitt": abschnitt.strip(),
             "typ": typ, "frage": frage.strip(), "antwort": antwort.strip(),
             "quelle": quelle.strip(), "gesperrt": not frei,
             "freigeschaltet": heute.isoformat() if frei else None,
             "lernzustand": neuer_zustand(schwer)}
    datei["karten"].append(karte)
    speichern(pfad, datei)
    return karte


def _dateien(ordner):
    ordner = Path(ordner or KARTEN)
    return ordner, {p.stem: laden(p) for p in sorted(ordner.glob("*.json"))}


def freischalten(ordner, abschnitt, heute=None):
    """Schaltet alle gesperrten Karten eines Abschnitts frei. Gibt deren ids zurück."""
    heute = heute or date.today()
    ordner, dateien = _dateien(ordner)
    frei = []
    for name, datei in dateien.items():
        geaendert = False
        for k in datei["karten"]:
            if k["abschnitt"] == abschnitt and k["gesperrt"]:
                k["gesperrt"] = False
                k["freigeschaltet"] = heute.isoformat()
                frei.append(k["id"])
                geaendert = True
        if geaendert:
            speichern(ordner / f"{name}.json", datei)
    return frei


def bewerten(ordner, paare, heute=None):
    """Mehrere Karten bewerten. Paare sind (id, qualität) oder (id, qualität, zuversicht).

    Unbekannte und gesperrte ids brechen ab, bevor etwas geschrieben wird.
    """
    ordner, dateien = _dateien(ordner)
    index = {k["id"]: k for d in dateien.values() for k in d["karten"]}
    unbekannt = [p[0] for p in paare if p[0] not in index]
    if unbekannt:
        raise KeyError(f"Unbekannte Karten-ids: {unbekannt}")
    gesperrt = [p[0] for p in paare if index[p[0]]["gesperrt"]]
    if gesperrt:
        raise ValueError(f"Gesperrte Karten lassen sich nicht bewerten: {gesperrt}")
    for p in paare:
        zuversicht = p[2] if len(p) > 2 else None
        sm2_step(index[p[0]]["lernzustand"], int(p[1]), heute, zuversicht)
    for name, datei in dateien.items():
        speichern(ordner / f"{name}.json", datei)
    return [index[p[0]] for p in paare]


def zeigen(ordner, ids):
    index = {k["id"]: k for _, k in alle_karten(ordner)}
    unbekannt = [i for i in ids if i not in index]
    if unbekannt:
        raise KeyError(f"Unbekannte Karten-ids: {unbekannt}")
    return [index[i] for i in ids]


def statistik(ordner=None, heute=None):
    heute = heute or date.today()
    je_projekt = {}
    for projekt, karte in alle_karten(ordner):
        s = je_projekt.setdefault(projekt, {"gesamt": 0, "gesperrt": 0, "bereit": 0,
                                            "im_kasten": 0, "faellig": 0, "sitzt": 0})
        s["gesamt"] += 1
        s[zustand(karte)] += 1
        s["faellig"] += ist_faellig(karte, heute)
        s["sitzt"] += sitzt(karte)
    return je_projekt


def zahl_faellig(ordner=None, heute=None):
    return sum(s["faellig"] for s in statistik(ordner, heute).values())


def _opt(args, name, default=None):
    return args[args.index(name) + 1] if name in args else default


def main(argv=None):
    args = list(sys.argv[1:] if argv is None else argv)
    if not args:
        print(__doc__)
        return 1
    cmd, rest = args[0], args[1:]
    try:
        if cmd == "add":
            karte = anlegen(KARTEN, _opt(rest, "--projekt", ""), _opt(rest, "--abschnitt", ""),
                            _opt(rest, "--typ", ""), _opt(rest, "--frage", ""),
                            _opt(rest, "--antwort", ""), _opt(rest, "--quelle", ""),
                            _opt(rest, "--id"), "--schwer" in rest, "--frei" in rest)
            print(json.dumps(karte, ensure_ascii=False, indent=2))
        elif cmd == "freischalten":
            frei = freischalten(KARTEN, rest[0])
            print(f"{rest[0]}: {len(frei)} Karten freigeschaltet")
        elif cmd in ("due", "neu"):
            lim = _opt(rest, "--limit")
            lim = int(lim) if lim else None
            projekt = _opt(rest, "--projekt")
            karten = (faellige(KARTEN, projekt, limit=lim) if cmd == "due"
                      else neue(KARTEN, projekt, limit=lim))
            print(json.dumps(karten, ensure_ascii=False, indent=2))
        elif cmd == "zeige":
            print(json.dumps(zeigen(KARTEN, rest), ensure_ascii=False, indent=2))
        elif cmd == "review":
            paare = []
            for a in rest:
                teile = a.split(":")
                paare.append((teile[0], int(teile[1])) + ((int(teile[2]),) if len(teile) > 2 else ()))
            for k in bewerten(KARTEN, paare):
                z = k["lernzustand"]
                print(f"{k['id']}: nächste Wiederholung {z['due_date']} "
                      f"(+{z['interval_days']}d, EF {z['easiness_factor']})")
        elif cmd == "stats":
            print(json.dumps(statistik(), ensure_ascii=False, indent=2))
        elif cmd == "zahl":
            print(zahl_faellig())
        else:
            print(__doc__)
            return 1
    except (ValueError, KeyError, IndexError) as fehler:
        print(f"Fehler: {fehler}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
