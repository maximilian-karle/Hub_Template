"""Gedächtnis eines Repos als eine Markdown-Datei sichern und wiederherstellen.

Das Claude-Gedächtnis liegt je Rechner unter ~/.claude/projects/<Slug>/memory
und wandert nicht über Git. Dieses Skript bündelt alle Dateien in eine
Markdown-Datei im Repo und stellt sie auf dem anderen Rechner wieder her.

Aufruf (aus dem Repo, dessen Gedächtnis gemeint ist):
    python 00_kern/gedaechtnis_sync.py export  [Repo] [Bündel]
    python 00_kern/gedaechtnis_sync.py import  [Repo] [Bündel]
    python 00_kern/gedaechtnis_sync.py status  [Repo] [Bündel]

Repo ist standardmäßig das aktuelle Verzeichnis, Bündel standardmäßig
<Repo>/00_kern/gedaechtnis.md. Der Slug folgt der Regel von Claude Code, jedes
Zeichen außer Buchstaben und Ziffern wird zu "-". Dadurch passt derselbe Befehl
auf Windows und Mac.

import überschreibt nichts still. Abweichende lokale Dateien werden gemeldet und
nur mit --force ersetzt. Lokale Dateien, die im Bündel fehlen, bleiben liegen.
"""
import re
import sys
from pathlib import Path

MARKE = "<!-- datei: "
ENDE = " -->"
KOPF = (
    "# Gedächtnis\n\n"
    "Automatisch erzeugt von `00_kern/gedaechtnis_sync.py`. Nicht von Hand\n"
    "bearbeiten, Änderungen entstehen im Gedächtnis selbst und werden mit\n"
    "`export` hierher geschrieben.\n"
)


def gedaechtnis_ordner(repo: Path) -> Path:
    slug = re.sub(r"[^A-Za-z0-9]", "-", str(repo.resolve()))
    return Path.home() / ".claude" / "projects" / slug / "memory"


def lesen(ordner: Path) -> dict[str, str]:
    if not ordner.is_dir():
        return {}
    dateien = {}
    for p in sorted(ordner.glob("*.md")):
        dateien[p.name] = p.read_text(encoding="utf-8").replace("\r\n", "\n")
    return dateien


def buendel_lesen(pfad: Path) -> dict[str, str]:
    if not pfad.is_file():
        return {}
    text = pfad.read_text(encoding="utf-8").replace("\r\n", "\n")
    teile = re.split(r"^" + re.escape(MARKE) + r"(.+?)" + re.escape(ENDE) + r"\n",
                     text, flags=re.M)
    # teile[0] ist der Kopf, danach abwechselnd Name und Inhalt
    return {teile[i]: teile[i + 1].rstrip("\n") + "\n" for i in range(1, len(teile) - 1, 2)}


def export(repo: Path, buendel: Path) -> None:
    dateien = lesen(gedaechtnis_ordner(repo))
    if not dateien:
        sys.exit(f"Kein Gedächtnis gefunden unter {gedaechtnis_ordner(repo)}")
    teile = [KOPF]
    # MEMORY.md zuerst, dann alphabetisch
    for name in sorted(dateien, key=lambda n: (n != "MEMORY.md", n)):
        teile.append(f"{MARKE}{name}{ENDE}\n{dateien[name].rstrip(chr(10))}\n")
    buendel.parent.mkdir(parents=True, exist_ok=True)
    buendel.write_text("\n".join(teile), encoding="utf-8", newline="\n")
    print(f"{len(dateien)} Dateien nach {buendel} geschrieben.")


def vergleich(repo: Path, buendel: Path):
    lokal = lesen(gedaechtnis_ordner(repo))
    bund = buendel_lesen(buendel)
    neu = [n for n in bund if n not in lokal]
    anders = [n for n in bund if n in lokal and bund[n] != lokal[n]]
    nur_lokal = [n for n in lokal if n not in bund]
    return lokal, bund, neu, anders, nur_lokal


def status(repo: Path, buendel: Path) -> None:
    _, bund, neu, anders, nur_lokal = vergleich(repo, buendel)
    print(f"Bündel {len(bund)} Dateien. Neu im Bündel {len(neu)}, abweichend {len(anders)}, "
          f"nur lokal {len(nur_lokal)}.")
    for titel, liste in (("neu im Bündel", neu), ("abweichend", anders), ("nur lokal", nur_lokal)):
        for n in liste:
            print(f"  {titel}: {n}")


def importieren(repo: Path, buendel: Path, force: bool) -> None:
    _, bund, neu, anders, _ = vergleich(repo, buendel)
    if not bund:
        sys.exit(f"Bündel {buendel} fehlt oder ist leer.")
    ordner = gedaechtnis_ordner(repo)
    ordner.mkdir(parents=True, exist_ok=True)
    schreiben = neu + (anders if force else [])
    for n in schreiben:
        (ordner / n).write_text(bund[n], encoding="utf-8", newline="\n")
    print(f"{len(schreiben)} Dateien nach {ordner} geschrieben.")
    if anders and not force:
        print("Abweichend und nicht überschrieben (mit --force ersetzen, vorher status prüfen):")
        for n in anders:
            print(f"  {n}")


def main() -> None:
    args = [a for a in sys.argv[1:] if a != "--force"]
    force = "--force" in sys.argv
    if not args or args[0] not in ("export", "import", "status"):
        sys.exit(__doc__)
    repo = Path(args[1]) if len(args) > 1 else Path.cwd()
    buendel = Path(args[2]) if len(args) > 2 else repo / "00_kern" / "gedaechtnis.md"
    {"export": lambda: export(repo, buendel),
     "import": lambda: importieren(repo, buendel, force),
     "status": lambda: status(repo, buendel)}[args[0]]()


if __name__ == "__main__":
    main()
