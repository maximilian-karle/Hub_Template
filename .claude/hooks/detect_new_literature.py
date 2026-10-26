#!/usr/bin/env python3
"""SessionStart-Hook für neue Literatur.

Durchsucht 02_bibliothek/ samt Themenordnern nach PDF-Dateien und vergleicht
sie mit Literatur_Index.md. Ordner, deren Name mit "_" beginnt, werden
übersprungen (etwa ein Studienordner mit eigenem Unterindex). Für jedes noch
nicht indizierte PDF liest der Hook die ersten 20 Seiten, wo Titelblatt und
Inhaltsverzeichnis fast immer stehen, und gibt den Text als Kontext an Claude.

Claude schlägt daraus einen Indexeintrag vor, die Person bestätigt oder
korrigiert, und erst /add-literature schreibt ihn. Der Hook ändert den Index
nie selbst, damit eine falsche Vermutung nicht still zur Wahrheit wird.

Benötigt pypdf (pip3 install pypdf). Fehlt es, meldet der Hook nur den
Dateinamen. Jeder Fehler endet still mit Exit 0, die Sitzung startet immer.
"""
import json
import re
import sys
from pathlib import Path

MAX_SEITEN = 20
MAX_ZEICHEN = 6000
HUB = Path(__file__).resolve().parents[2]
LIT_DIR = HUB / "02_bibliothek"
INDEX = LIT_DIR / "Literatur_Index.md"


def text_der_ersten_seiten(pdf: Path, max_seiten: int = MAX_SEITEN) -> str:
    try:
        from pypdf import PdfReader
    except ImportError:
        return ("[pypdf ist nicht installiert, der Text konnte nicht gelesen "
                "werden. Installieren mit pip3 install pypdf]")
    try:
        reader = PdfReader(str(pdf))
        n = min(max_seiten, len(reader.pages))
        text = "\n".join(reader.pages[i].extract_text() or "" for i in range(n))
        return text.strip() or "[keine lesbare Textebene auf den ersten Seiten]"
    except Exception as e:
        return f"[Fehler beim Lesen von {pdf.name}, {e}]"


def uebersprungen(pdf: Path) -> bool:
    teile = pdf.relative_to(LIT_DIR).parts[:-1]
    return any(t.startswith("_") for t in teile)


def melden() -> None:
    if not LIT_DIR.exists():
        return

    roh = INDEX.read_text(encoding="utf-8") if INDEX.exists() else ""
    # Leerraum normalisieren, weil der Index lange Dateinamen über zwei Zeilen
    # umbricht. Sonst meldet der Hook längst indizierte Titel bei jedem Start neu.
    index_text = re.sub(r"\s+", " ", roh)
    # Die Werke liegen in Themenordnern, verglichen wird über den Dateinamen.
    pdfs = sorted(p for p in LIT_DIR.rglob("*.pdf") if not uebersprungen(p))
    neu = [p for p in pdfs if re.sub(r"\s+", " ", p.name) not in index_text]
    if not neu:
        return

    bloecke = []
    for pdf in neu:
        auszug = text_der_ersten_seiten(pdf)[:MAX_ZEICHEN]
        bloecke.append(
            f"### {pdf.relative_to(LIT_DIR).as_posix()} (noch nicht in Literatur_Index.md)\n"
            f"Erste {MAX_SEITEN} Seiten (Titel und Inhaltsverzeichnis)\n{auszug}"
        )

    kontext = (
        f"{len(neu)} neue PDF-Datei(en) in 02_bibliothek/ gefunden, die noch "
        f"nicht in Literatur_Index.md stehen. Schlage der Person von dir aus "
        f"einen Indexeintrag vor (Titel, Autor, Relevanz, Inhaltsverzeichnis) "
        f"auf Grundlage des Auszugs. Nur zur Bestätigung, nicht selbst "
        f"eintragen.\n\n" + "\n\n".join(bloecke)
    )
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": kontext,
        }
    }))


def main() -> int:
    try:
        melden()
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
