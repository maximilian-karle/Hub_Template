"""Nächste Tätigkeit im Lernsystem ALTER, für den Befehl `/alter`.

Liest Karten, Modulpläne und den Verlauf der Tätigkeiten und wählt genau eine
nächste Tätigkeit. Reine Rechnung, das Modell entscheidet nicht selbst. Die
Rollen tragen ihr Kürzel aus ALTER (A Advisor, L Librarian, T Tutor, E Editor,
R Roommate).

Regeln, die erste zutreffende gewinnt:

1. Fällige Karten und heute noch kein `/heute`: T Behalten.
2. Problemkarte in einem Abschnitt (dieselbe Karte `PROBLEM_FOLGE`-mal
   hintereinander unter 3) und seit dem letzten Scheitern kein Sokrates zu
   diesem Abschnitt: T sokrates. Die Lücke liegt im Verstehen, nicht im
   Behalten.
3. Illusion des Wissens. Mindestens `ILLUSION_MIN` Abrufe eines Abschnitts in
   den letzten `ILLUSION_TAGE` Tagen mit Zuversicht ab `ILLUSION_ZUVERSICHT`
   und Note unter 3, und seitdem kein Feynman zu diesem Abschnitt: T feynman
   (Brown, Roediger, McDaniel, Make It Stick, Kap. 5).
4. Ein Abschnitt sitzt (mindestens `ABSTAND_MIN_KARTEN` Karten, alle im Kasten
   mit Intervall ab `engine.SITZT_AB_TAGEN`): T feynman mit Abstand, danach E
   auf eine kurze schriftliche Erklärung. Prüft, ob das Verständnis hält und
   nicht nur die Antwort (Make It Stick, Kap. 3, verteiltes Üben).
5. Nächster Schritt eines begonnenen Blocks.
6. Fälliger Meilenstein (alle Blöcke bis zu seinem Datum fertig): T feynman
   als Erklär-Check über die Abschnitte dieser Blöcke.
7. Nächster Block aus dem Modulplan, frühester Termin zuerst. Ein Block einer
   Spur, der auf einen Kern-Block verweist („wie K2“), wartet, bis dieser
   gelesen ist.
8. Alles erledigt oder noch kein Modul geplant: A plant mit `/advisor`.

Ein Kern-Block läuft in den Schritten `KERN_SCHRITTE`, ein Block einer Spur
(ein Ast aus `00_kern/einstellungen.json` oder Ö für öffentliche Daten) in
`SPUR_SCHRITTE`. Den Modus des Abschlusses bestimmt die Spalte
Nachweis im Modulplan. Ein Kern-Block, dessen Abschnitte schon freigeschaltet
sind, beginnt nach dem Lesen.

Hinweise ohne Vorrang: `/weekly-review`, wenn der letzte Messpunkt in
`rueckstau.json` älter als sieben Tage ist, `/roommate`, wenn im Monat noch
keine Notiz in `06_wissen/verbindungen/` liegt.

Aufruf (aus dem Hub):
    python 04_gedaechtnis/alter.py [--minimal]
    python 04_gedaechtnis/alter.py erledigt [--ergebnis TEXT] [--notiz TEXT]
    python 04_gedaechtnis/alter.py verlauf

`erledigt` trägt die gerade vorgeschlagene Tätigkeit in den Verlauf ein. Nach
dem Schritt Lesen schaltet es die Karten der Abschnitte frei.

Schwellen sind Annahmen, siehe `methodik.md`.
"""
import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))
sys.path.insert(0, str(HIER.parent / "00_kern"))
import engine  # noqa: E402

try:
    import einstellungen  # noqa: E402
except ImportError:         # Hub ohne 00_kern
    einstellungen = None

HUB = HIER.parent
MODULE = HUB / "01_kompass" / "module"
VERBINDUNGEN = HUB / "06_wissen" / "verbindungen"
VERLAUF = HIER / "alter_verlauf.json"
RUECKSTAU = HIER / "rueckstau.json"

PROBLEM_FOLGE = 2           # Anki nennt solche Karten Leech, dort ab 8 Fehlern
ILLUSION_TAGE = 14
ILLUSION_ZUVERSICHT = 70
ILLUSION_MIN = 2
ABSTAND_MIN_KARTEN = 3
REVIEW_TAGE = 7

