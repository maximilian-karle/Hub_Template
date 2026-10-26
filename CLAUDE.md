# Hub

<!-- ERSTEINRICHTUNG: Dieser Abschnitt wird am Ende von /einrichten entfernt. -->
## Ersteinrichtung

Dieser Hub ist noch nicht eingerichtet, solange in `00_kern/einstellungen.json`
`"eingerichtet": false` steht. Dann begrüßt Claude in jeder Sitzung die Person
in einem Satz, erklärt, dass der Hub erst eingerichtet werden will, und
bietet `/einrichten` an (Stand mit `python3 00_kern/einrichten.py status`).
Fragen beantwortet Claude trotzdem, legt aber keine Projekte, Module oder
Äste an, bevor die Einrichtung durch ist.
<!-- /ERSTEINRICHTUNG -->

Persönlicher Hub. Lädt in jeder Sitzung im Hub, auch wenn Claude in einem
Projektordner startet. Deshalb steht hier nur, was überall im Hub gilt.
Alles Projektbezogene steht in der `CLAUDE.md` des Projekts. Die Regeln für
alle Repos stehen in `00_kern/regeln.md` und `00_kern/persoenlich.md` und
laden über `~/.claude/CLAUDE.md` (Installskript `00_kern/installieren.py`).
Persönliche Parameter liegen in `00_kern/einstellungen.json`. Fragt die
Person, wie der Hub funktioniert oder wie sie damit lernt, ist `HANDBUCH.md`
die Grundlage der Antwort.

## 1. Wer ich bin und was ich will

<Wird in /einrichten, Schritt 2, gefüllt. Rolle, Ziel in ein bis zwei
Jahren, langfristiges Ziel, was der Hub leisten soll.>

Daraus folgt für jede Arbeit, dass ein abgeschlossenes Vorhaben eine Case
Study hinterlässt (Situation, Task, Approach, Result, quantifiziert) in
`05_werkstatt/case_studies/`.

## 2. Die Lernschleife

`01_kompass → 02_bibliothek → 03_projekte (und Äste) → 04_gedaechtnis → 05_werkstatt → 06_wissen → 01_kompass`

Der Kompass setzt Ziel und Budget, die Bibliothek liefert die Quellen, in
Projekten und Ästen wird angewendet, das Gedächtnis sorgt fürs Behalten, die
Werkstatt macht Ergebnisse vorzeigbar, und was sich bewährt, wird Wissen
und fließt in den nächsten Plan zurück. Budget steht in
`00_kern/einstellungen.json` unter `lernen`. Die Grundsätze für Lernprojekte
stehen in `01_kompass/lerngrundsaetze.md`, das Lernsystem ALTER in
`06_wissen/frameworks/ALTER_Lebenslanges_Lernen.md`.

## 3. Ordner

| Ordner | Rolle | Inhalt |
|---|---|---|
| `00_kern/` | Regeln | Kern-Regeln, persönliche Vorlieben, Einstellungen, Vertraulichkeit, Installskript, Skills und Agenten für `~/.claude` |
| `01_kompass/` | Advisor | Profil und Ziele, Studienplan, Module als Kompetenzfelder, Aufnahmen |
| `02_bibliothek/` | Librarian | Werke in Themenordnern, `Literatur_Index.md` |
| `03_projekte/` | Anwenden | Lernprojekte und Anliegen (Abschnitt 4) |
| `04_gedaechtnis/` | Tutor | Wiederholungs-Engine (SM-2), Karten, `/heute` |
| `05_werkstatt/` | Editor | Case Studies, Karriere |
| `06_wissen/` | Roommate | eigene Frameworks mit Register, Verbindungen zwischen Fächern |
| `07_handwerk/` | Werkzeug | Projekt-Scaffold, Definition of Done, Präsentationsstandard, Deck- und Dashboard-Bausatz |
| `vorlagen/` | Werkzeug | Vorlage für neue Äste (`/ast-anlegen`) |

## 4. Projekte und Projekttypen

Ein **Lernprojekt** hat Können als Ziel. Es führt ein `lernlog.md`, bekommt
seinen Lehrplan über `/advisor`, und jeder Block endet mit einem Nachweis.
Geübt wird in den Spuren der Äste, öffentliche Daten nur als Ersatz.

Ein **Anliegen** hat ein Ergebnis im eigenen Leben als Ziel (Steuer,
Gesundheit, Umzug). Es nutzt die Struktur des Scaffolds (Charter, Methodik
mit „Last Validated“, KPIs) und ist fertig, wenn die Definition of Done
erfüllt ist.

| Projekt | Typ | Kurz |
|---|---|---|

## 5. Äste und Grenze

Themen und Anliegen gehören in den Hub. Fremdes Eigentum (Arbeitgeber,
eigene Firma, Kunden) bekommt ein eigenes privates Repo, einen Ast. Die
Liste mit Repo, Spur und Sprache führt `00_kern/einstellungen.json`.

| Ast | Art | Spur | Sprache |
|---|---|---|---|

Arbeitsdaten bleiben im Ast. In den Hub kommt aus einem Ast nur, was über
einen festen Weg zurückläuft, also eine Lernkarte, ein erprobtes Framework
als Registereintrag oder eine Case Study. Alles davon anonymisiert nach
`00_kern/vertraulichkeit.md`, die finale Freigabe liegt bei mir. Den Stand
eines Asts liest `/ast-stand` über die GitHub-API, nur Dateien seiner
Positivliste, nie Daten, Analysen oder Berichte. Ein neuer Ast entsteht mit
`/ast-anlegen`.

Neue Aufgaben aus einem Ast beginnen im Hub mit `/aufnahme`. Sie ordnet die
Aufgabe einem Modul zu, prüft einen Zwilling in einer anderen Spur und
schreibt ein Aufnahmeblatt nach `01_kompass/aufnahmen/`. Daraus baut
`/new-project` im Ast das Projekt.

## 6. Bibliothek und Frameworks

Wer eine Methode braucht, liest `02_bibliothek/Literatur_Index.md` direkt,
aus einem Ast heraus fragt der Agent `literature-scout`. Neue Werke kommen
über `/add-literature` in den Index, ein Hook meldet neue PDFs beim
Sitzungsstart. Eigene Frameworks liegen in `06_wissen/frameworks/` mit dem
Lebenszyklus aus der README (Kandidat, In Erprobung, Bewährt).

## 7. Arbeitsweise

- Der Stand wandert über Git (`main`), vor der Arbeit `git pull --ff-only`.
- Das Claude-Gedächtnis wandert nicht über Git. Vor Arbeitsende
  `python3 00_kern/gedaechtnis_sync.py export` und mitcommitten, auf dem
  anderen Rechner nach dem Pull `python3 00_kern/gedaechtnis_sync.py import`.
- Commit nur des eigenen Projektordners, wenn mehrere Projekte offen sind.
- Lange Vorhaben laufen als Plan mit einem Befehl, der genau einen Schritt
  abarbeitet (`/<kurz>-next`, erzeugt von `/new-project`).
- Das Lernsystem läuft über `/alter`, die tägliche Wiederholung über
  `/heute`, der Wochenrückblick über `/weekly-review`.
- Ergebnisse folgen der Checkliste in `07_handwerk/Definition_of_Done.md`.
