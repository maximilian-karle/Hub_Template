"""Rendert Lebenslauf und Anschreiben aus einem Inhaltsmodul zu PDF.

Aufruf:  python3 render.py <inhaltsmodul.py> <ausgabeordner> [--final] [--schrift=NAME]

Das Inhaltsmodul liefert die Dicts CV und BRIEF (Aufbau siehe
cv_inhalt_vorlage.py). Fehlt BRIEF, entsteht nur der Lebenslauf. Gerendert
wird über einen Chromium-Browser im Headless-Modus (Edge oder Chrome), weil
das ohne zusätzliche Druckbibliotheken auf Windows und macOS läuft.

Gestaltung. Zentrierter Namenskopf mit rundem Foto, Abschnittstitel in
Versalien mit feiner Linie, Datumsspalte links, schwarz-weiß mit einer
Akzentfarbe für Hinweise. Die persönlichen Vorlieben (Schrift, Akzentfarbe,
Foto, Seitenzahl) stehen in `05_werkstatt/karriere/Profil/stil.json` und
werden von `/einrichten` (Schritt karriere) abgefragt. Mit --schrift lässt
sich eine Schrift einmalig überschreiben, der Dateiname bekommt sie dann als
Zusatz.

Prüfungen vor der Ausgabe:
- keine Gedankenstriche im sichtbaren Text, falls stil.json das verlangt
- Lebenslauf und Anschreiben höchstens so viele Seiten wie in stil.json
- mit --final zusätzlich keine offenen Platzhalter in eckigen Klammern
"""
import base64
import html
import importlib.util
import json
import os
import re
import subprocess
import sys
from pathlib import Path

from pypdf import PdfReader

