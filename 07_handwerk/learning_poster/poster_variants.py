"""The two renderings of a topic file.

  sketch_html    the mind map drawn as if by hand: organic tapered branches,
                 a handwriting face, terms sitting on their twigs, takeaways
                 as notes
  compact_html   the dense five-column sheet, after the layout of the LaTeX
                 cheat sheet template github.com/kenfehling/latex-cheatsheet

Both read the topic through poster_toolkit.load(), so they cannot show
different content. Built by build_poster.py.
"""

from __future__ import annotations

import math
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import poster_toolkit as tk  # noqa: E402

NAVY, TEXT, MUTED = tk.NAVY, tk.TEXT, tk.MUTED
PAPER = "#fdfbf4"
NOTE = "#fff3b0"
HAND = '"Segoe Print", "Ink Free", "Comic Sans MS", cursive'
SOFT = 'Candara, Corbel, Calibri, "Segoe UI", sans-serif'

PAGE_W, PAGE_H = tk.PAGE_W, tk.PAGE_H
PT = 0.352778                   # one point in millimetres
MARGIN = 5.0
SPINE_L, SPINE_R = 146.0, 274.0
STAGGER = [0.0, 5.0, 1.5, 6.0]  # no two neighbouring blocks start flush
TITLE_H = 10.0
GAP = 7.0
BLOB_RX, BLOB_RY = 31.0, 17.0   # centre shape


class Measure:
    """Text widths from the font file, so a twig ends where its word ends.

    Without the file the width is estimated from the character count; the
    drawing then still builds, only the twig lengths are approximate.
    """

    def __init__(self, filename: str, average_em: float):
        self.average_em = average_em
        self.font = None
        path = Path("C:/Windows/Fonts") / filename
        if path.exists():
            import pymupdf
            self.font = pymupdf.Font(fontfile=str(path))

    def mm(self, text: str, pt: float) -> float:
        if self.font is not None:
            return self.font.text_length(text, fontsize=pt) * PT
        return len(text) * pt * self.average_em * PT


# --------------------------------------------------------------------------
# hand-drawn geometry
# --------------------------------------------------------------------------
def smooth(points: list[tuple[float, float]], closed: bool = False) -> str:
    """A Catmull-Rom spline through the points, as an SVG path."""
    n = len(points)

    def at(i: int) -> tuple[float, float]:
        return points[i % n] if closed else points[max(0, min(n - 1, i))]

    d = f"M{points[0][0]:.2f},{points[0][1]:.2f}"
    for i in range(n if closed else n - 1):
        p0, p1, p2, p3 = at(i - 1), at(i), at(i + 1), at(i + 2)
        d += (f" C{p1[0] + (p2[0] - p0[0]) / 6:.2f},{p1[1] + (p2[1] - p0[1]) / 6:.2f}"
              f" {p2[0] - (p3[0] - p1[0]) / 6:.2f},{p2[1] - (p3[1] - p1[1]) / 6:.2f}"
              f" {p2[0]:.2f},{p2[1]:.2f}")
    return d + (" Z" if closed else "")


def cubic(p0, p1, p2, p3, steps: int = 22) -> list[tuple[float, float]]:
    out = []
    for k in range(steps + 1):
        t = k / steps
        a, b, c, e = (1 - t) ** 3, 3 * (1 - t) ** 2 * t, 3 * (1 - t) * t * t, t ** 3
        out.append((a * p0[0] + b * p1[0] + c * p2[0] + e * p3[0],
                    a * p0[1] + b * p1[1] + c * p2[1] + e * p3[1]))
    return out


def tapered(line: list[tuple[float, float]], w0: float, w1: float,
            rng: random.Random) -> str:
    """A filled stroke that thins out, as a brush or a marker leaves it."""
    left, right = [], []
    last = len(line) - 1
    for i, (x, y) in enumerate(line):
        ax, ay = line[max(i - 1, 0)]
        bx, by = line[min(i + 1, last)]
        length = math.hypot(bx - ax, by - ay) or 1.0
        nx, ny = -(by - ay) / length, (bx - ax) / length
        half = (w0 + (w1 - w0) * i / last) / 2 * (1 + rng.uniform(-.07, .07))
        left.append((x + nx * half, y + ny * half))
        right.append((x - nx * half, y - ny * half))
    return smooth(left + right[::-1], closed=True)


