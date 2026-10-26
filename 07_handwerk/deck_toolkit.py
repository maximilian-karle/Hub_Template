"""Wiederverwendbare Bausteine für PowerPoint-Decks aus dem Hub.

Das Modul hält an einer Stelle, was beim Bau von Decks immer wieder gebraucht
wird, Hilfsfunktionen ebenso wie die Fallstricke, die erst beim Rendern
auffallen.

Vorlage
-------
Liegt eine eigene Vorlage unter `07_handwerk/deck_vorlage.pptx`, öffnet
`open_template()` sie. Sie muss dieselbe Layout-Reihenfolge und dieselben
Platzhalter-Indizes haben wie die Konstanten `L_*` und `PH_*` unten. Fehlt
die Datei, baut `open_template()` eine neutrale Vorlage im Speicher (16 zu 9,
Edelstein-Palette, Name aus den Einstellungen im Fuß jeder Inhaltsfolie).
`vorlage_speichern()` schreibt diese neutrale Vorlage als Datei, als
Ausgangspunkt für eine eigene Gestaltung in PowerPoint.

Verwendung
----------
    import sys
    sys.path.insert(0, str(HUB / "07_handwerk"))
    import deck_toolkit as dt

    prs = dt.open_template()
    dt.cover(prs, "Titel des Decks", "Anlass, Datum")
    s = dt.new_slide(prs, dt.L_CHART)
    dt.head(s, "SITUATION", "Kernaussage in einem Satz")
    dt.kpi_card(s, dt.CL, dt.CONTENT_TOP, dt.Inches(2.7), "EUR 32.5 m", "Bestand")
    dt.save(prs, out_path)

`python 07_handwerk/deck_toolkit.py` baut ein kleines Probedeck in einen
temporären Ordner und meldet die Befunde.

Fallstricke (alle real aufgetreten, nicht theoretisch)
------------------------------------------------------
1. **Bild-Platzhalter.** `python-pptx` erzeugt für sie ein `<p:sp>` ohne
   `<p:txBody>`, das ist schemawidrig. `python-pptx` öffnet die Datei
   weiterhin, PowerPoint lehnt sie als beschädigt ab. `new_slide()` entfernt
   daher jeden nicht befüllten Platzhalter automatisch. Deshalb gibt es diese
   Funktion, `prs.slides.add_slide()` direkt aufzurufen ist die Fehlerquelle.

2. **Titellänge.** Der Titelplatzhalter ist 11,5 Zoll breit bei 24 pt. Ab etwa
   65 Zeichen bricht der Titel auf zwei Zeilen um und läuft in den Inhalt, der
   bei 1,72 Zoll beginnt. `head()` warnt bei Überlänge.

3. **Zahlenformate in Diagrammen hängen vom Gebietsschema ab.** PowerPoint
   rendert das Dezimaltrennzeichen nach den Systemeinstellungen,
   `#,##0.00,,"m"` erscheint auf einem deutschen System als "1,51m", neben
   "EUR 1.51 m" im englischen Fließtext. Tausender (`#,##0," k"`) sind sicher,
   weil der Trenner dort nur gruppiert. Siehe `CHART_NUMFMT_*`.

4. **Tabellenausrichtung.** Zahlen rechtsbündig, Text linksbündig. `table()`
   nimmt dafür `right_cols`. Ohne Angabe werden alle Spalten außer der ersten
   rechtsbündig gesetzt, was bei Textspalten unlesbar wird.

5. **Fußnoten.** Zweizeilige Fußnoten laufen unterhalb von 6,48 Zoll in die
   Linie am Folienfuß. `footnote()` setzt den Standard entsprechend.

6. **Interne Projektartefakte auf der Folie.** Nummern aus dem Arbeitsplan,
   Dateinamen (`CLAUDE.md`, `Arbeitsplan.md`) oder Ordnerpfade
   (`00_Charter/`) sind Verwaltungsdetails für den, der das Projekt führt.
   Für ein Publikum sind sie ohne Kontext und gehören nicht auf die Folie.
   Literaturzitate mit Autor, Werk und Kapitel (etwa "Werner, Supply Chain
   Controlling, Abschnitt 5.1") sind KEIN Fall davon, das sind
   veröffentlichte Quellen. `save()` prüft automatisch auf die typischen
   Muster, siehe `_find_internal_references()`.

Jedes gespeicherte Deck prüft `check_package()` technisch (doppelte
Paketeinträge, fehlende Content-Types, tote Verweise, Platzhalter ohne
Textkörper, Bildballast).
"""

from __future__ import annotations

import importlib.util
import re
import warnings
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Emu, Inches, Pt  # noqa: F401  (Re-Export für Aufrufer)

TEMPLATES_DIR = Path(__file__).resolve().parent
HUB = TEMPLATES_DIR.parent
# Eigene Vorlage, optional. Fehlt sie, gilt die eingebaute neutrale Vorlage.
TEMPLATE = TEMPLATES_DIR / "deck_vorlage.pptx"
# Quelle der Farbtokens, gemeinsam mit den HTML-Dashboards.
THEME_CSS = TEMPLATES_DIR / "dashboard_template" / "theme.css"
FONT = "Calibri"


def _autor() -> str:
    """Name aus `00_kern/einstellungen.json` (Feld person.name).

    Gelesen über `00_kern/einstellungen.py`, geladen per Dateipfad, damit
    kein Eintrag in sys.path nötig ist. Fehlt die Datei oder der Name, bleibt
    der Name leer und die Vorlage lässt den Stempel weg.
    """
    try:
        spec = importlib.util.spec_from_file_location(
            "einstellungen", HUB / "00_kern" / "einstellungen.py")
        modul = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modul)
        return modul.name() or ""
    except Exception:
        return ""


# Name des Vortragenden. Er gehört auf das Cover und in den Fuß jeder
# Inhaltsfolie, weil einzelne Folien weitergereicht werden und dann ihre
# Herkunft tragen sollen.
AUTHOR = _autor()


# --------------------------------------------------------------------------
# Edelstein-Palette. Sie ist genau einmal definiert, als Farbtokens im
# :root-Block von dashboard_template/theme.css, und wird hier gelesen. So
# haben Decks und Dashboards immer dieselben Farben. Der Befehl /einrichten
# bestätigt die Palette oder ersetzt sie dort. Neue Kategorien nehmen ihre
# Farbe aus dieser Liste, nie eine eigene.
# --------------------------------------------------------------------------
def _farbtokens(pfad: Path = THEME_CSS) -> dict[str, RGBColor]:
    if not pfad.exists():
        raise FileNotFoundError(
            f"{pfad} fehlt. Dort steht die Farbpalette für Decks und Dashboards.")
    css = pfad.read_text(encoding="utf-8")
    root = re.search(r":root\s*\{(.*?)\}", css, re.DOTALL)
    werte = re.findall(r"--([a-z-]+)\s*:\s*#([0-9A-Fa-f]{6})\s*;",
                       root.group(1) if root else "")
    return {name: RGBColor.from_string(hexwert.upper()) for name, hexwert in werte}


_FARBEN = _farbtokens()
SAPHIR = _FARBEN["saphir"]
RUBIN = _FARBEN["rubin"]
SMARAGD = _FARBEN["smaragd"]
AMETHYST = _FARBEN["amethyst"]
TOPAS = _FARBEN["topas"]
CITRIN = _FARBEN["citrin"]
TUERKIS = _FARBEN["tuerkis"]
GRAPHIT = _FARBEN["graphit"]   # neutral, für Linien und Rahmen

