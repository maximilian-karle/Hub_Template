import json
import shutil
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import einrichten  # noqa: E402
import einstellungen  # noqa: E402

VORLAGE = Path(__file__).resolve().parents[2]


@pytest.fixture
def hub(tmp_path, monkeypatch):
    """Ein leerer Hub mit Einstellungen und Ast-Vorlage im temporären Ordner."""
    h = tmp_path / "Hub"
    (h / "00_kern").mkdir(parents=True)
    shutil.copy(VORLAGE / "00_kern" / "einstellungen.json", h / "00_kern" / "einstellungen.json")
    shutil.copytree(VORLAGE / "vorlagen" / "ast", h / "vorlagen" / "ast")
    monkeypatch.setattr(einrichten, "VORLAGE_AST", h / "vorlagen" / "ast")
    return h


def _daten(hub):
    return json.loads((hub / "00_kern" / "einstellungen.json").read_text(encoding="utf-8"))


def test_ast_anlegen_kopiert_und_traegt_ein(hub):
    ziel = einrichten.ast_anlegen("AT_FIRMA", "arbeit", "a", "Englisch", None, hub=hub, mit_git=False)
    assert ziel == (hub.parent / "AT_FIRMA").resolve()
    assert (ziel / "CLAUDE.md").exists()
    assert (ziel / ".gitignore").exists()
    assert not (ziel / "CLAUDE.md.vorlage").exists()
    claude = (ziel / "CLAUDE.md").read_text(encoding="utf-8")
    assert "{{" not in claude and "AT_FIRMA" in claude and "Spur A" in claude
    assert json.loads((ziel / "ast.json").read_text(encoding="utf-8"))["spur"] == "A"
    ast = einstellungen.ast_nach_name("AT_FIRMA", _daten(hub))
    assert ast["art"] == "arbeit" and ast["repo"] == "" and "*/data/*" in ast["verborgen"]


def test_ast_spur_und_name_eindeutig(hub):
    einrichten.ast_anlegen("AT_FIRMA", "arbeit", "A", "Englisch", None, hub=hub, mit_git=False)
    with pytest.raises(SystemExit):
        einrichten.ast_anlegen("ST_FIRMA", "selbststaendig", "A", "Deutsch", None, hub=hub, mit_git=False)
    with pytest.raises(SystemExit):
        einrichten.ast_anlegen("at_firma", "sonstig", "V", "Deutsch", None, hub=hub, mit_git=False)
    with pytest.raises(SystemExit):
        einrichten.ast_anlegen("OEFFENTLICH", "sonstig", "Ö", "Deutsch", None, hub=hub, mit_git=False)


def test_spuren_enthalten_oeffentlich(hub):
    einrichten.ast_anlegen("ST_UG", "selbststaendig", "U", "Deutsch", None, hub=hub, mit_git=False)
    assert einstellungen.spuren(_daten(hub)) == ["U", "Ö"]


def test_erledigt_und_status(monkeypatch, tmp_path, capsys):
    datei = tmp_path / "e.json"
    datei.write_text(json.dumps({"eingerichtet": False}), encoding="utf-8")
    monkeypatch.setattr(einstellungen, "DATEI", datei)
    monkeypatch.setattr(einstellungen.laden, "__defaults__", (datei,))
    monkeypatch.setattr(einstellungen.speichern, "__defaults__", (datei,))
    einrichten.erledigt("technik")
    einrichten.erledigt("technik")
    assert json.loads(datei.read_text(encoding="utf-8"))["einrichtung"]["erledigt"] == ["technik"]
    einrichten.status()
    assert "Nächster Schritt: person" in capsys.readouterr().out
    with pytest.raises(SystemExit):
        einrichten.erledigt("gibtsnicht")
