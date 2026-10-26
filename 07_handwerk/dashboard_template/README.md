# Dashboard-Bausatz

Layout und Gestaltungssprache jedes HTML-Dashboards im Hub und in den Ästen.
Ein neues oder bestehendes Dashboard nutzt den Bausatz, statt Teile aus einem
anderen Projekt zu kopieren.

| Datei | Zweck |
|---|---|
| `theme.css` | Farbtokens (einzige Definition der Edelstein-Palette), Radien, Schrift, Rahmen aus Kopfleiste, Seitenleiste und Seite, gemeinsame Bausteine |
| `theme.js` | Theme-Schalter Auto, Hell, Dunkel, Plotly-Grundlayout aus den Tokens, Umfärben der Diagramme beim Wechsel des Themes |
| `dashboard_kit.py` | Python-Bausteine für Kopf, Kopfleiste, Seitenleiste, Fuß, eingebettete Skripte und `style_figure()` für plotly.py |
| `logo.svg` | Neutraler Platzhalter für die Kopfleiste (als Data-URI eingebettet), durch ein eigenes Logo unter demselben Namen ersetzbar |
| `template.html` | Referenzseite mit allen Bausteinen, direkt im Browser öffnen |

`template.html` braucht Plotly für seine Beispieldiagramme. Einmal
`python3 dashboard_kit.py` ausführen, das schreibt eine lokale
`plotly.min.js` daneben (nicht versioniert). Ohne sie greift die Seite auf das
CDN zurück, ohne Netz zeigt sie die Seite ohne Diagramme.

## Einsatz in einem Projekt

```python
sys.path.insert(0, str(HUB / "07_handwerk" / "dashboard_template"))
import dashboard_kit as dk

html = (
    dk.document_head("Bestand", theme_key="bestand-theme", extra_css=PROJECT_CSS)
    + "<body>"
    + dk.topbar("Bestand", "Monatlicher Bestandsbericht", status="Lauf TT.MM.JJJJ", pills=["Stand MM/JJJJ"])
    + sidebar_html + "<main>" + pages_html + "</main>"
    + dk.footer("...")
    + dk.body_scripts(PROJECT_JS)
    + "</body></html>"
)
```

- **Projekt-CSS ergänzt nur**, es definiert keine Tokens neu. Sonderbausteine
  (eine Matrix, eine Brücke, eine Ampelzelle) leben im Projekt und nutzen
  `var(--...)`.
- **Diagramme im Browser** mit `Dash.plot(el, data, layout)` statt
  `Plotly.newPlot`, Farben über `Dash.css('--rubin')`.
- **Diagramme aus plotly.py** mit `dk.style_figure(fig)`. `theme.js` färbt
  sie für den Dunkelmodus um.
- **Eine Spur in Textfarbe** (etwa „Ist“ als schwarze Linie) bekommt
  `meta: 'ink'`, damit sie im Dunkelmodus hell wird, statt zu verschwinden.
- `theme_key` ist der Speicherschlüssel der Theme-Wahl im Browser, einer je
  Produkt.

## Gestaltungsregeln

**Aufbau (Pyramid Principle auf dem Bildschirm)**
- Kopfleiste mit Logo, Produktname und Untertitel in gedämpftem Grau, rechts
  Laufstatus, Datenstatus als Pille und Theme-Schalter.
- Seitenleiste mit *Navigation*, *Daten* (Stichtag, Vergleich, Anzahlen) und
  *Quellen* (Eingangsdateien mit Datum).
- Eine Seite beginnt mit Titel, einer Untertitelzeile und, wo es eine
  Schlussfolgerung gibt, der **Aussage**-Karte mit dem Ergebnis in einem Satz
  samt seiner Zahl.
- Danach Kennzahlkacheln (4 oder 5 je Zeile), dann Abschnittsüberschriften
  `h3.sec` über Kartengruppen, Listen zuletzt.
- Jede Kennzahlkachel führt eine Ebene tiefer (Link oder Klick), wo es eine
  tiefere Ebene gibt.

**Flächen**
- Weiße Karten (`--card-bg`) mit Haarlinie auf hellgrauer Seite. Keine
  farbigen Hinweisflächen, der einzige Akzent auf einer Fläche ist der 3 px
  breite linke Rand der Aussage.
- Volle Seitenbreite, kein `max-width` am Inhalt.
- Kopfleiste und Seitenleiste sind durchscheinend (Unschärfe). Bei
  reduzierter Transparenz fallen sie auf die Kartenfarbe zurück.

**Farbe**
- Edelstein-Palette für Kategorien und Markierungen, Akzent `#007AFF`,
  Saphir `#0000FF`, Smaragd `#00EF91`, Citrin `#FFD500`, Topas `#FF9500`,
  Rubin `#E0115F`, Amethyst `#9D00FF`, Türkis `#00D4E0`, Graphit `#94A3B8`.
  Definiert sind die Werte nur in `theme.css`. `dashboard_kit.py` und
  `07_handwerk/deck_toolkit.py` lesen sie dort, `/einrichten` bestätigt oder
  ersetzt sie. Keine gedämpften oder pastelligen Standardpaletten (Tableau
  und ähnliche).
- Rubin heißt Aufmerksamkeit (Risiko, Verstoß, Anstieg von etwas
  Schlechtem). Nicht als gewöhnliche Kategoriefarbe nutzen.
- Farbige **Zahlen** nutzen `--pos`, `--neg` und `--flag-text`, nie einen
  reinen Edelstein, denn Smaragd oder Citrin als Schrift auf Weiß ist
  unlesbar.
- Der Dunkelmodus ist eine volle Palette (`[data-theme='dark']`), keine
  Umkehrung.

**Diagramme**
- Transparenter Hintergrund, kein Gitternetz, gedämpfte Achslinien, Titel
  linksbündig.
- Legende waagerecht unter dem Diagramm.
- Ein Diagramm beantwortet eine Frage, der Untertitel der Karte sagt, wie es
  zu lesen ist.
- Animationen dort, wo sie etwas hervorheben (Ausreißer, Warnungen,
  Übergänge), mit Rücksicht auf `prefers-reduced-motion`.

**Text**
- Die Sprache folgt dem Repo (Hub Deutsch, Ast laut Einstellungen), deutscher
  Text mit echten Umlauten.
- Keine Emojis. Status über Text, Farbe und schlichte Zeichen (▲ ▼ → Σ Δ).
- Keine Gedankenstriche (Halbgeviert- und Geviertstrich) im sichtbaren Text. Stattdessen ein Mittelpunkt
  ·, ein Pfeil oder ein neuer Satz. Bindestriche in Komposita (Ramp-up)
  bleiben.
- Zahlen in Tabellenziffern (`.num`), Einheiten klein neben dem Wert
  (`<small>Mio. EUR</small>`).

**Auslieferung**
- Eine in sich geschlossene HTML-Datei mit eingebettetem CSS, Skripten, Logo
  und Plotly, ohne Netzzugriff zur Laufzeit. Die Datei geht per E-Mail hinaus
  und wird offline geöffnet.
- Abweichungen über 15 % gegen die Vorperiode werden auf der Kachel markiert
  (`.kpi-delta-flag`), nach der Qualitätsregel in `00_kern/regeln.md`.

Stilreferenz hinter diesen Regeln ist financial-dashboard-example.plotly.app
(weiße Karten, linksbündig, kein Gitternetz, volle Breite).