# Rollen, unter denen die Bausteine die Farben ansprechen. GREY ist die dunkle
# Stufe von Graphit, denn Graphit selbst erreicht auf Weiß nur ein
# Kontrastverhältnis von etwa 2,6 zu 1 und ist als Schriftfarbe für
# Sekundärtext zu schwach. LIGHT ist eine helle Graphit-Fläche für
# Summenzeilen und Bänder, keine Kategoriefarbe.
BLUE = SAPHIR                          # Primärfarbe
RED = RUBIN                            # Warnung, Negativfall
GREY = RGBColor(0x47, 0x55, 0x69)      # Sekundärtext
LIGHT = RGBColor(0xEE, 0xF2, 0xF6)     # Flächen, Summenzeilen
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
BLACK = RGBColor(0x00, 0x00, 0x00)

# --------------------------------------------------------------------------
# Layout-Indizes der Vorlage, in der Reihenfolge der neutralen Vorlage
# (siehe `neutrale_vorlage()`). Eine eigene Vorlage hält dieselbe Reihenfolge.
# --------------------------------------------------------------------------
L_COVER = 0           # Titelfolie, Saphir-Fläche links
L_DIVIDER = 1         # Kapiteltrenner, Saphir vollflächig
L_TEXT = 2            # Inhalt mit Titel, Kicker und einem Textplatzhalter
L_BULLETS = 2
L_TEXT_SUB = 3        # Inhalt mit Subheadline
L_TWO_COL = 4         # zweispaltig mit zwei Subheadlines
L_CHART = 5           # freie Fläche, nur Titel und Kicker
L_GREY = 6            # wie L_CHART, Hintergrund hellgrau

# Platzhalter-Indizes, die in jedem Inhaltslayout gleich liegen
PH_TITLE = 0
PH_BODY = 1
PH_BODY_2 = 2
PH_SUB = 13           # Subheadline links
PH_SUB_2 = 14         # Subheadline rechts (nur zweispaltig)
PH_KICKER = 15        # schmale Zeile über dem Titel
PH_DATE, PH_FOOTER, PH_SLIDENUM = 10, 11, 12

# Geometrie des Inhaltsbereichs
CL = Inches(0.92)             # linker Rand
CW = Inches(11.5)             # nutzbare Breite
CONTENT_TOP = Inches(1.72)    # erste Zeile unter einem einzeiligen Titel
FOOTNOTE_TOP = 6.48           # Zoll, darunter kollidiert es mit der Fußlinie

# Heuristik, keine exakte Grenze. Die tatsächliche Breite hängt von den
# Glyphen ab (Großbuchstaben und "W"/"M" brauchen mehr Platz als "i"/"l").
# Empirisch passen 66 Zeichen bei 24 pt noch in eine Zeile, 75 nicht mehr.
# Die Warnung ist ein Prüfhinweis, kein Fehler, im Zweifel rendern.
TITLE_MAX_CHARS = 70

# Mittlere Glyphenbreite als Anteil der Schriftgröße. 0,5 ist der übliche
# Richtwert für eine Proportionalschrift im Fließtext. Großschreibung und
# breite Glyphen liegen darüber, weshalb CHAR_WIDTH_RATIO bewusst nicht
# kleiner angesetzt ist. Grundlage von estimate_lines().
CHAR_WIDTH_RATIO = 0.5
LINE_HEIGHT_RATIO = 1.2   # Zeilenabstand als Vielfaches der Schriftgröße

# Geometrie des Cover-Layouts (L_COVER), in Zoll. Der Titelplatzhalter ist
# schmaler als ein Inhaltstitel und unten verankert, der Untertitel beginnt
# 0,15 Zoll darunter. Ein Titel, der über seine Höhe hinauswächst, wächst
# nach oben, kollidiert also nicht mit dem Untertitel, verlässt aber die
# geplante Fläche. Eine feste Zeichengrenze wie TITLE_MAX_CHARS trägt hier
# nicht, sie wurde an einem 11,5 Zoll breiten Platzhalter gemessen.
COVER_LEFT = 5.0
COVER_TITLE_TOP = 2.3
COVER_TITLE_W = 7.4
COVER_TITLE_H_FREE = 1.7      # Höhe des Titelplatzhalters
COVER_SUBTITLE_TOP = 4.15
COVER_SUBTITLE_W = 7.4
COVER_SUBTITLE_H = 1.0

# Hochgestellte Ziffern für Quellenmarker im Fließtext (siehe Sources).
SUPERSCRIPTS = "¹²³⁴⁵⁶⁷⁸⁹"

# Zahlenformate für Diagramme, unabhängig vom Gebietsschema (Fallstrick 3)
CHART_NUMFMT_THOUSANDS = '#,##0," k"'
CHART_NUMFMT_THOUSANDS_EUR = '#,##0," k EUR"'
CHART_NUMFMT_MILLIONS = '#,##0,,"m"'   # nur ohne Nachkommastellen unbedenklich

# --------------------------------------------------------------------------
# Interne Projektartefakte, die auf keiner Folie stehen sollten (Fallstrick
# 6). Absichtlich als Textmuster statt als Abgleich mit dem Dateisystem, denn
# die Folie soll auch dann sauber sein, wenn die Datei, auf die sie verweist,
# längst umbenannt wurde. Heuristik, kein vollständiger Schutz. Die Prüfung
# fängt die wörtliche Übernahme aus dem Projekt (aus CLAUDE.md, dem
# Arbeitsplan, dem Statuslog), nicht jede Umschreibung.
_RE_INTERNAL_REFERENCE = re.compile(
    r"\bWorkplan\b"
    r"|\bArbeitsplan\b"
    r"|\bArbeitspaket\s+\d"
    r"|\bCLAUDE\.md\b"
    r"|\.md\b"
    r"|\b\d{2}_[A-Z][A-Za-z_]*/"          # Ordnerpfade wie 00_Charter/
    r"|\bPhase\s*\d+\.\d+\b"              # Phase 1.2
    r"|\bWorkplan\s+item\b"
    r"|\bitem\s+\d+\.\d+\b",
    re.IGNORECASE,
)


def _iter_slide_texts(prs: Presentation):
    """Liefert (Folienindex, Text) für jede sichtbare Textform.

    Sprechernotizen sind ausgenommen. Sie sind für den Vortragenden gedacht
    und dürfen interne Bezüge tragen, das Publikum sieht sie nie.
    """
    for i, slide in enumerate(prs.slides, start=1):
        for shape in slide.shapes:
            if shape.has_text_frame:
                yield i, shape.text_frame.text
            if shape.has_table:
                for row in shape.table.rows:
                    for cell in row.cells:
                        yield i, cell.text


def _find_internal_references(prs: Presentation) -> list[str]:
    """Sucht Verwaltungsbezüge (Nummern aus dem Arbeitsplan, Dateinamen,
    Pfade) im sichtbaren Folientext. Literaturzitate sind kein Treffer, da sie
    keinem der Muster entsprechen, siehe Modul-Docstring, Fallstrick 6."""
    findings = []
    for slide_no, text in _iter_slide_texts(prs):
        if not text:
            continue
        m = _RE_INTERNAL_REFERENCE.search(text)
        if m:
            findings.append(
                f"Folie {slide_no}: interner Bezug {m.group(0)!r} in "
                f"{text[:80]!r}")
    return findings


