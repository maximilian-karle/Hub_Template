---
description: Nimmt eine neue Aufgabe aus einem Ast (Arbeit, Selbständigkeit, weitere) im Hub auf, ordnet sie einem Modul zu, sucht einen Zwilling in einer anderen Spur und schreibt das Aufnahmeblatt für /new-project im Ast
argument-hint: [Aufgabe in einem Satz, optional]
---
Eine neue Aufgabe liegt auf dem Schreibtisch, bei der Arbeit, in der
Selbständigkeit oder in einem anderen Ast, egal ob sie ins laufende Trimester
passt. Du nimmst sie im Hub auf, damit Theorie und Praxis zusammenlaufen.
Antworte in `sprache.chat` aus `00_kern/einstellungen.json`, für alles, was
entsteht, gelten `00_kern/regeln.md` und `00_kern/persoenlich.md`.

Ergebnis ist ein Aufnahmeblatt unter `01_kompass/aufnahmen/`. Es ist die
Übergabe an `/new-project` im Ast. Liegt der Ast nicht auf diesem Rechner
(etwa ein Arbeits-Ast nur auf dem Firmenrechner), entsteht das Projekt dort
aus diesem Blatt nach einem `git pull` im Hub.

Aufgabe aus dem Aufruf: $ARGUMENTS

## 1. Einlesen, bevor du fragst

- `00_kern/einstellungen.json` (Äste mit Spur, Kompetenzbereiche, Budget)
- `01_kompass/entwicklung/profil.md` (Ziele, Kompetenzprofil)
- `01_kompass/studienplan/studienplan.md` (Trimester, Module, Freeze-Regel)
- `01_kompass/module/README.md` und die Modulordner, welche Module es schon
  gibt, mit Kern-Lesepfad und Register der Projekte
- `01_kompass/aufnahmen/README.md`, ob die Aufgabe schon aufgenommen ist
- Äste, die auf diesem Rechner liegen (Pfad in `einstellungen.json`), nur
  `CLAUDE.md` und `00_kontext/`. Äste ohne lokalen Klon nur über
  `python3 00_kern/ast_stand.py`.

Gibt es noch keinen Ast, verweis auf `/ast-anlegen` und stopp.

## 2. Interview

Eine Frage je Nachricht, jede mit einem Vorschlag aus den Unterlagen, den ich
bestätige oder korrigiere. Bestätige ich unverändert, kommt die nächste
Frage gleich in derselben Nachricht. Höchstens fünf Fragen je Stufe.

### Stufe 1, Auftrag

- Was ist die Aufgabe, was soll am Ende anders sein, wer erwartet es?
- In welchem Ast liegt sie?
- Spätestens wann? Termine sind Obergrenzen, gearbeitet wird so schnell wie
  möglich.
- Welche Theorie braucht die Aufgabe? Du schlägst die Fachgebiete vor, ich
  korrigiere.

Ins Aufnahmeblatt kommt nur eine neutrale Beschreibung, keine Zahlen, keine
Namen, keine Nummern aus dem Quellsystem (`00_kern/vertraulichkeit.md`).
Die Einzelheiten gehören in die Charter im Ast.

### Stufe 2, Einordnen

Prüffrage zuerst. Berührt die Aufgabe einen Bereich des Kompetenzprofils
oder ein Ziel aus `profil.md`? Wenn nein, wird sie **kein Modul**. Dann
entsteht im Ast ein Projekt mit eigenem Lesepfad, und das Aufnahmeblatt hält
nur das fest. Weiter mit Abschnitt 4.

Wenn ja, prüfst du die Freeze-Regel in `studienplan.md`, falls es eine
gibt. Dann genau einer von drei Fällen. Ein Modul ist ein Kompetenzfeld, das
über die Jahre Projekte sammelt. Je mehr Projekte in einem Modul laufen, desto
stärker ist der Beleg.

1. **Modul gibt es schon.** Es hat einen Ordner unter `01_kompass/module/`.
   Das Projekt kommt ins Register `projekte.md` und nutzt den Kern-Lesepfad.
   Braucht es Theorie, die der Kern noch nicht hat, schlägst du neue
   Abschnitte vor.
