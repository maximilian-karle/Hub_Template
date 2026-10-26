"""
dashboard_kit.py
================
Bausteine für ein in sich geschlossenes HTML-Dashboard im Layout des Hubs.
Kopf mit Theme-Start, Kopfleiste mit Logo und Theme-Schalter, Blöcke der
Seitenleiste, eingebettetes Stylesheet und Skript sowie die serverseitige
Gestaltung für plotly.py-Figuren.

In sich geschlossen ist eine Anforderung, keine Bequemlichkeit. Ein Dashboard
geht per E-Mail hinaus und wird offline geöffnet, deshalb sind Stylesheet,
Skripte, Logo und Diagrammbibliothek eingebettet und zur Laufzeit wird nichts
nachgeladen.

Aufruf aus einem Projekt

    import sys
    sys.path.insert(0, str(HUB / "07_handwerk" / "dashboard_template"))
    import dashboard_kit as dk

    html = (dk.document_head("Bestand", theme_key="bestand-theme", extra_css=MY_CSS)
            + "<body>" + dk.topbar("Bestand", "Monatlicher Bestandsbericht", pills=[...])
            + sidebar + "<main>...</main>" + dk.body_scripts(my_js) + "</body></html>")

Die Gestaltungsregeln hinter den Tokens stehen in README.md neben dieser Datei.
"""

from __future__ import annotations

import base64
import html as _html
import re
from pathlib import Path

ASSETS = Path(__file__).resolve().parent


def _farbtokens() -> dict[str, str]:
    """Farbtokens des hellen Themes aus dem :root-Block von theme.css."""
    css = (ASSETS / "theme.css").read_text(encoding="utf-8")
    root = re.search(r":root\s*\{(.*?)\}", css, re.DOTALL)
    return dict(re.findall(r"--([a-z-]+)\s*:\s*(#[0-9A-Fa-f]{6})\s*;",
                           root.group(1) if root else ""))


# Edelstein-Palette. Definiert ist sie nur in theme.css (dort ändert sie auch
# /einrichten), hier wird sie gelesen, damit Diagramme aus Python und aus dem
# Browser nicht auseinanderlaufen.
_TOKENS = _farbtokens()
PALETTE = {name: _TOKENS[name] for name in (
    "accent", "saphir", "smaragd", "citrin", "topas", "rubin", "amethyst",
    "tuerkis", "graphit", "pos", "neg")}
# schriftsichere Variante für farbige Warnzahlen auf weißer Karte
PALETTE["flag"] = _TOKENS["flag-text"]

# Reihenfolge für Kategorien ohne eigene Bedeutung. Rubin fehlt absichtlich,
# es ist der Markierung für Aufmerksamkeit in einem Diagramm vorbehalten.
CATEGORICAL = ["accent", "amethyst", "tuerkis", "topas", "smaragd", "citrin", "graphit"]

FONT_STACK = ('Inter, -apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", '
              'Roboto, "Helvetica Neue", Arial, sans-serif')


def e(text: object) -> str:
    """Maskiert beliebigen Text für HTML, None wird leer."""
    return _html.escape("" if text is None else str(text))


def theme_css() -> str:
    return (ASSETS / "theme.css").read_text(encoding="utf-8")


def theme_js() -> str:
    return (ASSETS / "theme.js").read_text(encoding="utf-8")


def logo_data_uri() -> str:
    svg = (ASSETS / "logo.svg").read_bytes()
    return "data:image/svg+xml;base64," + base64.b64encode(svg).decode("ascii")


def plotly_js() -> str:
    from plotly.offline import get_plotlyjs
    return get_plotlyjs()


def theme_boot(theme_key: str) -> str:
    """Setzt data-theme vor dem ersten Zeichnen, damit im Dunkelmodus kein
    weißer Blitz erscheint. Gehört in <head>, vor das Stylesheet."""
    return (
        "<script>(function(){var r=document.documentElement,k=r.getAttribute('data-theme-key')||'dash-theme',"
        "c='auto';try{c=localStorage.getItem(k)||'auto';}catch(e){}"
        "var d=c==='dark'||(c==='auto'&&window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches);"
        "r.setAttribute('data-theme',d?'dark':'light');})();</script>"
    )