# ==========================================================================
# Vorlage öffnen, Deck speichern
# ==========================================================================
def open_template(path: Path | str | None = None) -> Presentation:
    """Öffnet die Vorlage und entfernt deren Beispielfolien.

    Ohne `path` gilt `07_handwerk/deck_vorlage.pptx`. Fehlt diese Datei,
    entsteht die neutrale Vorlage im Speicher, mit einem Hinweis, wo eine
    eigene Vorlage abgelegt wird. Ein ausdrücklich genannter Pfad, der fehlt,
    ist ein Fehler.

    Die Beziehung wird mitgelöst, sonst bleiben die Slide-Parts im Paket und
    kollidieren beim Speichern mit neu erzeugten Folien (doppelte ZIP-Einträge).
    """
    if path is None and not TEMPLATE.exists():
        warnings.warn(
            f"Keine eigene Vorlage unter {TEMPLATE}, es gilt die eingebaute "
            f"neutrale Vorlage. Eine eigene Vorlage mit derselben "
            f"Layout-Reihenfolge dort ablegen, Ausgangspunkt liefert "
            f"vorlage_speichern().", stacklevel=2)
        return neutrale_vorlage()
    path = Path(path) if path is not None else TEMPLATE
    if not path.exists():
        raise FileNotFoundError(
            f"Vorlage {path} fehlt. Eigene Vorlage unter {TEMPLATE} ablegen "
            f"oder open_template() ohne Pfad aufrufen.")
    prs = Presentation(str(path))
    sld_id_lst = prs.slides._sldIdLst
    for sld_id in list(sld_id_lst):
        prs.part.drop_rel(sld_id.rId)
        sld_id_lst.remove(sld_id)
    return prs


def save(prs: Presentation, path: Path | str, validate: bool = True) -> list[str]:
    """Speichert das Deck und prüft es. Liefert die Befundliste (leer = sauber).

    Zwei unabhängige Prüfungen: die technische Paketprüfung
    (`check_package`) und die inhaltliche Prüfung auf interne
    Projektbezüge (Fallstrick 6). Letztere läuft vor dem Speichern auf
    dem `Presentation`-Objekt, weil sie kein PPTX-Paket braucht.
    """
    content_findings = _find_internal_references(prs)
    for f in content_findings:
        warnings.warn(f"{Path(path).name}: {f}", stacklevel=2)

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(path))

    if not validate:
        return content_findings

    findings = check_package(path)
    for f in findings:
        warnings.warn(f"{path.name}: {f}", stacklevel=2)
    return content_findings + findings


# Grenze für eingebettete Bilder. Darüber ist ein Bild fast immer
# unverkleinert eingefügt und bläht das Deck auf, ohne schärfer zu werden.
MAX_MEDIA_BYTES = 3_000_000
_RE_REF = re.compile(r'r:(?:id|embed|link|pict)="([^"]*)"')
_RE_REL_ID = re.compile(r'Id="([^"]+)"')
_RE_SP = re.compile(r"<p:sp>.*?</p:sp>", re.DOTALL)


def check_package(path: Path | str) -> list[str]:
    """Technische Prüfung eines gespeicherten Decks oder der Vorlage.

    Liefert die Befunde als Text, leer heißt sauber. Geprüft wird, woran
    PowerPoint eine Datei als beschädigt ablehnt, obwohl python-pptx sie
    noch öffnet: doppelte Paketeinträge, Teile ohne Content-Type, Verweise
    ohne Beziehung und Platzhalter ohne Textkörper (Fallstrick 1). Dazu
    Bilder über MAX_MEDIA_BYTES.
    """
    import collections
    import posixpath
    import zipfile

    findings: list[str] = []
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        dups = [n for n, c in collections.Counter(names).items() if c > 1]
        if dups:
            findings.append(f"Doppelte Paketeinträge: {dups}")
        name_set = set(names)

        ct = z.read("[Content_Types].xml").decode("utf-8", "replace")
        defaults = {e.lower() for e in
                    re.findall(r'<Default Extension="([^"]+)"', ct)}
        overrides = set(re.findall(r'<Override PartName="([^"]+)"', ct))
        for n in names:
            if n.endswith(".rels") or n == "[Content_Types].xml":
                continue
            if "/" + n not in overrides and \
                    n.rsplit(".", 1)[-1].lower() not in defaults:
                findings.append(f"Kein Content-Type: {n}")

        for n in names:
            if n.endswith(".rels") or not n.endswith(".xml"):
                continue
            xml = z.read(n).decode("utf-8", "replace")
            refs = {r for r in _RE_REF.findall(xml) if r}
            if refs:
                rels = posixpath.join(posixpath.dirname(n), "_rels",
                                      posixpath.basename(n) + ".rels")
                known = (set(_RE_REL_ID.findall(
                    z.read(rels).decode("utf-8", "replace")))
                    if rels in name_set else set())
                if refs - known:
                    findings.append(
                        f"Tote Verweise in {n}: {sorted(refs - known)}")
            if n.startswith("ppt/slides/slide"):
                for sp in _RE_SP.findall(xml):
                    if "<p:ph" in sp and "<p:txBody" not in sp:
                        findings.append(
                            f"Platzhalter ohne Textkörper in {n}")
                        break

        for info in z.infolist():
            if info.filename.startswith("ppt/media/") and \
                    info.file_size > MAX_MEDIA_BYTES:
                findings.append(f"Großes Bild: {info.filename} "
                                f"({info.file_size / 1e6:.1f} MB)")
    return findings


# ==========================================================================
# Folien
# ==========================================================================
def new_slide(prs: Presentation, layout_idx: int, keep: set[int] | None = None):
    """Legt eine Folie an und entfernt jeden Platzhalter, der nicht befüllt wird.

    `keep` = Indizes, die erhalten bleiben sollen. Datum (10), Fußzeile (11)
    und Foliennummer (12) bleiben immer. Alle übrigen, insbesondere
    BILD-Platzhalter, werden entfernt: leere Platzhalter erscheinen sonst als
    Rahmen auf der Folie, und Bild-Platzhalter erzeugen schemawidriges XML
    (siehe Modul-Docstring, Fallstrick 1).
    """
    slide = prs.slides.add_slide(prs.slide_masters[0].slide_layouts[layout_idx])
    keep = set(keep or ())
    for ph in list(slide.placeholders):
        idx = ph.placeholder_format.idx
        if idx in keep or idx in (PH_DATE, PH_FOOTER, PH_SLIDENUM):
            continue
        ph._element.getparent().remove(ph._element)
    return slide


def slide_numbers(prs: Presentation, skip_first: bool = True) -> int:
    """Blendet die Foliennummer auf jeder Folie ein. Liefert die Anzahl.

    Der Foliennummern-Platzhalter steht zwar in jedem Layout der Vorlage,
    wird von python-pptx beim Anlegen einer Folie aber nicht mitkopiert,
    genau wie Datum und Fußzeile. Ohne diesen Schritt hat ein erzeugtes
    Deck also keine Seitenzahlen, obwohl `new_slide()` den Index 12
    ausdrücklich erhält: erhalten werden kann nur, was vorhanden ist.
    Kopiert wird deshalb die Form aus dem Layout, samt Nummernfeld, die
    Nummer selbst zählt PowerPoint beim Öffnen.

    `skip_first`: das Deckblatt bleibt ohne Nummer, wie in der Vorlage.
    """
    from copy import deepcopy

    count = 0
    for i, slide in enumerate(prs.slides):
        if skip_first and i == 0:
            continue
        if any(ph.placeholder_format.idx == PH_SLIDENUM
               for ph in slide.placeholders):
            continue
        src = [ph for ph in slide.slide_layout.placeholders
               if ph.placeholder_format.idx == PH_SLIDENUM]
        if not src:
            continue
        slide.shapes._spTree.append(deepcopy(src[0]._element))
        count += 1
    return count


