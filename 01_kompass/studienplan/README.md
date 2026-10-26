# Curriculum und Modulhandbuch als PDF

`build_curriculum.py` baut aus einer Datendatei zwei PDFs im Stil eines
Hochschul-Studienplans.

- **Curriculum**, zwei Seiten A4 hoch. Seite 1 zeigt den Trimesterplan mit
  Modulkacheln je Bereichsspalte, Klammern mit Stunden und der
  Stundenverteilung je Bereich. Seite 2 zeigt die Profilentwicklung, je
  Trimester und Spalte den Nachweis mit seiner Stufe.
- **Modulhandbuch**, je Modul eine Seite mit Kennzahlen, Ausgangslage,
  Lernzielen, Inhalten, Anwendung, Prüfungsform, Literatur und Meilensteinen,
  dazu auf Wunsch ein Lesebegleiter mit den Abschnitten des Kern-Lesepfads.

Der Code enthält keine Inhalte. Alles steht in `curriculum.json`, Breiten und
Höhen rechnet der Builder aus der Zahl der Spalten und Trimester.

## Aufruf

```
python3 build_curriculum.py                      # Daten aus curriculum.json
python3 build_curriculum.py --daten meine.json   # andere Datendatei
python3 build_curriculum.py --beispiel           # Ausgabe unter den Beispielnamen
python3 build_curriculum.py --curriculum X.pdf --modulhandbuch Y.pdf
python3 build_curriculum.py --html               # HTML neben dem PDF behalten
```

Die Ausgabepfade gelten relativ zum Ordner der Datendatei. Vorrang hat das
Argument, danach `--beispiel` oder `"beispiel": true` in den Daten, danach
das Feld `ausgabe`, danach der Standard.

| Fall | Curriculum | Modulhandbuch |
|---|---|---|
| Standard | `Curriculum.pdf` | `../module/Modulhandbuch.pdf` |
| Beispiel | `Beispiel_Curriculum.pdf` | `../module/_beispiele/Beispiel_Modulhandbuch.pdf` |

## Voraussetzung

- Python 3.9 oder neuer, keine Zusatzpakete. Ist `pypdf` installiert, meldet
  der Builder zusätzlich die Seitenzahl.
- Ein Chromium-Browser zum Drucken. Der Builder sucht Edge und Chrome an den
  üblichen Orten unter Windows (`C:\Program Files (x86)\Microsoft\Edge\...`,
  `C:\Program Files\Google\Chrome\...`) und unter macOS
  (`/Applications/Google Chrome.app`, `/Applications/Microsoft Edge.app`),
  danach im `PATH`. Ein anderer Ort geht über die Umgebungsvariable
  `CURRICULUM_BROWSER` mit dem vollen Pfad zur ausführbaren Datei.
- Das PDF darf beim Bauen nicht in einem Viewer geöffnet sein, sonst bricht
  der Builder mit einem Hinweis ab.

## Von Beispiel auf eigene Daten wechseln

1. `curriculum.json` öffnen (oder vorher als `curriculum_beispiel.json`
   sichern, um das Muster zu behalten).
2. `"beispiel": true` löschen oder auf `false` setzen. Dann schreibt der
   Builder `Curriculum.pdf` und `../module/Modulhandbuch.pdf`.
3. `bereiche` an `profil.bereiche` in `00_kern/einstellungen.json` angleichen
   (gleiche Kürzel und Namen). Fehlt `bereiche` in der Datendatei, nimmt der
   Builder sie direkt aus den Einstellungen. Weichen beide ab, meldet er einen
   Hinweis.
4. Trimester, Module, Klammern, Profil und Handbuch durch die eigenen
   ersetzen, Felder nach dem Schema unten. `person` darf leer bleiben, dann
   gilt der Name aus den Einstellungen.
5. `python3 build_curriculum.py` ausführen und jede Seite ansehen. Passt ein
   Name nicht in seine Kachel, hilft eine Trennstelle `|` oder ein fester
   Umbruch `\n` im Namen.

## Schema der Datendatei

Schlüssel mit führendem Unterstrich (etwa `_hinweis`) ignoriert der Builder.
In allen Texten setzt `|` eine mögliche Trennstelle und `\n` einen festen
Umbruch. In `tag` und `untertitel` werden `{person}`, `{stand}` und
`{zeitraum}` ersetzt.

### Kopf und Steuerung

| Feld | Pflicht | Inhalt |
|---|---|---|
| `titel` | ja | eine oder zwei Zeilen für den großen Kopf, Liste |
| `zeitraum` | nein | Text wie `2027 bis 2028`, für `tag` |
| `stand` | nein | Stand der Planung, etwa `01/2027` |
| `person` | nein | Name für die Kopfzeile, leer heißt aus den Einstellungen |
| `tag` | nein | Text im hellblauen Feld, Standard `Curriculum {zeitraum}` |
| `untertitel` | nein | zwei Zeilen unter dem Kopf, Liste |
| `wort_trimester` | nein | Wort unter der Nummer im Pfeil, Standard `Trimester` |
| `farben` | nein | `navy` (Standard, Stil der Vorlage) oder `edelstein` |
| `regeln.modul_je_spalte` | nein | `true` prüft, dass ab Trimester 2 jede Spalte ein Modul hat |
| `beispiel` | nein | `true` schreibt unter den Beispielnamen |
| `ausgabe.curriculum`, `ausgabe.modulhandbuch` | nein | eigene Zielpfade |

### Bereiche, Spalten, Sprachen

