import json
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import engine  # noqa: E402
import wochenlage  # noqa: E402

HEUTE = date(2026, 11, 2)


def tag(n):
    return HEUTE + timedelta(days=n)


def lernlog(projekte, name, zeilen):
    ordner = projekte / name
    ordner.mkdir(parents=True)
    kopf = "| Datum | Block | Minuten | Prüfung | Nachweis | Notiz |\n|---|---|---|---|---|---|\n"
    (ordner / "lernlog.md").write_text(
        kopf + "".join(f"| {d} | B | {m} | P | N | |\n" for d, m in zeilen), encoding="utf-8")


def test_minuten_nur_im_fenster_und_beide_datumsformate(tmp_path):
    lernlog(tmp_path, "statistik", [("2026-11-02", 60), ("30.10.2026", 45), ("2026-10-20", 90)])
    ist = wochenlage.ist_minuten(tmp_path, HEUTE, 7)
    assert ist["je_projekt"]["statistik"] == 105
    assert ist["minuten"] == 105


def test_budget_aus_den_einstellungen():
    assert wochenlage.deep_dive_min({"lernen": {"deep_dive_h_woche": 3}}) == 180
    assert wochenlage.deep_dive_min({"lernen": {"deep_dive_h_woche": ""}}) == 300
    assert wochenlage.deep_dive_min({}) == 300


def test_erster_kontakt_zaehlt_nicht_in_der_abrufquote(tmp_path):
    k = engine.anlegen(tmp_path, "p", "A1", "Begriff", "f", "a", "Q Kap. 1", frei=True, heute=tag(-9))
    engine.bewerten(tmp_path, [(k["id"], 0)], tag(-8))      # Erstkontakt, ausgelassen
    engine.bewerten(tmp_path, [(k["id"], 4, 80)], tag(-1))  # richtig
    engine.bewerten(tmp_path, [(k["id"], 1, 60)], tag(0))   # falsch
    q = wochenlage.abrufquote(tmp_path, HEUTE, 7)
    assert (q["abrufe"], q["richtig"], q["quote_prozent"]) == (2, 1, 50.0)
    assert q["lage"] == "unter dem Korridor"
    assert q["kalibrierung"] is None                        # unter fünf Karten mit Zuversicht


def test_ohne_abrufe_keine_quote(tmp_path):
    q = wochenlage.abrufquote(tmp_path, HEUTE, 7)
    assert q["quote_prozent"] is None and q["lage"] == "keine Abrufe"


def test_rueckstau_trend_gegen_aelteren_messpunkt(tmp_path):
    verlauf = tmp_path.parent / (tmp_path.name + "_rueckstau.json")
    verlauf.write_text(json.dumps([{"datum": tag(-7).isoformat(), "last_sek": 30}]))
    for i in range(3):
        k = engine.anlegen(tmp_path, "p", "A1", "Anwendung", f"f{i}", "a", "Q Kap. 1", frei=True, heute=tag(-60))
        engine.bewerten(tmp_path, [(k["id"], 4)], tag(-20))
    r = wochenlage.rueckstau(tmp_path, HEUTE, verlauf)
    assert r["last_sek"] == 180 and r["trend"]["richtung"] == "waechst"
    assert r["bremse"] is False


def test_merken_ueberschreibt_den_punkt_des_tages(tmp_path):
    verlauf = tmp_path.parent / (tmp_path.name + "_rueckstau.json")
    wochenlage.merken(tmp_path, HEUTE, verlauf)
    wochenlage.merken(tmp_path, HEUTE, verlauf)
    assert len(json.loads(verlauf.read_text())) == 1


def test_naechster_abschnitt_ist_der_erste_gesperrte(tmp_path):
    engine.anlegen(tmp_path, "p", "XY2-K02", "Begriff", "f", "a", "Q Kap. 1")
    engine.anlegen(tmp_path, "p", "XY2-K01", "Begriff", "f", "a", "Q Kap. 1")
    assert wochenlage.naechster_abschnitt(tmp_path)["naechster"] == "XY2-K01"
