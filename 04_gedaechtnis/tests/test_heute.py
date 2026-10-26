import json
import sys
from datetime import date, timedelta
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import engine  # noqa: E402
import heute  # noqa: E402

HEUTE = date(2026, 11, 2)


def tag(n):
    return HEUTE + timedelta(days=n)


def faellige(ordner, projekt, n, typ="Begriff", abschnitt="XY2-K00"):
    """n Karten im Kasten, überfällig, die ersten am längsten."""
    ids = []
    for i in range(n):
        k = engine.anlegen(ordner, projekt, abschnitt, typ, f"f{i}", "a", "Quelle Kap. 1",
                           frei=True, heute=tag(-60))
        engine.bewerten(ordner, [(k["id"], 4)], tag(-5 - (n - i)))
        ids.append(k["id"])
    return ids


def bereite(ordner, projekt, n, frei_seit=0, typ="Begriff", abschnitt="XY2-K01"):
    """n freigeschaltete, nie abgerufene Karten, freigeschaltet vor `frei_seit` Tagen."""
    return [engine.anlegen(ordner, projekt, abschnitt, typ, f"n{i}", "a", "Quelle Kap. 1",
                           frei=True, heute=tag(-frei_seit))["id"] for i in range(n)]


def lauf(ordner, **kw):
    return heute.plan(ordner=ordner, heute=HEUTE, **kw)


def zeit_von(ordner, ids):
    return sum(heute.kosten(k) for k in engine.zeigen(ordner, ids))


# Obergrenze und Gleichgewicht

def test_obergrenze_folgt_aus_dem_gleichgewicht():
    assert heute.neu_max(15 * 60) == 6
    assert heute.neu_max(20 * 60) == 8
    assert heute.neu_max(30 * 60) == 12
    assert heute.neu_max(60) == heute.MIN_NEU


def test_tagesbudget_aus_den_einstellungen_in_der_spanne():
    assert heute.standard_minuten({"lernen": {"wiederholung_min_tag": 25}}) == 25
    assert heute.standard_minuten({"lernen": {"wiederholung_min_tag": 90}}) == heute.MAX_MINUTEN
    assert heute.standard_minuten({"lernen": {"wiederholung_min_tag": 5}}) == heute.MIN_MINUTEN
    assert heute.standard_minuten({}) == heute.VORGABE_MINUTEN


def test_ohne_karten_ist_nichts_dran(tmp_path):
    p = lauf(tmp_path / "fehlt", minuten=20)
    assert p["wiederholung"] == [] and p["neu"] == [] and p["zeit_sek"] == 0


# Wiederholung zuerst

def test_wiederholung_zuerst_neues_fuellt_den_rest(tmp_path):
    w = faellige(tmp_path, "ml", 10)                  # 300 s
    n = bereite(tmp_path, "ml", 20)
    p = lauf(tmp_path, minuten=15)
    assert p["wiederholung"] == w
    assert p["neu_erlaubt"]
    assert len(p["neu"]) == heute.neu_max(900)
    assert set(p["neu"]) <= set(n)


def test_wiederholung_ueber_projekte_nach_ueberfaelligkeit(tmp_path):
    a = engine.anlegen(tmp_path, "ml", "XY2-K00", "Begriff", "a", "a", "Q", frei=True, heute=tag(-60))
    b = engine.anlegen(tmp_path, "englisch", "E1-01", "Begriff", "b", "b", "Q", frei=True, heute=tag(-60))
    engine.bewerten(tmp_path, [(a["id"], 4)], tag(-3))
    engine.bewerten(tmp_path, [(b["id"], 4)], tag(-8))
    p = lauf(tmp_path, minuten=15)
    assert p["wiederholung"] == [b["id"], a["id"]]
    assert p["je_projekt"]["englisch"]["wiederholung"] == 1