def estimate_lines(text: str, width_in: float, size_pt: float) -> int:
    """Schätzt, über wie viele Zeilen ein Text in einem Rahmen umbricht.

    Absichtlich eine Schätzung: die exakte Zeilenzahl kennt nur die
    Rendering-Engine. Für die Frage "passt das noch oder läuft es in das
    Element darunter" reicht die Schätzung, und sie fällt durch
    CHAR_WIDTH_RATIO eher zu vorsichtig als zu großzügig aus.
    """
    chars_per_line = max(1, int(width_in * 72 / (size_pt * CHAR_WIDTH_RATIO)))
    lines = 0
    for para in text.split("\n"):
        lines += max(1, -(-len(para) // chars_per_line))  # aufgerundet
    return lines


def check_fits(text: str, width_in: float, height_in: float, size_pt: float,
               label: str) -> str | None:
    """Warnt, wenn `text` bei `size_pt` nicht in den Rahmen passt.

    Liefert den Befund als Text (oder None). Die Warnung nennt die
    Schriftgröße, bei der es passen würde, eine Warnung ohne Ausweg
    wird sonst ignoriert.
    """
    lines = estimate_lines(text, width_in, size_pt)
    needed = lines * size_pt * LINE_HEIGHT_RATIO / 72
    if needed <= height_in:
        return None

    fitting = size_pt
    while fitting > 8:
        fitting -= 1
        if (estimate_lines(text, width_in, fitting) * fitting
                * LINE_HEIGHT_RATIO / 72) <= height_in:
            break
    finding = (f"{label}: {len(text)} Zeichen brechen bei {size_pt:g} pt auf "
               f"{lines} Zeilen um und brauchen {needed:.2f} Zoll, verfügbar "
               f"sind {height_in:.2f}. Kürzen oder auf {fitting:g} pt "
               f"verkleinern: {text[:60]!r}")
    warnings.warn(finding, stacklevel=3)
    return finding


def cover(prs: Presentation, title: str, subtitle: str,
          title_size: float = 30, subtitle_size: float = 14):
    """Titelfolie mit automatischer Lesbarkeitsprüfung.

    Existiert als eigener Baustein, weil der Cover-Titelplatzhalter deutlich
    schmaler ist als jeder Inhaltstitel und ein zu langer Titel dort nicht
    abgeschnitten, sondern über den Untertitel gelegt wird, er wird also
    nicht kürzer, sondern unlesbar. Siehe COVER_TITLE_W.

    check_fits() schätzt nur. Ein Cover-Titel gehört deshalb gerendert
    angesehen, auch wenn keine Warnung kommt. Der Name des Vortragenden steht
    fest im Layout und muss nicht übergeben werden.
    """
    check_fits(title, COVER_TITLE_W, COVER_TITLE_H_FREE, title_size,
               "Cover-Titel")
    check_fits(subtitle, COVER_SUBTITLE_W, COVER_SUBTITLE_H, subtitle_size,
               "Cover-Untertitel")

    slide = new_slide(prs, L_COVER, keep={0, 1})
    for ph in slide.placeholders:
        idx = ph.placeholder_format.idx
        if idx == 0:
            put(ph, title, size=title_size, bold=True)
        elif idx == 1:
            put(ph, subtitle, size=subtitle_size)
    return slide


def head(slide, kicker: str, title: str, sub: str | None = None,
         title_size: int = 24) -> None:
    """Setzt Kicker (über dem Titel), Titel und optional die Subheadline."""
    if len(title) > TITLE_MAX_CHARS:
        warnings.warn(
            f"Titel mit {len(title)} Zeichen bricht auf zwei Zeilen um und läuft "
            f"in den Inhalt (Grenze ~{TITLE_MAX_CHARS}): {title!r}", stacklevel=2)
    for ph in slide.placeholders:
        i = ph.placeholder_format.idx
        if i == PH_KICKER:
            put(ph, kicker, size=10, bold=True, color=BLUE)
        elif i == PH_TITLE:
            put(ph, title, size=title_size, bold=True)
        elif i == PH_SUB and sub:
            put(ph, sub, size=12, color=GREY)


# ==========================================================================
# Text
# ==========================================================================
def put(ph, text: str, size: float | None = None, bold: bool = False,
        color: RGBColor | None = None) -> None:
    """Beschriftet einen Platzhalter. `\\n` erzeugt weitere Absätze."""
    tf = ph.text_frame
    tf.word_wrap = True
    tf.text = text
    for para in tf.paragraphs:
        for run in para.runs:
            if size:
                run.font.size = Pt(size)
            run.font.bold = bold
            if color:
                run.font.color.rgb = color


def bullets(ph, items, size: float = 13) -> None:
    """Füllt einen Platzhalter mit Aufzählung.

    `items`: Liste aus `str` oder `(text, level)`. Ebene > 0 wird kleiner und
    grau gesetzt, gedacht für die Schlussfolgerung unter einem Punkt.
    """
    tf = ph.text_frame
    tf.word_wrap = True
    tf.clear()
    for i, item in enumerate(items):
        text, level = (item, 0) if isinstance(item, str) else item
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = text
        p.level = level
        p.space_after = Pt(7)
        for run in p.runs:
            run.font.size = Pt(size if level == 0 else size - 1.5)
            if level > 0:
                run.font.color.rgb = GREY


def textbox(slide, left, top, width, height, text: str, size: float = 12,
            bold: bool = False, color: RGBColor = BLACK,
            align=PP_ALIGN.LEFT, space_after: float = 4):
    """Freies Textfeld. `\\n` trennt Absätze."""
    box = slide.shapes.add_textbox(left, top, width, height)
    tf = box.text_frame
    tf.word_wrap = True
    lines = text.split("\n")
    tf.text = lines[0]
    for extra in lines[1:]:
        tf.add_paragraph().text = extra
    for p in tf.paragraphs:
        p.alignment = align
        p.space_after = Pt(space_after)
        for run in p.runs:
            run.font.size = Pt(size)
            run.font.bold = bold
            run.font.color.rgb = color
    return box


def footnote(slide, text: str, top: float = FOOTNOTE_TOP):
    """Freier Hinweis am Folienfuß. Trägt zwei Zeilen kollisionsfrei.

    Für LITERATUR ist `Sources` + `footnote_sources()` vorgesehen, nicht
    diese Funktion: ein Zitat gehört an die Textstelle verwiesen, damit der
    Leser weiß, WELCHE Aussage belegt ist, eine Quellenzeile ohne Marker
    im Text belegt formal alles und faktisch nichts.
    """
    return textbox(slide, CL, Inches(top), CW, Inches(0.4), text,
                   size=8.5, color=GREY)


class Sources:
    """Quellenapparat einer Folie: Marker im Text, Beleg in der Fußzeile.

    Verwendung::

        src = Sources()
        bullets(ph, [f"Die Zielgrößen laufen gegeneinander{src.ref(
            'Autor, Werk (Jahr), Abschnitt 2.4')}."])
        footnote_sources(slide, src)

    Dieselbe Quelle zweimal referenziert bekommt denselben Marker; die
    Nummerierung entsteht also aus der Reihenfolge des ersten Auftretens und
    nicht aus der Aufrufreihenfolge im Code.
    """

    def __init__(self) -> None:
        self._items: list[str] = []

    def ref(self, citation: str) -> str:
        """Registriert eine Quelle und liefert den Marker für die Textstelle."""
        if citation not in self._items:
            self._items.append(citation)
        i = self._items.index(citation)
        if i >= len(SUPERSCRIPTS):
            raise ValueError(
                f"Mehr als {len(SUPERSCRIPTS)} Quellen auf einer Folie, das "
                f"ist kein Markerproblem, sondern ein Hinweis, dass die Folie "
                f"zu viel trägt.")
        return SUPERSCRIPTS[i]

    def footnote_text(self, note: str | None = None) -> str:
        """Die Fußzeile: optionaler Hinweis, danach die nummerierten Quellen."""
        refs = "   ".join(f"{SUPERSCRIPTS[i]} {c}"
                          for i, c in enumerate(self._items))
        if note and refs:
            return f"{note}\n{refs}"
        return note or refs

    def __bool__(self) -> bool:
        return bool(self._items)


def footnote_sources(slide, sources: "Sources", note: str | None = None,
                     top: float = FOOTNOTE_TOP):
    """Rendert Quellenverzeichnis (und optional einen Hinweis) am Folienfuß."""
    text = sources.footnote_text(note)
    if not text:
        return None
    return textbox(slide, CL, Inches(top), CW, Inches(0.4), text,
                   size=8.5, color=GREY, space_after=1)


# ==========================================================================
# Kennzahlen-Kachel
# ==========================================================================
def kpi_card(slide, left, top, width, value: str, label: str, sub: str = "",
             accent: RGBColor = BLUE):
    """Kachel mit farbiger Kopflinie, großer Zahl, Label und Fußnote.

    Höhe ist implizit ~1,4 Zoll. Bei mehreren Kacheln nebeneinander hat sich
    ein Abstand von 0,21-0,35 Zoll bewährt.
    """
    from pptx.enum.shapes import MSO_SHAPE

    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, Inches(0.05))
    bar.fill.solid()
    bar.fill.fore_color.rgb = accent
    bar.line.fill.background()
    bar.shadow.inherit = False

    box = slide.shapes.add_textbox(left, top + Inches(0.13), width, Inches(1.25))
    tf = box.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = value
    for r in p.runs:
        r.font.size = Pt(25)
        r.font.bold = True
        r.font.color.rgb = accent

    p2 = tf.add_paragraph()
    p2.text = label
    p2.space_before = Pt(1)
    for r in p2.runs:
        r.font.size = Pt(10.5)
        r.font.bold = True

    if sub:
        p3 = tf.add_paragraph()
        p3.text = sub
        for r in p3.runs:
            r.font.size = Pt(9)
            r.font.color.rgb = GREY
    return box


# ==========================================================================
# Grafische Grundformen
#
# Zweck: eine Aussage, die als Ablauf, Gegenüberstellung oder Ebenenmodell
# gebaut ist, wird schneller erfasst als dieselbe Aussage als Aufzählung.
# Die Formen hier sind die wiederkehrenden Fälle beim Bau von Decks.
# ==========================================================================
def flow_box(slide, left, top, width, height, title: str, body: str = "",
             accent: RGBColor = BLUE, fill: RGBColor = WHITE,
             title_size: float = 11, body_size: float = 9):
    """Kasten mit farbiger Kopflinie, Grundform für Ablauf und Vergleich.

    `title_size`/`body_size`: die Vorgabewerte sind auf den Ablaufkasten
    gemünzt, der eine Beschriftung trägt und keinen Fließtext. Sobald der
    Kasten die Begründung selbst enthält und nicht nur benennt, ist 9 pt zu
    klein für die Fläche, dann bleibt der Kasten halb leer und der Text
    trotzdem unlesbar. Beide Größen sind deshalb setzbar, statt den Kasten
    für diesen Fall neu zu bauen.
    """
    from pptx.enum.shapes import MSO_SHAPE

    box = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    box.fill.solid()
    box.fill.fore_color.rgb = fill
    box.line.color.rgb = LIGHT
    box.shadow.inherit = False
    box.text_frame.text = ""

    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width,
                                 Inches(0.05))
    bar.fill.solid()
    bar.fill.fore_color.rgb = accent
    bar.line.fill.background()
    bar.shadow.inherit = False

    tb = slide.shapes.add_textbox(left + Inches(0.11), top + Inches(0.15),
                                  width - Inches(0.22), height - Inches(0.22))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.text = title
    for r in tf.paragraphs[0].runs:
        r.font.size = Pt(title_size)
        r.font.bold = True
        r.font.color.rgb = accent
    # Ein Zeilenumbruch im `body` trennt Absätze. Ein Kasten, der eine
    # Begründung trägt statt nur einer Beschriftung, braucht sie: ein
    # einziger Block ohne Absatz ist auf einer Folie nicht lesbar.
    for i, absatz in enumerate(body.splitlines() if body else []):
        para = tf.add_paragraph()
        para.text = absatz
        para.space_before = Pt(3 if i == 0 else 0)
        para.space_after = Pt(4)
        for r in para.runs:
            r.font.size = Pt(body_size)
            r.font.color.rgb = BLACK
    return box


