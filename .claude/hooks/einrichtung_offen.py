#!/usr/bin/env python3
"""SessionStart-Hook: erinnert an `/einrichten`, solange der Hub nicht eingerichtet ist.

Liest nur `00_kern/einstellungen.json`. Ist die Einrichtung abgeschlossen,
bleibt der Hook still. Er darf die Sitzung nie aufhalten, jeder Fehler endet
stumm.
"""
import json
import sys
from pathlib import Path

EINSTELLUNGEN = Path(__file__).resolve().parents[2] / "00_kern" / "einstellungen.json"


def schritte() -> int:
    try:
        sys.path.insert(0, str(EINSTELLUNGEN.parent))
        import einrichten
        return len(einrichten.SCHRITTE)
    except Exception:
        return 11


def main() -> int:
    try:
        daten = json.loads(EINSTELLUNGEN.read_text(encoding="utf-8"))
    except Exception:
        return 0
    if daten.get("eingerichtet"):
        return 0
    erledigt = len(daten.get("einrichtung", {}).get("erledigt", []))
    if erledigt:
        text = f"Hub zu {erledigt} von {schritte()} Schritten eingerichtet. Weiter mit /einrichten"
    else:
        text = "Willkommen im Hub. Tippe /einrichten, um ihn für dich einzurichten"
    print(json.dumps({
        "systemMessage": text,
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": (
                "Der Hub ist noch nicht eingerichtet (00_kern/einstellungen.json, "
                f"{erledigt} von {schritte()} Schritten). Biete der Person zu Beginn /einrichten an."
            ),
        },
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