KERN_SCHRITTE = ("feynman_start", "lesen", "sokrates", "abschluss", "editor", "lernlog")
SPUR_SCHRITTE = ("arbeiten", "abschluss", "lernlog")
# Modul-ID aus Bereichskürzel und Nummer, dann Kern-Abschnitt, etwa XY2-K00
ABSCHNITT = re.compile(r"\b[A-ZÄÖÜ]{1,4}\d{1,2}-K\d{2}\b")
# „wie K1, K5“ verweist auf Kern-Blöcke, „XY2-K00“ ist ein Abschnitt und zählt nicht
KERN_VERWEIS = re.compile(r"(?<![-\w])(K\d+)\b")


def _datum(text):
    m = re.search(r"(\d{1,2})\.(\d{1,2})\.(\d{4})", text or "")
    return date(int(m[3]), int(m[2]), int(m[1])) if m else None


def tabellen(text):
    """Markdown-Tabellen als Liste von (Kopf, Zeilen), Zellen ohne Rand."""
    out, block = [], []
    for z in text.splitlines() + [""]:
        if z.strip().startswith("|"):
            block.append([c.strip() for c in z.strip().strip("|").split("|")])
            continue
        if len(block) >= 2 and set("".join(block[1])) <= set("-: "):
            out.append((block[0], block[2:]))
        block = []
    return out


def _letzte(tabs, *spalten):
    passend = [t for t in tabs if all(s in t[0] for s in spalten)]
    return passend[-1] if passend else None


def modulplan(pfad):
    """Blöcke und Meilensteine des neuesten Durchlaufs einer modul.md."""
    modul = Path(pfad).parent.name.split("_")[0]
    tabs = tabellen(Path(pfad).read_text(encoding="utf-8"))
    bloecke, meilensteine = [], []
    tab = _letzte(tabs, "Block", "spätestens", "Quelle", "Spur", "Nachweis")
    if tab:
        kopf, zeilen = tab
        i = {s: kopf.index(s) for s in ("Block", "spätestens", "Inhalt", "Quelle", "Spur", "Nachweis")}
        for n, z in enumerate(zeilen):
            spur = z[i["Spur"]]
            bloecke.append({
                "modul": modul, "block": z[i["Block"]], "nr": n,
                "spaetestens": _datum(z[i["spätestens"]]), "inhalt": z[i["Inhalt"]],
                "quelle": z[i["Quelle"]], "spur": "Kern" if spur.lower() == "kern" else spur,
                "nachweis": z[i["Nachweis"]],
                "abschnitte": ABSCHNITT.findall(z[i["Quelle"]]),
                "verweise": KERN_VERWEIS.findall(z[i["Quelle"]]) if spur.lower() != "kern" else [],
            })
        kern = {b["block"]: b for b in bloecke if b["spur"] == "Kern"}
        for b in bloecke:
            for v in b["verweise"]:
                for a in kern.get(v, {}).get("abschnitte", []):
                    if a not in b["abschnitte"]:
                        b["abschnitte"].append(a)
    tab = _letzte(tabs, "spätestens", "Output", "Prüfung")
    if tab:
        kopf, zeilen = tab
        for z in zeilen:
            erste = z[kopf.index("spätestens")]
            meilensteine.append({"modul": modul, "name": erste.split(",")[0].strip(),
                                 "datum": _datum(erste), "pruefung": z[kopf.index("Prüfung")]})
    return bloecke, meilensteine


def abschluss_modus(nachweis):
    n = nachweis.lower()
    if "erklär" in n or "verteidigt" in n:
        return "feynman"
    if "kontrollfragen" in n or "probefrage" in n:
        return "test"
    return "editor"


def _verlauf_datei(pfad):
    """Verlauf als {"eintraege": [...]}. Eine leere Liste in der Datei gilt als leerer Verlauf."""
    pfad = Path(pfad)
    if not pfad.exists() or not pfad.read_text(encoding="utf-8-sig").strip():
        return {"eintraege": []}
    daten = engine.laden(pfad)
    return {"eintraege": daten} if isinstance(daten, list) else daten


def verlauf_laden(pfad=VERLAUF):
    return _verlauf_datei(pfad)["eintraege"]


def _erledigt(verlauf, modul, block, schritt):
    return any(e.get("modul") == modul and e.get("block") == block and e["schritt"] == schritt
               for e in verlauf)


def _letztes_datum(verlauf, abschnitt, modi):
    daten = [date.fromisoformat(e["datum"]) for e in verlauf
             if e.get("modus") in modi and abschnitt in e.get("abschnitte", [])]
    return max(daten) if daten else None


def _je_abschnitt(karten):
    out = {}
    for k in karten:
        out.setdefault(k["abschnitt"], []).append(k)
    return out