def arrow(slide, left, top, width=None, height=None,
          color: RGBColor = GREY, direction: str = "right"):
    """Pfeil zwischen zwei Formen. `direction`: right | left | both | down."""
    from pptx.enum.shapes import MSO_SHAPE

    shapes = {"right": MSO_SHAPE.RIGHT_ARROW, "left": MSO_SHAPE.LEFT_ARROW,
              "both": MSO_SHAPE.LEFT_RIGHT_ARROW, "down": MSO_SHAPE.DOWN_ARROW}
    width = width if width is not None else Inches(0.26)
    height = height if height is not None else Inches(0.2)
    a = slide.shapes.add_shape(shapes[direction], left, top, width, height)
    a.fill.solid()
    a.fill.fore_color.rgb = color
    a.line.fill.background()
    a.shadow.inherit = False
    a.text_frame.text = ""
    return a


def chip(slide, left, top, width, text: str, height: float = 0.32,
         color: RGBColor = BLUE, filled: bool = False, size: float = 9.5):
    """Kleines abgerundetes Label, für Rollen, Owner, Status."""
    from pptx.enum.shapes import MSO_SHAPE

    box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width,
                                 Inches(height))
    box.fill.solid()
    box.fill.fore_color.rgb = color if filled else WHITE
    box.line.color.rgb = color
    box.shadow.inherit = False
    tf = box.text_frame
    tf.word_wrap = True
    tf.text = text
    for p in tf.paragraphs:
        p.alignment = PP_ALIGN.CENTER
        for r in p.runs:
            r.font.size = Pt(size)
            r.font.bold = filled
            r.font.color.rgb = WHITE if filled else color
    return box