def test_zeit_ueberschreitet_das_budget_nie(tmp_path):
    faellige(tmp_path, "ml", 7, typ="Rechnung")
    faellige(tmp_path, "englisch", 5, typ="Anwendung")
    bereite(tmp_path, "ml", 20, typ="Rechnung")
    bereite(tmp_path, "englisch", 20, frei_seit=40)
    for minuten in (15, 20, 30):
        p = lauf(tmp_path, minuten=minuten)
        assert zeit_von(tmp_path, p["wiederholung"] + p["neu"]) == p["zeit_sek"]
        assert p["zeit_sek"] <= minuten * 60
        assert p["ungenutzt_sek"] >= 0


def test_typ_bestimmt_die_zeitkosten(tmp_path):
    faellige(tmp_path, "ml", 3, typ="Rechnung")
    p = lauf(tmp_path, minuten=15)
    assert p["zeit_sek"] == 3 * heute.KOSTEN["Rechnung"]


# Bremse und Mindestzufluss

def test_rueckstau_ueber_der_bremse_sperrt_den_zufluss(tmp_path):
    faellige(tmp_path, "ml", 50)                      # 1500 s > 1,5 * 900 s
    bereite(tmp_path, "ml", 5)
    p = lauf(tmp_path, minuten=15)
    assert p["bremse"]
    assert not p["neu_erlaubt"]
    assert p["neu"] == []
    assert len(p["wiederholung"]) == 30
    assert p["zurueckgestellt"] == 20


def test_unter_der_bremse_kommt_der_mindestzufluss_trotz_knapper_zeit(tmp_path):
    faellige(tmp_path, "ml", 40)                      # 1200 s, über Budget, unter Bremse
    n = bereite(tmp_path, "ml", 5)
    p = lauf(tmp_path, minuten=15)
    assert not p["bremse"]
    assert p["neu"] == n[:heute.MIN_NEU]
    assert len(p["wiederholung"]) == 28               # 900 s minus 60 s Reserve
    assert p["zeit_sek"] == 900


def test_mindestzufluss_nur_aus_aktiven_abschnitten(tmp_path):
    faellige(tmp_path, "ml", 40)
    bereite(tmp_path, "ml", 5, frei_seit=30)          # nur Vorrat, nichts aktiv
    p = lauf(tmp_path, minuten=15)
    assert p["neu"] == []
    assert len(p["wiederholung"]) == 30


def test_minimalbetrieb_nur_wiederholung_zehn_minuten(tmp_path):
    faellige(tmp_path, "ml", 40)
    bereite(tmp_path, "ml", 5)
    p = lauf(tmp_path, minuten=30, minimal=True)
    assert p["modus"] == "minimal"
    assert p["minuten"] == heute.MINIMAL_MINUTEN
    assert not p["neu_erlaubt"]
    assert p["neu"] == []
    assert len(p["wiederholung"]) == 20


# Aktiv gegen Vorrat

def test_aktiv_vor_vorrat_im_verhaeltnis_70_zu_30(tmp_path):
    aktiv = bereite(tmp_path, "ml", 20, frei_seit=2, abschnitt="XY2-K01")
    vorrat = bereite(tmp_path, "ml", 20, frei_seit=40, abschnitt="XY2-K00")
    p = lauf(tmp_path, minuten=30)                    # Obergrenze 12
    assert len(p["neu"]) == 12
    assert p["neu_aktiv"] == 8                        # 70 % von 12, gerundet
    assert p["neu_vorrat"] == 4
    assert p["neu"][:8] == aktiv[:8]
    assert set(p["neu"][8:]) <= set(vorrat)


def test_aktiv_bekommt_den_anteil_des_vorrats_wenn_der_leer_ist(tmp_path):
    aktiv = bereite(tmp_path, "ml", 20, frei_seit=2)
    p = lauf(tmp_path, minuten=30)
    assert p["neu"] == aktiv[:12]


def test_vorrat_bekommt_den_anteil_der_aktiven_wenn_die_knapp_sind(tmp_path):
    aktiv = bereite(tmp_path, "ml", 3, frei_seit=2, abschnitt="XY2-K01")
    bereite(tmp_path, "ml", 20, frei_seit=40, abschnitt="XY2-K00")
    p = lauf(tmp_path, minuten=30)
    assert p["neu_aktiv"] == 3
    assert p["neu_vorrat"] == 9
    assert p["neu"][:3] == aktiv


