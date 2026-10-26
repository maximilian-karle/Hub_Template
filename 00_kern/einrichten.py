#!/usr/bin/env python3
"""Technik hinter dem Befehl `/einrichten`. Rechnet und legt an, fragt nichts.

Das Gespräch führt Claude im Befehl `.claude/commands/einrichten.md`. Dieses
Skript übernimmt die Teile, die immer gleich ablaufen sollen, und merkt sich
den Fortschritt in `00_kern/einstellungen.json`, damit die Einrichtung eine
Pause überlebt.

Aufruf (aus der Hub-Wurzel):
    python3 00_kern/einrichten.py pruefen               Werkzeuge prüfen (git, gh, Python)
    python3 00_kern/einrichten.py status                erledigte und offene Schritte
    python3 00_kern/einrichten.py erledigt SCHRITT      Schritt abhaken
    python3 00_kern/einrichten.py fertig                Einrichtung abschließen
    python3 00_kern/einrichten.py ast NAME --art ART --spur S --sprache SPRACHE [--ziel PFAD]
                                                        neuen Ast aus vorlagen/ast anlegen

Ein Ast entsteht standardmäßig neben dem Hub (gleicher Elternordner) als
eigenes Git-Repo mit erstem Commit. Das GitHub-Repo dazu legt Claude erst nach
Rückfrage an, das Skript spricht nie mit GitHub.
"""
from __future__ import annotations
import argparse
import platform
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import einstellungen  # noqa: E402

HUB = Path(__file__).resolve().parents[1]
VORLAGE_AST = HUB / "vorlagen" / "ast"

# Reihenfolge der Einrichtung, wie im Befehl /einrichten.
SCHRITTE = [
    ("technik", "Werkzeuge prüfen und GitHub anmelden"),
    ("person", "Wer du bist und wohin du willst"),
    ("stil", "Sprache, Schreibregeln, Farben"),
    ("arbeitsweise", "Delegation, Qualität, Git"),
    ("lernen", "Kompetenzprofil und Lernbudget"),
    ("aeste", "Äste für Arbeit, Selbständigkeit und weitere"),
    ("bibliothek", "Bibliothek und Themenordner"),
    ("karriere", "Lebenslauf, Anschreiben und Jobsuche"),
    ("installieren", "Regeln und Skills nach ~/.claude"),
    ("github", "Eigenes privates Repo für den Hub"),
    ("start", "Erste Aufgabe und Rundgang"),
]
NAMEN = [s for s, _ in SCHRITTE]

# Was ein Ast für den Hub lesbar macht. Daten, Analysen und Berichte bleiben
# verborgen, auch wenn sie unter einem sichtbaren Ordner liegen.
SICHTBAR = [
    "CLAUDE.md",
    "*/CLAUDE.md",
    ".claude/commands/*.md",
    "00_kontext/*.md",
    "01_frameworks/*.md",
    "projekte/*/00_Charter/*.md",
    "projekte/*/methodology/*.md",
    "projekte/*/kpis/*.md",
    "projekte/*/docs/*.md",
]
VERBORGEN = ["*/data/*", "*/analysis/*", "*/reports/*", "*/archiv/*"]

INSTALLATION = {
    "Darwin": {
        "git": "xcode-select --install   (oder: brew install git)",
        "gh": "brew install gh",
        "python3": "brew install python@3.12",
        "brew": '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"',
    },
    "Windows": {
        "git": "winget install --id Git.Git",
        "gh": "winget install --id GitHub.cli",
        "python3": "winget install --id Python.Python.3.12",
    },
    "Linux": {
        "git": "sudo apt install git",
        "gh": "siehe https://cli.github.com",
        "python3": "sudo apt install python3",
    },
}


def lauf(befehl: list[str], cwd: Path | None = None) -> tuple[int, str]:
    try:
        r = subprocess.run(befehl, capture_output=True, text=True, encoding="utf-8", cwd=cwd)
    except FileNotFoundError:
        return 127, ""
    return r.returncode, (r.stdout + r.stderr).strip()


