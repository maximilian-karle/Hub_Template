"""Stand eines Astes lesen, ohne ihn zu klonen.

Der Hub soll mitbekommen, welche Ideen und Entscheidungen in einem Ast
entstehen, ohne dass dessen Arbeitsdaten auf einen Rechner gelangen, auf den
sie nicht gehören. Das Skript liest deshalb nur über die GitHub-API (`gh api`)
und nur Dateien einer festen Positivliste (Projektkontext, Charter, Methodik,
Kennzahlendefinitionen, Frameworks, Lesebegleiter). Daten, Analysen, Berichte
und Binärdateien bleiben unsichtbar. Nichts wird auf die Platte geschrieben
außer dem zuletzt gesehenen Commit in `00_kern/ast_stand.json`, der über Git
auf beide Rechner wandert.

Lesen ist damit transparent. Zurück in den Hub fließt weiterhin nur, was über
die festen Wege läuft (Lernkarte, Framework-Registereintrag, Case Study), nach
`00_kern/vertraulichkeit.md` anonymisiert und vom Nutzer freigegeben.

Aufruf:
    python 00_kern/ast_stand.py neu      [AST]           Commits seit dem letzten Blick
    python 00_kern/ast_stand.py liste    [AST] [PRÄFIX]  sichtbare Dateien
    python 00_kern/ast_stand.py zeige    AST PFAD        Inhalt einer sichtbaren Datei
    python 00_kern/ast_stand.py gesehen  [AST] [SHA]     Blick bis HEAD (oder SHA) quittieren

AST ist standardmäßig der erste Ast mit GitHub-Repo in
`00_kern/einstellungen.json`. Voraussetzung ist ein angemeldetes `gh`.
"""
from __future__ import annotations
import json
import subprocess
import sys
from datetime import date
from fnmatch import fnmatch
from pathlib import Path
from urllib.parse import quote

STAND = Path(__file__).resolve().parent / "ast_stand.json"
OHNE_STAND = 15  # so viele Commits zeigt `neu`, solange noch nichts quittiert ist

# Die Äste stehen in 00_kern/einstellungen.json unter "aeste", je Ast mit
# repo (Besitzer/Name auf GitHub), zweig und den Mustern "sichtbar" und
# "verborgen". Muster nach fnmatch, ein * greift auch über Ordnergrenzen.
# Ausschlüsse haben Vorrang, damit Analysen und Archive nicht über ein tiefer
# liegendes methodology/ oder kpis/ doch sichtbar werden.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import einstellungen  # noqa: E402


def aeste_laden() -> dict:
    return {a["name"]: a for a in einstellungen.aeste() if a.get("repo")}


def sichtbar(pfad: str, ast: dict) -> bool:
    if any(fnmatch(pfad, m) for m in ast["verborgen"]):
        return False
    return any(fnmatch(pfad, m) for m in ast["sichtbar"])


def gh(pfad: str, roh: bool = False) -> str:
    befehl = ["gh", "api", pfad]
    if roh:
        befehl += ["-H", "Accept: application/vnd.github.raw"]
    lauf = subprocess.run(befehl, capture_output=True, text=True, encoding="utf-8")
    if lauf.returncode != 0:
        sys.exit(f"gh api {pfad} scheitert: {lauf.stderr.strip()}")
    return lauf.stdout


def gh_json(pfad: str):
    return json.loads(gh(pfad))


def lies_stand() -> dict:
    if not STAND.exists():
        return {}
    return json.loads(STAND.read_text(encoding="utf-8"))


def schreib_stand(stand: dict) -> None:
    STAND.write_text(json.dumps(stand, indent=2, ensure_ascii=False) + "\n",
                     encoding="utf-8", newline="\n")


def commits_seit(ast: dict, basis: str | None, api=gh_json) -> list[dict]:
    """Commits von alt nach neu. Ohne Basis die letzten OHNE_STAND."""
    repo, zweig = ast["repo"], ast["zweig"]
    if basis:
        commits = api(f"repos/{repo}/compare/{basis}...{zweig}")["commits"]
    else:
        commits = api(f"repos/{repo}/commits?sha={zweig}&per_page={OHNE_STAND}")
        commits.reverse()
    return commits


def neu(name: str, ast: dict, api=gh_json) -> list[str]:
    basis = lies_stand().get(name, {}).get("gesehen")
    commits = commits_seit(ast, basis, api)
    zeilen = [f"{name}, {len(commits)} Commits seit "
              + (basis[:7] if basis else f"Beginn (letzte {OHNE_STAND})")]
    for c in commits:
        sha = c["sha"]
        tag = c["commit"]["author"]["date"][:10]
        titel = c["commit"]["message"].splitlines()[0]
        dateien = [f["filename"] for f in api(f"repos/{ast['repo']}/commits/{sha}").get("files", [])]
        offen = [d for d in dateien if sichtbar(d, ast)]
        zeilen.append(f"\n{tag}  {sha[:7]}  {titel}")
        zeilen += [f"    {d}" for d in offen]
        if len(dateien) > len(offen):
            zeilen.append(f"    (+ {len(dateien) - len(offen)} verborgene Dateien)")
    return zeilen


def liste(ast: dict, praefix: str = "", api=gh_json) -> list[str]:
    baum = api(f"repos/{ast['repo']}/git/trees/{ast['zweig']}?recursive=1")["tree"]
    return [b["path"] for b in baum
            if b["type"] == "blob" and b["path"].startswith(praefix) and sichtbar(b["path"], ast)]


def zeige(ast: dict, pfad: str, holen=gh) -> str:
    if not sichtbar(pfad, ast):
        sys.exit(f"{pfad} steht nicht auf der Positivliste und wird nicht gelesen.")
    return holen(f"repos/{ast['repo']}/contents/{quote(pfad)}?ref={ast['zweig']}", roh=True)


def gesehen(name: str, ast: dict, sha: str | None = None, api=gh_json) -> str:
    if not sha:
        sha = api(f"repos/{ast['repo']}/commits/{ast['zweig']}")["sha"]
    stand = lies_stand()
    stand[name] = {"gesehen": sha, "am": date.today().isoformat()}
    schreib_stand(stand)
    return sha


def main(argv: list[str]) -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    if not argv or argv[0] not in {"neu", "liste", "zeige", "gesehen"}:
        sys.exit(__doc__)
    befehl, rest = argv[0], argv[1:]
    aste = aeste_laden()
    if not aste:
        sys.exit("Kein Ast mit GitHub-Repo in 00_kern/einstellungen.json. Erst /einrichten oder /ast-anlegen.")
    name = rest.pop(0) if rest and rest[0] in aste else next(iter(aste))
    ast = aste[name]
    if befehl == "neu":
        print("\n".join(neu(name, ast)))
    elif befehl == "liste":
        print("\n".join(liste(ast, rest[0] if rest else "")))
    elif befehl == "zeige":
        if not rest:
            sys.exit("Pfad fehlt.")
        print(zeige(ast, rest[0]))
    else:
        sha = gesehen(name, ast, rest[0] if rest else None)
        print(f"{name} gesehen bis {sha[:7]}")


if __name__ == "__main__":
    main(sys.argv[1:])
