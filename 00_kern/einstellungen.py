"""Einstellungen des Hub lesen, für Skripte und Befehle.

Alle persönlichen Parameter stehen in `00_kern/einstellungen.json`. Der Befehl
`/einrichten` füllt sie, danach liest jedes Skript sie von hier, statt Namen,
Äste oder Budgets im Code zu führen. So bleibt der Code für jeden Nutzer gleich.

Ein Ast ist ein eigenes Repo neben dem Hub (Arbeit, Selbständigkeit, Verein).
Jeder Ast hat eine Spur, einen Großbuchstaben, unter dem Lernprojekte im Ast
geübt werden. Üblich sind A für die Arbeit und U für das eigene Unternehmen.
Spur Ö steht für öffentliche Daten und braucht keinen Ast.

Als Modul:
    from einstellungen import laden, aeste, ast_nach_spur
"""
from __future__ import annotations
import json
from pathlib import Path

DATEI = Path(__file__).resolve().parent / "einstellungen.json"
SPUR_OEFFENTLICH = "Ö"


def laden(pfad: Path = DATEI) -> dict:
    if not Path(pfad).exists():
        return {}
    return json.loads(Path(pfad).read_text(encoding="utf-8"))


def speichern(daten: dict, pfad: Path = DATEI) -> None:
    Path(pfad).write_text(json.dumps(daten, indent=2, ensure_ascii=False) + "\n",
                          encoding="utf-8", newline="\n")


def aeste(daten: dict | None = None) -> list[dict]:
    return (laden() if daten is None else daten).get("aeste", [])


def ast_nach_name(name: str, daten: dict | None = None) -> dict | None:
    return next((a for a in aeste(daten) if a["name"].lower() == name.lower()), None)


def ast_nach_spur(spur: str, daten: dict | None = None) -> dict | None:
    return next((a for a in aeste(daten) if a.get("spur") == spur), None)


def spuren(daten: dict | None = None) -> list[str]:
    """Alle Spuren der Äste, dazu Ö für öffentliche Daten."""
    return [a["spur"] for a in aeste(daten) if a.get("spur")] + [SPUR_OEFFENTLICH]


def name(daten: dict | None = None) -> str:
    return (laden() if daten is None else daten).get("person", {}).get("name", "")
