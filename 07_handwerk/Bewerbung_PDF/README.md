# Bewerbung als PDF

Lebenslauf und Anschreiben entstehen aus einem Python-Inhaltsmodul über
HTML und einen Chromium-Browser (Edge oder Chrome) im Headless-Modus. Kein
LaTeX und kein Word nötig, die Seitenzahl wird beim Bauen geprüft.

| Datei | Zweck |
|---|---|
| `render.py` | baut Lebenslauf und Anschreiben aus einem Inhaltsmodul, prüft Seitenzahl, Gedankenstriche und mit `--final` offene Platzhalter |
| `cv_inhalt_vorlage.py` | leerer Aufbau eines Inhaltsmoduls, aus dem `/einrichten` die eigene Basis `Profil/cv_inhalt_basis.py` macht |
| `mappe.py` | baut die Anlagen (Zeugnisse, Zertifikate) nach `Profil/mappe.json` |
| `muster/` | erfundene Person im Stil der Vorlage, Inhaltsmodul und fertige PDFs zum Ansehen |

Gestaltung. Zentrierter Namenskopf mit rundem Foto, Abschnittstitel in
Versalien mit feiner Linie, Datumsspalte links, schwarz-weiß mit einer
Akzentfarbe. Die eigenen Vorlieben stehen in
`05_werkstatt/karriere/Profil/stil.json`.

| Schlüssel | Werte | Standard |
|---|---|---|
| `schrift` | `auto`, `helvetica`, `arial`, `georgia`, `garamond`, `franklin`, `gill`, `century` | `auto` (Franklin Gothic, wo installiert, sonst Helvetica Neue) |
| `akzentfarbe` | Hexwert | `#e5483f` |
| `foto` | `true`, `false` | `true` |
| `seiten_lebenslauf` | Zahl | `1` |
| `seiten_anschreiben` | Zahl | `1` |
| `gedankenstriche_verbieten` | `true`, `false` | `true` |

Foto und Unterschrift werden eingebunden, wenn
`Profil/Bewerbungsfoto.jpg` und `Profil/Unterschrift.png` existieren.

```bash
python3 07_handwerk/Bewerbung_PDF/render.py 05_werkstatt/karriere/Profil/cv_inhalt_basis.py 05_werkstatt/karriere/Bewerbungen/_Basis
```

Voraussetzung ist `pip install pypdf` (für `mappe.py` zusätzlich `pillow`) und
Microsoft Edge oder Google Chrome.
