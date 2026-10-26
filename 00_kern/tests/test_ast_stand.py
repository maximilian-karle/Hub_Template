import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import ast_stand  # noqa: E402
import einrichten  # noqa: E402

# Ein Ast so, wie ihn `einrichten.py ast` in die Einstellungen schreibt.
AST = {"name": "ARBEIT", "repo": "nutzer/ARBEIT", "zweig": "main",
       "sichtbar": einrichten.SICHTBAR, "verborgen": einrichten.VERBORGEN}


@pytest.mark.parametrize("pfad", [
    "CLAUDE.md",
    "projekte/bestand/CLAUDE.md",
    "projekte/bestand/00_Charter/Arbeitsplan.md",
    "projekte/forecast/methodology/Annahmen.md",
    "projekte/forecast/kpis/kpi_definitions.md",
    "00_kontext/Rolle.md",
    "01_frameworks/Segmentierung.md",
    ".claude/commands/bs-next.md",
])
def test_sichtbar(pfad):
    assert ast_stand.sichtbar(pfad, AST)


@pytest.mark.parametrize("pfad", [
    "projekte/bestand/data/input/export.xlsx",
    "projekte/forecast/reports/Mail_an_Vorstand.md",
    "projekte/oee/analysis/x/doku/methodology/score.md",
    "projekte/bestand/00_Charter/Projektauftrag.pdf",
    "projekte/bestand/src/build_report.py",
    "projekte/alt/archiv/methodology/alt.md",
])
def test_verborgen(pfad):
    assert not ast_stand.sichtbar(pfad, AST)


def test_zeige_verweigert_verborgene_datei():
    def holen(*_a, **_k):
        raise AssertionError("darf nicht aufgerufen werden")
    with pytest.raises(SystemExit):
        ast_stand.zeige(AST, "projekte/bestand/data/x.csv", holen)


def _api(commits, dateien):
    def api(pfad):
        if "/compare/" in pfad or "/commits?" in pfad:
            return {"commits": commits} if "/compare/" in pfad else list(reversed(commits))
        sha = pfad.rsplit("/", 1)[1]
        return {"files": [{"filename": f} for f in dateien[sha]]}
    return api


def _commit(sha, titel):
    return {"sha": sha, "commit": {"message": titel + "\n\nText", "author": {"date": "2026-10-22T08:00:00Z"}}}


def test_neu_zeigt_nur_sichtbare_dateien(tmp_path, monkeypatch):
    monkeypatch.setattr(ast_stand, "STAND", tmp_path / "stand.json")
    commits = [_commit("a" * 40, "Lesepfad ergänzt"), _commit("b" * 40, "Daten neu gezogen")]
    dateien = {
        "a" * 40: ["projekte/bestand/00_Charter/Lesepfad.md"],
        "b" * 40: ["projekte/bestand/data/input/export.xlsx"],
    }
    zeilen = ast_stand.neu("ARBEIT", AST, _api(commits, dateien))
    text = "\n".join(zeilen)
    assert "Beginn" in zeilen[0]
    assert text.index("Lesepfad ergänzt") < text.index("Daten neu gezogen")
    assert "Lesepfad.md" in text
    assert "export.xlsx" not in text
    assert "(+ 1 verborgene Dateien)" in text


def test_neu_ab_quittiertem_stand(tmp_path, monkeypatch):
    stand = tmp_path / "stand.json"
    stand.write_text(json.dumps({"ARBEIT": {"gesehen": "c" * 40}}), encoding="utf-8")
    monkeypatch.setattr(ast_stand, "STAND", stand)
    gefragt = []

    def api(pfad):
        gefragt.append(pfad)
        return {"commits": []}
    zeilen = ast_stand.neu("ARBEIT", AST, api)
    assert gefragt == [f"repos/{AST['repo']}/compare/{'c' * 40}...main"]
    assert zeilen[0].startswith("ARBEIT, 0 Commits seit ccccccc")


def test_gesehen_schreibt_head(tmp_path, monkeypatch):
    monkeypatch.setattr(ast_stand, "STAND", tmp_path / "stand.json")
    sha = ast_stand.gesehen("ARBEIT", AST, api=lambda _p: {"sha": "d" * 40})
    assert sha == "d" * 40
    assert json.loads((tmp_path / "stand.json").read_text(encoding="utf-8"))["ARBEIT"]["gesehen"] == "d" * 40


def test_aeste_laden_nur_mit_repo(monkeypatch):
    monkeypatch.setattr(ast_stand.einstellungen, "aeste",
                        lambda: [{"name": "A", "repo": "x/A"}, {"name": "B", "repo": ""}])
    assert list(ast_stand.aeste_laden()) == ["A"]
