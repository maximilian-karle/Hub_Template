#!/usr/bin/env python3
"""PreToolUse-Hook für Write und Edit.

Hält Schreibzugriffe auf den Ordner reports/steering_committee/ eines Projekts
an, solange data/output/data_quality_log.md desselben Projekts nicht in den
letzten sieben Tagen geändert wurde. Die Logik dahinter ist, dass /qa-check
dann vermutlich nicht gelaufen ist und ungeprüfte Zahlen in eine
Lenkungskreisvorlage wandern würden.

Eingetragen in .claude/settings.json für Write und Edit.
Exit 0 lässt den Zugriff zu, Exit 2 hält ihn an (Claude Code zeigt stderr als
Grund). Jeder Fehler im Hook selbst endet mit Exit 0, damit ein Fehler im Hook
nie die Arbeit aufhält.
"""
import json
import sys
import time
from pathlib import Path

ALTER_TAGE_MAX = 7
ZIELORDNER = "/reports/steering_committee/"


def pruefen() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0

    eingabe = payload.get("tool_input", {}) if isinstance(payload, dict) else {}
    pfad = (eingabe.get("file_path") or eingabe.get("path") or "").replace("\\", "/")
    if ZIELORDNER not in pfad:
        return 0

    projekt = pfad.split(ZIELORDNER)[0]
    log = Path(projekt) / "data" / "output" / "data_quality_log.md"

    if not log.exists():
        print(f"ANGEHALTEN: {log} fehlt. Vor einer Lenkungskreisvorlage "
              f"zuerst /qa-check für dieses Projekt ausführen.", file=sys.stderr)
        return 2

    alter = (time.time() - log.stat().st_mtime) / 86400
    if alter > ALTER_TAGE_MAX:
        print(f"ANGEHALTEN: data_quality_log.md ist {alter:.1f} Tage alt "
              f"(mehr als {ALTER_TAGE_MAX}). Vor einer Lenkungskreisvorlage "
              f"zuerst /qa-check ausführen.", file=sys.stderr)
        return 2
    return 0


def main() -> int:
    try:
        sys.stderr.reconfigure(encoding="utf-8")
        return pruefen()
    except Exception:
        return 0


if __name__ == "__main__":
    sys.exit(main())