def band(slide, left, top, width, height, label: str, sub: str = "",
         accent: RGBColor = BLUE):
    """Waagerechtes Band mit Beschriftung links, Grundform für Ebenenmodelle.

    Liefert die linke Kante des freien Bereichs zurück, in den der Aufrufer
    die Inhalte des Bandes (typisch: `chip()`) setzt.
    """
    from pptx.enum.shapes import MSO_SHAPE

    box = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    box.fill.solid()
    box.fill.fore_color.rgb = LIGHT
    box.line.fill.background()
    box.shadow.inherit = False
    box.text_frame.text = ""

    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, Inches(0.06),
                                 height)
    bar.fill.solid()
    bar.fill.fore_color.rgb = accent
    bar.line.fill.background()
    bar.shadow.inherit = False

    tb = slide.shapes.add_textbox(left + Inches(0.16), top + Inches(0.08),
                                  Inches(1.85), height - Inches(0.16))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.text = label
    for r in tf.paragraphs[0].runs:
        r.font.size = Pt(11)
        r.font.bold = True
        r.font.color.rgb = accent
    if sub:
        p = tf.add_paragraph()
        p.text = sub
        for r in p.runs:
            r.font.size = Pt(8.5)
            r.font.color.rgb = GREY
    return left + Inches(2.05)


# ==========================================================================
# Tabelle
# ==========================================================================
def table(slide, left, top, width, headers: list[str], rows: list[list],
          col_w: list[float] | None = None, font_size: float = 10,
          row_height: float = 0.26, bold_last: bool = False,
          right_cols: set[int] | None = None):
    """Tabelle mit Saphir-Kopf und weißen Zeilen.

    `right_cols`: Spaltenindizes, die rechtsbündig stehen. None = alle außer
    der ersten (sinnvoll für Zahlentabellen). Für Tabellen mit Textspalten
    ausdrücklich `set()` oder die Zahlenspalten angeben, sonst wird
    Fließtext rechtsbündig und damit unlesbar (Fallstrick 4).

    `bold_last`: letzte Zeile als Summenzeile hervorheben.
    """
    shape = slide.shapes.add_table(len(rows) + 1, len(headers), left, top, width,
                                   Inches(row_height * (len(rows) + 1)))
    t = shape.table

    if col_w:
        total = sum(col_w)
        for i, cw in enumerate(col_w):
            t.columns[i].width = Emu(int(width * cw / total))

    if right_cols is None:
        right_cols = set(range(1, len(headers)))

    for c, h in enumerate(headers):
        cell = t.cell(0, c)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = BLUE
        for p in cell.text_frame.paragraphs:
            p.alignment = PP_ALIGN.RIGHT if c in right_cols else PP_ALIGN.LEFT
            for r in p.runs:
                r.font.size = Pt(font_size)
                r.font.bold = True
                r.font.color.rgb = WHITE

    for ri, row in enumerate(rows, start=1):
        is_last = bold_last and ri == len(rows)
        for ci, val in enumerate(row):
            cell = t.cell(ri, ci)
            cell.text = str(val)
            cell.fill.solid()
            cell.fill.fore_color.rgb = LIGHT if is_last else WHITE
            for p in cell.text_frame.paragraphs:
                p.alignment = PP_ALIGN.RIGHT if ci in right_cols else PP_ALIGN.LEFT
                for r in p.runs:
                    r.font.size = Pt(font_size)
                    r.font.bold = is_last
    return t


# ==========================================================================
# Zahlformatierung für Fließtext
# ==========================================================================
def eur_m(value: float) -> str:
    """1513577 -> 'EUR 1.51 m'"""
    return f"EUR {value / 1_000_000:.2f} m"


def eur_k(value: float) -> str:
    """689695 -> 'EUR 690 k'"""
    return f"EUR {value / 1_000:,.0f} k"


# ==========================================================================
# Neutrale Vorlage
#
# Entsteht aus Code statt aus einer in PowerPoint gepflegten Datei. So kommen
# Farben, Geometrie und Name aus den Konstanten oben und können nicht von dem
# abweichen, womit die Bausteine rechnen. Grundlage ist die leere
# Standardvorlage von python-pptx. Master, Layouts und Farbschema werden
# vollständig ersetzt, damit nichts aus der Standardvorlage unbemerkt
# mitläuft. Die Reihenfolge der Layouts muss zu den L_*-Konstanten passen,
# `neutrale_vorlage()` prüft das.
# ==========================================================================
_P = "http://schemas.openxmlformats.org/presentationml/2006/main"
_A = "http://schemas.openxmlformats.org/drawingml/2006/main"
_NS = {"p": _P, "a": _A}
_DECL = f'xmlns:p="{_P}" xmlns:a="{_A}"'


def _emu(inch: float) -> int:
    return int(Inches(inch))


def _xml_text(text: str) -> str:
    from xml.sax.saxutils import escape
    return escape(text)


def _xfrm(x, y, w, h) -> str:
    return (f'<a:xfrm><a:off x="{_emu(x)}" y="{_emu(y)}"/>'
            f'<a:ext cx="{_emu(w)}" cy="{_emu(h)}"/></a:xfrm>')


def _run_props(size, bold, color) -> tuple[str, str]:
    attrs = f' sz="{int(size * 100)}"' if size else ""
    attrs += ' b="1"' if bold else ""
    fill = (f'<a:solidFill><a:srgbClr val="{color}"/></a:solidFill>'
            if color is not None else "")
    return attrs, fill


def _placeholder(sid: int, name: str, ph: str, box, *, size=None, bold=False,
                 color=None, anchor="t", align=None, bullets=True,
                 prompt="", slide_number=False) -> str:
    """Platzhalter eines Layouts. `ph` ist das Attribut-Stück des <p:ph>."""
    attrs, fill = _run_props(size, bold, color)
    algn = f' algn="{align}"' if align else ""
    # Ohne Aufzählungszeichen beginnt der Text an der Kante, mit ihnen gilt
    # der Einzug aus dem Master.
    bu = "" if bullets else "<a:buNone/>"
    indent = "" if bullets else ' marL="0" indent="0"'
    lst = (f'<a:lstStyle><a:lvl1pPr{indent}{algn}>{bu}'
           f'<a:defRPr{attrs}>{fill}</a:defRPr></a:lvl1pPr></a:lstStyle>')
    if slide_number:
        para = ('<a:p><a:fld id="{B6F15528-21DE-4FAA-801E-634DDDAF4B2B}" '
                'type="slidenum"><a:rPr lang="de-DE"/><a:t>‹#›</a:t></a:fld></a:p>')
    elif prompt:
        para = (f'<a:p><a:r><a:rPr lang="de-DE"/><a:t>{_xml_text(prompt)}</a:t>'
                f'</a:r></a:p>')
    else:
        para = '<a:p><a:endParaRPr lang="de-DE"/></a:p>'
    return (f'<p:sp {_DECL}><p:nvSpPr><p:cNvPr id="{sid}" name="{name}"/>'
            f'<p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr>'
            f'<p:nvPr><p:ph {ph}/></p:nvPr></p:nvSpPr>'
            f'<p:spPr>{_xfrm(*box)}</p:spPr>'
            f'<p:txBody><a:bodyPr lIns="0" tIns="0" rIns="0" bIns="0" '
            f'anchor="{anchor}"><a:normAutofit/></a:bodyPr>{lst}{para}'
            f'</p:txBody></p:sp>')


