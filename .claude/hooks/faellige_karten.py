#!/usr/bin/env python3
"""SessionStart-Hook, zeigt die Zahl fälliger Karten über alle Lernprojekte.

Nur die Zahl, keine Karten, keine Wertung. Neuer Stoff zählt nicht, nur
Wiederholungen im Kasten. Bei null bleibt der Hook still.
Der Hook darf die Sitzung nie aufhalten, jeder Fehler endet stumm.
"""
import json
import sys
from pathlib import Path

GEDAECHTNIS = Path(__file__).resolve().parents[2] / "04_gedaechtnis"


def main() -> int:
    try:
        sys.path.insert(0, str(GEDAECHTNIS))
        import engine
        zahl = engine.zahl_faellig()
        if zahl:
            # json.dumps schreibt Umlaute als ASCII-Escapes, so scheitert keine
            # Konsole mit enger Codepage am Text.
            print(json.dumps({"systemMessage": f"{zahl} fällige Karten im Gedächtnis, /heute"}))
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
