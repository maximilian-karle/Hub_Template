"""Baut Curriculum und Modulhandbuch als PDF aus einer Datendatei.

Der Stil folgt einem Hochschul-Studienplan. Das Curriculum hat zwei Seiten A4
hoch. Seite 1 zeigt den Trimesterplan mit Trimesterpfeil links, Modulkacheln
je Bereichsspalte, Klammern mit Stunden rechts und der Verteilung nach
Bereich unten. Seite 2 zeigt die Profilentwicklung, je Trimester und Spalte
den Nachweis mit seiner Stufe. Das Modulhandbuch hat je Modul eine Seite und,
wo vorhanden, einen Lesebegleiter.

Alle Inhalte stehen in der Datendatei (Standard `curriculum.json` neben
diesem Skript), das Schema beschreibt die README im selben Ordner. Breiten
und Höhen rechnet der Builder aus der Zahl der Spalten und Trimester.

Aufruf
    python3 build_curriculum.py [--daten DATEI] [--beispiel]
                                [--curriculum PDF] [--modulhandbuch PDF] [--html]

Gedruckt wird über einen Chromium-Browser im Headless-Modus (Edge oder
Chrome), weil das ohne zusätzliche Druckbibliotheken auf Windows und macOS
läuft.
"""
from __future__ import annotations

import argparse
import html
import json
import math
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
HUB = HERE.parents[1]
EINSTELLUNGEN = HUB / "00_kern" / "einstellungen.json"

# Erster vorhandener Chromium-Browser. Eine Umgebungsvariable CURRICULUM_BROWSER
# geht allen Pfaden vor.
BROWSER = [
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
    Path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"),
    Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),
    Path("/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"),
    Path("/Applications/Chromium.app/Contents/MacOS/Chromium"),
]

# Feste Stilfarben (Kopf, Pfeil, Schrift). Sie bleiben in jeder Farbwahl gleich.
NAVY = "#004a85"
TIEF = "#0b2a4a"
TAG = "#59bdeb"

# Standardfarben der Kacheln, wenn ein Bereich keine eigene Farbe hat.
# "navy" ist der Stil der Vorlage (Blautöne, ein Akzent in Orange),
# "edelstein" die gesättigte Palette für Diagramme.
PALETTEN = {
    "navy": dict(bereiche=["#0b2a4a", "#0a4a83", "#3f6fb6", "#0098d6", "#f39b11", "#1f6fb5"],
                 sprachen=["#5ac1ee", "#7fcdf0", "#3fb0e0"], abschluss="#4e8a28",
                 ausblick=["#7ab648", "#4e8a28"]),
    "edelstein": dict(bereiche=["#0000FF", "#9D00FF", "#E0115F", "#FF9500", "#00D4E0", "#94A3B8"],
                      sprachen=["#00D4E0", "#94A3B8", "#FFD500"], abschluss="#00EF91",
                      ausblick=["#00EF91", "#00D4E0"]),
}
STUFE_FARBEN = [("#dbeef9", TIEF), ("#7fcdf0", TIEF), ("#1f6fb5", "#ffffff"), (TIEF, "#ffffff")]
STUFEN_STANDARD = [
    dict(name="Grundlagen", text="Theorie gelernt, noch kein eigener Fall"),
    dict(name="angewandt", text="an einem echten Fall umgesetzt, Wirkung nicht gemessen"),
    dict(name="belegt", text="Case Study mit gemessener Wirkung"),
    dict(name="trägt", text="mehrfach belegt, vor Dritten vertretbar"),
]

# Geometrie in mm. Die Kachelfläche ist fest, Spaltenbreiten und Zeilenhöhen
# werden aus der Zahl der Spalten und Trimester gerechnet.
X_TILES, W_TILES, GAP = 60.0, 127.0, 0.8
W_SPR = 21.4
ROW_GAP, PAIR_GAP, PAD, FRAME_GAP = 1.2, 3.0, 2.0, 3.0
Y_GRID = 63.0
Y_LEG = 266.5
H_TRIMESTER_MAX = 48.0
H_PROFIL_MAX = 24.0
H_MIN = 11.0
KLAMMER_VOLL = 26.0  # ab dieser Höhe steht das Symbol über dem Klammertext


class Datenfehler(ValueError):
    pass


# ----------------------------------------------------------------------------
# Daten laden und vorbereiten
# ----------------------------------------------------------------------------

def praefix(code: str) -> str:
    m = re.match(r"[^\d]+", code or "")
    return m.group(0) if m else ""


def ist_hell(farbe: str) -> bool:
    """Relative Helligkeit nach WCAG, damit Text auf hellen Kacheln dunkel wird."""
    f = farbe.lstrip("#")
    if len(f) == 3:
        f = "".join(c * 2 for c in f)
    try:
        r, g, b = (int(f[i:i + 2], 16) / 255 for i in (0, 2, 4))
    except ValueError:
        return False
    lin = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in (r, g, b)]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2] > 0.5


def textfarbe(bg: str) -> str:
    return TIEF if ist_hell(bg) else "#ffffff"


