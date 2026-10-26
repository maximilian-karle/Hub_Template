---
description: Hängt einen neuen Ast an den Hub, ein eigenes privates Repo für Arbeit, Selbständigkeit, Verein oder Kunden, mit Spur, Sprache und GitHub-Repo
argument-hint: [Name des Asts, optional]
---
Wir hängen einen neuen Ast an den Hub. Ein Ast ist ein eigenes privates Repo
neben dem Hub für fremdes Eigentum (Arbeitgeber, eigene Firma, Verein,
Kunde). Arbeitsdaten bleiben dort, in den Hub kommt nur Anonymisiertes über
die festen Wege. Antworte in `sprache.chat` aus `00_kern/einstellungen.json`,
Schreibregeln aus `00_kern/persoenlich.md`.

Name aus dem Aufruf: $ARGUMENTS

## 1. Einlesen

- `00_kern/einstellungen.json`, welche Äste und Spuren es schon gibt
- `CLAUDE.md` Abschnitt 5

## 2. Fragen

Höchstens drei je Nachricht, geschlossene über `AskUserQuestion`.

1. Art (Arbeit beim Arbeitgeber, eigene Selbständigkeit, Sonstiges).
2. Name, Vorschlag `AT_<KÜRZEL>` für angestellt, `ST_<KÜRZEL>` für
   selbständig, sonst ein sprechender Name. Nur Buchstaben, Ziffern, `_`.
3. Spur, der nächste freie Großbuchstabe (A Arbeit, U Unternehmen üblich).
   Ö ist für öffentliche Daten reserviert.
4. Sprache der Dateien im Ast.
5. Ort. Vorschlag neben dem Hub. Bei Arbeit fragen, ob Firmendaten auf diesem
   Rechner liegen dürfen. Wenn nein, nur eintragen und auf dem erlaubten
   Rechner anlegen.
6. Zwei bis vier Sätze, worum es im Ast geht (Rolle, Auftrag, neutral).

Rückspiegeln in sechs Zeilen, erst nach „passt“ weiter.

## 3. Anlegen

1. `python3 00_kern/einrichten.py ast <NAME> --art <art> --spur <S> --sprache <Sprache> [--ziel <Pfad>]`
2. Im Ast `CLAUDE.md` Abschnitt 1 füllen.
3. Nach ausdrücklichem Ja das private GitHub-Repo anlegen,
   `gh repo create <NAME> --private --source <Pfad> --push`, dann in
   `00_kern/einstellungen.json` beim Ast `repo` auf `<konto>/<NAME>` setzen
   (Konto aus `person.github` oder `gh api user -q .login`).
4. Zeile in der Tabelle in `CLAUDE.md` Abschnitt 5 des Hubs ergänzen.
5. Commit im Hub vorschlagen (`00_kern/einstellungen.json`, `CLAUDE.md`).

## 4. Abschluss

Nenne den Pfad, das Repo und die nächsten Befehle zum Kopieren:
`/aufnahme <Aufgabe>` im Hub, danach im Ast `/new-project <kurzname>`.
`/ast-stand <NAME>` liest den Ast künftig aus dem Hub.