def blob(cx: float, cy: float, rx: float, ry: float, rng: random.Random,
         square: float = 1.0, noise: float = .05, n: int = 18) -> str:
    """An uneven closed shape; square < 1 pulls it towards a rounded box."""
    points = []
    for k in range(n):
        t = 2 * math.pi * k / n
        c, s = math.cos(t), math.sin(t)
        wobble = 1 + rng.uniform(-noise, noise)
        points.append(
            (cx + rx * wobble * math.copysign(abs(c) ** square, c),
             cy + ry * wobble * math.copysign(abs(s) ** square, s)))
    return smooth(points, closed=True)


def bud(x: float, y: float, level: str) -> str:
    """The level marker, drawn where a twig meets its term."""
    r = 1.0
    fill = NAVY if level == "nutze" else PAPER
    out = (f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r}" fill="{fill}" '
           f'stroke="{NAVY}" stroke-width=".28"/>')
    if level == "kenne":
        out += (f'<path d="M{x:.2f},{y - r:.2f} A{r},{r} 0 0 0 {x:.2f},{y + r:.2f} Z" '
                f'fill="{NAVY}"/>')
    return out


def arrow(x0, y0, x1, y1, bend: float, rng: random.Random) -> str:
    """A short curved arrow with a two-stroke head."""
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    length = math.hypot(x1 - x0, y1 - y0) or 1.0
    qx = mx - (y1 - y0) / length * bend
    qy = my + (x1 - x0) / length * bend
    heading = math.atan2(y1 - qy, x1 - qx)
    head = ""
    for turn in (2.55, -2.55):
        hx = x1 + 1.5 * math.cos(heading + turn + rng.uniform(-.1, .1))
        hy = y1 + 1.5 * math.sin(heading + turn + rng.uniform(-.1, .1))
        head += f" M{x1:.2f},{y1:.2f} L{hx:.2f},{hy:.2f}"
    return (f'<path d="M{x0:.2f},{y0:.2f} Q{qx:.2f},{qy:.2f} {x1:.2f},{y1:.2f}{head}" '
            f'fill="none" stroke="{MUTED}" stroke-width=".4" stroke-linecap="round"/>')


