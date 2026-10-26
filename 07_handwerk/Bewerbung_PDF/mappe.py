"""Baut die Anlagen zur Bewerbung aus den Einzelnachweisen.

Aufruf:  python3 mappe.py

Welche Dokumente mit welchen Seiten in welche Anlage gehören, steht in
`05_werkstatt/karriere/Profil/mappe.json` (Vorlage daneben). Pfade sind
relativ zu `Profil/Nachweise/`. Ergebnis in `Profil/Nachweise/00_Bewerbungsmappe/`,
je Anlage ein PDF, dazu eine Gesamtmappe.

Auswahl je Dokument über Seitennummern. Begleitschreiben, Deckblätter,
Signaturseiten und Seiten mit Ausweisnummern bleiben draußen. Scans werden
auf etwa 150 dpi heruntergerechnet, damit die Gesamtmappe unter den üblichen
Upload-Grenzen der Bewerbungsportale bleibt, die Textebene digitaler
Dokumente bleibt erhalten. Alle Seiten werden auf A4 normalisiert.
"""
import json
from pathlib import Path

from PIL import Image
from pypdf import PageObject, PdfReader, PdfWriter, Transformation

NACHWEISE = (Path(__file__).resolve().parents[2] / "05_werkstatt" / "karriere"
             / "Profil" / "Nachweise")
ZIEL = NACHWEISE / "00_Bewerbungsmappe"
MAX_BREITE = 1300   # Pixel, entspricht rund 150 dpi auf A4-Breite
QUALITAET = 72
A4 = (595.28, 841.89)

KONFIG = NACHWEISE.parent / "mappe.json"


def mappen_laden():
    """{Anlage: [(Datei, [Seiten])]} aus mappe.json, Schlüssel mit _ am Anfang sind Kommentare."""
    if not KONFIG.exists():
        raise SystemExit(f"{KONFIG} fehlt. Vorlage mappe.vorlage.json kopieren und füllen.")
    daten = json.loads(KONFIG.read_text(encoding="utf-8"))
    return {name: [(d["datei"], d["seiten"]) for d in liste]
            for name, liste in daten.items() if not name.startswith("_")}


def verkleinern(writer):
    for seite in writer.pages:
        for bild in seite.images:
            img = bild.image
            if img.width <= MAX_BREITE:
                continue
            faktor = MAX_BREITE / img.width
            klein = img.convert("RGB").resize((MAX_BREITE, round(img.height * faktor)), Image.LANCZOS)
            bild.replace(klein, quality=QUALITAET)
        seite.compress_content_streams()


def auf_a4(seite):
    """Skaliert eine Seite auf A4 und zentriert sie; Querformat bleibt quer.

    Einige Scans haben ein übergroßes Seitenformat und wirken in der Mappe
    sonst wie Plakate neben den übrigen Seiten.
    """
    breite, hoehe = float(seite.mediabox.width), float(seite.mediabox.height)
    if seite.get("/Rotate", 0) % 180:
        breite, hoehe = hoehe, breite
    zb, zh = A4 if hoehe >= breite else (A4[1], A4[0])
    seite.transfer_rotation_to_content()
    f = min(zb / breite, zh / hoehe)
    blatt = PageObject.create_blank_page(width=zb, height=zh)
    x0, y0 = float(seite.mediabox.left), float(seite.mediabox.bottom)
    blatt.merge_transformed_page(seite, Transformation().translate(-x0, -y0).scale(f, f)
                                 .translate((zb - breite * f) / 2, (zh - hoehe * f) / 2))
    return blatt


def bauen(name, quellen):
    writer = PdfWriter()
    for datei, seiten in quellen:
        leser = PdfReader(NACHWEISE / datei)
        for nr in seiten:
            writer.add_page(auf_a4(leser.pages[nr - 1]))
    verkleinern(writer)
    ziel = ZIEL / f"{name}.pdf"
    with open(ziel, "wb") as f:
        writer.write(f)
    return ziel


def main():
    ZIEL.mkdir(parents=True, exist_ok=True)
    teile = [bauen(name, quellen) for name, quellen in mappen_laden().items()]
    gesamt = PdfWriter()
    for teil in teile:
        gesamt.append(str(teil))
    ziel = ZIEL / "Anlagen_Gesamt.pdf"
    with open(ziel, "wb") as f:
        gesamt.write(f)
    for pdf in teile + [ziel]:
        print(f"{pdf.name}: {len(PdfReader(pdf).pages)} Seiten, {pdf.stat().st_size / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
