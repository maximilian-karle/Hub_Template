#!/usr/bin/env python3
"""Richtet ~/.claude für den Hub ein. Idempotent, zeigt jede Änderung an.

Was das Skript tut:
  1. Agenten aus 00_kern/claude/agents/ nach ~/.claude/agents/ kopieren.
  2. Skills aus 00_kern/claude/skills/<name>/ nach ~/.claude/skills/<name>/ kopieren.
     In allen kopierten Dateien wird der Platzhalter {{HUB}} durch den Pfad der
     Hub-Wurzel ersetzt, damit die Skills auch in jedem Ast laufen.
  3. In ~/.claude/CLAUDE.md je eine Importzeile für 00_kern/persoenlich.md und
     00_kern/regeln.md setzen (eine veraltete Zeile wird ersetzt, nicht
     verdoppelt, eigener Text in der Datei bleibt stehen).
  4. In ~/.claude/settings.json permissions.additionalDirectories um den Pfad
     von 02_bibliothek ergänzen (veraltete Einträge auf 02_bibliothek entfallen).

Aufruf:
  python 00_kern/installieren.py              führt aus
  python 00_kern/installieren.py --dry-run    zeigt nur an
  python 00_kern/installieren.py --hub PFAD   Hub-Wurzel statt Skriptordner
  python 00_kern/installieren.py --claude-home PFAD   statt ~/.claude (für Tests)
"""
import argparse
import json
import re
import sys
from pathlib import Path

PLATZHALTER = "{{HUB}}"
IMPORTE = ["00_kern/persoenlich.md", "00_kern/regeln.md"]


def posix(p: Path) -> str:
    return p.as_posix()


def schreibe(ziel: Path, inhalt: str, trocken: bool, log: list) -> bool:
    """Schreibt nur bei Abweichung. Gibt True zurück, wenn etwas zu ändern war."""
    alt = ziel.read_text(encoding="utf-8") if ziel.exists() else None
    if alt == inhalt:
        return False
    log.append(("neu" if alt is None else "ändert") + f"  {ziel}")
    if not trocken:
        ziel.parent.mkdir(parents=True, exist_ok=True)
        ziel.write_text(inhalt, encoding="utf-8", newline="\n")
    return True


def kopiere_quellen(hub: Path, home: Path, trocken: bool, log: list) -> int:
    quelle = hub / "00_kern" / "claude"
    n = 0
    for datei in sorted(quelle.rglob("*")):
        if not datei.is_file():
            continue
        rel = datei.relative_to(quelle)
        text = datei.read_text(encoding="utf-8").replace(PLATZHALTER, posix(hub))
        n += schreibe(home / rel, text, trocken, log)
    return n


def import_zeile(hub: Path, ende: str) -> str:
    ziel = hub / ende
    try:
        return "@~/" + posix(ziel.relative_to(Path.home()))
    except ValueError:
        return "@" + posix(ziel)


def setze_import(hub: Path, claude_md: Path, trocken: bool, log: list) -> int:
    text = claude_md.read_text(encoding="utf-8") if claude_md.exists() else ""
    zeilen = text.split("\n") if text else []
    for ende in IMPORTE:
        zeile = import_zeile(hub, ende)
        treffer = [i for i, z in enumerate(zeilen) if re.match(r"^@.*" + re.escape(ende) + r"\s*$", z)]
        if treffer:
            for i in treffer:
                zeilen[i] = zeile
        else:
            while zeilen and zeilen[-1] == "":
                zeilen.pop()
            zeilen += ([""] if zeilen else []) + [zeile]
    neu = "\n".join(zeilen).rstrip("\n") + "\n"
    return schreibe(claude_md, neu, trocken, log)


def setze_verzeichnis(hub: Path, settings: Path, trocken: bool, log: list) -> int:
    daten = json.loads(settings.read_text(encoding="utf-8")) if settings.exists() else {}
    perm = daten.setdefault("permissions", {})
    liste = perm.get("additionalDirectories", [])
    ziel = posix(hub / "02_bibliothek")
    behalten = [p for p in liste if not p.replace("\\", "/").rstrip("/").endswith("02_bibliothek")]
    perm["additionalDirectories"] = behalten + [ziel]
    neu = json.dumps(daten, indent=2, ensure_ascii=False) + "\n"
    return schreibe(settings, neu, trocken, log)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--hub", type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument("--claude-home", type=Path, default=Path.home() / ".claude")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    hub = a.hub.resolve()
    home = a.claude_home
    if not (hub / "00_kern" / "claude").is_dir():
        print(f"FEHLER: {hub / '00_kern' / 'claude'} fehlt", file=sys.stderr)
        return 1

    log: list = []
    n = kopiere_quellen(hub, home, a.dry_run, log)
    n += setze_import(hub, home / "CLAUDE.md", a.dry_run, log)
    n += setze_verzeichnis(hub, home / "settings.json", a.dry_run, log)

    print(f"Hub: {hub}")
    print(f"Ziel: {home}" + ("  (Trockenlauf)" if a.dry_run else ""))
    for z in log:
        print("  " + z)
    print(f"{n} Änderung(en)" if n else "Nichts zu ändern.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