# --------------------------------------------------------------------------
# sketch poster
# --------------------------------------------------------------------------
def sketch_html(topic: dict) -> str:
    rng = random.Random(topic["slug"])       # same drawing on every build
    hand = Measure("segoeprb.ttf", .62)
    soft = Measure("Candara.ttf", .47)
    clusters = topic["clusters"]
    cut = tk.split_sides(clusters)
    cx, cy = PAGE_W / 2, PAGE_H / 2
    under, over = [], []                     # branches below, text above

    def text(x, y, content, pt, family, fill, anchor="start", weight="400",
             style="normal"):
        return (f'<text x="{x:.2f}" y="{y:.2f}" font-family=\'{family}\' '
                f'font-size="{pt * PT:.3f}" font-weight="{weight}" '
                f'font-style="{style}" fill="{fill}" text-anchor="{anchor}">'
                f'{content}</text>')

    def draw_side(group: list[dict], sign: int, base: float) -> None:
        leaves = sum(len(c["terms"]) for c in group)
        fixed = len(group) * TITLE_H + (len(group) - 1) * GAP
        pitch = min(7.0, (PAGE_H - 2 * MARGIN - fixed) / leaves)
        term_pt = min(8.6, pitch / PT * .47)
        anchor = "start" if sign > 0 else "end"
        edge = PAGE_W - MARGIN if sign > 0 else MARGIN
        y = MARGIN + (PAGE_H - 2 * MARGIN - fixed - leaves * pitch) / 2

        for index, cluster in enumerate(group):
            colour = cluster["color"]
            spine_x = base + sign * STAGGER[index % len(STAGGER)]
            title_y = y + TITLE_H / 2
            count = len(cluster["terms"])

            # title on a marker blob, slightly off the horizontal
            label = f'{cluster["no"]}  {cluster["name"]}'
            rx = (hand.mm(label, 13) + 9) / 2
            bx = spine_x + sign * (rx - 4)
            tilt = rng.uniform(-1.3, 1.3)
            over.append(
                f'<g transform="rotate({tilt:.2f} {bx:.2f} {title_y:.2f})">'
                f'<path d="{blob(bx, title_y, rx, 4.7, rng, square=.45, noise=.035)}" '
                f'fill="{colour}"/>'
                + text(bx, title_y + 1.7, tk.esc(label), 13, HAND,
                       tk.ink_on(colour), "middle", "700") + "</g>")
            over.append(text(bx + sign * (rx + 2.5), title_y + 1.1,
                             tk.esc(cluster["question"]), 8.2, SOFT, MUTED,
                             anchor, style="italic"))

            # main branch: leaves the centre towards the title, arrives level
            ex = bx - sign * rx
            angle = math.atan2(title_y - cy, ex - cx)
            limit = math.radians(50)
            if sign > 0:
                angle = max(-limit, min(limit, angle))
            else:
                turn = math.pi - abs(angle)
                angle = math.copysign(math.pi - min(turn, limit), angle)
            start = (cx + (BLOB_RX - 2) * math.cos(angle),
                     cy + (BLOB_RY - 1.5) * math.sin(angle))
            line = cubic(start,
                         (start[0] + 22 * math.cos(angle),
                          start[1] + 22 * math.sin(angle)),
                         (ex - sign * 20, title_y + rng.uniform(-2, 2)),
                         (ex + sign * 1.5, title_y))
            under.append(f'<path d="{tapered(line, 5.4, 1.7, rng)}" fill="{colour}"/>')

            # spine: hangs from the title, wanders a little on its way down
            rows_top = y + TITLE_H
            last_y = rows_top + (count - .5) * pitch + .7
            steps = max(3, int((last_y - title_y) / 9))
            spine = [(spine_x + (0 if k in (0, steps) else rng.uniform(-.5, .5)),
                      title_y + 3 + (last_y - title_y - 3) * k / steps)
                     for k in range(steps + 1)]

            def spine_at(py: float) -> float:
                for (x0, y0), (x1, y1) in zip(spine, spine[1:]):
                    if y0 <= py <= y1:
                        return x0 + (x1 - x0) * (py - y0) / (y1 - y0)
                return spine[-1][0]

            under.append(f'<path d="{tapered(spine, 1.5, .55, rng)}" fill="{colour}"/>')

            for i, term in enumerate(cluster["terms"]):
                base_y = rows_top + (i + .5) * pitch       # term baseline
                line_y = base_y + .7                       # twig under the term
                indent = 4 + 6 * math.sin(math.pi * (i + .5) / count)
                xt = spine_x + sign * indent
                name = term.get("p", term["t"])
                term_w = hand.mm(name, term_pt)
                room = abs(edge - xt) - 3.2 - term_w - 2.2
                if soft.mm(term["s"], term_pt - .2) > room:
                    print("check on the sketch: gloss runs out of room:", term["t"])

                sx = spine_at(line_y - 1.4)
                end = xt + sign * (3.2 + term_w + 1)
                under.append(
                    f'<path d="M{sx:.2f},{line_y - 1.4:.2f} '
                    f'Q{sx + sign * indent * .45:.2f},{line_y + .35:.2f} '
                    f'{xt:.2f},{line_y:.2f} '
                    f'Q{(xt + end) / 2:.2f},{line_y + rng.uniform(-.4, .4):.2f} '
                    f'{end:.2f},{line_y + rng.uniform(-.15, .15):.2f}" fill="none" '
                    f'stroke="{colour}" stroke-width=".5" stroke-linecap="round"/>')
                over.append(bud(xt + sign * 1.4, base_y - 1.15, term["lv"]))
                over.append(text(xt + sign * 3.2, base_y, tk.esc(name), term_pt,
                                 HAND, NAVY, anchor, "700"))
                over.append(text(xt + sign * (3.2 + term_w + 2.2), base_y,
                                 tk.esc(term["s"]), term_pt - .2, SOFT, TEXT,
                                 anchor))
                chips = "".join(
                    f'<tspan fill="{tk.colour_of(topic, target)}">&#9632; </tspan>'
                    f'<tspan fill="{MUTED}">{tk.esc(tk.short(target))}'
                    f'&#160;&#160;&#160;</tspan>' for target in term.get("l", []))
                over.append(text(xt + sign * 3.4, base_y + pitch * .43, chips,
                                 term_pt - 2.0, SOFT, MUTED, anchor))

            # reading path: the verb to the next cluster, written in the gap
            if index < len(group) - 1:
                gap_y = y + TITLE_H + count * pitch + GAP / 2
                gx = spine_x + sign * 42
                upper, lower = cluster, group[index + 1]
                verb = (upper if sign > 0 else lower).get("next", "")
                if verb:
                    ax = gx - sign * 3
                    if sign > 0:
                        over.append(arrow(ax, gap_y - 2.4, ax, gap_y + 2.4, 1.2, rng))
                    else:
                        over.append(arrow(ax, gap_y + 2.4, ax, gap_y - 2.4, 1.2, rng))
                    over.append(text(gx, gap_y + 1, tk.esc(verb), 7.8, HAND,
                                     MUTED, anchor))
            y += TITLE_H + count * pitch + GAP

    draw_side(clusters[:cut], +1, SPINE_R)
    draw_side(list(reversed(clusters[cut:])), -1, SPINE_L)

    # the step from the right side over to the left runs below the centre
    crossing = clusters[cut - 1].get("next", "")
    if crossing:
        over.append(arrow(cx + 24, PAGE_H - 8.5, cx - 24, PAGE_H - 8.5, 2.2, rng))
        over.append(text(cx, PAGE_H - 5.2, tk.esc(crossing), 7.8, HAND, MUTED,
                         "middle"))

    centre = (f'<path d="{blob(cx, cy, BLOB_RX, BLOB_RY, rng, noise=.04)}" '
              f'fill="{NAVY}"/>'
              f'<path d="{blob(cx + .6, cy + .4, BLOB_RX + 1.6, BLOB_RY + 1.6, rng, noise=.03)}" '
              f'fill="none" stroke="{NAVY}" stroke-width=".35"/>')

    def notes(items: list[tuple[int, str]]) -> str:
        return "".join(
            f'<div class="note" style="transform:rotate({rng.uniform(-2.2, 2.2):.2f}deg);'
            f'margin-left:{rng.uniform(-2, 2):.1f}mm"><b>{number}</b> {tk.esc(body)}</div>'
            for number, body in items)

    takes = list(enumerate(topic["takeaways"], 1))
    half = (len(takes) + 1) // 2
    counts = tk.level_counts(topic)
    css = f"""
*{{box-sizing:border-box}} html,body{{margin:0;padding:0}}
@page{{size:{PAGE_W}mm {PAGE_H}mm; margin:0}}
body{{width:{PAGE_W}mm; height:{PAGE_H}mm; position:relative; overflow:hidden;
     background:{PAPER}; -webkit-print-color-adjust:exact; print-color-adjust:exact}}
svg{{position:absolute; left:0; top:0; width:{PAGE_W}mm; height:{PAGE_H}mm}}
.mid{{position:absolute; left:{cx - BLOB_RX}mm; top:{cy - BLOB_RY}mm;
     width:{2 * BLOB_RX}mm; height:{2 * BLOB_RY}mm; display:flex;
     flex-direction:column; justify-content:center; text-align:center;
     color:#fff; padding:0 5mm 1.5mm}}
.mid .tt{{font-family:{HAND}; font-weight:700; font-size:21pt; line-height:1.1;
         white-space:nowrap}}
.mid .st{{font-family:{SOFT}; font-size:8.4pt; line-height:1.2; margin-top:.6mm}}
.stack{{position:absolute; left:{cx - 25}mm; width:50mm; display:flex;
       flex-direction:column; justify-content:space-evenly}}
.note{{background:{NOTE}; border:.15mm solid #e3d58a; border-radius:.5mm;
      padding:2mm 2.4mm; font-family:{HAND}; font-size:6.9pt; line-height:1.32;
      color:{NAVY}}}
.note b{{font-size:9pt; margin-right:.8mm}}
.leg{{position:absolute; left:{cx - 25}mm; width:50mm; font-family:{SOFT};
     font-size:7.3pt; line-height:1.55; color:{TEXT}}}
.leg svg{{position:static; width:2.6mm; height:2.6mm; vertical-align:-.4mm;
         margin-right:1mm}}
.leg .stamp{{color:{MUTED}; font-size:6.6pt; margin-top:1mm}}
"""

    def key(level: str) -> str:
        return f'<svg viewBox="-1.3 -1.3 2.6 2.6">{bud(0, 0, level)}</svg>'

    top_h = cy - BLOB_RY - MARGIN - 5
    low_top = cy + BLOB_RY + 5
    return (
        '<!doctype html><html lang="de"><head><meta charset="utf-8">'
        f'<title>{tk.esc(topic["title"])}</title><style>{css}</style></head><body>'
        f'<svg viewBox="0 0 {PAGE_W} {PAGE_H}">{"".join(under)}{centre}'
        f'{"".join(over)}</svg>'
        f'<div class="mid"><div class="tt">{tk.esc(topic["title"])}</div>'
        f'<div class="st">{tk.esc(topic["subtitle"])}</div></div>'
        f'<div class="stack" style="top:{MARGIN + 2}mm; height:{top_h}mm">'
        f'{notes(takes[:half])}</div>'
        f'<div class="stack" style="top:{low_top}mm; height:{PAGE_H - low_top - 38}mm">'
        f'{notes(takes[half:])}</div>'
        f'<div class="leg" style="top:{PAGE_H - 35}mm">'
        f'{key("nutze")}nutze ich schon ({counts["nutze"]})<br>'
        f'{key("kenne")}kenne ich ({counts["kenne"]})<br>'
        f'{key("neu")}neu für mich ({counts["neu"]})<br>'
        f'<span style="color:{MUTED}">&#9632;</span> hängt zusammen mit, '
        'Farbe zeigt das Feld'
        f'<div class="stamp">Stand {tk.esc(topic["as_of"])} · '
        f'{tk.esc(topic["author"])}</div></div></body></html>')