def einstellungen_bereiche() -> list:
    try:
        daten = json.loads(EINSTELLUNGEN.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return []
    return daten.get("profil", {}).get("bereiche", []) or []


def einstellungen_name() -> str:
    try:
        return json.loads(EINSTELLUNGEN.read_text(encoding="utf-8")).get("person", {}).get("name", "")
    except (OSError, ValueError):
        return ""


class Plan:
    """Aufbereitete Daten. Alle Zugriffe der Seitenbauer laufen hierüber."""

    def __init__(self, d: dict):
        self.d = d
        self.hinweise: list = []
        palette = PALETTEN.get(d.get("farben", "navy"))
        if palette is None:
            raise Datenfehler(f"farben muss eine von {', '.join(PALETTEN)} sein")
        self.palette = palette

        bereiche = d.get("bereiche") or einstellungen_bereiche()
        if not bereiche:
            raise Datenfehler("keine Bereiche, weder in der Datendatei noch in 00_kern/einstellungen.json")
        self.bereiche = []
        for i, b in enumerate(bereiche):
            farbe = b.get("farbe") or palette["bereiche"][i % len(palette["bereiche"])]
            self.bereiche.append(dict(kuerzel=b["kuerzel"], name=b["name"], farbe=farbe))
        self.farbe = {b["kuerzel"]: b["farbe"] for b in self.bereiche}
        self.bereich_name = {b["kuerzel"]: b["name"] for b in self.bereiche}

        spalten = d.get("spalten") or [dict(kopf=b["name"], unterzeile="", bereiche=[b["kuerzel"]])
                                       for b in self.bereiche]
        self.spalten = [dict(kopf=s["kopf"], unterzeile=s.get("unterzeile", ""), bereiche=list(s["bereiche"]))
                        for s in spalten]
        if not 1 <= len(self.spalten) <= 6:
            raise Datenfehler("es braucht 1 bis 6 Bereichsspalten, gedacht sind 3 bis 5")
        self.spalte_von = {}
        for i, s in enumerate(self.spalten):
            for k in s["bereiche"]:
                if k not in self.farbe:
                    raise Datenfehler(f"Spalte {s['kopf']} nennt Bereich {k}, der in bereiche fehlt")
                self.spalte_von[k] = i
        fehlend = [b["kuerzel"] for b in self.bereiche if b["kuerzel"] not in self.spalte_von]
        if fehlend:
            raise Datenfehler(f"Bereiche ohne Spalte: {', '.join(fehlend)}")

        spr = d.get("sprachen")
        self.sprachen = None
        if spr and spr.get("bereiche"):
            self.sprachen = dict(kopf=spr.get("kopf", "Sprachen"), unterzeile=spr.get("unterzeile", ""))
            for i, b in enumerate(spr["bereiche"]):
                farbe = b.get("farbe") or palette["sprachen"][i % len(palette["sprachen"])]
                self.farbe[b["kuerzel"]] = farbe
                self.bereich_name[b["kuerzel"]] = b["name"]
            self.sprach_bereiche = [b["kuerzel"] for b in spr["bereiche"]]
        else:
            self.sprach_bereiche = []

        self.trimester = d.get("trimester", [])
        if not 2 <= len(self.trimester) <= 10:
            raise Datenfehler("es braucht 2 bis 10 Trimester")
        self.stunden: dict = {}
        self.modul_bereich: dict = {}
        self.abschluss_farbe = None
        for t in self.trimester:
            t["nr"] = str(t["nr"])
            t["_spalten"] = [[] for _ in self.spalten]
            t["_sprachen"] = []
            for m in t.get("module", []):
                k = m.get("bereich") or self.bereich_zu(m.get("kuerzel", ""))
                if k is None:
                    raise Datenfehler(f"Modul {m.get('kuerzel') or m.get('name')} in Trimester {t['nr']} "
                                      "passt zu keinem Bereich, Feld bereich setzen")
                if m.get("kuerzel") and not m.get("offen"):
                    if m["kuerzel"] in self.stunden:
                        raise Datenfehler(f"Modul {m['kuerzel']} steht zweimal im Plan")
                    self.stunden[m["kuerzel"]] = float(m.get("stunden", 0))
                    self.modul_bereich[m["kuerzel"]] = k
                if k in self.sprach_bereiche:
                    t["_sprachen"].append(m)
                else:
                    t["_spalten"][self.spalte_von[k]].append(m)
            a = t.get("abschluss")
            if a:
                a.setdefault("kuerzel", "AA1")
                a.setdefault("name", "Abschlussarbeit")
                a.setdefault("bereich_name", a["name"])
                self.abschluss_farbe = a.get("farbe") or palette["abschluss"]
                self.farbe[praefix(a["kuerzel"])] = self.abschluss_farbe
                self.stunden[a["kuerzel"]] = float(a.get("stunden", 0))
                self.modul_bereich[a["kuerzel"]] = praefix(a["kuerzel"])
                self.bereich_name[praefix(a["kuerzel"])] = a["bereich_name"]
                if any(t["_spalten"]):
                    raise Datenfehler(f"Trimester {t['nr']} hat eine Abschlussarbeit und weitere Module, "
                                      "neben ihr sind nur Sprachen möglich")
        self.trimester_index = {t["nr"]: i for i, t in enumerate(self.trimester)}

        stufen = d.get("profil", {}).get("stufen") or STUFEN_STANDARD
        if not 2 <= len(stufen) <= 4:
            raise Datenfehler("profil.stufen braucht 2 bis 4 Einträge")
        farben = STUFE_FARBEN if len(stufen) == 4 else [STUFE_FARBEN[i] for i in
                                                        ([0, 2, 3] if len(stufen) == 3 else [0, 3])]
        self.stufen = [dict(name=s["name"], text=s.get("text", ""), bg=f[0], fg=f[1])
                       for s, f in zip(stufen, farben)]
        self.einstellungen_abgleichen()

    def bereich_zu(self, code: str):
        """Längster Bereich, dessen Kürzel am Anfang des Modulkürzels steht."""
        treffer = [k for k in list(self.spalte_von) + self.sprach_bereiche if code.startswith(k)]
        return max(treffer, key=len) if treffer else None

    def einstellungen_abgleichen(self):
        eigen = {b["kuerzel"] for b in einstellungen_bereiche()}
        hier = {b["kuerzel"] for b in self.bereiche}
        if eigen and eigen != hier:
            self.hinweise.append("Bereiche weichen von profil.bereiche in 00_kern/einstellungen.json ab "
                                 f"(dort {', '.join(sorted(eigen))}, hier {', '.join(sorted(hier))})")

    def summe(self, codes) -> float:
        return sum(self.stunden.get(c, 0) for c in codes)

    def codes_trimester(self, i: int) -> list:
        t = self.trimester[i]
        codes = [m["kuerzel"] for col in t["_spalten"] for m in col if m.get("kuerzel") and not m.get("offen")]
        codes += [m["kuerzel"] for m in t["_sprachen"] if m.get("kuerzel") and not m.get("offen")]
        if t.get("abschluss"):
            codes.append(t["abschluss"]["kuerzel"])
        return codes

    def stunden_bereich(self, kuerzel: str) -> float:
        return sum(v for c, v in self.stunden.items() if self.modul_bereich.get(c) == kuerzel)

    def farbe_modul(self, code: str) -> str:
        k = self.modul_bereich.get(code) or self.bereich_zu(code) or praefix(code)
        return self.farbe.get(k, NAVY)


def ersetzen(text: str, d: dict) -> str:
    """Platzhalter {person}, {stand} und {zeitraum} in Kopfzeilen. Ohne Person fällt " von {person}" weg."""
    if not d.get("person"):
        text = text.replace(" von {person}", "").replace("{person}", "")
    for k in ("person", "stand", "zeitraum"):
        text = text.replace("{" + k + "}", str(d.get(k, "")))
    return text


def untertitel(liste_, d):
    zeilen = [ersetzen(z, d) for z in liste_] + ["", ""]
    return zeilen[:2]


def zahl(x: float) -> str:
    """Deutsche Schreibweise mit Tausenderpunkt, ganze Stunden ohne Nachkomma."""
    if abs(x - round(x)) < 1e-9:
        return f"{int(round(x)):,}".replace(",", ".")
    return f"{x:,.1f}".replace(",", "X").replace(".", ",").replace("X", ".")


# ----------------------------------------------------------------------------
# Bausteine
# ----------------------------------------------------------------------------

def esc(s) -> str:
    """Escaped Text. "|" wird zur Trennstelle, "\\n" zum festen Umbruch."""
    return html.escape(str(s)).replace("|", "&shy;").replace("\n", "<br>")


def box(x, y, w, h, inner="", cls="", style=""):
    return (f'<div class="a {cls}" style="left:{x:.2f}mm;top:{y:.2f}mm;width:{w:.2f}mm;'
            f'height:{h:.2f}mm;{style}">{inner}</div>')


ICONS = {
    "flag": '<path d="M7 4v17M7 5h10l-2 3.5 2 3.5H7" fill="none" stroke="#fff" stroke-width="1.6"/>',
    "key": '<circle cx="8" cy="12" r="3.6" fill="none" stroke="#fff" stroke-width="1.6"/>'
           '<path d="M11.6 12H20M17 12v3M20 12v3" stroke="#fff" stroke-width="1.6"/>',
    "gear": '<circle cx="12" cy="12" r="3" fill="none" stroke="#fff" stroke-width="1.6"/>'
            '<path d="M12 4v3M12 17v3M4 12h3M17 12h3M6.3 6.3l2.1 2.1M15.6 15.6l2.1 2.1'
            'M6.3 17.7l2.1-2.1M15.6 8.4l2.1-2.1" stroke="#fff" stroke-width="1.6"/>',
    "cap": '<path d="M3 10l9-4 9 4-9 4z" fill="none" stroke="#fff" stroke-width="1.6"/>'
           '<path d="M7 12v4c2.5 2 7.5 2 10 0v-4M21 10v5" fill="none" stroke="#fff" stroke-width="1.6"/>',
    "book": '<path d="M4 6c3-1.5 5.5-1.5 8 0v13c-2.5-1.5-5-1.5-8 0zM12 6c2.5-1.5 5-1.5 8 0v13c-3-1.5-5.5-1.5-8 0z" '
            'fill="none" stroke="#fff" stroke-width="1.6"/>',
    "chart": '<path d="M4 20h16M7 20v-6M12 20V8M17 20v-9" fill="none" stroke="#fff" stroke-width="1.8"/>',
}


def icon(kind):
    if kind not in ICONS:
        raise Datenfehler(f"unbekanntes Symbol {kind}, erlaubt {', '.join(ICONS)}")
    return (f'<svg viewBox="0 0 24 24" width="100%" height="100%" style="background:{NAVY}">'
            f'{ICONS[kind]}</svg>')


def kopf(titel1, titel2, tag, zeile1, zeile2):
    titel = esc(titel1) + (f"<br>{esc(titel2)}" if titel2 else "")
    out = [box(12, 9, 150, 31, f'<div class="titel">{titel}</div>', style=f"background:{NAVY}")]
    out.append(box(119, 38, 85, 11, f'<div class="tag">{esc(tag)}</div>', style=f"background:{TAG}"))
    out.append(box(14, 42.5, 102, 8, f'<div class="unter">{esc(zeile1)}<br>{esc(zeile2)}</div>'))
    return out


def spaltenkopf(spalten, breiten):
    out, x = [], X_TILES
    for s, w in zip(spalten, breiten):
        out.append(box(x, Y_GRID - 8.5, w, 7,
                       f'<div class="sk"><b>{esc(s["kopf"])}</b><br>{esc(s.get("unterzeile", ""))}</div>'))
        x += w + GAP
    return out


def gruppen_index(plan_index, gruppen, schluessel):
    """Ersetzt die Trimesternummern der Klammern durch Zeilenindizes und prüft Lücken."""
    gesehen = []
    for g in gruppen:
        for k in g["klammern"]:
            try:
                k["rows"] = [plan_index[str(n)] for n in k[schluessel]]
            except KeyError as e:
                raise Datenfehler(f"Klammer {k.get('titel')} nennt unbekannte Zeile {e}") from None
            gesehen += k["rows"]
    if sorted(gesehen) != list(range(len(plan_index))):
        raise Datenfehler(f"Klammern müssen jede Zeile genau einmal und in Reihenfolge enthalten ({schluessel})")
    return gruppen


def ueberbau(gruppen):
    """Höhe aller Abstände ohne die Zeilen selbst."""
    rows = sum(len(k["rows"]) for g in gruppen for k in g["klammern"])
    kl = sum(len(g["klammern"]) for g in gruppen)
    return (2 * PAD * len(gruppen) + FRAME_GAP * (len(gruppen) - 1)
            + ROW_GAP * (rows - kl) + PAIR_GAP * (kl - len(gruppen)))


def hoehen_rechnen(n, gruppen, vorgaben, ende_max, h_max):
    """Feste Höhen aus den Daten, der Rest teilt den freien Platz gleich auf."""
    frei = ende_max - Y_GRID - ueberbau(gruppen)
    fest = [v for v in vorgaben if v]
    offen = n - len(fest)
    h = min(h_max, (frei - sum(fest)) / offen) if offen else h_max
    hoehen = [float(v) if v else h for v in vorgaben]
    if min(hoehen) < H_MIN or sum(hoehen) > frei + 0.01:
        raise Datenfehler(f"die Zeilen passen nicht auf die Seite (frei {frei:.0f} mm, "
                          f"gebraucht {sum(hoehen):.0f} mm, Mindesthöhe {H_MIN} mm)")
    return hoehen


def layout(gruppen, hoehen):
    """Liefert y je Zeile und die Rahmen der Gruppen und Klammern."""
    y = Y_GRID
    ys, rahmen = {}, []
    for g in gruppen:
        top = y
        y += PAD
        kl = []
        for i, k in enumerate(g["klammern"]):
            if i:
                y += PAIR_GAP - ROW_GAP
            kt = y
            for r in k["rows"]:
                ys[r] = y
                y += hoehen[r] + ROW_GAP
            kl.append((k, kt, y - ROW_GAP))
        y += PAD - ROW_GAP
        rahmen.append((g, top, y, kl))
        y += FRAME_GAP
    return ys, rahmen, y - FRAME_GAP


def gerust(rahmen, ys, hoehen, labels, rechts, wort_trimester):
    """Rahmen, Jahreslabel, Pfeil, Klammern, Meilensteine und Zahlen rechts."""
    svg, out = [], []
    for g, top, bot, kl in rahmen:
        svg.append(f'<rect x="9" y="{top:.2f}" width="198" height="{bot - top:.2f}" fill="none" '
                   f'stroke="#9aa3ad" stroke-width="0.25" stroke-dasharray="0.6 0.6"/>')
        hl = max(8, min(42, bot - top - 6))
        out.append(box(6.3, (top + bot) / 2 - hl / 2, 5, hl,
                       f'<div class="jahr">{esc(g["jahr"])}</div>', style=f"background:{TIEF}"))
        for k, kt, kb in kl:
            mid = (kt + kb) / 2
            x0, x1, xm = 44.0, 57.5, 50.75
            svg.append(f'<polygon fill="{TIEF}" points="{x0},{kt - 1.2} {xm},{kt + 1.6} {x1},{kt - 1.2} '
                       f'{x1},{kb - 0.6} {xm},{kb + 2.4} {x0},{kb - 0.6}"/>')
            svg.append(f'<path d="M42.4 {kt:.2f}H41.2V{kb:.2f}H42.4" fill="none" stroke="{TIEF}" stroke-width="0.3"/>')
            svg.append(f'<path d="M188.4 {kt:.2f}H189.6V{kb:.2f}H188.4M189.6 {mid:.2f}H191" '
                       f'fill="none" stroke="{TIEF}" stroke-width="0.3"/>')
            text = f'<div class="mt">{esc(k["titel"])}</div><div class="mx">{esc(k.get("text", ""))}</div>'
            if kb - kt >= KLAMMER_VOLL:
                iy = mid - 12
                out.append(box(13, iy, 8, 8, icon(k.get("icon", "flag"))))
                svg.append(f'<path d="M22 {iy + 4:.2f}H41.2" stroke="{TIEF}" stroke-width="0.3"/>')
                out.append(box(13, iy + 9, 27, 16, text))
            else:
                # Kurze Klammer, Text ohne Symbol mittig neben der Klammer
                out.append(box(13, kt, 27, kb - kt, text, cls="mitte"))
            gross, klein = rechts(k)
            out.append(box(191.5, mid - 5, 17, 10,
                           f'<div class="rz">{esc(gross)}</div><div class="rk">{esc(klein)}</div>'))
            for r in k["rows"]:
                nr, zeit = labels[r]
                h = hoehen[r]
                ist_zahl = nr.isdigit()
                txt = (f'<div class="pnr{"" if ist_zahl else " heute"}">{esc(nr + ("." if ist_zahl else ""))}</div>'
                       f'<div class="pt">{esc(wort_trimester) if ist_zahl else ""}</div>'
                       f'<div class="pz">{esc(zeit)}</div>')
                out.append(box(x0, ys[r], x1 - x0, h, txt, cls="pfeil"))
    s = ('<svg class="a" style="left:0;top:0" width="210mm" height="297mm" viewBox="0 0 210 297">'
         + "".join(svg) + "</svg>")
    return [s] + out


def kachel(x, y, w, h, m, farbe, halb=False):
    if m.get("offen"):
        return box(x, y, w, h, f'<div class="kn">{esc(m["name"])}</div>',
                   cls="kachel offen" + (" halb" if halb else ""))
    fg = textfarbe(farbe)
    badge = (f'<div class="badge" style="border-color:{fg};color:{fg}">{esc(m["kuerzel"])}</div>'
             if m.get("kuerzel") else "")
    return box(x, y, w, h, f'<div class="kn" style="color:{fg}">{esc(m["name"])}</div>{badge}',
               cls="kachel" + (" halb" if halb else ""), style=f"background:{farbe}")


def spalte_kacheln(plan, x, y, w, h, module, immer_halb=False):
    out = []
    n = len(module)
    if not n:
        return out
    hh = (h - GAP * (n - 1)) / n
    for j, m in enumerate(module):
        farbe = plan.farbe_modul(m.get("kuerzel", "")) if not m.get("offen") else "#fff"
        out.append(kachel(x, y + j * (hh + GAP), w, hh, m, farbe, halb=immer_halb or n > 1))
    return out


def breiten(plan, mit_sprachen):
    n = len(plan.spalten)
    rest = W_TILES - ((W_SPR + GAP) if mit_sprachen else 0)
    w = (rest - (n - 1) * GAP) / n
    return w


def legende(titel, eintraege, notiz):
    """Verteilung je Bereich. Bis acht Einträge in zwei Reihen zu je vier, darüber breiter verteilt."""
    y0 = Y_LEG
    out = [box(13, y0, 186, 27.5, style="background:#f1f2f4")]
    out.append(box(15, y0 - 2.6, 36, 5.2, f'<div class="lt">{esc(titel)}</div>', style=f"background:{TIEF}"))
    je_reihe = max(4, math.ceil(len(eintraege) / 2))
    schritt = 184 / je_reihe
    for i, (name, code, farbe, wert) in enumerate(eintraege):
        x = 17 + (i % je_reihe) * schritt
        y = y0 + 3.6 + (i // je_reihe) * 10.5
        fg = textfarbe(farbe)
        rand = ";border:0.2mm solid #c9d3dc" if fg != "#ffffff" else ""
        out.append(box(x, y, schritt - 2, 4, f'<div class="ln" style="color:{farbe if fg == "#ffffff" else TIEF}">'
                                             f'{esc(name)}</div>'))
        out.append(box(x, y + 4.4, 8.5, 6.2, f'<div class="lc" style="color:{fg}">{esc(code)}</div>',
                       style=f"background:{farbe}{rand}"))
        out.append(box(x + 9.1, y + 4.4, 9.5, 6.2,
                       f'<div class="lw" style="color:{fg}">{zahl(wert)}</div>'
                       f'<div class="lu" style="color:{fg}">Stunden</div>', style=f"background:{farbe}{rand}"))
    out.append(box(17, y0 + 24.7, 180, 2.6, f'<div class="lnote">{esc(notiz)}</div>'))
    return out


# ----------------------------------------------------------------------------
# Seiten des Curriculums
# ----------------------------------------------------------------------------

def seite_plan(plan: Plan):
    d = plan.d
    gruppen = gruppen_index(plan.trimester_index, d["klammern"], "trimester")
    hoehen = hoehen_rechnen(len(plan.trimester), gruppen, [t.get("hoehe") for t in plan.trimester],
                            Y_LEG - 16, H_TRIMESTER_MAX)
    ys, rahmen, ende = layout(gruppen, hoehen)
    titel = d["titel"]
    out = kopf(titel[0], titel[1] if len(titel) > 1 else "",
               ersetzen(d.get("tag", "Curriculum {zeitraum}"), d), *untertitel(d.get("untertitel", []), d))
    mit_spr = plan.sprachen is not None
    w_col = breiten(plan, mit_spr)
    kopfzeilen = plan.spalten + ([plan.sprachen] if mit_spr else [])
    out += spaltenkopf(kopfzeilen, [w_col] * len(plan.spalten) + ([W_SPR] if mit_spr else []))

    def rechts(k):
        return zahl(sum(plan.summe(plan.codes_trimester(r)) for r in k["rows"])), "Stunden"

    out += gerust(rahmen, ys, hoehen, [(t["nr"], t["zeit"]) for t in plan.trimester], rechts,
                  d.get("wort_trimester", "Trimester"))
    for i, t in enumerate(plan.trimester):
        y, h = ys[i], hoehen[i]
        if t.get("abschluss"):
            a = t["abschluss"]
            w = len(plan.spalten) * w_col + (len(plan.spalten) - 1) * GAP
            fg = textfarbe(plan.abschluss_farbe)
            out.append(box(X_TILES, y, w, h,
                           f'<div class="kn" style="color:{fg}">{esc(a["name"])}</div>'
                           f'<div class="ks" style="color:{fg}">{esc(a.get("text", ""))}</div>'
                           f'<div class="badge" style="border-color:{fg};color:{fg}">{esc(a["kuerzel"])}</div>',
                           cls="kachel", style=f"background:{plan.abschluss_farbe}"))
        else:
            x = X_TILES
            for col in t["_spalten"]:
                out += spalte_kacheln(plan, x, y, w_col, h, col)
                x += w_col + GAP
        if mit_spr:
            x = X_TILES + len(plan.spalten) * (w_col + GAP)
            out += spalte_kacheln(plan, x, y, W_SPR, h, t["_sprachen"], immer_halb=True)

    gesamt = sum(plan.stunden.values())
    out.append(box(186, ende + 1.5, 23, 11,
                   f'<div class="rz">{zahl(gesamt)}</div><div class="rk">Stunden gesamt</div>'))

    eintraege = [(b["name"], b["kuerzel"], b["farbe"], plan.stunden_bereich(b["kuerzel"])) for b in plan.bereiche]
    if plan.abschluss_farbe:
        k = next(praefix(t["abschluss"]["kuerzel"]) for t in plan.trimester if t.get("abschluss"))
        eintraege.append((plan.bereich_name[k], k, plan.abschluss_farbe, plan.stunden_bereich(k)))
    for k in plan.sprach_bereiche:
        eintraege.append((plan.bereich_name[k], k, plan.farbe[k], plan.stunden_bereich(k)))
    out += legende("Stunden-Verteilung", eintraege,
                   d.get("verteilung_notiz", f"Stunden je Bereich über {len(plan.trimester)} Trimester."))
    return '<section class="page">' + "".join(out) + "</section>"


def zelle(plan, x, y, w, h, z):
    s = plan.stufen[z["stufe"]]
    bg, fg = s["bg"], s["fg"]
    code = z.get("module", "")
    badge = f'<div class="badge" style="border-color:{fg};color:{fg}">{esc(code)}</div>' if code else ""
    return box(x, y, w, h, f'<div class="kn" style="color:{fg}">{esc(z["text"])}</div>'
               f'<div class="stufe" style="color:{fg}">{esc(s["name"])}</div>{badge}',
               cls="kachel profil", style=f"background:{bg}")


def stufen_legende(plan, notiz, bis):
    y0 = Y_LEG
    out = [box(13, y0, 186, 27.5, style="background:#f1f2f4")]
    out.append(box(15, y0 - 2.6, 36, 5.2, '<div class="lt">Profil-Stufen</div>', style=f"background:{TIEF}"))
    schritt = 184 / max(4, len(plan.stufen))
    for i, s in enumerate(plan.stufen):
        x = 17 + i * schritt
        name = s["name"][:1].upper() + s["name"][1:]
        out.append(box(x, y0 + 3.6, schritt - 2, 4, f'<div class="ln" style="color:{TIEF}">{esc(name)}</div>'))
        out.append(box(x, y0 + 7.8, 8.5, 6.2, style=f"background:{s['bg']};border:0.2mm solid #c9d3dc"))
        out.append(box(x + 9.8, y0 + 7.6, schritt - 12, 7, f'<div class="lx">{esc(s["text"])}</div>'))
    n = len(plan.spalten)
    schritt = 184 / max(4, n)
    for i, sp in enumerate(plan.spalten):
        wert = sum(plan.stunden_bereich(k) for k in sp["bereiche"])
        x = 17 + i * schritt
        out.append(box(x, y0 + 16.9, 13, 6.2, f'<div class="lw">{zahl(wert)}</div><div class="lu">Stunden</div>',
                       style=f"background:{TIEF}"))
        out.append(box(x + 14, y0 + 17.1, schritt - 15, 6,
                       f'<div class="lh">{esc(sp["kopf"])} bis {esc(bis)}</div>'))
    out.append(box(17, y0 + 24.7, 180, 2.6, f'<div class="lnote">{esc(notiz)}</div>'))
    return out


def seite_profil(plan: Plan):
    p = plan.d["profil"]
    zeilen = p["zeilen"]
    for z in zeilen:
        z["nr"] = str(z["nr"])
    index = {z["nr"]: i for i, z in enumerate(zeilen)}
    gruppen = gruppen_index(index, p["klammern"], "zeilen")
    hoehen = hoehen_rechnen(len(zeilen), gruppen, [z.get("hoehe") for z in zeilen], Y_LEG - 5, H_PROFIL_MAX)
    ys, rahmen, _ = layout(gruppen, hoehen)
    titel = p["titel"]
    out = kopf(titel[0], titel[1] if len(titel) > 1 else "",
               ersetzen(p.get("tag", "Profilentwicklung {zeitraum}"), plan.d), *untertitel(p.get("untertitel", []), plan.d))
    n = len(plan.spalten)
    w = (W_TILES - (n - 1) * GAP) / n
    out += spaltenkopf(plan.spalten, [w] * n)
    out += gerust(rahmen, ys, hoehen, [(z["nr"], z["zeit"]) for z in zeilen],
                  lambda k: (k.get("gross", ""), k.get("klein", "")), plan.d.get("wort_trimester", "Trimester"))
    ausblick_nr = 0
    for i, z in enumerate(zeilen):
        y, h = ys[i], hoehen[i]
        if "ausblick" in z:
            a = z["ausblick"]
            farbe = a.get("farbe") or plan.palette["ausblick"][ausblick_nr % 2]
            ausblick_nr += 1
            fg = textfarbe(farbe)
            out.append(box(X_TILES, y, W_TILES, h,
                           f'<div class="kn" style="color:{fg}">{esc(a["titel"])}</div>'
                           f'<div class="ks" style="color:{fg}">{esc(a.get("text", ""))}</div>',
                           cls="kachel", style=f"background:{farbe}"))
            continue
        zellen = z.get("zellen", [])
        if len(zellen) != n:
            raise Datenfehler(f"Profilzeile {z['nr']} hat {len(zellen)} Zellen, erwartet {n} (eine je Spalte)")
        x = X_TILES
        for c in zellen:
            if c:
                if not 0 <= c["stufe"] < len(plan.stufen):
                    raise Datenfehler(f"Profilzeile {z['nr']}, Stufe {c['stufe']} gibt es nicht")
                out.append(zelle(plan, x, y, w, h, c))
            x += w + GAP
    bis = f'T{plan.trimester[-1]["nr"]}'
    out += stufen_legende(plan, p.get("notiz", "Stufe am Ende des Trimesters."), bis)
    return '<section class="page">' + "".join(out) + "</section>"


# ----------------------------------------------------------------------------
# Modulhandbuch
# ----------------------------------------------------------------------------

def liste(punkte):
    return "<ul>" + "".join(f"<li>{esc(p)}</li>" for p in punkte) + "</ul>"


def karte(titel, inhalt, cls=""):
    return f'<div class="karte {cls}"><div class="tab">{esc(titel)}</div>{inhalt}</div>'


def titel_teilen(m):
    if m.get("titel"):
        t = m["titel"]
        return t[0], t[1] if len(t) > 1 else ""
    worte = m["name"].split(" und ")
    if len(worte) > 1:
        return worte[0] + " und", " und ".join(worte[1:])
    return m["name"], ""


def kennzahlen(farbe, kenn):
    fg = textfarbe(farbe)
    return "".join(f'<div class="kz" style="background:{farbe};color:{fg}"><div class="kl">{esc(a)}</div>'
                   f'<div class="kw">{esc(b)}</div><div class="ks2">{esc(c)}</div></div>' for a, b, c in kenn)


def seite_handbuch(plan, m, stand):
    farbe = plan.farbe_modul(m["kuerzel"])
    t1, t2 = titel_teilen(m)
    dl = m.get("durchlauf", {})
    pr = m.get("pruefung", {})
    out = kopf(t1, t2, f'Modulhandbuch {m["kuerzel"]}',
               f'Kompetenzfeld {m.get("bereich", "")}, Durchlauf {dl.get("kurz", "")} {dl.get("text", "")}'
               .rstrip() + (f", Stand {stand}" if stand else ""),
               m.get("unterzeile", "Ein Modul läuft über das Trimester hinaus weiter und sammelt Projekte als Belege."))
    kenn = [("Kürzel", m["kuerzel"], m.get("bereich", "")),
            ("Stunden", zahl(float(m.get("stunden", 0))), m.get("aufteilung", "")),
            ("Durchlauf", dl.get("kurz", ""), dl.get("text", "")),
            ("Prüfung", pr.get("kurz", "ohne System"), pr.get("text", ""))]
    spuren = "".join(f'<p><b>{esc(s["spur"])}.</b> {esc(s["text"])}</p>' for s in m.get("anwendung", []))
    termine = "".join(f'<div class="tm"><b>{esc(t["titel"])}</b><br>{esc(t["datum"])}</div>'
                      for t in m.get("meilensteine", []))
    karten = [("Ausgangslage", f'<p>{esc(m.get("ausgangslage", ""))}</p>'),
              ("Am Ende kann ich", liste(m.get("koennen", []))),
              ("Was gelernt wird", liste(m.get("inhalte", []))),
              ("Anwendung", spuren),
              ("Prüfungsform", liste(m.get("pruefungsform", []))),
              ("Literatur", liste(m.get("literatur", [])))]
    inhalt = (f'<div class="kenn">{kennzahlen(farbe, kenn)}</div><div class="karten">'
              + "".join(karte(a, b) for a, b in karten)
              + (karte("Meilensteine", f'<div class="tms">{termine}</div>', "voll") if termine else "")
              + "</div>")
    return '<section class="page">' + "".join(out) + f'<div class="hb">{inhalt}</div></section>'


def kurzname(werk):
    return werk.split(",")[0]


def seite_lesebegleiter(plan, m, stand):
    gruppen = m["lesebegleiter"]
    schritte = [s for g in gruppen for s in g["schritte"]]
    im_modul = [s for g in gruppen if not g.get("spaeter") for s in g["schritte"]]
    spaeter = len(schritte) - len(im_modul)
    minuten = sum(s.get("minuten") or 0 for s in im_modul)
    offen = [s for s in im_modul if not s.get("minuten")]
    lesen = [w for s in im_modul for w in s.get("lesen", [])]
    werke = sorted({w["werk"] for w in lesen if not w.get("luecke") and "," in w["werk"]})
    luecken = list(dict.fromkeys(w["stelle"] for w in lesen if w.get("luecke")))
    t1, t2 = titel_teilen(m)
    out = kopf(t1, t2, f'Lesebegleiter {m["kuerzel"]}',
               "Was ich zu welchem Arbeitsschritt lese, in der Reihenfolge des Moduls"
               + (f", Stand {stand}" if stand else ""),
               "Seiten sind PDF-Seiten der Dateien in der Bibliothek, gedruckte Seiten in Klammern, wo geprüft.")
    kenn = [("Abschnitte", str(len(im_modul)),
             f"dazu {spaeter} später in einem anderen Modul" if spaeter else "alle im ersten Durchlauf"),
            ("Lesezeit", f"{minuten // 60} h {minuten % 60} Min.",
             f"{minuten} Minuten Pflicht" + (", ein Teil noch ohne Zeit" if offen else " im Modul")),
            ("Werke", str(len(werke)), ", ".join(kurzname(w) for w in werke)),
            ("Nach jedem Abschnitt", "Fragen", "Kontrollfragen und Karten, nach jedem Gate der Erklär-Check")]
    farbe = plan.farbe_modul(m["kuerzel"])
    rows, nr = [], 0
    for g in gruppen:
        rows.append(f'<div class="lg">{esc(g["titel"])}</div>')
        for s in g["schritte"]:
            nr += 1
            buch = "".join(f'<div class="lw2"><b>{esc("Lücke" if w.get("luecke") else kurzname(w["werk"]))}</b> '
                           f'{esc(w["stelle"])}, <span>{esc(w.get("seiten", ""))}</span></div>'
                           for w in s.get("lesen", []))
            mins = s.get("minuten")
            rows.append(f'<div class="lr"><div class="ln2">{nr}</div>'
                        f'<div class="ls"><b>{esc(s["titel"])}</b><br><span>{esc(s.get("id", ""))}, '
                        f'{esc(s.get("spur", ""))}</span></div>'
                        f'<div class="lb">{buch}</div><div class="lm"><b>{mins if mins else "offen"}</b><br>Min.</div>'
                        f'<div class="lm"><b>{esc(s.get("bis", ""))}</b><br>spätestens</div></div>')
    fuss = f'Werke in der Bibliothek. {esc("; ".join(werke))}.' if werke else ""
    if luecken:
        fuss += f' Lücken, die noch beschafft werden. {esc("; ".join(luecken))}.'
    inhalt = (f'<div class="kenn">{kennzahlen(farbe, kenn)}</div><div class="lese">{"".join(rows)}</div>'
              f'<div class="lfuss">{fuss}</div>')
    return '<section class="page">' + "".join(out) + f'<div class="hb">{inhalt}</div></section>'


def handbuch(plan: Plan):
    stand = plan.d.get("stand", "")
    teile = []
    for m in plan.d.get("handbuch", []):
        teile.append(seite_handbuch(plan, m, stand))
        if m.get("lesebegleiter"):
            teile.append(seite_lesebegleiter(plan, m, stand))
    return "".join(teile)


# ----------------------------------------------------------------------------
# Stil
# ----------------------------------------------------------------------------

CSS = """
@page { size: 210mm 297mm; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; background: #fff; }
body { font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; color: #1d2733;
  -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.page { position: relative; width: 210mm; height: 297mm; overflow: hidden; page-break-after: always; }
.page:last-child { page-break-after: auto; }
.a { position: absolute; }
.titel { color: #fff; font-weight: 700; font-size: 24pt; line-height: 1.08; text-transform: uppercase;
  padding: 4.2mm 0 0 5mm; letter-spacing: 0.2pt; }
.tag { color: #fff; font-size: 14pt; padding: 2.1mm 0 0 4mm; }
.unter { font-size: 6.4pt; color: #3a4450; line-height: 1.35; }
.sk { font-size: 5.6pt; color: #4b5560; line-height: 1.25; }
.sk b { font-size: 7pt; color: #0b2a4a; }
.jahr { writing-mode: vertical-rl; transform: rotate(180deg); color: #fff; font-weight: 700;
  font-size: 7pt; height: 100%; text-align: center; padding-right: 1mm; white-space: nowrap; }
.mt { font-weight: 700; font-size: 7.4pt; color: #0b2a4a; }
.mx { font-size: 5.4pt; color: #2b3540; line-height: 1.3; margin-top: 0.3mm; }
.mitte { display: flex; flex-direction: column; justify-content: center; }
.rz { font-weight: 700; font-size: 13pt; color: #0b2a4a; line-height: 1; }
.rk { font-weight: 700; font-size: 5.6pt; color: #0b2a4a; }
.pfeil { color: #fff; text-align: center; display: flex; flex-direction: column; justify-content: center; }
.pnr { font-weight: 700; font-size: 15pt; line-height: 1; }
.pnr.heute { font-size: 8pt; }
.pt { font-size: 5.4pt; }
.pz { font-size: 4.4pt; opacity: 0.85; }
.kachel { color: #fff; padding: 1.5mm 1.6mm; overflow: hidden; }
.kachel .kn { font-weight: 700; font-size: 6.6pt; line-height: 1.2; hyphens: manual; }
.kachel.halb { padding: 1.1mm 1.4mm; }
.kachel.halb .kn { font-size: 5.9pt; line-height: 1.15; }
.kachel.halb .badge { font-size: 4.6pt; bottom: 0.8mm; }
.kachel .ks { font-size: 5.6pt; line-height: 1.35; margin-top: 1mm; max-width: 80mm; }
.kachel.offen { border: 0.25mm dashed #8fb8d6; background: #fff; }
.kachel.offen .kn { color: #6c8aa3; font-weight: 400; }
.kachel.profil .kn { font-size: 6.1pt; font-weight: 600; }
.stufe { position: absolute; left: 1.6mm; bottom: 1.1mm; font-size: 4.8pt; opacity: 0.85; }
.badge { position: absolute; right: 1.1mm; bottom: 1mm; border: 0.25mm solid #fff; color: #fff;
  font-weight: 700; font-size: 5pt; padding: 0.35mm 0.6mm; line-height: 1; }
.lt { color: #fff; font-weight: 700; font-size: 8pt; padding: 0.9mm 0 0 2mm; }
.ln { font-weight: 700; font-size: 7.6pt; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.lh { font-weight: 700; font-size: 6.8pt; color: #0b2a4a; line-height: 1.15; }
.lc { color: #fff; font-weight: 700; font-size: 10pt; text-align: center; padding-top: 1.2mm; }
.lw { color: #fff; font-weight: 700; font-size: 7.6pt; text-align: center; padding-top: 0.5mm; line-height: 1; }
.lu { color: #fff; font-size: 4.2pt; text-align: center; }
.lx { font-size: 5.6pt; color: #2b3540; line-height: 1.3; }
.lnote { font-size: 5.6pt; color: #2b3540; }
.hb { position: absolute; left: 13mm; top: 58mm; width: 184mm; }
.kenn { display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.8mm; }
.kz { color: #fff; padding: 1.8mm 2.2mm; height: 21mm; overflow: hidden; }
.kl { font-size: 5.8pt; opacity: 0.9; }
.kw { font-weight: 700; font-size: 15pt; line-height: 1.15; margin-top: 0.6mm; }
.ks2 { font-size: 5.8pt; line-height: 1.3; margin-top: 0.6mm; }
.karten { display: grid; grid-template-columns: 1fr 1fr; column-gap: 4mm; row-gap: 6.5mm; margin-top: 8mm; }
.karte { background: #f1f2f4; padding: 5mm 3.2mm 2.6mm; position: relative; }
.karte.voll { grid-column: 1 / -1; }
.karte .tab { position: absolute; top: -2.6mm; left: 2mm; background: #0b2a4a; color: #fff; font-weight: 700;
  font-size: 8pt; padding: 0.9mm 2mm; }
.karte p { font-size: 7pt; line-height: 1.45; margin: 0 0 1.2mm 0; color: #1d2733; }
.karte ul { margin: 0; padding-left: 3.6mm; }
.karte li { font-size: 7pt; line-height: 1.45; margin-bottom: 0.6mm; color: #1d2733; }
.tms { display: flex; gap: 0.8mm; }
.tm { flex: 1; background: #0b2a4a; color: #fff; font-size: 6.4pt; padding: 1.6mm 2mm; line-height: 1.35; }
.lese { margin-top: 4mm; }
.lg { font-weight: 700; font-size: 7.6pt; color: #0b2a4a; border-bottom: 0.4mm solid #0b2a4a;
  margin: 2.4mm 0 1mm 0; padding-bottom: 0.6mm; }
.lr { display: grid; grid-template-columns: 7mm 50mm 1fr 11mm 15mm; gap: 0.8mm; margin-bottom: 0.8mm; }
.lr > div { background: #f1f2f4; padding: 1.1mm 1.6mm; font-size: 6.3pt; line-height: 1.3; }
.lr .ln2 { background: #0b2a4a; color: #fff; font-weight: 700; font-size: 9pt; text-align: center; padding-top: 1.4mm; }
.ls span { color: #6c7a88; font-size: 5.6pt; }
.lw2 span { color: #6c7a88; }
.lm { text-align: center; color: #0b2a4a; font-size: 5.4pt !important; }
.lm b { font-size: 7pt; }
.lfuss { font-size: 5.6pt; color: #2b3540; margin-top: 2mm; line-height: 1.35; }
"""


# ----------------------------------------------------------------------------
# Prüfen und Drucken
# ----------------------------------------------------------------------------

def pruefen(text, plan: Plan):
    """Schreibregeln im sichtbaren Text und Mindestregeln des Plans."""
    sichtbar = html.unescape(re.sub(r"<[^>]+>", " ", text.split("</style>")[-1]))
    for zeichen in ("\u2013", "\u2014"):
        stelle = re.search(rf".{{0,30}}{zeichen}.{{0,30}}", sichtbar)
        assert not stelle, f"Gedankenstrich im Text: {stelle.group(0)!r}"
    stelle = re.search(r"\S.{0,30}\s-\s.{0,30}", sichtbar)
    assert not stelle, f"Bindestrich als Pause im Text: {stelle.group(0)!r}"
    if plan.d.get("regeln", {}).get("modul_je_spalte", False):
        for t in plan.trimester[1:]:
            if not t.get("abschluss"):
                leer = [plan.spalten[i]["kopf"] for i, col in enumerate(t["_spalten"]) if not col]
                assert not leer, f"Trimester {t['nr']} ohne Modul in Spalte {', '.join(leer)}"


def browser_finden() -> Path:
    eigen = os.environ.get("CURRICULUM_BROWSER")
    if eigen:
        return Path(eigen)
    for b in BROWSER:
        if b.exists():
            return b
    for name in ("google-chrome", "chromium", "chromium-browser", "microsoft-edge", "msedge", "chrome"):
        pfad = shutil.which(name)
        if pfad:
            return Path(pfad)
    raise SystemExit("Kein Edge oder Chrome gefunden. Pfad über die Umgebungsvariable CURRICULUM_BROWSER setzen.")


def seitenzahl(pdf: Path):
    try:
        from pypdf import PdfReader
    except ImportError:
        return None
    return len(PdfReader(pdf).pages)


def drucken(doc: str, ziel: Path, html_behalten: bool):
    ziel.parent.mkdir(parents=True, exist_ok=True)
    quelle = ziel.with_suffix(".html")
    quelle.write_text(doc, encoding="utf-8")
    vorher = ziel.stat().st_mtime if ziel.exists() else 0
    subprocess.run([str(browser_finden()), "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={ziel}", quelle.resolve().as_uri()],
                   check=True, capture_output=True, timeout=180)
    # Der Browser meldet keinen Fehler, wenn das PDF gesperrt ist (etwa im Viewer geöffnet).
    if not ziel.exists() or ziel.stat().st_mtime == vorher:
        raise RuntimeError(f"{ziel.name} wurde nicht neu geschrieben, ist die Datei geöffnet?")
    if not html_behalten:
        quelle.unlink()
    return seitenzahl(ziel)


def dokument(titel, seiten):
    return (f'<!doctype html><html lang="de"><head><meta charset="utf-8"><title>{esc(titel)}</title>'
            f"<style>{CSS}</style></head><body>{seiten}</body></html>")


def ausgabepfade(d: dict, daten_pfad: Path, args) -> tuple:
    """Vorrang hat das Argument, dann --beispiel oder "beispiel" in den Daten, dann "ausgabe", dann der Standard."""
    basis = daten_pfad.parent
    if args.beispiel or d.get("beispiel"):
        standard = {"curriculum": "Beispiel_Curriculum.pdf",
                    "modulhandbuch": "../module/_beispiele/Beispiel_Modulhandbuch.pdf"}
    else:
        standard = {"curriculum": "Curriculum.pdf", "modulhandbuch": "../module/Modulhandbuch.pdf"}
        standard.update(d.get("ausgabe", {}))
    cur = Path(args.curriculum) if args.curriculum else basis / standard["curriculum"]
    hb = Path(args.modulhandbuch) if args.modulhandbuch else basis / standard["modulhandbuch"]
    return cur.resolve(), hb.resolve()


def main(argv=None):
    ap = argparse.ArgumentParser(description="Baut Curriculum und Modulhandbuch als PDF aus einer Datendatei.")
    ap.add_argument("--daten", default=str(HERE / "curriculum.json"), help="Datendatei (JSON)")
    ap.add_argument("--beispiel", action="store_true", help="Ausgabe unter den Namen der Beispiel-PDFs")
    ap.add_argument("--curriculum", help="Zielpfad für das Curriculum")
    ap.add_argument("--modulhandbuch", help="Zielpfad für das Modulhandbuch")
    ap.add_argument("--html", action="store_true", help="HTML neben dem PDF behalten")
    args = ap.parse_args(argv)

    daten_pfad = Path(args.daten).resolve()
    d = json.loads(daten_pfad.read_text(encoding="utf-8"))
    if not d.get("person"):
        d["person"] = einstellungen_name()
    try:
        plan = Plan(d)
        cur_pdf, hb_pdf = ausgabepfade(d, daten_pfad, args)
        dokumente = [(cur_pdf, f'Curriculum {d.get("zeitraum", "")}'.strip(),
                      seite_plan(plan) + (seite_profil(plan) if d.get("profil") else ""), 2 if d.get("profil") else 1)]
        hb = handbuch(plan)
        if hb:
            n = sum(1 + bool(m.get("lesebegleiter")) for m in d["handbuch"])
            dokumente.append((hb_pdf, "Modulhandbuch", hb, n))
    except Datenfehler as e:
        raise SystemExit(f"Fehler in {daten_pfad.name}: {e}")
    for h in plan.hinweise:
        print(f"Hinweis: {h}")
    for pdf, titel, seiten, soll in dokumente:
        doc = dokument(titel, seiten)
        pruefen(doc, plan)
        ist = drucken(doc, pdf, args.html)
        status = "" if ist is None else (f", {ist} Seiten" + ("" if ist == soll else f", erwartet {soll}"))
        print(f"geschrieben {pdf}{status}")


if __name__ == "__main__":
    main()
