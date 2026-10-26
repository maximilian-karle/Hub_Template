import json
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import alter  # noqa: E402
import engine  # noqa: E402

HEUTE = date(2026, 11, 2)

MODUL = """# M99 Testmodul

## Erster Durchlauf

| Block | spätestens | Inhalt | Quelle | Spur | h max | Nachweis |
|---|---|---|---|---|---|---|
| K1 | 10.11.2026 | Grundlagen | M99-K00, Werk Kap. 1 | Kern | 2 | Kontrollfragen |
| K2 | 20.11.2026 | Vertiefung | M99-K01, Werk Kap. 2 | Kern | 2 | ADR verteidigt |
| U1 | 05.11.2026 | Übung | wie K2 | U | 2 | Designblatt |

| spätestens | Output | Prüfung |
|---|---|---|
| G1, 12.11.2026 | K1 fertig | Erklär-Check G1 |
"""


def tag(n):
    return HEUTE + timedelta(days=n)


def umgebung(tmp_path, verlauf=()):
    (tmp_path / "karten").mkdir(parents=True)
    (tmp_path / "module" / "M99_test").mkdir(parents=True)
    (tmp_path / "module" / "M99_test" / "modul.md").write_text(MODUL, encoding="utf-8")
    (tmp_path / "verbindungen").mkdir()
    (tmp_path / "verlauf.json").write_text(json.dumps({"eintraege": list(verlauf)}), encoding="utf-8")
    return tmp_path


def lauf(u, heute=HEUTE, **kw):
    return alter.naechste(heute=heute, karten_ordner=u / "karten", module=u / "module",
                          verlauf_pfad=u / "verlauf.json", rueckstau=u / "rueckstau.json",
                          verbindungen=u / "verbindungen", **kw)


def eintrag(schritt, block=None, abschnitte=(), modus=None, datum=HEUTE):
    return {"datum": datum.isoformat(), "schritt": schritt, "modus": modus,
            "modul": "M99" if block else None, "block": block, "abschnitte": list(abschnitte)}


def karte(u, abschnitt, noten=(), zuversicht=None, start=-30):
    k = engine.anlegen(u / "karten", "p", abschnitt, "Begriff", "f", "a", "Werk Kap. 1",
                       frei=True, heute=tag(start))
    for i, q in enumerate(noten):
        engine.bewerten(u / "karten", [(k["id"], q) + ((zuversicht,) if zuversicht is not None else ())],
                        heute=tag(start + 1 + i))
    return k


def test_modulplan_liest_bloecke_verweise_und_meilensteine(tmp_path):
    u = umgebung(tmp_path)
    bloecke, meilensteine = alter.modulplan(u / "module" / "M99_test" / "modul.md")
    u1 = [b for b in bloecke if b["block"] == "U1"][0]
    assert u1["verweise"] == ["K2"] and u1["abschnitte"] == ["M99-K01"]
    assert [b["abschnitte"] for b in bloecke if b["spur"] == "Kern"] == [["M99-K00"], ["M99-K01"]]
    assert meilensteine[0]["name"] == "G1" and meilensteine[0]["datum"] == date(2026, 11, 12)


def test_abschluss_modus_aus_nachweis():
    assert alter.abschluss_modus("Kontrollfragen LP") == "test"
    assert alter.abschluss_modus("Erklär-Check G1") == "feynman"
    assert alter.abschluss_modus("ADR-002 verteidigt") == "feynman"
    assert alter.abschluss_modus("Schema in DuckDB") == "editor"


def test_faellige_karten_gehen_vor_und_nur_einmal_am_tag(tmp_path):
    u = umgebung(tmp_path)
    karte(u, "M99-K00", noten=[4], start=-3)
    assert lauf(u)["schritt"] == "heute"
    (u / "verlauf.json").write_text(json.dumps({"eintraege": [eintrag("heute")]}), encoding="utf-8")
    assert lauf(u)["schritt"] != "heute"


def test_minimalbetrieb_nur_wiederholung(tmp_path):
    u = umgebung(tmp_path)
    assert lauf(u, minimal=True)["schritt"] == "pause"


def test_spur_wartet_auf_gelesenen_kern(tmp_path):
    u = umgebung(tmp_path)
    v = lauf(u)
    # U1 hat den frühesten Termin, verweist aber auf K2, das noch nicht gelesen ist
    assert (v["block"], v["schritt"], v["befehl"]) == ("K1", "feynman_start", "/tutor feynman M99-K00")


def test_kern_block_durchlaeuft_alle_schritte_und_lesen_schaltet_frei(tmp_path):
    u = umgebung(tmp_path)
    k = engine.anlegen(u / "karten", "p", "M99-K00", "Begriff", "f", "a", "Werk Kap. 1", heute=tag(-1))
    gesehen = []
    for _ in range(6):
        v = lauf(u)
        gesehen.append(v["schritt"])
        alter.erledigt(v, verlauf_pfad=u / "verlauf.json", karten_ordner=u / "karten")
    assert gesehen == list(alter.KERN_SCHRITTE)
    assert not engine.zeigen(u / "karten", [k["id"]])[0]["gesperrt"]


def test_freigeschalteter_kern_beginnt_nach_dem_lesen(tmp_path):
    u = umgebung(tmp_path)
    engine.anlegen(u / "karten", "p", "M99-K00", "Begriff", "f", "a", "Werk Kap. 1", frei=True, heute=tag(-1))
    v = lauf(u)
    assert (v["regel"], v["block"], v["schritt"]) == (5, "K1", "sokrates")