def schon_freigeschaltet(abschnitte, karten_je):
    """Alle Abschnitte haben Karten und keine davon ist gesperrt."""
    return bool(abschnitte) and all(
        karten_je.get(a) and not any(k["gesperrt"] for k in karten_je[a]) for a in abschnitte)


def problemkarten(karten):
    """(Karte, Datum des letzten Scheiterns) für Karten mit PROBLEM_FOLGE Fehlern in Folge."""
    out = []
    for k in karten:
        h = k["lernzustand"].get("review_history", [])
        if len(h) >= PROBLEM_FOLGE and all(e["quality"] < 3 for e in h[-PROBLEM_FOLGE:]):
            out.append((k, date.fromisoformat(h[-1]["date"])))
    return out


def schritte(block):
    return KERN_SCHRITTE if block["spur"] == "Kern" else SPUR_SCHRITTE


def naechster_schritt(block, verlauf, karten_je):
    for s in schritte(block):
        if _erledigt(verlauf, block["modul"], block["block"], s):
            continue
        if s in ("feynman_start", "lesen") and schon_freigeschaltet(block["abschnitte"], karten_je):
            continue
        return s
    return None


def _modus(block, schritt):
    return {"feynman_start": "feynman", "sokrates": "sokrates", "editor": "editor",
            "abschluss": abschluss_modus(block["nachweis"])}.get(schritt)


def wo_arbeiten(spur, daten=None):
    """Ort der Arbeit für einen Block einer Spur, aus den Ästen der Einstellungen."""
    if spur == "Ö":
        return "mit öffentlichen Daten im Lernprojekt arbeiten (Spur Ö)"
    try:
        ast = einstellungen.ast_nach_spur(spur, daten) if einstellungen else None
    except (OSError, ValueError):
        ast = None
    if ast:
        return f"im Ast {ast['name']} arbeiten (Spur {spur}, Repo {ast.get('repo') or ast['name']})"
    return f"Spur {spur} hat noch keinen Ast in 00_kern/einstellungen.json, erst /einrichten"


def _befehl(modus, abschnitte, schritt=None, block=None):
    ziel = " ".join(abschnitte)
    if modus in ("sokrates", "feynman", "test"):
        return f"/tutor {modus} {ziel}".strip()
    if modus == "editor":
        return "/editor chat erklaerung" if block is None or block["spur"] == "Kern" else "/editor <Pfad zum Artefakt>"
    return {"lesen": f"lesen laut Lesepfad, dann `alter.py erledigt` (schaltet {ziel} frei)",
            "arbeiten": wo_arbeiten((block or {}).get("spur")) if schritt == "arbeiten" else "",
            "lernlog": "Zeile in lernlog.md des Lernprojekts"}.get(schritt, "")


ROLLE = {"sokrates": "T", "feynman": "T", "test": "T", "editor": "E"}
SCHRITT_ROLLE = {"lesen": "L", "arbeiten": "Ast", "lernlog": "A"}


def _vorschlag(regel, schritt, grund, block=None, abschnitte=None, modus=None, **mehr):
    abschnitte = abschnitte if abschnitte is not None else (block or {}).get("abschnitte", [])
    v = {"regel": regel, "schritt": schritt, "modus": modus,
         "rolle": ROLLE.get(modus) or SCHRITT_ROLLE.get(schritt, "T"),
         "befehl": _befehl(modus, abschnitte, schritt, block),
         "modul": (block or {}).get("modul"), "block": (block or {}).get("block"),
         "abschnitte": abschnitte, "grund": grund}
    if block:
        v.update(inhalt=block["inhalt"], quelle=block["quelle"], nachweis=block["nachweis"])
    v.update(mehr)
    return v


def _block_zu(abschnitt, bloecke):
    for b in bloecke:
        if b["spur"] == "Kern" and abschnitt in b["abschnitte"]:
            return b
    return None


def hinweise(heute, rueckstau=RUECKSTAU, verbindungen=VERBINDUNGEN):
    out = []
    punkte = json.loads(Path(rueckstau).read_text(encoding="utf-8")) if Path(rueckstau).exists() else []
    letzter = max((date.fromisoformat(p["datum"]) for p in punkte), default=None)
    if letzter is None or (heute - letzter).days >= REVIEW_TAGE:
        out.append("A /weekly-review, letzter Messpunkt "
                   + (letzter.strftime("%d.%m.%Y") if letzter else "fehlt"))
    if not list(Path(verbindungen).glob(f"{heute:%Y-%m}_*.md")):
        out.append(f"R /roommate, im {heute:%m/%Y} noch keine Verbindung")
    return out


