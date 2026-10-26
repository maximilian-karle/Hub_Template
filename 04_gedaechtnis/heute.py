"""Tagesbudget und Zufluss neuer Karten für die Lernprojekte des Hub.

Die tägliche Lernzeit (15 bis 30 Minuten) wird auf fällige Wiederholungen und
neue Karten verteilt. Der Standard kommt aus `lernen.wiederholung_min_tag` in
`00_kern/einstellungen.json`, ohne Eintrag 20 Minuten.

Regeln, in dieser Reihenfolge:

1. Wiederholung zuerst, über alle Projekte gemischt, die am längsten
   überfälligen voran. Jede Karte kostet Zeit je nach Typ (`KOSTEN`).
2. Neues füllt den Rest. Davon gehen `ANTEIL_AKTIV` an bereite Karten aus
   aktiven Abschnitten (in den letzten `AKTIV_TAGE` Tagen freigeschaltet), in
   Reihenfolge des Lesepfads, der Rest an zufällig gezogene bereite Karten aus
   dem übrigen Vorrat, damit Älteres nicht ewig liegt. Was ein Anteil nicht
   braucht, geht an den anderen.
3. Bremse. Ist die Wiederholungslast größer als `STAU_FAKTOR` Tagesbudgets,
   kommt nichts Neues, bis sie schrumpft.
4. Mindestzufluss. Unterhalb der Bremse kommen immer mindestens `MIN_NEU`
   Karten aus aktiven Abschnitten, auch wenn die Wiederholung die Zeit
   bräuchte. Kontinuität im laufenden Stoff geht vor Vollständigkeit beim
   alten.
5. Obergrenze. Mehr als `neu_max(budget)` neue Karten am Tag trägt der Kasten
   nicht, weil jede neue Karte in den ersten zwei Monaten rund
   `WIEDERHOLUNGEN_JE_NEUER` Wiederholungen nach sich zieht.
6. Der Minimalbetrieb (`--minimal`) ist ein Schalter für schlechte Tage:
   `MINIMAL_MINUTEN` Minuten, nur Wiederholung, nie neue Karten.

Was nicht in die Zeit passt, wird zurückgestellt. Es entsteht kein Rückstand
als Schuld, die Karten bleiben fällig und kommen als nächste dran.

Der Zufall ist je Tag fest (Startwert ist das Datum), damit ein zweiter Lauf am
selben Tag denselben Plan liefert.

Aufruf (aus dem Hub):
    python 04_gedaechtnis/heute.py [--minuten N] [--minimal]

Die Zeitkosten und Schwellen sind Annahmen, siehe `methodik.md`.
"""
import json
import random
import sys
from datetime import date
from pathlib import Path

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))
sys.path.insert(0, str(HIER.parent / "00_kern"))
import engine  # noqa: E402

try:
    import einstellungen  # noqa: E402
except ImportError:         # Hub ohne 00_kern, etwa in einer Kopie nur des Gedächtnisses
    einstellungen = None

MIN_MINUTEN = 15
MAX_MINUTEN = 30
MINIMAL_MINUTEN = 10
VORGABE_MINUTEN = 20


def lernen(daten=None):
    """Abschnitt `lernen` aus den Einstellungen, leer, wenn es keine gibt."""
    if daten is None:
        try:
            daten = einstellungen.laden() if einstellungen else {}
        except (OSError, ValueError):
            daten = {}
    return daten.get("lernen") or {}


def standard_minuten(daten=None):
    """Tagesbudget aus den Einstellungen, in die Spanne MIN bis MAX gezogen."""
    try:
        wert = int(lernen(daten).get("wiederholung_min_tag") or VORGABE_MINUTEN)
    except (TypeError, ValueError):
        wert = VORGABE_MINUTEN
    return min(MAX_MINUTEN, max(MIN_MINUTEN, wert))


STANDARD_MINUTEN = standard_minuten()

# Sekunden je Karte. Ein Begriff ist ein kurzer Abruf, Anwendung und Rechnung
# dauern länger, weil übertragen oder gerechnet wird.
KOSTEN = {"Begriff": 30, "Anwendung": 60, "Rechnung": 90}

ANTEIL_AKTIV = 0.7          # Vorrang für den laufenden Stoff
AKTIV_TAGE = 14
STAU_FAKTOR = 1.5           # Bremse ab anderthalb Tagesbudgets Wiederholung
MIN_NEU = 2
# Abrufe einer neuen Karte in den ersten zwei Monaten bei durchweg richtiger
# Antwort: Tag 1, 7, 22, 60 (Intervalle 1, 6, 15, 38).
WIEDERHOLUNGEN_JE_NEUER = 4


def kosten(karte):
    return KOSTEN[karte["typ"]]


