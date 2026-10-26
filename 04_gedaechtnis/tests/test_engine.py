import json
import sys
from datetime import date, timedelta
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import engine  # noqa: E402

HEUTE = date(2026, 11, 2)


def tag(n):
    return HEUTE + timedelta(days=n)


def karte(ordner, **kw):
    args = dict(projekt="ml", abschnitt="XY3-K01", typ="Begriff", frage="Was ist Bias?",
                antwort="Systematischer Fehler", quelle="ISLP Kap. 2", frei=True, heute=HEUTE)
    args.update(kw)
    return engine.anlegen(ordner, **args)


# Intervalle

def test_erste_intervalle_sind_1_und_6_dann_ef_mal_intervall():
    z = engine.neuer_zustand()
    engine.sm2_step(z, 4, HEUTE)
    assert z["interval_days"] == 1
    engine.sm2_step(z, 4, tag(1))
    assert z["interval_days"] == 6
    engine.sm2_step(z, 4, tag(7))
    assert z["interval_days"] == round(6 * 2.5)
    assert z["due_date"] == tag(7 + 15).isoformat()


@pytest.mark.parametrize("q,delta", [(5, 0.1), (4, 0.0), (3, -0.14), (2, -0.32), (0, -0.8)])
def test_easiness_aenderung_je_qualitaet(q, delta):
    z = engine.neuer_zustand()
    engine.sm2_step(z, q, HEUTE)
    assert z["easiness_factor"] == pytest.approx(max(engine.EF_MIN, 2.5 + delta), abs=1e-4)


def test_easiness_faellt_nie_unter_minimum():
    z = engine.neuer_zustand()
    for i in range(10):
        engine.sm2_step(z, 0, tag(i))
    assert z["easiness_factor"] == engine.EF_MIN


def test_falsche_antwort_holt_die_karte_ins_erste_fach_zurueck():
    z = engine.neuer_zustand()
    for d in (0, 1, 7):
        engine.sm2_step(z, 5, tag(d))
    engine.sm2_step(z, 2, tag(30))
    assert z["repetitions"] == 0
    assert z["interval_days"] == 1
    assert z["due_date"] == tag(31).isoformat()


def test_schwere_karte_startet_mit_engerem_ef():
    assert engine.neuer_zustand(schwer=True)["easiness_factor"] == engine.EF_START_SCHWER


def test_verspaetung_kuerzt_die_basis():
    z = engine.neuer_zustand()
    engine.sm2_step(z, 4, HEUTE)
    engine.sm2_step(z, 4, tag(1))
    engine.sm2_step(z, 4, tag(7))          # Intervall 15
    letzte = date.fromisoformat(z["last_reviewed"])
    engine.sm2_step(z, 4, letzte + timedelta(days=40))
    basis = 15 * engine.VERSPAETUNG_AB / (40 / 15)
    assert z["interval_days"] == round(basis * 2.5)
    assert z["interval_days"] < round(15 * 2.5)


def test_puenktlich_und_leicht_spaet_ohne_kuerzung():
    z = engine.neuer_zustand()
    engine.sm2_step(z, 4, HEUTE)
    engine.sm2_step(z, 4, tag(1))
    engine.sm2_step(z, 4, tag(7))
    letzte = date.fromisoformat(z["last_reviewed"])
    engine.sm2_step(z, 4, letzte + timedelta(days=25))   # Verhältnis 1,67
    assert z["interval_days"] == round(15 * 2.5)


def test_qualitaet_ausserhalb_des_bereichs_ist_fehler():
    z = engine.neuer_zustand()
    with pytest.raises(ValueError):
        engine.sm2_step(z, 6, HEUTE)
    with pytest.raises(ValueError):
        engine.sm2_step(z, 3, HEUTE, zuversicht=101)
    assert z["review_history"] == []


def test_zuversicht_wird_nur_bei_angabe_gespeichert():
    z = engine.neuer_zustand()
    engine.sm2_step(z, 4, HEUTE)
    engine.sm2_step(z, 4, tag(1), zuversicht=70)
    assert "zuversicht" not in z["review_history"][0]
    assert z["review_history"][1]["zuversicht"] == 70


# Drei Zustände