def test_problemkarte_schickt_zu_sokrates_bis_er_gelaufen_ist(tmp_path):
    u = umgebung(tmp_path)
    karte(u, "M99-K00", noten=[4, 2, 1], start=-10)
    (u / "verlauf.json").write_text(json.dumps({"eintraege": [eintrag("heute", datum=tag(-5))]}),
                                    encoding="utf-8")
    v = lauf(u, heute=tag(-5))
    assert (v["regel"], v["befehl"]) == (2, "/tutor sokrates M99-K00")
    (u / "verlauf.json").write_text(json.dumps({"eintraege": [
        eintrag("heute", datum=tag(-5)), eintrag("sokrates_luecke", "K1", ["M99-K00"], "sokrates", tag(-5))]}),
        encoding="utf-8")
    assert lauf(u, heute=tag(-5))["regel"] != 2


def test_illusion_des_wissens_schickt_zu_feynman(tmp_path):
    u = umgebung(tmp_path)
    karte(u, "M99-K01", noten=[4, 2], zuversicht=80, start=-6)
    karte(u, "M99-K01", noten=[4, 2], zuversicht=90, start=-6)
    (u / "verlauf.json").write_text(json.dumps({"eintraege": [eintrag("heute")]}), encoding="utf-8")
    v = lauf(u)
    # beide Karten scheitern nur einmal, Regel 2 greift nicht, Regel 3 schon
    assert (v["regel"], v["befehl"]) == (3, "/tutor feynman M99-K01")


def test_sitzender_abschnitt_feynman_mit_abstand_dann_editor(tmp_path):
    u = umgebung(tmp_path)
    for _ in range(alter.ABSTAND_MIN_KARTEN):
        k = karte(u, "M99-K00", noten=[5, 5, 5], start=-60)
        engine.bewerten(u / "karten", [(k["id"], 5)], heute=tag(-20))
    assert all(engine.sitzt(k) for _, k in engine.alle_karten(u / "karten"))
    v = lauf(u)
    assert (v["regel"], v["schritt"]) == (4, "feynman_abstand")
    alter.erledigt(v, verlauf_pfad=u / "verlauf.json", karten_ordner=u / "karten")
    v = lauf(u)
    assert (v["regel"], v["schritt"], v["rolle"]) == (4, "editor_abstand", "E")


def test_meilenstein_nach_den_bloecken_davor(tmp_path):
    erledigt = [eintrag(s, "K1") for s in alter.KERN_SCHRITTE]
    u = umgebung(tmp_path, erledigt)
    # U1 liegt vor G1 und ist offen, also noch kein Meilenstein
    assert lauf(u)["regel"] != 6
    erledigt += [eintrag(s, "U1") for s in alter.SPUR_SCHRITTE]
    u = umgebung(tmp_path / "zwei", erledigt)
    v = lauf(u)
    assert (v["regel"], v["schritt"], v["block"], v["abschnitte"]) == (6, "gate", "G1", ["M99-K00", "M99-K01"])


def test_alles_erledigt_fuehrt_zum_advisor(tmp_path):
    erledigt = ([eintrag(s, b) for b in ("K1", "K2") for s in alter.KERN_SCHRITTE]
                + [eintrag(s, "U1") for s in alter.SPUR_SCHRITTE] + [eintrag("gate", "G1")])
    u = umgebung(tmp_path, erledigt)
    assert lauf(u)["befehl"] == "/advisor"


def test_hinweise_review_und_roommate(tmp_path):
    u = umgebung(tmp_path)
    (u / "rueckstau.json").write_text(json.dumps([{"datum": tag(-8).isoformat(), "last_sek": 0}]))
    h = lauf(u)["hinweise"]
    assert any("/weekly-review" in x for x in h) and any("/roommate" in x for x in h)
    (u / "rueckstau.json").write_text(json.dumps([{"datum": tag(-2).isoformat(), "last_sek": 0}]))
    (u / "verbindungen" / f"{HEUTE:%Y-%m}_thema.md").write_text("x", encoding="utf-8")
    assert lauf(u)["hinweise"] == []


def test_ohne_modul_und_karten_fuehrt_zum_advisor(tmp_path):
    v = alter.naechste(heute=HEUTE, karten_ordner=tmp_path / "karten", module=tmp_path / "module",
                       verlauf_pfad=tmp_path / "verlauf.json", rueckstau=tmp_path / "rueckstau.json",
                       verbindungen=tmp_path / "verbindungen")
    assert (v["regel"], v["befehl"]) == (8, "/advisor") and "/aufnahme" in v["grund"]


def test_verlauf_als_leere_liste(tmp_path):
    (tmp_path / "verlauf.json").write_text("[]", encoding="utf-8")
    assert alter.verlauf_laden(tmp_path / "verlauf.json") == []
    alter.erledigt({"datum": HEUTE.isoformat(), "schritt": "heute"}, verlauf_pfad=tmp_path / "verlauf.json",
                   karten_ordner=tmp_path)
    assert len(alter.verlauf_laden(tmp_path / "verlauf.json")) == 1


def test_arbeitsort_aus_den_aesten():
    daten = {"aeste": [{"name": "Firma", "art": "arbeit", "spur": "A", "repo": "nutzer/Firma"}]}
    assert "Ast Firma" in alter.wo_arbeiten("A", daten)
    assert "/einrichten" in alter.wo_arbeiten("U", daten)
    assert "öffentlichen Daten" in alter.wo_arbeiten("Ö", daten)
