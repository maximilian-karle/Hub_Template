"""Shared base of the learning poster: topic file, palette, PDF rendering.

One JSON file per topic is the single source: clusters, their terms, a one-line
gloss, a full explanation, an example and the related terms. The renderers in
poster_variants.py read it through load(), so the sheet and the poster cannot
drift apart. Entry point is build_poster.py.

Rendering runs through a headless Chromium, as the house-style PDFs do, so
text is laid out by a real layout engine with the installed fonts.
"""

from __future__ import annotations

import html
import json
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

# House palette, measured from the company role description.
NAVY = "#14304f"
LINE = "#c3ccd6"
TEXT = "#1a1a1a"
MUTED = "#5a6673"

LEVELS = {"nutze": "nutze ich", "kenne": "kenne ich", "neu": "neu"}

PAGE_W, PAGE_H = 420.0, 297.0   # A3 landscape, millimetres

# Lengths beyond which a leaf no longer fits its poster row at the usual
# density. Checked at build time, since a cut-off line on a poster is a
# defect that the build log would otherwise not show.
MAX_TERM = 31
MAX_GLOSS = 66


def esc(value: object) -> str:
    return html.escape(str(value))


def short(term: str) -> str:
    """The term without its bracketed expansion, for the tight link line."""
    return term.split(" (")[0]


def ink_on(colour: str) -> str:
    """Navy on a light cluster colour, white on a dark one."""
    r, g, b = (int(colour[i:i + 2], 16) for i in (1, 3, 5))
    return NAVY if (0.299 * r + 0.587 * g + 0.114 * b) > 150 else "#ffffff"


def load(path: Path) -> dict:
    topic = json.loads(path.read_text(encoding="utf-8"))
    home: dict[str, int] = {}
    for number, cluster in enumerate(topic["clusters"], 1):
        cluster["no"] = number
        for term in cluster["terms"]:
            if term["t"] in home:
                sys.exit(f"Term defined twice: {term['t']}")
            home[term["t"]] = number
    topic["home"] = home

    problems, hints = [], []
    for cluster in topic["clusters"]:
        for term in cluster["terms"]:
            for target in term.get("l", []):
                if target not in home:
                    problems.append(f"{term['t']} -> {target}")
            if term.get("lv") not in LEVELS:
                problems.append(f"{term['t']}: level {term.get('lv')!r}")
            label = term.get("p", term["t"])
            if len(label) > MAX_TERM:
                hints.append(f"term label long ({len(label)}): {label}")
            if len(term["s"]) > MAX_GLOSS:
                hints.append(f"gloss long ({len(term['s'])}): {term['t']}")
    if problems:
        sys.exit("Unknown link target or level:\n  " + "\n  ".join(problems))
    for hint in hints:
        print("check on the poster:", hint)
    return topic


def colour_of(topic: dict, term: str) -> str:
    return topic["clusters"][topic["home"][term] - 1]["color"]


def level_counts(topic: dict) -> dict[str, int]:
    counts = dict.fromkeys(LEVELS, 0)
    for cluster in topic["clusters"]:
        for term in cluster["terms"]:
            counts[term["lv"]] += 1
    return counts


def split_sides(clusters: list[dict]) -> int:
    """Index that splits the clusters into two sides of similar leaf count."""
    total = sum(len(c["terms"]) for c in clusters)
    best, best_gap, running = 1, None, 0
    for index, cluster in enumerate(clusters[:-1], 1):
        running += len(cluster["terms"])
        gap = abs(total - 2 * running)
        if best_gap is None or gap < best_gap:
            best, best_gap = index, gap
    return best


# The level marker as a CSS shape, shared by sheet and poster legend.
SHARED_CSS = f"""
*{{box-sizing:border-box}}
html,body{{margin:0; padding:0}}
body{{color:{TEXT}; background:#fff;
     -webkit-print-color-adjust:exact; print-color-adjust:exact}}
.lv{{display:inline-block; flex:0 0 auto; width:1.9mm; height:1.9mm;
    border-radius:50%; border:.3mm solid {NAVY}; background:#fff}}
.lv.nutze{{background:{NAVY}}}
.lv.kenne{{background:linear-gradient(90deg,{NAVY} 50%,#fff 50%)}}
"""

_BROWSERS = [
    Path(r"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"),
    Path(r"C:/Program Files/Microsoft/Edge/Application/msedge.exe"),
    Path(r"C:/Program Files/Google/Chrome/Application/chrome.exe"),
    Path("/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"),
    Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),
    Path("/usr/bin/microsoft-edge"),
    Path("/usr/bin/google-chrome"),
    Path("/usr/bin/chromium"),
]


def to_pdf(markup: str, pdf_path: Path, patience: int = 120) -> None:
    """Render HTML to PDF.

    The browser writes the PDF reliably but does not always exit afterwards,
    so the wait is on the file: once its size has been stable for two seconds
    it is complete and the process is killed.
    """
    exe = next((p for p in _BROWSERS if p.exists()), None)
    if exe is None:
        sys.exit("No Chromium found:\n  " + "\n  ".join(map(str, _BROWSERS)))
    if pdf_path.exists():
        pdf_path.unlink()
    work = Path(tempfile.mkdtemp(prefix="learning-poster-"))
    page = work / "page.html"
    page.write_text(markup, encoding="utf-8")
    proc = subprocess.Popen(
        [str(exe), "--headless", "--disable-gpu", "--no-first-run",
         f"--user-data-dir={work / 'profile'}", "--no-pdf-header-footer",
         f"--print-to-pdf={pdf_path.resolve()}", page.resolve().as_uri()],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    last, stable = -1, 0
    for _ in range(patience * 2):
        if pdf_path.exists():
            size = pdf_path.stat().st_size
            stable = stable + 1 if size > 0 and size == last else 0
            last = size
            if stable >= 4 or proc.poll() is not None:
                break
        time.sleep(0.5)
    if proc.poll() is None:
        proc.kill()
        try:
            proc.wait(timeout=30)
        except subprocess.TimeoutExpired:
            pass
    shutil.rmtree(work, ignore_errors=True)
    if not pdf_path.exists() or pdf_path.stat().st_size == 0:
        sys.exit(f"PDF was not produced: {pdf_path}")


def preview(pdf_path: Path, out_dir: Path, dpi: int) -> None:
    """Page images for the visual check; overlaps do not show in a build log."""
    import pymupdf

    out_dir.mkdir(parents=True, exist_ok=True)
    with pymupdf.open(pdf_path) as doc:
        for number, page in enumerate(doc, 1):
            target = out_dir / f"{pdf_path.stem}_{number}.png"
            page.get_pixmap(dpi=dpi).save(target)
            print("preview:", target)