def _rect(sid: int, name: str, box, color) -> str:
    """Farbfläche. Leerer Textkörper, damit die Form schemakonform bleibt."""
    return (f'<p:sp {_DECL}><p:nvSpPr><p:cNvPr id="{sid}" name="{name}"/>'
            f'<p:cNvSpPr/><p:nvPr userDrawn="1"/></p:nvSpPr>'
            f'<p:spPr>{_xfrm(*box)}<a:prstGeom prst="rect"><a:avLst/>'
            f'</a:prstGeom><a:solidFill><a:srgbClr val="{color}"/>'
            f'</a:solidFill><a:ln><a:noFill/></a:ln></p:spPr>'
            f'<p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:endParaRPr lang="de-DE"/>'
            f'</a:p></p:txBody></p:sp>')


def _text(sid: int, name: str, box, content: str, *, size, color,
          bold=False, align="l", anchor="t") -> list[str]:
    """Fester Text auf Master oder Layout. Leerer Text ergibt keine Form."""
    if not content:
        return []
    attrs, fill = _run_props(size, bold, color)
    return [(f'<p:sp {_DECL}><p:nvSpPr><p:cNvPr id="{sid}" name="{name}"/>'
             f'<p:cNvSpPr txBox="1"/><p:nvPr userDrawn="1"/></p:nvSpPr>'
             f'<p:spPr>{_xfrm(*box)}<a:prstGeom prst="rect"><a:avLst/>'
             f'</a:prstGeom><a:noFill/></p:spPr>'
             f'<p:txBody><a:bodyPr wrap="square" lIns="0" tIns="0" rIns="0" '
             f'bIns="0" anchor="{anchor}"/><a:lstStyle/>'
             f'<a:p><a:pPr algn="{align}"/><a:r><a:rPr lang="de-DE"{attrs}>'
             f'{fill}</a:rPr><a:t>{_xml_text(content)}</a:t></a:r></a:p>'
             f'</p:txBody></p:sp>')]


def _background(color) -> str:
    return (f'<p:bg {_DECL}><p:bgPr><a:solidFill><a:srgbClr '
            f'val="{color}"/></a:solidFill><a:effectLst/></p:bgPr></p:bg>')


def _replace_tree(element, shapes: list[str], bg: str | None = None) -> None:
    """Ersetzt alle Formen eines Masters oder Layouts durch `shapes`."""
    from lxml import etree

    csld = element.find("p:cSld", _NS)
    old_bg = csld.find("p:bg", _NS)
    if old_bg is not None:
        csld.remove(old_bg)
    if bg:
        csld.insert(0, etree.fromstring(bg))
    tree = csld.find("p:spTree", _NS)
    for child in list(tree)[2:]:          # nvGrpSpPr und grpSpPr bleiben
        tree.remove(child)
    for xml in shapes:
        tree.append(etree.fromstring(xml))


# Gemeinsame Geometrie in Zoll, abgeleitet aus den Konstanten oben
_LEFT = CL / 914400
_WIDTH = CW / 914400
_COL_W = 5.63
_COL_2 = _LEFT + _WIDTH - _COL_W
_KICKER = (_LEFT, 0.42, 10.2, 0.32)
_TITLE = (_LEFT, 0.82, _WIDTH, 0.62)
_SLIDENUM = (_LEFT + _WIDTH - 3.0, 7.06, 3.0, 0.28)
_BODY_TOP = CONTENT_TOP / 914400
_BODY_H = FOOTNOTE_TOP - _BODY_TOP - 0.1


def _kicker(sid: int, color=None) -> str:
    return _placeholder(sid, "Kicker", 'type="body" idx="15"', _KICKER, size=10,
                        bold=True, color=color or SAPHIR, bullets=False,
                        prompt="KICKER")


def _title(sid: int) -> str:
    return _placeholder(sid, "Titel", 'type="title"', _TITLE, size=24,
                        bold=True, color=BLACK, anchor="t",
                        prompt="Kernaussage der Folie in einem Satz")


def _slidenum(sid: int) -> str:
    return _placeholder(sid, "Foliennummer",
                        'type="sldNum" sz="quarter" idx="12"', _SLIDENUM,
                        size=9, color=GREY, align="r", bullets=False,
                        slide_number=True)


def _sub(sid: int, idx: int, x: float, w: float) -> str:
    return _placeholder(sid, f"Subheadline {idx}", f'type="body" idx="{idx}"',
                        (x, _BODY_TOP, w, 0.43), size=12, bold=True,
                        color=GREY, bullets=False, prompt="Subheadline")


def _body(sid: int, idx: int, box) -> str:
    return _placeholder(sid, f"Inhalt {idx}", f'idx="{idx}"', box,
                        prompt="Text")


def _build_master(master) -> None:
    shapes = [
        # Platzhalter des Masters, Layouts erben Schrift und Lage von hier.
        _placeholder(2, "Titel", 'type="title"', _TITLE, anchor="t"),
        _placeholder(3, "Text", 'type="body" idx="1"',
                     (_LEFT, _BODY_TOP, _WIDTH, _BODY_H)),
        _placeholder(4, "Datum", 'type="dt" sz="half" idx="2"',
                     (_LEFT, 7.06, 2.0, 0.28), size=9, color=GREY),
        _placeholder(5, "Fußzeile", 'type="ftr" sz="quarter" idx="3"',
                     (4.6, 7.06, 4.0, 0.28), size=9, color=GREY),
        _placeholder(6, "Foliennummer", 'type="sldNum" sz="quarter" idx="4"',
                     _SLIDENUM, size=9, color=GREY, align="r",
                     slide_number=True),
        # Feste Elemente jeder Inhaltsfolie
        _rect(7, "Akzent oben", (_LEFT, 0.28, 0.55, 0.06), SAPHIR),
        _rect(8, "Linie unten", (_LEFT, 6.96, _WIDTH, 0.012), GRAPHIT),
        *_text(9, "Autor", (_LEFT, 7.06, 5.0, 0.28), AUTHOR, size=9,
               color=GREY),
    ]
    _replace_tree(master._element, shapes)

    # Textstile, Titel fett und linksbündig an derselben Kante wie Kicker
    # und Inhalt (die Standardvorlage zentriert Titel), Fließtext in Stufen.
    ts = master._element.find("p:txStyles", _NS)
    ts.find("p:titleStyle/a:lvl1pPr", _NS).set("algn", "l")
    title_rpr = ts.find("p:titleStyle/a:lvl1pPr/a:defRPr", _NS)
    title_rpr.set("sz", "2400")
    title_rpr.set("b", "1")
    sizes = [1600, 1400, 1200, 1200, 1200, 1200, 1200, 1200, 1200]
    for lvl, sz in enumerate(sizes, start=1):
        ppr = ts.find(f"p:bodyStyle/a:lvl{lvl}pPr", _NS)
        if ppr is not None:
            ppr.find("a:defRPr", _NS).set("sz", str(sz))


def _layout_cover():
    panel_w = 4.2
    return "Titel", [
        _rect(2, "Fläche Saphir", (0, 0, panel_w, 7.5), SAPHIR),
        _rect(3, "Akzent Smaragd", (0.6, 6.12, 0.6, 0.06), SMARAGD),
        *_text(4, "Autor", (0.6, 6.3, panel_w - 1.0, 0.4), AUTHOR, size=14,
               bold=True, color=WHITE),
        _placeholder(5, "Titel", 'type="ctrTitle"',
                     (COVER_LEFT, COVER_TITLE_TOP, COVER_TITLE_W,
                      COVER_TITLE_H_FREE),
                     size=30, bold=True, color=BLACK, anchor="b",
                     prompt="Titel des Decks"),
        _placeholder(6, "Untertitel", 'type="subTitle" idx="1"',
                     (COVER_LEFT, COVER_SUBTITLE_TOP, COVER_SUBTITLE_W,
                      COVER_SUBTITLE_H),
                     size=14, color=GREY, bullets=False,
                     prompt="Untertitel, Anlass, Datum"),
    ], None, False