def naechste(heute=None, minimal=False, karten_ordner=None, module=MODULE,
             verlauf_pfad=VERLAUF, rueckstau=RUECKSTAU, verbindungen=VERBINDUNGEN):
    """Genau eine nächste Tätigkeit als Dict. Schreibt nichts."""
    heute = heute or date.today()
    karten = [k for _, k in engine.alle_karten(karten_ordner)]
    karten_je = _je_abschnitt(karten)
    verlauf = verlauf_laden(verlauf_pfad)
    v = _waehlen(heute, minimal, karten, karten_je, verlauf, module)
    v["datum"] = heute.isoformat()
    v["hinweise"] = [] if minimal else hinweise(heute, rueckstau, verbindungen)
    return v


def _waehlen(heute, minimal, karten, karten_je, verlauf, module):
    faellig = [k for k in karten if engine.ist_faellig(k, heute)]
    heute_schon = any(e["schritt"] == "heute" and e["datum"] == heute.isoformat() for e in verlauf)
    if faellig and not heute_schon:
        return _vorschlag(1, "heute", f"{len(faellig)} fällige Karten, Behalten geht vor",
                          abschnitte=[]) | {"befehl": "/heute", "rolle": "T"}
    if minimal:
        return _vorschlag(0, "pause", "Minimalbetrieb, nur Wiederholung, für heute fertig",
                          abschnitte=[]) | {"befehl": "", "rolle": "-"}

    bloecke, meilensteine = [], []
    for pfad in sorted(Path(module).glob("*/modul.md")):
        b, m = modulplan(pfad)
        bloecke += b
        meilensteine += m

    # Regel 2, Problemkarten
    for k, gescheitert in sorted(problemkarten(karten), key=lambda p: (p[0]["abschnitt"], p[0]["id"])):
        a = k["abschnitt"]
        zuletzt = _letztes_datum(verlauf, a, ("sokrates",))
        if zuletzt is None or zuletzt < gescheitert:
            n = sum(1 for p, _ in problemkarten(karten_je[a]))
            return _vorschlag(2, "sokrates_luecke",
                              f"{n} Karte(n) in {a} {PROBLEM_FOLGE}-mal in Folge unter 3, zuletzt {k['id']}",
                              block=_block_zu(a, bloecke), abschnitte=[a], modus="sokrates")

    # Regel 3, Illusion des Wissens
    grenze = heute - timedelta(days=ILLUSION_TAGE - 1)
    for a in sorted(karten_je):
        treffer = [date.fromisoformat(e["date"]) for k in karten_je[a]
                   for e in k["lernzustand"].get("review_history", [])
                   if e.get("zuversicht", -1) >= ILLUSION_ZUVERSICHT and e["quality"] < 3
                   and date.fromisoformat(e["date"]) >= grenze]
        zuletzt = _letztes_datum(verlauf, a, ("feynman",))
        if zuletzt is not None:
            treffer = [d for d in treffer if d > zuletzt]
        if len(treffer) >= ILLUSION_MIN:
            return _vorschlag(3, "feynman_illusion",
                              f"{len(treffer)} Abrufe in {a} mit Zuversicht ab {ILLUSION_ZUVERSICHT} % falsch",
                              block=_block_zu(a, bloecke), abschnitte=[a], modus="feynman")

    # Regel 4, Abschnitt sitzt, Feynman mit Abstand und danach Editor
    for a in sorted(karten_je):
        ks = karten_je[a]
        if len(ks) < ABSTAND_MIN_KARTEN or not all(engine.sitzt(k) for k in ks):
            continue
        f = [e for e in verlauf if e["schritt"] == "feynman_abstand" and a in e.get("abschnitte", [])]
        e_ = [e for e in verlauf if e["schritt"] == "editor_abstand" and a in e.get("abschnitte", [])]
        if not f:
            return _vorschlag(4, "feynman_abstand", f"alle {len(ks)} Karten in {a} sitzen, hält das Verständnis?",
                              block=_block_zu(a, bloecke), abschnitte=[a], modus="feynman")
        if not e_:
            return _vorschlag(4, "editor_abstand", f"Feynman mit Abstand zu {a} gelaufen, jetzt schriftlich",
                              block=_block_zu(a, bloecke), abschnitte=[a], modus="editor")

    bloecke.sort(key=lambda b: (b["spaetestens"] or date.max, b["modul"], b["nr"]))
    offen = [(b, naechster_schritt(b, verlauf, karten_je)) for b in bloecke]
    offen = [(b, s) for b, s in offen if s is not None]

    def begonnen(b):
        return any(_erledigt(verlauf, b["modul"], b["block"], s) for s in schritte(b)) or (
            b["spur"] == "Kern" and schon_freigeschaltet(b["abschnitte"], karten_je))

    # Regel 5, begonnener Block
    for b, s in offen:
        if begonnen(b):
            return _vorschlag(5, s, f"Block {b['modul']} {b['block']} läuft, nächster Schritt {s}",
                              block=b, modus=_modus(b, s))

    # Regel 6, Meilenstein
    fertig = {(b["modul"], b["block"]) for b in bloecke} - {(b["modul"], b["block"]) for b, _ in offen}
    for m in sorted(meilensteine, key=lambda m: m["datum"] or date.max):
        if _erledigt(verlauf, m["modul"], m["name"], "gate"):
            continue
        davor = [b for b in bloecke if b["modul"] == m["modul"] and b["spaetestens"]
                 and m["datum"] and b["spaetestens"] <= m["datum"]]
        if davor and all((b["modul"], b["block"]) in fertig for b in davor):
            abschnitte = sorted({a for b in davor for a in b["abschnitte"]})
            v = _vorschlag(6, "gate", f"alle Blöcke bis {m['name']} fertig, Erklär-Check",
                           abschnitte=abschnitte, modus="feynman", pruefung=m["pruefung"])
            v.update(modul=m["modul"], block=m["name"])
            return v
        break   # spätere Meilensteine erst nach diesem

    # Regel 7, nächster Block
    def wartet(b):
        kern = {x["block"]: x for x in bloecke if x["modul"] == b["modul"] and x["spur"] == "Kern"}
        return any(v in kern and naechster_schritt(kern[v], verlauf, karten_je) in ("feynman_start", "lesen")
                   for v in b["verweise"])

    for b, s in offen:
        if not wartet(b):
            return _vorschlag(7, s, f"nächster Block {b['modul']} {b['block']}, spätestens "
                              + (b["spaetestens"].strftime("%d.%m.%Y") if b["spaetestens"] else "offen"),
                              block=b, modus=_modus(b, s))

    if offen:
        b, s = offen[0]
        return _vorschlag(7, s, "alle offenen Blöcke warten auf einen Kern-Block, dieser zuerst",
                          block=b, modus=_modus(b, s))
    if not bloecke:
        return _vorschlag(8, "advisor", "noch kein Modul mit Blockplan unter 01_kompass/module/, "
                          "eine Aufgabe mit /aufnahme aufnehmen oder ein Modul mit /advisor planen",
                          abschnitte=[]) | {"befehl": "/advisor", "rolle": "A"}
    return _vorschlag(8, "advisor", "alle Blöcke und Meilensteine erledigt",
                      abschnitte=[]) | {"befehl": "/advisor", "rolle": "A"}