# --------------------------------------------------------------------------
# compact sheet
# --------------------------------------------------------------------------
def compact_html(topic: dict) -> str:
    """Five columns, almost no margin, running text: the exam-sheet layout."""
    serif = '"Sitka Text", Cambria, Georgia, serif'
    sans = '"Segoe UI", Calibri, sans-serif'
    blue = "#1f4e9c"
    parts = []
    for cluster in topic["clusters"]:
        parts.append(
            f'<h2 style="border-color:{cluster["color"]}">'
            f'<span>{cluster["no"]}</span>{tk.esc(cluster["name"])}</h2>'
            f'<p class="q">{tk.esc(cluster["question"])}</p>')
        for term in cluster["terms"]:
            links = ", ".join(tk.esc(tk.short(t)) for t in term.get("l", []))
            parts.append(
                f'<div class="e"><h3><span class="lv {term["lv"]}"></span>'
                f'{tk.esc(term["t"])}</h3>'
                f'<p>{tk.esc(term["e"])} <i>Beispiel</i> {tk.esc(term["x"])}</p>'
                f'<p class="l">&rarr; {links}</p></div>')
    takes = "".join(f"<li>{tk.esc(t)}</li>" for t in topic["takeaways"])
    path = " &rarr; ".join(tk.esc(c["name"]) for c in topic["clusters"])
    css = tk.SHARED_CSS + f"""
@page{{size:A4 landscape; margin:3mm 3mm 3mm}}
body{{font-family:{serif}; font-size:6.95pt; line-height:1.15;
     columns:5; column-gap:3.2mm; column-rule:.2mm solid {tk.LINE}}}
.box{{border:.3mm solid #666; padding:1.6mm 2mm; margin:0 0 1.6mm;
     font-family:{sans}; font-size:7.6pt; break-inside:avoid}}
.box b{{font-size:9.4pt}}
h2{{font-family:{sans}; font-size:9.6pt; color:{blue}; margin:1.8mm 0 0;
   padding-left:1.4mm; border-left:1.4mm solid; break-after:avoid}}
h2 span{{margin-right:2.4mm}}
.q{{font-style:italic; color:{MUTED}; margin:.2mm 0 .8mm}}
h3{{font-family:{sans}; font-size:7.7pt; margin:.8mm 0 0; color:#000;
   break-after:avoid}}
h3 .lv{{width:1.6mm; height:1.6mm; margin-right:1mm; vertical-align:.1mm}}
p{{margin:0; text-align:left}}
.e{{break-inside:avoid}}
.e i{{color:{blue}}}
.l{{color:{blue}; font-size:6.6pt}}
ol{{margin:.6mm 0 0; padding-left:3.6mm}}
li{{margin:0 0 .5mm}}
"""
    return (
        '<!doctype html><html lang="de"><head><meta charset="utf-8">'
        f'<title>{tk.esc(topic["title"])}</title><style>{css}</style></head><body>'
        f'<div class="box"><b>{tk.esc(topic["title"])}</b><br>'
        f'Hilfszettel, Stand {tk.esc(topic["as_of"])}, {tk.esc(topic["author"])}'
        '</div>'
        f'<h2 style="border-color:{NAVY}"><span>0</span>Überblick</h2>'
        f'<p><i>Lesepfad</i> {path}.</p><ol>{takes}</ol>'
        + "".join(parts) + '</body></html>')