def _layout_divider():
    return "Kapiteltrenner", [
        _kicker(2, color=SMARAGD),
        _placeholder(3, "Titel", 'type="title"', (_LEFT, 3.0, _WIDTH, 1.2),
                     size=36, bold=True, color=WHITE, anchor="t",
                     prompt="Kapitel"),
        *_text(4, "Autor", (_LEFT, 7.06, 5.0, 0.28), AUTHOR, size=9,
               color=WHITE),
    ], _background(SAPHIR), False


def _layout_content():
    return "Inhalt", [
        _kicker(2), _title(3),
        _body(4, 1, (_LEFT, _BODY_TOP, _WIDTH, _BODY_H)),
        _slidenum(5),
    ], None, True


def _layout_content_sub():
    top = _BODY_TOP + 0.48
    return "Inhalt mit Subheadline", [
        _kicker(2), _title(3), _sub(4, 13, _LEFT, _WIDTH),
        _body(5, 1, (_LEFT, top, _WIDTH, _BODY_H - 0.48)),
        _slidenum(6),
    ], None, True


def _layout_two_col():
    top = _BODY_TOP + 0.48
    h = _BODY_H - 0.48
    return "Zweispaltig", [
        _kicker(2), _title(3),
        _sub(4, 13, _LEFT, _COL_W), _sub(5, 14, _COL_2, _COL_W),
        _body(6, 1, (_LEFT, top, _COL_W, h)),
        _body(7, 2, (_COL_2, top, _COL_W, h)),
        _slidenum(8),
    ], None, True


def _layout_title_only():
    return "Nur Titel", [_kicker(2), _title(3), _slidenum(4)], None, True


def _layout_grey():
    return ("Nur Titel, hellgrau", [_kicker(2), _title(3), _slidenum(4)],
            _background(LIGHT), True)


_LAYOUTS = [  # (Konstante, Bauer)
    ("L_COVER", _layout_cover),
    ("L_DIVIDER", _layout_divider),
    ("L_TEXT", _layout_content),
    ("L_TEXT_SUB", _layout_content_sub),
    ("L_TWO_COL", _layout_two_col),
    ("L_CHART", _layout_title_only),
    ("L_GREY", _layout_grey),
]


def _build_theme(master) -> None:
    from lxml import etree
    from pptx.opc.constants import RELATIONSHIP_TYPE as RT

    theme_colors = {
        "dk1": BLACK, "lt1": WHITE, "dk2": GREY, "lt2": LIGHT,
        "accent1": SAPHIR, "accent2": RUBIN, "accent3": SMARAGD,
        "accent4": AMETHYST, "accent5": TOPAS, "accent6": TUERKIS,
        "hlink": SAPHIR, "folHlink": AMETHYST,
    }
    part = master.part.part_related_by(RT.THEME)
    root = etree.fromstring(part.blob)
    root.set("name", "Hub")
    scheme = root.find(".//a:clrScheme", _NS)
    scheme.set("name", "Edelstein")
    for name, color in theme_colors.items():
        slot = scheme.find(f"a:{name}", _NS)
        for child in list(slot):
            slot.remove(child)
        etree.SubElement(slot, f"{{{_A}}}srgbClr", val=str(color))
    fonts = root.find(".//a:fontScheme", _NS)
    fonts.set("name", "Hub")
    for kind in ("majorFont", "minorFont"):
        fonts.find(f"a:{kind}/a:latin", _NS).set("typeface", FONT)
    part._blob = etree.tostring(root, xml_declaration=True,
                                encoding="UTF-8", standalone=True)


def neutrale_vorlage() -> Presentation:
    """Baut die neutrale Vorlage im Speicher und liefert sie ohne Folien."""
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    master = prs.slide_masters[0]
    _build_theme(master)
    _build_master(master)

    for extra in list(master.slide_layouts)[len(_LAYOUTS):]:
        master.slide_layouts.remove(extra)

    for (const, builder), layout in zip(_LAYOUTS, master.slide_layouts):
        if globals()[const] != master.slide_layouts.index(layout):
            raise RuntimeError(f"{const} passt nicht zur Layout-Reihenfolge")
        name, shapes, bg, show_master = builder()
        el = layout._element
        el.find("p:cSld", _NS).set("name", name)
        el.attrib.pop("type", None)
        el.set("showMasterSp", "1" if show_master else "0")
        _replace_tree(el, shapes, bg)

    prs.core_properties.author = AUTHOR
    prs.core_properties.title = "Hub-Vorlage"
    return prs


def vorlage_speichern(path: Path | str = TEMPLATE) -> Path:
    """Schreibt die neutrale Vorlage als Datei, als Ausgangspunkt für eine
    eigene Gestaltung. Nach einer Änderung an Palette oder Name neu
    schreiben, sonst trägt die Datei den alten Stand."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    neutrale_vorlage().save(str(path))
    findings = check_package(path)
    if findings:
        raise RuntimeError("Vorlage fehlerhaft:\n" + "\n".join(findings))
    return path


def _probedeck(ziel: Path) -> list[str]:
    """Baut ein kleines Deck mit den wichtigsten Bausteinen, als Rauchtest."""
    prs = open_template()
    cover(prs, "Probedeck", "Rauchtest der Bausteine")
    s = new_slide(prs, L_TEXT, keep={PH_TITLE, PH_BODY, PH_KICKER})
    head(s, "SITUATION", "Kernaussage der Folie in einem Satz")
    src = Sources()
    for ph in s.placeholders:
        if ph.placeholder_format.idx == PH_BODY:
            bullets(ph, [f"Erste Aussage mit Beleg{src.ref('Autor, Werk, Kapitel 1')}",
                         ("Schlussfolgerung darunter", 1)])
    footnote_sources(s, src)
    s = new_slide(prs, L_CHART, keep={PH_TITLE, PH_KICKER})
    head(s, "ERGEBNIS", "Drei Kennzahlen und ein Ablauf")
    for i, (wert, label) in enumerate([("EUR 1.2 m", "Bestand"),
                                       ("98 %", "Liefertreue"),
                                       ("14 d", "Reichweite")]):
        kpi_card(s, CL + Inches(3.0 * i), CONTENT_TOP, Inches(2.7), wert, label)
    flow_box(s, CL, Inches(3.6), Inches(3.0), Inches(1.2), "Schritt 1", "Daten lesen")
    arrow(s, CL + Inches(3.1), Inches(4.1))
    flow_box(s, CL + Inches(3.5), Inches(3.6), Inches(3.0), Inches(1.2),
             "Schritt 2", "Rechnen", accent=AMETHYST)
    slide_numbers(prs)
    return save(prs, ziel)


if __name__ == "__main__":
    import sys
    import tempfile

    sys.stdout.reconfigure(encoding="utf-8")
    ziel = Path(tempfile.mkdtemp()) / "probedeck.pptx"
    befunde = _probedeck(ziel)
    print(f"Probedeck gebaut: {ziel}")
    print(f"Autor laut Einstellungen: {AUTHOR or '(leer)'}")
    print("Befunde: " + ("keine" if not befunde else "\n".join(befunde)))
