"""Builds the learning material of a topic file. This is the entry point.

  <slug>_Kompakt.pdf            five-column sheet with every term (A4)
  <slug>_Poster_A3_Skizze.pdf   the mind map, drawn as if by hand (A3)

Usage:
    python build_poster.py <topic.json> [--preview <dir>]
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import poster_toolkit as tk  # noqa: E402
import poster_variants as pv  # noqa: E402


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    source = Path(sys.argv[1]).resolve()
    topic = tk.load(source)
    slug = topic["slug"]
    jobs = [(pv.compact_html, f"{slug}_Kompakt.pdf", 120),
            (pv.sketch_html, f"{slug}_Poster_A3_Skizze.pdf", 150)]
    for build, name, dpi in jobs:
        target = source.parent / name
        try:
            tk.to_pdf(build(topic), target)
        except PermissionError:
            # A PDF open in a viewer is locked on Windows. The other file is
            # still worth building.
            print("NOT rebuilt, close it in the viewer first:", target)
            continue
        print("written:", target)
        if "--preview" in sys.argv:
            tk.preview(target, Path(sys.argv[sys.argv.index("--preview") + 1]), dpi)


if __name__ == "__main__":
    main()