def test_aktiv_in_reihenfolge_des_lesepfads(tmp_path):
    spaet = bereite(tmp_path, "ml", 3, abschnitt="XY2-K02")
    frueh = bereite(tmp_path, "ml", 3, abschnitt="XY2-K01")
    p = lauf(tmp_path, minuten=15)
    assert p["neu"] == frueh + spaet


def test_ohne_aktive_bekommt_der_vorrat_die_ganze_restzeit(tmp_path):
    vorrat = bereite(tmp_path, "ml", 20, frei_seit=40)
    p = lauf(tmp_path, minuten=15)
    assert p["neu_aktiv"] == 0
    assert len(p["neu"]) == heute.neu_max(900)
    assert set(p["neu"]) <= set(vorrat)


def test_ohne_vorrat_bekommen_die_aktiven_dessen_anteil(tmp_path):
    aktiv = bereite(tmp_path, "ml", 20)
    p = lauf(tmp_path, minuten=15)
    assert p["neu"] == aktiv[:heute.neu_max(900)]


def test_aktiv_heisst_in_den_letzten_14_tagen_freigeschaltet(tmp_path):
    a = bereite(tmp_path, "ml", 1, frei_seit=13)
    b = bereite(tmp_path, "ml", 1, frei_seit=14)
    karten = {k["id"]: k for k in engine.zeigen(tmp_path, a + b)}
    assert heute.ist_aktiv(karten[a[0]], HEUTE)
    assert not heute.ist_aktiv(karten[b[0]], HEUTE)


def test_zufall_im_vorrat_ist_je_tag_fest(tmp_path):
    bereite(tmp_path, "ml", 30, frei_seit=40)
    assert lauf(tmp_path, minuten=15)["neu"] == lauf(tmp_path, minuten=15)["neu"]
    anderer_tag = heute.plan(15, ordner=tmp_path, heute=tag(1))["neu"]
    assert anderer_tag != lauf(tmp_path, minuten=15)["neu"]


def test_gesperrte_karten_kommen_nie(tmp_path):
    for i in range(5):
        engine.anlegen(tmp_path, "ml", "XY2-K05", "Begriff", f"g{i}", "a", "Q", heute=HEUTE)
    p = lauf(tmp_path, minuten=30)
    assert p["neu"] == [] and p["wiederholung"] == []


# Eingaben

@pytest.mark.parametrize("minuten", [14, 31, 0, 60])
def test_minuten_ausserhalb_von_15_bis_30_sind_ein_fehler(tmp_path, minuten):
    with pytest.raises(ValueError):
        lauf(tmp_path, minuten=minuten)


def test_ohne_karten_ist_der_plan_leer_aber_gueltig(tmp_path):
    p = lauf(tmp_path, minuten=20)
    assert p["wiederholung"] == [] and p["neu"] == []
    assert p["neu_erlaubt"]


def test_plan_schreibt_nichts(tmp_path):
    faellige(tmp_path, "ml", 3)
    bereite(tmp_path, "ml", 3)
    vorher = {p: p.read_bytes() for p in tmp_path.iterdir()}
    lauf(tmp_path, minuten=20)
    assert {p: p.read_bytes() for p in tmp_path.iterdir()} == vorher


def test_aufruf_gibt_json_und_meldet_fehler(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(engine, "KARTEN", tmp_path)
    faellige(tmp_path, "ml", 1)
    assert heute.main(["--minuten", "15"]) == 0
    assert json.loads(capsys.readouterr().out)["minuten"] == 15
    assert heute.main(["--minimal"]) == 0
    assert json.loads(capsys.readouterr().out)["modus"] == "minimal"
    assert heute.main(["--minuten", "99"]) == 1
    assert heute.main(["--minuten"]) == 1