| Feld | Pflicht | Inhalt |
|---|---|---|
| `bereiche[]` | ja, sonst aus den Einstellungen | `kuerzel` (zwei Großbuchstaben), `name`, `farbe` (optional, Hex) |
| `spalten[]` | nein | `kopf`, `unterzeile`, `bereiche` (Liste von Kürzeln). Fehlt das Feld, wird jeder Bereich eine Spalte |
| `sprachen` | nein | schmale Spalte rechts mit `kopf`, `unterzeile` und `bereiche[]` (`kuerzel`, `name`, `farbe`) |

Gedacht sind drei bis fünf Spalten. Mehrere Bereiche können eine Spalte
teilen, etwa Operations und Business. Ohne eigene Farbe nimmt jeder Bereich
die nächste Farbe der gewählten Palette. Auf hellen Farben wird die Schrift
automatisch dunkel.

### Trimester

| Feld | Pflicht | Inhalt |
|---|---|---|
| `trimester[]` | ja, 2 bis 10 | je Trimester ein Eintrag |
| `.nr` | ja | Nummer als Text oder Zahl |
| `.zeit` | ja | Zeitraum, etwa `02/27 bis 04/27` |
| `.hoehe` | nein | Zeilenhöhe in mm, sonst teilt der Builder den Platz auf |
| `.module[]` | ja | `kuerzel`, `name`, `stunden`. Die Spalte folgt aus dem Bereichskürzel am Anfang des Modulkürzels, abweichend über `bereich` |
| `.module[].offen` | nein | `true` zeichnet eine gestrichelte Platzhalterkachel, dann `bereich` setzen |
| `.abschluss` | nein | Abschlussarbeit über alle Bereichsspalten mit `kuerzel` (Standard `AA1`), `name`, `text`, `stunden`, `farbe`. Daneben sind nur Sprachen erlaubt |

Mehrere Module einer Spalte im selben Trimester teilen sich die Höhe.

### Klammern

| Feld | Pflicht | Inhalt |
|---|---|---|
| `klammern[]` | ja | Gruppen mit gestricheltem Rahmen und senkrechtem Label `jahr` |
| `.klammern[]` | ja | `trimester` (Liste der Nummern), `icon`, `titel`, `text` |

Jedes Trimester steht in genau einer Klammer, in der Reihenfolge des Plans.
Symbole sind `flag`, `key`, `gear`, `cap`, `book` und `chart`. Rechts neben
jeder Klammer steht die Summe ihrer Stunden.

`verteilung_notiz` ist die Fußzeile unter der Stundenverteilung.

### Profil (Seite 2, optional)

| Feld | Pflicht | Inhalt |
|---|---|---|
| `profil.titel` | ja | eine oder zwei Zeilen |
| `profil.tag`, `profil.untertitel` | nein | wie oben, Standard `Profilentwicklung {zeitraum}` |
| `profil.stufen[]` | nein | zwei bis vier Stufen mit `name` und `text`, Standard sind Grundlagen, angewandt, belegt, trägt |
| `profil.zeilen[]` | ja | `nr`, `zeit` und entweder `zellen` oder `ausblick` |
| `.zellen[]` | | genau eine je Spalte, `null` für leer, sonst `stufe` (0 bis 3), `text`, `module` |
| `.ausblick` | | Kachel über alle Spalten mit `titel`, `text`, `farbe` (optional) |
| `profil.klammern[]` | ja | wie oben, aber `zeilen` statt `trimester`, dazu `gross` und `klein` für die Angabe rechts |
| `profil.notiz` | nein | Fußzeile unter der Stufenlegende |

Eine Zeile `nr` ohne Ziffern (etwa `heute`) erscheint im Pfeil ohne das Wort
Trimester.

### Handbuch

| Feld | Pflicht | Inhalt |
|---|---|---|
| `handbuch[]` | nein | je Modul eine Seite, die Farbe kommt aus dem Bereich des Moduls |
| `.kuerzel`, `.name` | ja | Modulkürzel und Name. Der Kopf teilt den Namen am ersten „und“, abweichend über `titel` (Liste mit zwei Zeilen) |
| `.bereich` | ja | Kompetenzfeld als Text |
| `.durchlauf` | ja | `kurz` (etwa `T1`) und `text` |
| `.stunden`, `.aufteilung` | ja | Stunden und ihre Aufteilung als Text |
| `.pruefung` | nein | `kurz` (Standard `ohne System`) und `text` |
| `.ausgangslage` | ja | Absatz |
| `.koennen[]`, `.inhalte[]`, `.pruefungsform[]`, `.literatur[]` | ja | Listen von Sätzen |
| `.anwendung[]` | ja | `spur` und `text` |
| `.meilensteine[]` | nein | `titel` und `datum` |
| `.lesebegleiter[]` | nein | Gruppen mit `titel`, `spaeter` (optional, zählt nicht zur Lesezeit) und `schritte[]` |
| `.schritte[]` | | `bis`, `titel`, `id`, `spur`, `minuten`, `lesen[]` |
| `.lesen[]` | | `werk` (Autor, Titel), `stelle`, `seiten`, `luecke: true` für ein fehlendes Werk |

Die Werke im Kopf des Lesebegleiters zählt der Builder aus `lesen`, als Werk
gilt ein Eintrag mit Komma zwischen Autor und Titel.

## Prüfungen

Vor dem Druck prüft der Builder den sichtbaren Text auf Gedankenstriche und
auf einen Bindestrich als Pause. Er bricht außerdem ab, wenn ein Modul zu
keinem Bereich passt, ein Kürzel doppelt vorkommt, eine Klammer ein
Trimester auslässt, eine Profilzeile nicht eine Zelle je Spalte hat oder die
Zeilen nicht auf die Seite passen. Überlaufende Texte in Kacheln erkennt er
nicht, deshalb jede Seite nach dem Bauen ansehen.