# Erster vorhandener Chromium-Browser: Edge unter Windows, sonst Edge oder Chrome unter macOS.
BROWSER = [Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
           Path("/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"),
           Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")]
EDGE = next((b for b in BROWSER if b.exists()), BROWSER[0])
PROFIL = Path(__file__).resolve().parents[2] / "05_werkstatt" / "karriere" / "Profil"
FOTOS = [PROFIL / n for n in ("Bewerbungsfoto.jpg", "Bewerbungsfoto.jpeg", "Bewerbungsfoto.png")]
UNTERSCHRIFT = PROFIL / "Unterschrift.png"
STIL_DATEI = PROFIL / "stil.json"
STIL_STANDARD = {
    "schrift": "auto",
    "akzentfarbe": "#e5483f",
    "foto": True,
    "seiten_lebenslauf": 1,
    "seiten_anschreiben": 1,
    "gedankenstriche_verbieten": True,
}


def stil_laden():
    try:
        eigen = json.loads(STIL_DATEI.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        eigen = {}
    return {**STIL_STANDARD, **{k: v for k, v in eigen.items() if not k.startswith("_")}}


STIL = stil_laden()

CSS = """
@page { size: A4; margin: 0 0 8mm 0; }
:root { --text:#1e1e1e; --grau:#4a4a4a; --linie:#8c8c8c; }
* { box-sizing: border-box; }
html, body { margin: 0; background: #fff; }
body { font-family: "CVSchrift", sans-serif; color: var(--text); }
b { font-weight: bold; }

/* Lebenslauf */
.cv { width: 210mm; padding: 11mm 13mm 0 13mm; font-size: var(--cv-pt); line-height: 1.3; position: relative; }
.cv .kopf { text-align: center; padding: 4mm 0 4mm; border-bottom: 0.8pt solid var(--linie); }
.cv .kopf h1 { font-size: 27pt; font-weight: normal; letter-spacing: 0.5pt; margin: 0; line-height: 1.1; }
.cv .kopf .titel { font-size: 10pt; margin-top: 4pt; }
.cv .kopf .kontakt { font-size: 9.3pt; margin-top: 6pt; }
.cv .foto { position: absolute; top: 7mm; right: 11mm; width: 31mm; height: 31mm;
            border-radius: 50%; object-fit: cover; object-position: 50% 20%; }
.cv .foto-leer { position: absolute; top: 7mm; right: 11mm; width: 31mm; height: 31mm;
                 border-radius: 50%; background: #e6e6e6; }
.cv h2 { font-size: 12.5pt; font-weight: normal; text-transform: uppercase; margin: 7pt 0 4.5pt;
         padding-bottom: 3pt; border-bottom: 0.8pt solid var(--linie); letter-spacing: 0.2pt; }
.cv .text { text-align: justify; margin: 0; }
.eintrag { display: grid; grid-template-columns: 21mm 1fr; column-gap: 3mm; margin-bottom: 4pt;
           break-inside: avoid; }
.eintrag .zeit { text-align: center; font-weight: bold; font-size: 8.3pt; line-height: 1.35;
                 padding-top: 1pt; white-space: pre-line; }
.eintrag .zeile.mit-hinweis { display: flex; justify-content: space-between; align-items: flex-start;
                              gap: 5pt; margin-right: -9mm; }
.eintrag .zeile .hinweis { flex-shrink: 0; color: var(--rot); font-weight: bold; font-size: 7.6pt;
                           line-height: 1.15; display: flex; align-items: center; gap: 3pt; }
.hinweis .kreis { width: 12pt; height: 12pt; border: 1.3pt solid var(--rot); border-radius: 50%;
                  display: inline-flex; align-items: center; justify-content: center; font-size: 8pt; }
.eintrag .beschreibung { color: var(--grau); margin-top: 1.5pt; }
.eintrag ul { margin: 2.5pt 0 0; padding-left: 12pt; }
.eintrag li { margin-bottom: 1pt; }
.skills { display: grid; grid-template-columns: 1.25fr 1.15fr 0.8fr; column-gap: 8mm; }
.skills h3 { font-size: 10.5pt; font-weight: bold; margin: 0 0 4pt; }
.skills ul { margin: 0; padding-left: 11pt; }
.skills li { margin-bottom: 1.5pt; }
.skills .zert { margin-bottom: 3pt; }
.skills .paar { display: grid; grid-template-columns: 17mm auto; column-gap: 6pt; margin-bottom: 1.5pt; }

/* Anschreiben */
.brief { width: 210mm; padding: 20mm 22mm 0 20mm; font-size: var(--brief-pt); line-height: 1.5; }
.brief .kopf { display: flex; justify-content: space-between; align-items: flex-start; }
.brief .name { font-size: 25pt; font-weight: bold; letter-spacing: 2pt; margin-top: 11mm; line-height: 1; }
.brief .titel { font-size: 14.5pt; letter-spacing: 1.6pt; margin-top: 4pt; white-space: nowrap; }
.brief .rechts { text-align: right; font-size: var(--brief-pt); line-height: 1.45; padding-right: 5mm;
                 border-right: 1.6pt solid var(--text); padding-bottom: 1mm; }
.brief .rechts .datum { margin-top: 5mm; }
.brief .empfaenger { margin-top: 19mm; line-height: 1.45; }
.brief .betreff { font-size: 17pt; margin-top: 10mm; line-height: 1.2; }
.brief .betreff-zusatz { font-size: 10.5pt; margin-top: 2pt; }
.brief .anrede { margin-top: 8mm; }
.brief p { margin: 0 0 9pt; text-align: justify; }
.brief .gruss { margin-top: 12mm; }
.brief .unterschrift { height: 14mm; display: block; margin: 1mm 0; }
.brief .anlagen { margin-top: 8mm; display: flex; gap: 12mm; }
"""


# Schlüssel: (Normal-Schnitt, Fett-Schnitt, Grundgröße Lebenslauf, Grundgröße Brief).
# Schnitte als lokale Font-Namen, voller Name und PostScript-Name, damit Edge
# echte Fettschnitte nimmt statt sie künstlich zu verstärken. Die Grundgrößen
# gleichen die unterschiedliche x-Höhe aus, damit alle Varianten gleich
# groß wirken.
SCHRIFTEN = {
    "gill": (["Gill Sans MT", "GillSansMT"], ["Gill Sans MT Bold", "GillSansMT-Bold"], "9pt", "10pt"),
    "franklin": (["Franklin Gothic Book", "FranklinGothic-Book"],
                 ["Franklin Gothic Demi", "FranklinGothic-Demi"], "8.5pt", "9.4pt"),
    "garamond": (["Garamond"], ["Garamond Bold", "Garamond-Bold"], "9.2pt", "10.6pt"),
    "century": (["Century Gothic", "CenturyGothic"], ["Century Gothic Bold", "CenturyGothic-Bold"],
                "8.1pt", "8.9pt"),
    # Ersatz für Rechner ohne Franklin Gothic (macOS), Grotesk wie Franklin, Größe auf gleiche
    # Zeilenlänge abgestimmt.
    "helvetica": (["Helvetica Neue", "HelveticaNeue"], ["Helvetica Neue Medium", "HelveticaNeue-Medium"],
                  "7.9pt", "8.8pt"),
    "arial": (["Arial", "ArialMT"], ["Arial Bold", "Arial-BoldMT"], "8.2pt", "9.2pt"),
    "georgia": (["Georgia"], ["Georgia Bold", "Georgia-Bold"], "8.2pt", "9.3pt"),
}


def franklin_installiert():
    """Sucht die Datei von Franklin Gothic Book in den üblichen Schriftordnern von Windows und macOS."""
    ordner = [Path(os.environ.get("WINDIR", r"C:\Windows")) / "Fonts",
              Path(os.environ.get("LOCALAPPDATA", "")) / "Microsoft" / "Windows" / "Fonts",
              Path.home() / "Library" / "Fonts", Path("/Library/Fonts")]
    return any(any(o.glob(m)) for o in ordner if o.is_dir() for m in ("FRABK*", "Franklin*Book*"))


# Schrift aus stil.json. Bei "auto" Franklin Gothic, wo installiert, sonst Helvetica Neue.
SCHRIFT = STIL["schrift"] if STIL["schrift"] in SCHRIFTEN else (
    "franklin" if franklin_installiert() else "helvetica")


def schrift_css():
    normal, fett_, cv_pt, brief_pt = SCHRIFTEN[SCHRIFT]
    quelle = lambda namen: ", ".join(f'local("{n}")' for n in namen)
    return (f'@font-face {{ font-family: "CVSchrift"; font-weight: 400; src: {quelle(normal)}; }}'
            f'@font-face {{ font-family: "CVSchrift"; font-weight: 700; src: {quelle(fett_)}; }}'
            f":root {{ --cv-pt: {cv_pt}; --brief-pt: {brief_pt}; --rot: {STIL['akzentfarbe']}; }}")


def e(text):
    # Geschütztes Leerzeichen zwischen Zahl und Einheit, damit "0,002 %" nicht umbricht
    text = re.sub(r"(\d) (%|EUR)", r"\1" + "\u00a0" + r"\2", text)
    return html.escape(text, quote=False)


def fett(text):
    """**x** im Inhalt wird fett, alles andere escaped."""
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", e(text))


def bild_uri(pfad):
    mime = "image/png" if pfad.suffix.lower() == ".png" else "image/jpeg"
    return f"data:{mime};base64,{base64.b64encode(pfad.read_bytes()).decode()}"


def foto_html():
    if not STIL["foto"]:
        return ""
    for pfad in FOTOS:
        if pfad.exists():
            return f'<img class="foto" src="{bild_uri(pfad)}" alt="">'
    return '<div class="foto-leer"></div>'


def eintrag(x):
    hinweis = ""
    if x.get("hinweis"):
        zeilen = "<br>".join(e(z) for z in x["hinweis"].split("\n"))
        hinweis = f'<span class="hinweis"><span class="kreis">!</span><span>{zeilen}</span></span>'
    beschreibung = "".join(f'<div class="beschreibung">{fett(b)}</div>' for b in x.get("beschreibung", []))
    punkte = "".join(f"<li>{fett(p)}</li>" for p in x.get("punkte", []))
    return (f'<div class="eintrag"><div class="zeit">{e(x["zeit"])}</div><div>'
            f'<div class="zeile{" mit-hinweis" if hinweis else ""}"><span>{fett(x["kopf"])}</span>{hinweis}</div>{beschreibung}'
            + (f"<ul>{punkte}</ul>" if punkte else "") + "</div></div>")


def cv_html(cv):
    p, t, s = cv["person"], cv["ueberschriften"], cv["skills"]
    kontakt = " • ".join(e(k) for k in p["kontakt"])
    # Optional "schriftgroesse" (z. B. "7.6pt") verdichtet einen ausführlichen Lebenslauf auf eine Seite.
    dichte = f' style="font-size: {cv["schriftgroesse"]}"' if cv.get("schriftgroesse") else ""
    teile = [f'<div class="cv"{dichte}>{foto_html()}<div class="kopf"><h1>{e(p["name"].upper())}</h1>'
             f'<div class="titel">{e(p["titel"])}</div><div class="kontakt">{kontakt}</div></div>',
             f'<h2>{e(t["zusammenfassung"])}</h2><p class="text">{e(cv["zusammenfassung"])}</p>']
    for schluessel in cv["reihenfolge"]:
        teile.append(f'<h2>{e(t[schluessel])}</h2>' + "".join(eintrag(x) for x in cv[schluessel]))
    komp = "".join(f"<li>{e(k)}</li>" for k in s["kompetenzen"])
    zert = "".join(f'<div class="zert">{e(d)} | {e(n)}<br><b>{e(a)}</b></div>' for d, n, a in s["zertifikate"])
    spr = "".join(f'<div class="paar"><span>{e(a)}</span><span>{e(b)}</span></div>' for a, b in s["sprachen"])
    teile.append(f'<h2>{e(t["skills"])}</h2><div class="skills">'
                 f'<div><h3>{e(t["kompetenzen"])}</h3><ul>{komp}</ul></div>'
                 f'<div><h3>{e(t["zertifikate"])}</h3>{zert}</div>'
                 f'<div><h3>{e(t["sprachen"])}</h3>{spr}</div></div></div>')
    return seite(f'{p["name"]} {t["dokument"]}', "".join(teile), cv["sprache"])


def brief_html(cv, b):
    p = cv["person"]
    rechts = "<br>".join(e(z) for z in p["adresse_brief"])
    empf = "<br>".join(e(z) for z in b["empfaenger"])
    absatz = "".join(f"<p>{e(x)}</p>" for x in b["absaetze"])
    unterschrift = (f'<img class="unterschrift" src="{bild_uri(UNTERSCHRIFT)}" alt="">'
                    if UNTERSCHRIFT.exists() else "")
    zusatz = f'<div class="betreff-zusatz">{e(b["betreff_zusatz"])}</div>' if b.get("betreff_zusatz") else ""
    anlagen = (f'<div class="anlagen"><span>{e(b["anlagen_titel"])}</span>'
               f'<span>{e(" | ".join(b["anlagen"]))}</span></div>' if b.get("anlagen") else "")
    inhalt = (f'<div class="brief"><div class="kopf"><div><div class="name">{e(p["name"].upper())}</div>'
              f'<div class="titel">{e(p["titel"])}</div></div>'
              f'<div class="rechts">{rechts}<div class="datum">{e(b["datum"])}</div></div></div>'
              f'<div class="empfaenger">{empf}</div>'
              f'<div class="betreff">{e(b["betreff"])}</div>{zusatz}'
              f'<p class="anrede">{e(b["anrede"])}</p>{absatz}'
              f'<div class="gruss">{e(b["gruss"])}<br>{unterschrift}{e(p["name"])}</div>{anlagen}</div>')
    return seite(f'{p["name"]} {b["dokument"]}', inhalt, cv["sprache"])


def seite(titel, inhalt, sprache):
    return (f'<!doctype html><html lang="{sprache}"><head><meta charset="utf-8">'
            f'<title>{e(titel)}</title><style>{schrift_css()}{CSS}</style></head><body>{inhalt}</body></html>')


def pruefen(name, htmltext, final):
    sichtbar = re.sub(r"<style>.*?</style>|<[^>]+>", " ", htmltext, flags=re.S)
    sichtbar = html.unescape(sichtbar)
    striche = [m.group(0) for m in re.finditer(r".{0,25}[–—].{0,25}", sichtbar)]
    if striche and STIL["gedankenstriche_verbieten"]:
        raise ValueError(f"{name}: Gedankenstriche gefunden: {striche}")
    if final:
        # [Note: ...] und englisch [Grade ...] sind gewollter Inhalt, alles andere in eckigen
        # Klammern ein Platzhalter
        offen = re.findall(r"\[(?!Note|Grade)[^\]]{2,}\]", sichtbar)
        if offen:
            raise ValueError(f"{name}: offene Platzhalter: {offen}")


def drucken(htmltext, ziel):
    quelle = ziel.with_suffix(".html")
    quelle.write_text(htmltext, encoding="utf-8")
    vorher = ziel.stat().st_mtime if ziel.exists() else 0
    subprocess.run([str(EDGE), "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={ziel}", quelle.as_uri()],
                   check=True, capture_output=True, timeout=120)
    # Edge meldet keinen Fehler, wenn das PDF gesperrt ist (z. B. im Viewer geöffnet).
    if not ziel.exists() or ziel.stat().st_mtime == vorher:
        raise RuntimeError(f"{ziel.name} wurde nicht neu geschrieben, ist die Datei geöffnet?")
    quelle.unlink()
    return len(PdfReader(ziel).pages)


def main():
    modulpfad, ausgabe = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
    final = "--final" in sys.argv
    global SCHRIFT
    wahl = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--schrift=")), None)
    if wahl:
        if wahl not in SCHRIFTEN:
            raise SystemExit(f"Unbekannte Schrift {wahl}, erlaubt: {', '.join(SCHRIFTEN)}")
        SCHRIFT = wahl
    zusatz = f"_{wahl.capitalize()}" if wahl else ""
    spec = importlib.util.spec_from_file_location("inhalt", modulpfad)
    inhalt = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(inhalt)
    ausgabe.mkdir(parents=True, exist_ok=True)

    # BRIEF darf fehlen, etwa beim Standard-CV für einen Personalvermittler ohne Anschreiben.
    cv, brief = inhalt.CV, getattr(inhalt, "BRIEF", None)
    dokumente = [("Lebenslauf", cv_html(cv), cv["dateiname"], STIL["seiten_lebenslauf"])]
    if brief:
        dokumente.append(("Anschreiben", brief_html(cv, brief), brief["dateiname"], STIL["seiten_anschreiben"]))
    for name, text, dateiname, ziel in dokumente:
        pruefen(name, text, final)
        dateiname = dateiname.replace(".pdf", f"{zusatz}.pdf")
        seiten = drucken(text, ausgabe / dateiname)
        print(f"{dateiname}: {seiten} Seite(n), {'ok' if seiten <= ziel else f'ZU LANG, Ziel ist höchstens {ziel}'}")
    if STIL["foto"] and not any(p.exists() for p in FOTOS):
        print("Hinweis: Bewerbungsfoto.jpg fehlt in Profil/, Kreis bleibt leer")
    if brief and not UNTERSCHRIFT.exists():
        print("Hinweis: Unterschrift.png fehlt in Profil/, Anschreiben ohne Unterschrift")
    print(f"Schrift: {SCHRIFTEN[SCHRIFT][0][0]}")


if __name__ == "__main__":
    main()
