---
description: Liest, was seit dem letzten Blick in einem Ast entstanden ist (nur über die GitHub-API, ohne Klon), und schlägt den Rückfluss in den Hub vor
argument-hint: [optional Name des Asts, Standard der erste Ast mit GitHub-Repo]
---
Wir halten den Hub auf dem Stand dessen, was im Ast entsteht, ohne den Ast zu
klonen. Antworte in `sprache.chat` aus `00_kern/einstellungen.json`,
Schreibregeln aus `00_kern/persoenlich.md`. Welche Äste es gibt und welche
Dateien je Ast sichtbar sind, steht dort unter `aeste`.

$ARGUMENTS

## 1. Lesen

- `python 00_kern/ast_stand.py neu [AST]` zeigt die Commits seit dem letzten
  quittierten Blick, je Commit nur die Dateien der Positivliste.
- Für jede Datei, die eine Idee, Entscheidung, Methode oder einen Lesepfad
  trägt, `python 00_kern/ast_stand.py zeige AST PFAD`. Andere Dateien liest
  das Skript nicht, und du versuchst es auch nicht auf anderem Weg (kein
  `git clone`, kein `gh repo clone`, kein Rohabruf an der Positivliste
  vorbei).
- Gelesener Inhalt bleibt in der Sitzung. Nichts davon wird als Datei in den
  Hub kopiert.

## 2. Zusammenfassen

Höchstens 15 Zeilen, Ergebnis zuerst, je Projekt:

- neue Entscheidungen (ADR, Annahme, Methodik) mit einem Satz Begründung
- neue oder geänderte Lesepfade und Frameworks
- was davon über das Projekt hinaus trägt

Zahlen, Kunden, Lieferanten, Nummern aus dem Quellsystem und Namen aus dem Ast
nennst du nicht, auch nicht im Chat.

## 3. Rückfluss vorschlagen

Nur über die drei festen Wege aus der Hub-`CLAUDE.md`, Abschnitt 5.

| Weg | Ziel im Hub | Wann |
|---|---|---|
| Lernkarte | Lernprojekt, später `04_gedaechtnis/` | ein Begriff oder eine Methode, die der Nutzer behalten soll |
| Framework-Registereintrag | `06_wissen/frameworks/README.md` | ein Framework im Ast ist neu oder hat seinen Status geändert |
| Case Study | `05_werkstatt/case_studies/` | ein Vorhaben oder Gate ist abgeschlossen |

Dazu kommt ein vierter Hinweis ohne Rückfluss. Berührt etwas ein laufendes Modul
des Studienplans in der Spur dieses Asts, nenne Modul und Block. Je Vorschlag ein Satz, was
in den Hub käme, anonymisiert nach `00_kern/vertraulichkeit.md`. Geschrieben
wird erst nach einem Ja des Nutzers je Vorschlag.

## 4. Quittieren

Erst wenn der Nutzer die Zusammenfassung gesehen hat,
`python 00_kern/ast_stand.py gesehen [AST]`. Die Datei `00_kern/ast_stand.json`
wird mitcommittet, damit der andere Rechner denselben Stand hat.