def pruefen() -> int:
    system = platform.system()
    tipps = INSTALLATION.get(system, INSTALLATION["Linux"])
    zeilen = []
    fehlt = 0

    def zeile(name: str, ok: bool, info: str, tipp: str = "") -> None:
        nonlocal fehlt
        fehlt += not ok
        zeilen.append(f"{'OK    ' if ok else 'FEHLT '} {name:<16} {info}" + (f"\n         → {tipp}" if tipp and not ok else ""))

    if system == "Darwin":
        code, _ = lauf(["brew", "--version"])
        zeile("Homebrew", code == 0, "Paketverwaltung für macOS", tipps["brew"])
    v = sys.version_info
    zeile("Python", v >= (3, 9), f"{v.major}.{v.minor}.{v.micro}, nötig ab 3.9", tipps["python3"])
    code, aus = lauf(["git", "--version"])
    zeile("git", code == 0, aus.splitlines()[0] if code == 0 else "", tipps["git"])
    if code == 0:
        _, nutzer = lauf(["git", "config", "--global", "user.name"])
        _, mail = lauf(["git", "config", "--global", "user.email"])
        zeile("git Identität", bool(nutzer and mail), f"{nutzer or '?'} <{mail or '?'}>",
              'git config --global user.name "Vorname Nachname" und user.email')
    code, aus = lauf(["gh", "--version"])
    zeile("GitHub CLI", code == 0, aus.splitlines()[0] if code == 0 else "", tipps["gh"])
    if code == 0:
        code, aus = lauf(["gh", "auth", "status"])
        konto = re.search(r"account (\S+)", aus) or re.search(r"as (\S+)", aus)
        zeile("GitHub Anmeldung", code == 0, konto.group(1) if konto and code == 0 else "",
              "im Terminal selbst ausführen: gh auth login")
    code, aus = lauf(["git", "remote", "get-url", "origin"], cwd=HUB)
    vorlage = einstellungen.laden().get("vorlage_repo", "")
    if code == 0 and vorlage and vorlage.lower() in aus.lower():
        zeilen.append(f"HINWEIS origin zeigt noch auf die Vorlage ({aus}). Schritt github legt dein eigenes Repo an.")
    elif code != 0:
        zeilen.append("HINWEIS Der Hub hat noch kein origin. Schritt github legt dein eigenes Repo an.")
    else:
        zeilen.append(f"OK     origin           {aus}")

    print(f"System: {system} {platform.release()}")
    print("\n".join(zeilen))
    print(f"\n{fehlt} offen." if fehlt else "\nAlles bereit.")
    return 1 if fehlt else 0


def status() -> int:
    daten = einstellungen.laden()
    erledigt = set(daten.get("einrichtung", {}).get("erledigt", []))
    print("Eingerichtet." if daten.get("eingerichtet") else "Einrichtung läuft.")
    for i, (name, text) in enumerate(SCHRITTE, 1):
        print(f"  {'[x]' if name in erledigt else '[ ]'} {i:>2} {name:<13} {text}")
    offen = [n for n in NAMEN if n not in erledigt]
    if offen:
        print(f"Nächster Schritt: {offen[0]}")
    return 0


def erledigt(schritt: str) -> int:
    if schritt not in NAMEN:
        sys.exit(f"Unbekannter Schritt {schritt}. Möglich sind {', '.join(NAMEN)}.")
    daten = einstellungen.laden()
    e = daten.setdefault("einrichtung", {})
    if not e.get("begonnen_am"):
        e["begonnen_am"] = date.today().isoformat()
    liste = e.setdefault("erledigt", [])
    if schritt not in liste:
        liste.append(schritt)
    einstellungen.speichern(daten)
    print(f"{schritt} erledigt ({len(liste)} von {len(NAMEN)}).")
    return 0


def fertig() -> int:
    daten = einstellungen.laden()
    offen = [n for n in NAMEN if n not in daten.get("einrichtung", {}).get("erledigt", [])]
    if offen:
        print(f"Noch offen: {', '.join(offen)}. Trotzdem abgeschlossen.")
    daten["eingerichtet"] = True
    einstellungen.speichern(daten)
    print("Hub eingerichtet.")
    return 0


def hub_pfad_kurz(hub: Path) -> str:
    try:
        return "~/" + hub.relative_to(Path.home()).as_posix()
    except ValueError:
        return hub.as_posix()