2. **Modul ist nur geplant.** Es steht im Studienplan, hat aber noch keinen
   Ordner. Es wird sofort ausgearbeitet. Du zeigst die zusätzliche Last mit
   Rechenweg gegen das Budget aus `einstellungen.json`.
3. **Kein Modul passt.** Brainstorming mit mir, in dieser Reihenfolge.
   Bereich im Kompetenzprofil, Lernziel, Kern in drei bis fünf Stichworten,
   Quellen aus `02_bibliothek/` mit Kapitel (Literatur-Index, bei Bedarf der
   Agent `literature-scout`), Lücken als Empfehlung, Stunden für Kern und
   Spuren. Die Modul-ID ist das Bereichskürzel plus die nächste freie Nummer.
   Danach die Last wie in Fall 2.

Bei Fall 2 und 3 änderst du `studienplan.md` erst nach meinem Ja. Danach
legst du den Modulordner nach `01_kompass/module/README.md` an.

### Stufe 3, Zwilling in einer anderen Spur

Prüfe, ob derselbe Kern in einem anderen Ast nebenher laufen kann, etwa eine
Methode aus der Arbeit an den Daten der Selbständigkeit. Ein Zwilling braucht
alle vier Punkte.

| Kriterium | Frage |
|---|---|
| gleicher Kern | Wendet er dieselbe Methode in derselben Reihenfolge an? |
| Daten | Liegen die Daten im anderen Ast vor oder sind sie in der ersten Modulwoche beschaffbar? |
| Nutzen | Hilft das Ergebnis dem anderen Ast wirklich? |
| Umfang | Passt er ins Budget, ohne es zu sprengen? |

Fehlt ein Punkt, gibt es keinen Zwilling. Dann nennst du den Grund und
prüfst Spur Ö (öffentliche Daten) nur als Ersatz. Gibt es einen, nennst du
Ast, Spur, Projektname, Leitfrage und Datenquelle.

## 3. Modulordner im Hub

Die Theorie des Moduls liegt einmal im Hub, damit alle Projekte des Moduls
auf dieselben Abschnitte verweisen und ein Jobwechsel nur einen Ast ändert.

- Kern-Lesepfad `01_kompass/module/<Modul-ID>_<kurzname>/lesepfad.md`.
- Gibt es die Datei schon, prüfst du nur, ob der Kern die Aufgabe trägt, und
  schlägst fehlende Abschnitte vor.
- Sonst legst du sie nach der Vorlage
  `07_handwerk/project_scaffold/00_Charter/Lesepfad.md` an, mit IDs
  `<Modul-ID>-K01` und folgende. Je Abschnitt Werk, Kapitel, Seiten (vorher
  im PDF der Bibliothek geprüft), Pflichtminuten, Warum jetzt, Worauf achten,
  zwei Kontrollfragen. Fehlt ein Werk in der Bibliothek, steht die Lücke als
  Empfehlung da.
- Keine Zusammenfassung der Bücher, keine wörtlichen Zitate über 15 Wörter.
- Je Spur eine Zeile im Register `projekte.md` (Ast, Spur, Projekt, Ort im
  Ast noch „nicht angelegt“) und die Tabelle in `01_kompass/module/README.md`
  nachziehen.

## 4. Aufnahmeblatt

Vorlage `01_kompass/aufnahmen/_Vorlage_Aufnahmeblatt.md`, Datei
`01_kompass/aufnahmen/<JJJJ-MM-TT>_<kurzname>.md`, Zeile in der Tabelle der
`README.md`. Leg das Blatt vollständig im Chat vor und schreib erst nach
meinem Ja.

## 5. Übergabe

Nenne am Ende die nächsten Schritte als Befehle zum Kopieren, je Ast.

- im Ast `<NAME>` (Pfad aus `einstellungen.json`) `/new-project <kurzname>`
- danach im Hub `/advisor <Modul-ID>`

`/new-project` findet das Aufnahmeblatt über den Kurznamen und füllt daraus
Anlass, Ziele, Scope und Methoden vor.

## 6. Was du nicht tust

- keine Arbeitsdaten in den Hub schreiben, auch nicht im Aufnahmeblatt
- kein Projekt in einem Ast anlegen, das macht `/new-project` dort
- Studienplan nicht ohne mein Ja ändern
- einen Zwilling nicht erzwingen, ein Modul läuft auch mit nur einer Spur