def erledigt(vorschlag, ergebnis=None, notiz=None, verlauf_pfad=VERLAUF, karten_ordner=None):
    """Trägt den Vorschlag in den Verlauf ein, nach dem Lesen mit Freischalten."""
    pfad = Path(verlauf_pfad)
    datei = _verlauf_datei(pfad)
    eintrag = {k: vorschlag.get(k) for k in ("datum", "schritt", "modus", "rolle", "modul", "block", "abschnitte")}
    if ergebnis:
        eintrag["ergebnis"] = ergebnis
    if notiz:
        eintrag["notiz"] = notiz
    if vorschlag["schritt"] == "lesen":
        heute = date.fromisoformat(vorschlag["datum"])
        eintrag["freigeschaltet"] = [i for a in vorschlag["abschnitte"]
                                     for i in engine.freischalten(karten_ordner or engine.KARTEN, a, heute)]
    datei["eintraege"].append(eintrag)
    engine.speichern(pfad, datei)
    return eintrag


def main(argv=None):
    args = list(sys.argv[1:] if argv is None else argv)

    def opt(name):
        return args[args.index(name) + 1] if name in args and args.index(name) + 1 < len(args) else None

    if args and args[0] == "verlauf":
        print(json.dumps(verlauf_laden(), ensure_ascii=False, indent=2))
        return 0
    v = naechste(minimal="--minimal" in args)
    if args and args[0] == "erledigt":
        if v["schritt"] == "pause":
            print("Fehler: nichts vorgeschlagen, nichts einzutragen", file=sys.stderr)
            return 1
        print(json.dumps(erledigt(v, opt("--ergebnis"), opt("--notiz")), ensure_ascii=False, indent=2))
        print(json.dumps(naechste(), ensure_ascii=False, indent=2, default=str))
        return 0
    print(json.dumps(v, ensure_ascii=False, indent=2, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(main())
