"""Prüft Text auf die Schreibregeln aus ~/.claude/CLAUDE.md und 00_kern/regeln.md.

Fehler sind Gedankenstriche (– und —) und ein Bindestrich mit Leerzeichen
auf beiden Seiten als Pause. Hinweise sind Doppelpunkte im Fließtext und
Semikolons, weil sich dort nicht jeder Fall maschinell entscheiden lässt.
Erlaubt bleibt der Doppelpunkt am Zeilenende vor einer Liste und als
fester Label am Zeilenanfang („Note:“, „**Engpass:**“).

Code (Codeblöcke und Backticks), Tabellentrenner und Überschriften werden
nicht auf Doppelpunkte geprüft, Tabellenzeilen ebenfalls nicht.

Aufruf:
    python 00_kern/stilpruefung.py DATEI [DATEI ...]          Fehler und Hinweise
    python 00_kern/stilpruefung.py --nur-fehler DATEI [...]   nur Fehler, Exit 1 bei Treffer

Als Modul für Builder:
    from stilpruefung import fehler
    assert not fehler(text), fehler(text)
"""
import re
import sys
from pathlib import Path

STRICH = re.compile(r"[–—]")
PAUSE = re.compile(r"(?<=\S) - (?=\S)")
SEMIKOLON = re.compile(r";")
# Ein Label steht am Zeilenanfang, fett gesetzt oder als ein einzelnes Wort.
LABEL = re.compile(r"^\s*(?:[-*+]\s+|\d+\.\s+)?(?:\*\*[^*:]{1,40}:\*\*|\w[\w-]{0,24}:)\s")
DOPPELPUNKT = re.compile(r":(?=\s+\S)")


def _ohne_code(zeile: str) -> str:
    return re.sub(r"`[^`]*`", "", zeile)


def befunde(text: str) -> list[tuple[int, str, str]]:
    """Liste von (Zeile, Art, Ausschnitt), Art ist 'fehler' oder 'hinweis'."""
    aus = []
    im_code = False
    zeilen = text.splitlines()
    # YAML-Kopf von Befehlen und Skills gehört nicht zum Fließtext.
    kopf = zeilen.index("---", 1) + 1 if zeilen and zeilen[0] == "---" and "---" in zeilen[1:] else 0
    for nr, roh in enumerate(zeilen, 1):
        if nr <= kopf:
            continue
        if roh.lstrip().startswith("```"):
            im_code = not im_code
            continue
        if im_code:
            continue
        if re.fullmatch(r"\s*\|?[\s|:-]+\|?\s*", roh):
            continue
        zeile = _ohne_code(roh)
        for muster, art in ((STRICH, "fehler"), (PAUSE, "fehler"), (SEMIKOLON, "hinweis")):
            for m in muster.finditer(zeile):
                aus.append((nr, art, zeile[max(0, m.start() - 30):m.end() + 30].strip()))
        rest = zeile[LABEL.match(zeile).end():] if LABEL.match(zeile) else zeile
        if "|" not in zeile and not zeile.lstrip().startswith("#"):
            for m in DOPPELPUNKT.finditer(rest):
                if re.match(r"\s*//", rest[m.start() + 1:]):
                    continue
                aus.append((nr, "hinweis", rest[max(0, m.start() - 30):m.end() + 30].strip()))
    return aus


def fehler(text: str) -> list[tuple[int, str, str]]:
    return [b for b in befunde(text) if b[1] == "fehler"]


def main(argv: list[str]) -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    nur_fehler = "--nur-fehler" in argv
    dateien = [a for a in argv if a != "--nur-fehler"]
    if not dateien:
        sys.exit(__doc__)
    treffer = 0
    for d in dateien:
        liste = befunde(Path(d).read_text(encoding="utf-8"))
        if nur_fehler:
            liste = [b for b in liste if b[1] == "fehler"]
        for nr, art, stelle in liste:
            print(f"{d}:{nr}  {art}  {stelle}")
        treffer += sum(1 for b in liste if b[1] == "fehler")
    return 1 if treffer else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
