import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import stilpruefung  # noqa: E402


@pytest.mark.parametrize("text", [
    "Das gilt – meistens.",
    "Das gilt — meistens.",
    "Das gilt - meistens.",
])
def test_fehler(text):
    assert stilpruefung.fehler(text)


@pytest.mark.parametrize("text", [
    "Supply-Chain-Reporting und 2022-2025",
    "- Listenpunkt am Zeilenanfang",
    "Im Code `a – b` ist es egal.",
    "```\nx = a - b\n```",
])
def test_kein_fehler(text):
    assert not stilpruefung.fehler(text)


@pytest.mark.parametrize("text", [
    "Ziel dieses Projekts: den Prozess dokumentieren.",
    "Erst das; dann jenes.",
])
def test_hinweis(text):
    assert any(b[1] == "hinweis" for b in stilpruefung.befunde(text))


@pytest.mark.parametrize("text", [
    "Die Ordner sind:",
    "**Engpass:** Bilanz fehlt.",
    "Note: gilt nur hier.",
    "| Spalte: A | B |",
    "## Status: offen",
    "Siehe https://example.com/pfad",
])
def test_kein_hinweis(text):
    assert not stilpruefung.befunde(text)


def test_yaml_kopf_wird_uebersprungen():
    assert not stilpruefung.befunde("---\ndescription: Liest: etwas\n---\nText.")