def document_head(title: str, *, theme_key: str, lang: str = "de", extra_css: str = "",
                  plotly_in_head: bool = False) -> str:
    """<!DOCTYPE> bis </head> mit den Tokens, danach dem CSS des Projekts
    (das damit überschreiben darf) und dem Startskript für das Theme.
    `plotly_in_head` ist nötig, wenn plotly.py-Figuren im Body eingebettet
    sind, denn deren Inline-Skripte laufen schon beim Parsen der Seite."""
    plotly = f"<script>{plotly_js()}</script>\n" if plotly_in_head else ""
    return (
        f"<!DOCTYPE html>\n<html lang='{e(lang)}' data-theme-key='{e(theme_key)}'>\n<head>\n"
        "<meta charset='utf-8'>\n<meta name='viewport' content='width=device-width, initial-scale=1'>\n"
        f"<title>{e(title)}</title>\n{theme_boot(theme_key)}\n"
        f"<style>{theme_css()}\n{extra_css}</style>\n{plotly}</head>\n"
    )


def theme_switch() -> str:
    return (
        "<div class='tile-group' role='group' aria-label='Farbschema'>"
        "<button class='tile' data-theme-choice='auto'>Auto</button>"
        "<button class='tile' data-theme-choice='light'>Hell</button>"
        "<button class='tile' data-theme-choice='dark'>Dunkel</button></div>"
    )


def topbar(title: str, subtitle: str = "", *, status: str = "", pills: list[str] | None = None,
           logo: bool = True, logo_alt: str = "Logo") -> str:
    """Kopfleiste. `status` ist die Laufzeile mit grünem Punkt (etwa
    "Lauf TT.MM.JJJJ"), `pills` sind fertige HTML-Stücke oder schlichte Texte,
    die als Pille erscheinen."""
    brand_logo = f"<img src='{logo_data_uri()}' alt='{e(logo_alt)}'>" if logo else ""
    sub = f"<span>{e(subtitle)}</span>" if subtitle else ""
    pill_html = "".join(p if p.lstrip().startswith("<") else f"<span class='pill'>{e(p)}</span>"
                        for p in (pills or []))
    status_html = f"<span class='status-dot'>{e(status)}</span>" if status else ""
    return (
        "<header class='topbar'>"
        f"<div class='topbar-brand'>{brand_logo}<div class='topbar-title'>{e(title)}{sub}</div></div>"
        f"<div class='topbar-status'>{pill_html}{status_html}{theme_switch()}</div>"
        "</header>"
    )


def sidebar_label(text: str) -> str:
    return f"<div class='sidebar-section-label'>{e(text)}</div>"


def sidebar_info(rows: list[tuple[str, str]]) -> str:
    """Zeilen aus Bezeichnung und Wert unter einem Abschnitt der Seitenleiste."""
    inner = "".join(f"<div class='sidebar-info-row'><span>{e(k)}</span><b>{e(v)}</b></div>" for k, v in rows)
    return f"<div class='sidebar-info'>{inner}</div>"


def footer(text: str) -> str:
    return f"<footer class='page-footer'>{e(text)}</footer>"


def body_scripts(product_js: str = "", *, include_plotly: bool = True) -> str:
    """Plotly, das Theme-Skript und das Skript des Produkts, in dieser
    Reihenfolge. Gehört ans Ende von <body>. include_plotly=False, wenn
    document_head Plotly schon trägt (plotly_in_head=True)."""
    plotly = f"<script>{plotly_js()}</script>" if include_plotly else ""
    return f"{plotly}<script>{theme_js()}</script>" + (f"<script>{product_js}</script>" if product_js else "")


def style_figure(fig):
    """Serverseitiges Gegenstück zu Dash.layout für plotly.py-Figuren, mit
    transparenten Flächen, ohne Gitternetz, Titel linksbündig. Die Farben
    sind die des hellen Themes, theme.js färbt die Figur im Browser für den
    Dunkelmodus um."""
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family=FONT_STACK, size=12, color="#1A1B1E"),
        title=dict(x=0, xanchor="left", font=dict(size=14)),
        margin=dict(t=48, b=40, l=60, r=20),
        legend=dict(font=dict(size=11)),
        hoverlabel=dict(bgcolor="#FFFFFF", bordercolor="#DEE2E6", font=dict(color="#1A1B1E", size=12)),
    )
    axis = dict(showgrid=False, zeroline=False, linecolor="#DEE2E6", tickcolor="#DEE2E6", color="#868E96")
    fig.update_xaxes(**axis)
    fig.update_yaxes(**axis)
    return fig


if __name__ == "__main__":
    # Legt die Diagrammbibliothek neben template.html, damit die Referenzseite
    # ihre Beispieldiagramme offline zeigt. Die Kopie ist nicht versioniert
    # (.gitignore).
    target = ASSETS / "plotly.min.js"
    target.write_text(plotly_js(), encoding="utf-8")
    print(f"Geschrieben: {target}")