def test_neue_karte_ist_ohne_frei_gesperrt(tmp_path):
    k = karte(tmp_path, frei=False)
    assert engine.zustand(k) == "gesperrt"
    assert k["freigeschaltet"] is None
    assert engine.neue(tmp_path) == []
    assert not engine.ist_faellig(k, tag(100))


def test_freischalten_je_abschnitt(tmp_path):
    a = karte(tmp_path, frei=False, abschnitt="XY2-K00")
    b = karte(tmp_path, frei=False, abschnitt="XY2-K00", projekt="mathe")
    c = karte(tmp_path, frei=False, abschnitt="XY2-K01")
    frei = engine.freischalten(tmp_path, "XY2-K00", tag(3))
    assert sorted(frei) == sorted([a["id"], b["id"]])
    zustaende = {k["id"]: (engine.zustand(k), k["freigeschaltet"]) for _, k in engine.alle_karten(tmp_path)}
    assert zustaende[a["id"]] == ("bereit", tag(3).isoformat())
    assert zustaende[c["id"]] == ("gesperrt", None)
    assert engine.freischalten(tmp_path, "XY2-K00", tag(4)) == []


def test_gesperrte_karte_laesst_sich_nicht_bewerten(tmp_path):
    k = karte(tmp_path, frei=False)
    with pytest.raises(ValueError):
        engine.bewerten(tmp_path, [(k["id"], 4)], HEUTE)


def test_bereit_dann_im_kasten_dann_sitzt(tmp_path):
    k = karte(tmp_path)
    assert engine.zustand(k) == "bereit"
    for d in (0, 1, 7, 22):
        engine.bewerten(tmp_path, [(k["id"], 5)], tag(d))
    k = engine.alle_karten(tmp_path)[0][1]
    assert engine.zustand(k) == "im_kasten"
    assert engine.sitzt(k)


def test_neue_karte_ist_nicht_faellig_aber_bereit(tmp_path):
    k = karte(tmp_path)
    assert engine.ist_neu(k)
    assert not engine.ist_faellig(k, HEUTE)
    assert engine.faellige(tmp_path, heute=HEUTE) == []
    assert [x["id"] for x in engine.neue(tmp_path)] == [k["id"]]


def test_neue_in_reihenfolge_des_lesepfads(tmp_path):
    spaet = karte(tmp_path, abschnitt="XY2-K02")
    frueh1 = karte(tmp_path, abschnitt="XY2-K00")
    frueh2 = karte(tmp_path, abschnitt="XY2-K00")
    assert [k["id"] for k in engine.neue(tmp_path)] == [frueh1["id"], frueh2["id"], spaet["id"]]


# Fälligkeit

def test_faellig_ab_dem_faelligkeitstag(tmp_path):
    k = karte(tmp_path)
    engine.bewerten(tmp_path, [(k["id"], 4)], HEUTE)
    assert engine.faellige(tmp_path, heute=HEUTE) == []
    assert [x["id"] for x in engine.faellige(tmp_path, heute=tag(1))] == [k["id"]]
    assert [x["id"] for x in engine.faellige(tmp_path, heute=tag(30))] == [k["id"]]


def test_verfehlte_karte_ist_nicht_mehr_neu(tmp_path):
    k = karte(tmp_path)
    engine.bewerten(tmp_path, [(k["id"], 0)], HEUTE)
    assert engine.neue(tmp_path) == []
    assert engine.ist_faellig(engine.alle_karten(tmp_path)[0][1], tag(1))


def test_faellige_ueber_projekte_nach_ueberfaelligkeit(tmp_path):
    a = karte(tmp_path)
    b = karte(tmp_path, frage="Varianz?")
    c = karte(tmp_path, projekt="englisch", frage="Rang?")
    engine.bewerten(tmp_path, [(b["id"], 4)], tag(-5))
    engine.bewerten(tmp_path, [(a["id"], 4)], tag(-2))
    engine.bewerten(tmp_path, [(c["id"], 4)], tag(-9))
    ids = [k["id"] for k in engine.faellige(tmp_path, heute=HEUTE)]
    assert ids == [c["id"], b["id"], a["id"]]
    assert [k["id"] for k in engine.faellige(tmp_path, heute=HEUTE, limit=2)] == ids[:2]
    assert [k["id"] for k in engine.faellige(tmp_path, projekt="ml", heute=HEUTE)] == ids[1:]


# Anlegen und bewerten