def neu_max(budget_sek):
    """Neue Karten je Tag, deren Folgelast im Gleichgewicht ins Budget passt.

    n neue Karten kosten n * (1 + WIEDERHOLUNGEN_JE_NEUER) Begriffsabrufe am
    Tag, sobald der Kasten eingeschwungen ist.
    """
    return max(MIN_NEU, int(budget_sek // (KOSTEN["Begriff"] * (1 + WIEDERHOLUNGEN_JE_NEUER))))


def ist_aktiv(karte, heute):
    frei = karte.get("freigeschaltet")
    return bool(frei) and (heute - date.fromisoformat(frei)).days < AKTIV_TAGE


def _nehmen(karten, zeit, anzahl):
    """Karten der Reihe nach, solange Zeit und Anzahl reichen. Stoppt an der ersten, die nicht passt."""
    genommen, genutzt = [], 0
    for k in karten:
        if len(genommen) >= anzahl or genutzt + kosten(k) > zeit:
            break
        genommen.append(k)
        genutzt += kosten(k)
    return genommen, genutzt


def plan(minuten=None, minimal=False, ordner=None, heute=None):
    """Tagesplan als Dict. Reine Rechnung, schreibt nichts."""
    heute = heute or date.today()
    if minuten is None:
        minuten = STANDARD_MINUTEN
    if minimal:
        minuten = MINIMAL_MINUTEN
    elif not MIN_MINUTEN <= minuten <= MAX_MINUTEN:
        raise ValueError(f"Minuten müssen zwischen {MIN_MINUTEN} und {MAX_MINUTEN} liegen")
    budget = minuten * 60

    faellig = engine.faellige(ordner, heute=heute)
    last = sum(kosten(k) for k in faellig)
    bremse = last > STAU_FAKTOR * budget
    neu_erlaubt = not minimal and not bremse

    bereit = engine.neue(ordner)
    aktiv = [k for k in bereit if ist_aktiv(k, heute)]
    topf = [k for k in bereit if not ist_aktiv(k, heute)]
    random.Random(heute.isoformat()).shuffle(topf)
    obergrenze = neu_max(budget) if neu_erlaubt else 0

    mindest, reserve = _nehmen(aktiv, budget, MIN_NEU if neu_erlaubt else 0)
    wiederholung, zeit_wdh = _nehmen(faellig, budget - reserve, len(faellig))
    rest = budget - zeit_wdh - reserve

    neu = list(mindest)
    if neu_erlaubt:
        # Der Anteil gilt für Zeit und Anzahl, sonst nähme bei viel Zeit die
        # Obergrenze alles für die aktiven Abschnitte weg.
        anzahl_aktiv = max(MIN_NEU, round(obergrenze * ANTEIL_AKTIV))
        aktiv_rest = aktiv[len(mindest):]
        zeit_aktiv = rest * ANTEIL_AKTIV
        a, genutzt_a = _nehmen(aktiv_rest, zeit_aktiv, anzahl_aktiv - len(neu))
        neu += a
        zeit_topf = rest - genutzt_a
        t, genutzt_t = _nehmen(topf, zeit_topf, obergrenze - len(neu))
        neu += t
        # Was der Vorrat nicht braucht, geht zurück an die aktiven Abschnitte
        b, genutzt_b = _nehmen(aktiv_rest[len(a):], zeit_topf - genutzt_t, obergrenze - len(neu))
        neu += b
        rest -= genutzt_a + genutzt_t + genutzt_b

    je_projekt = {}
    for k in wiederholung:
        je_projekt.setdefault(k["projekt"], {"wiederholung": 0, "neu": 0})["wiederholung"] += 1
    for k in neu:
        je_projekt.setdefault(k["projekt"], {"wiederholung": 0, "neu": 0})["neu"] += 1
    aktive_ids = {k["id"] for k in aktiv}
    zeit = budget - rest
    return {
        "datum": heute.isoformat(),
        "modus": "minimal" if minimal else "normal",
        "minuten": minuten,
        "bremse": bremse,
        "neu_erlaubt": neu_erlaubt,
        "neu_max": obergrenze,
        "wiederholung": [k["id"] for k in wiederholung],
        "neu": [k["id"] for k in neu],
        "neu_aktiv": sum(1 for k in neu if k["id"] in aktive_ids),
        "neu_vorrat": sum(1 for k in neu if k["id"] not in aktive_ids),
        "zurueckgestellt": len(faellig) - len(wiederholung),
        "zeit_sek": zeit,
        "zeit_min": round(zeit / 60, 1),
        "ungenutzt_sek": rest,
        "je_projekt": je_projekt,
    }


def main(argv=None):
    args = list(sys.argv[1:] if argv is None else argv)
    minimal = "--minimal" in args
    minuten = STANDARD_MINUTEN
    if "--minuten" in args:
        try:
            minuten = int(args[args.index("--minuten") + 1])
        except (IndexError, ValueError):
            print("Fehler: --minuten braucht eine ganze Zahl", file=sys.stderr)
            return 1
    try:
        ergebnis = plan(minuten, minimal)
    except ValueError as fehler:
        print(f"Fehler: {fehler}", file=sys.stderr)
        return 1
    print(json.dumps(ergebnis, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
