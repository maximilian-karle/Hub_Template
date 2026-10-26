# Gedächtnis

Rolle in der Lernschleife ist **Tutor, Behalten**. Ein Gedächtnis für alle
Lernprojekte des Hub unter `03_projekte/`. Behalten ist eine eigene Aufgabe,
deshalb liegt es neben den Projekten und nicht in ihnen. Ein Lernprojekt mit
eigener Engine (etwa eine Sprach-App) bleibt draußen, das steht dann im
Studienplan `01_kompass/studienplan/studienplan.md`.

Im frischen Hub ist der Ordner `karten/` leer. Karten entstehen aus `/tutor`
oder von Hand mit `engine.py add`, sobald ein Modul geplant ist (`/aufnahme`,
`/advisor`). Budgets für Tag und Woche stehen unter `lernen` in
`00_kern/einstellungen.json` (`/einrichten`).

## Aufbau

| Pfad | Inhalt |
|---|---|
| `engine.py` | SM-2-Scheduler, Karten anlegen, freischalten, bewerten, Fälligkeit, Statistik |
| `heute.py` | Tagesbudget, verteilt 15 bis 30 Minuten auf Wiederholung und neue Karten |
| `wochenlage.py` | Lernlage der Woche für `/weekly-review` mit Ist-Minuten, Abrufquote, Rückstau samt Trend und nächstem Abschnitt |
| `alter.py` | nächste Tätigkeit im Lernsystem für `/alter` aus Karten, Modulplan und Verlauf (Behalten, Tutor, Editor, Lesen, Meilenstein) |
| `alter_verlauf.json` | erledigte Tätigkeiten mit Ergebnis, geschrieben von `alter.py erledigt` |
| `rueckstau.json` | Messpunkte der Wiederholungslast, geschrieben von `wochenlage.py --merken` |
| `methodik.md` | Annahmen mit Last Validated, Rechnung für die Obergrenze, Entscheidungen |
| `karten/<projekt>.json` | Karten eines Lernprojekts |
| `tests/` | Tests für Intervalle, Zustände, Fälligkeit, das Tagesbudget und die Wochenlage |

Der Scheduler ist reine Arithmetik in Python und wird nicht vom Modell
gerechnet. Er folgt SM-2 mit einer Abweichung für verspätete Abrufe (Kopf von
`engine.py`).

## Eine Karte

| Feld | Bedeutung |
|---|---|
| `id` | eindeutig über alle Projekte, ohne Angabe `<projekt>-<nnn>` |
| `projekt` | Lernprojekt, Kleinbuchstaben, Ziffern, Unterstrich |
| `abschnitt` | Abschnitt des Lesepfads, Modul-ID plus Kern-Nummer, etwa `XY2-K00` |
| `typ` | `Begriff`, `Anwendung` oder `Rechnung` |
| `frage`, `antwort` | Inhalt der Karte |
| `quelle` | Werk und Kapitel aus der Bibliothek, Pflicht |
| `gesperrt`, `freigeschaltet` | gesperrt bis zum Freischalten, Datum der Freischaltung |
| `lernzustand` | Easiness-Faktor, Wiederholungen, Intervall, letzter und nächster Abruf, Verlauf mit Zuversicht |

## Der Karteikasten

| Zustand | Bedeutung | Übergang |
|---|---|---|
| gesperrt | angelegt, Stoff noch nicht gelesen, erscheint nie | `freischalten ABSCHNITT`, sobald der Abschnitt gelesen ist |
| bereit | freigeschaltet, nie abgerufen, das ist der Vorrat | erster Kontakt im Zufluss |
| im Kasten | wandert mit jeder richtigen Antwort ein Fach nach hinten (1, 6, 15, 38 Tage und weiter), eine falsche holt sie ins erste Fach zurück | ab 21 Tagen Intervall sitzt sie |

## Tagesbudget

`heute.py` plant den Tag. Wiederholung zuerst, über alle Projekte gemischt.
Neues füllt den Rest, 70 % aus aktiven Abschnitten (in den letzten 14 Tagen
freigeschaltet) in Reihenfolge des Lesepfads, 30 % zufällig aus dem Vorrat.
Ist der Wiederholungsberg größer als 1,5 Tagesbudgets, kommt nichts Neues.
Darunter kommen immer mindestens zwei Karten aus aktiven Abschnitten. Mehr als
sechs neue Karten bei 15 Minuten (acht bei 20, zwölf bei 30) trägt der Kasten
nicht. Rechnung und Annahmen in `methodik.md`.

## Aufruf

Aus dem Hub, für den täglichen Ablauf mit `/heute`.

```bash
python 04_gedaechtnis/heute.py --minuten 20
```

Karte anlegen, ohne `--frei` ist sie gesperrt.

```bash
python 04_gedaechtnis/engine.py add --projekt statistik --abschnitt XY2-K00 --typ Begriff --frage "..." --antwort "..." --quelle "Autor, Werk, Kap. 1"
```

Abschnitt nach dem Lesen freischalten.

```bash
python 04_gedaechtnis/engine.py freischalten XY2-K00
```

Bewerten mit Zuversicht.

```bash
python 04_gedaechtnis/engine.py review statistik-001:4:70
```

`review` nimmt `ID:Qualität` oder `ID:Qualität:Zuversicht`, Qualität 0 bis 5,
ab 3 gilt die Antwort als richtig. `zeige ID ...` gibt Karten aus, `due` die
fälligen, `neu` die bereiten, `stats` je Projekt die Zustände, `zahl` die
fälligen Karten insgesamt (für den Hook).

## Vertraulichkeit

Karten aus der Arbeit kommen nur anonymisiert hierher, nach
`00_kern/vertraulichkeit.md`, die Freigabe liegt beim Nutzer.

## Tests

```bash
python3 -m pytest 04_gedaechtnis/tests -q
```