def ast_anlegen(name: str, art: str, spur: str, sprache: str, ziel: Path | None,
                hub: Path = HUB, mit_git: bool = True) -> Path:
    if not re.fullmatch(r"[A-Za-z0-9_.-]+", name):
        sys.exit("Der Name eines Asts besteht nur aus Buchstaben, Ziffern, _ . und -.")
    spur = spur.upper()
    daten = einstellungen.laden(hub / "00_kern" / "einstellungen.json")
    if einstellungen.ast_nach_name(name, daten):
        sys.exit(f"Ast {name} ist schon eingetragen.")
    if spur == einstellungen.SPUR_OEFFENTLICH or einstellungen.ast_nach_spur(spur, daten):
        sys.exit(f"Spur {spur} ist vergeben.")
    ziel = (ziel or hub.parent / name).expanduser().resolve()
    if ziel.exists() and any(ziel.iterdir()):
        sys.exit(f"{ziel} existiert und ist nicht leer.")

    werte = {"{{AST}}": name, "{{ART}}": art, "{{SPUR}}": spur, "{{SPRACHE}}": sprache,
             "{{HUB}}": hub_pfad_kurz(hub), "{{NAME}}": daten.get("person", {}).get("name", ""),
             "{{DATUM}}": date.today().strftime("%d.%m.%Y")}
    for quelle in sorted(VORLAGE_AST.rglob("*")):
        rel = quelle.relative_to(VORLAGE_AST)
        # Die Vorlage liegt im Hub. CLAUDE.md und .gitignore tragen dort die
        # Endung .vorlage, damit sie im Hub selbst nicht wirken.
        if rel.name == "gitignore.vorlage":
            rel = rel.with_name(".gitignore")
        elif rel.suffix == ".vorlage":
            rel = rel.with_suffix("")
        z = ziel / rel
        if quelle.is_dir():
            z.mkdir(parents=True, exist_ok=True)
            continue
        z.parent.mkdir(parents=True, exist_ok=True)
        try:
            text = quelle.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            shutil.copy2(quelle, z)
            continue
        for k, v in werte.items():
            text = text.replace(k, v)
        z.write_text(text, encoding="utf-8", newline="\n")
    # Git kennt keine leeren Ordner, die Vorlage führt sie über .gitkeep.

    daten.setdefault("aeste", []).append({
        "name": name, "art": art, "spur": spur, "sprache": sprache,
        "repo": "", "zweig": "main", "pfad": hub_pfad_kurz(ziel),
        "sichtbar": SICHTBAR, "verborgen": VERBORGEN,
    })
    einstellungen.speichern(daten, hub / "00_kern" / "einstellungen.json")

    if mit_git:
        lauf(["git", "init", "-b", "main"], cwd=ziel)
        lauf(["git", "add", "-A"], cwd=ziel)
        code, aus = lauf(["git", "commit", "-m", f"{name}: Ast aus der Hub-Vorlage angelegt"], cwd=ziel)
        if code != 0:
            print(f"Hinweis: erster Commit nicht möglich ({aus.splitlines()[-1] if aus else 'git fehlt'}).")
    print(f"Ast {name} angelegt unter {ziel} (Art {art}, Spur {spur}, Sprache {sprache}).")
    print("Nächster Schritt: privates GitHub-Repo anlegen, siehe /einrichten Schritt 6 oder /ast-anlegen.")
    return ziel


def main(argv: list[str]) -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="befehl", required=True)
    sub.add_parser("pruefen")
    sub.add_parser("status")
    e = sub.add_parser("erledigt")
    e.add_argument("schritt")
    sub.add_parser("fertig")
    a = sub.add_parser("ast")
    a.add_argument("name")
    a.add_argument("--art", required=True, choices=["arbeit", "selbststaendig", "sonstig"])
    a.add_argument("--spur", required=True)
    a.add_argument("--sprache", default="Deutsch")
    a.add_argument("--ziel", type=Path)
    a.add_argument("--ohne-git", action="store_true")
    x = ap.parse_args(argv)
    if x.befehl == "pruefen":
        return pruefen()
    if x.befehl == "status":
        return status()
    if x.befehl == "erledigt":
        return erledigt(x.schritt)
    if x.befehl == "fertig":
        return fertig()
    ast_anlegen(x.name, x.art, x.spur, x.sprache, x.ziel, mit_git=not x.ohne_git)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