def test_anlegen_vergibt_fortlaufende_ids_und_alle_felder(tmp_path):
    k1 = karte(tmp_path)
    k2 = karte(tmp_path, typ="Rechnung")
    assert (k1["id"], k2["id"]) == ("ml-001", "ml-002")
    for feld in ("id", "projekt", "abschnitt", "typ", "frage", "antwort", "quelle",
                 "gesperrt", "freigeschaltet", "lernzustand"):
        assert feld in k1
    daten = json.loads((tmp_path / "ml.json").read_text(encoding="utf-8"))
    assert len(daten["karten"]) == 2


def test_anlegen_prueft_typ_quelle_abschnitt_und_doppelte_id(tmp_path):
    with pytest.raises(ValueError):
        karte(tmp_path, typ="Vokabel")
    with pytest.raises(ValueError):
        karte(tmp_path, quelle="  ")
    with pytest.raises(ValueError):
        karte(tmp_path, abschnitt="")
    with pytest.raises(ValueError):
        karte(tmp_path, frage="")
    with pytest.raises(ValueError):
        karte(tmp_path, projekt="ML-Projekt")
    karte(tmp_path, karten_id="x-1")
    with pytest.raises(ValueError):
        karte(tmp_path, karten_id="x-1")
    assert len(engine.alle_karten(tmp_path)) == 1


def test_id_ist_ueber_projekte_eindeutig(tmp_path):
    karte(tmp_path, projekt="a", karten_id="gemeinsam")
    with pytest.raises(ValueError):
        karte(tmp_path, projekt="b", karten_id="gemeinsam")


def test_bewerten_bricht_bei_unbekannter_id_ab_ohne_zu_schreiben(tmp_path):
    k = karte(tmp_path)
    with pytest.raises(KeyError):
        engine.bewerten(tmp_path, [(k["id"], 4), ("gibt-es-nicht", 4)], HEUTE)
    assert engine.ist_neu(engine.alle_karten(tmp_path)[0][1])


def test_bewerten_mit_zuversicht_ueber_mehrere_projekte(tmp_path):
    a = karte(tmp_path)
    b = karte(tmp_path, projekt="englisch")
    engine.bewerten(tmp_path, [(a["id"], 5, 90), (b["id"], 3)], HEUTE)
    karten = dict(engine.alle_karten(tmp_path))
    assert karten["ml"]["lernzustand"]["review_history"][0]["zuversicht"] == 90
    assert karten["englisch"]["lernzustand"]["repetitions"] == 1


def test_zeigen_liefert_karten_in_angefragter_reihenfolge(tmp_path):
    a = karte(tmp_path)
    b = karte(tmp_path, frage="zwei")
    assert [k["id"] for k in engine.zeigen(tmp_path, [b["id"], a["id"]])] == [b["id"], a["id"]]
    with pytest.raises(KeyError):
        engine.zeigen(tmp_path, ["nope"])


def test_statistik_je_zustand(tmp_path):
    a = karte(tmp_path)
    karte(tmp_path, frage="bereit")
    karte(tmp_path, frage="gesperrt", frei=False)
    engine.bewerten(tmp_path, [(a["id"], 4)], tag(-3))
    s = engine.statistik(tmp_path, HEUTE)
    assert s["ml"] == {"gesamt": 3, "gesperrt": 1, "bereit": 1, "im_kasten": 1,
                       "faellig": 1, "sitzt": 0}
    assert engine.zahl_faellig(tmp_path, HEUTE) == 1


# Aufruf

def test_cli_add_freischalten_review_zahl(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(engine, "KARTEN", tmp_path)
    basis = ["add", "--projekt", "ml", "--abschnitt", "XY3-K01", "--typ", "Begriff",
             "--frage", "F", "--antwort", "A"]
    assert engine.main(basis + ["--quelle", "ISLP Kap. 3"]) == 0
    assert engine.main(["review", "ml-001:4"]) == 1          # noch gesperrt
    assert engine.main(["freischalten", "XY3-K01"]) == 0
    assert engine.main(["review", "ml-001:4:60"]) == 0
    assert "nächste Wiederholung" in capsys.readouterr().out
    assert engine.main(basis) == 1                            # ohne Quelle
    assert engine.main(["review", "nope:4"]) == 1
    capsys.readouterr()
    assert engine.main(["zahl"]) == 0
    assert capsys.readouterr().out.strip() == "0"
