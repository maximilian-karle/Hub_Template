# Arbeitsplan <Projektname>

| Feld | Wert |
|---|---|
| Version / Datum | v0.1 / <TT.MM.JJJJ> |
| Grundlage | Charter, Aufnahmeblatt `<Hub>/01_kompass/aufnahmen/<Datei>` (falls vorhanden) |
| Modul | <Modul-ID>, Spur <Buchstabe des Asts aus `00_kern/einstellungen.json`, Ö für öffentliche Daten>, Kern-Lesepfad `<Hub>/01_kompass/module/<Modul-ID>_<kurzname>/lesepfad.md` |
| Arbeitsweise | ein Arbeitspaket je Sitzung über `/<kurz>-next`, das erste ohne Erledigt-Vermerk in der Reihenfolge der Tabellen |
| Erledigt-Vermerk | die Zelle „Was“ beginnt mit `**Erledigt TT.MM.JJJJ.**` und einem Satz Ergebnis |
| Termine | alle Termine sind Obergrenzen, gearbeitet wird so schnell wie möglich |
| Lesebegleitung | Spalte LP nennt den Abschnitt, entweder aus dem Kern-Lesepfad im Hub (`<Modul-ID>-Knn`) oder projektspezifisch aus `00_Charter/Lesepfad.md` (`LP-nn`). Er wird zu Beginn des Pakets vollständig ausgegeben, „kein Eintrag“ wird ausdrücklich gesagt |

## Kurzfassung

Ergebnis zuerst in drei bis fünf Sätzen. Was steht am Ende, woran hängt der
Termin.

## Entscheidungen

| ID | Thema | Entscheidung | Begründung | Bestätigen |
|---|---|---|---|---|

## Phasen und Gates

| Phase | spätestens | Ziel | Gate mit Kriterium |
|---|---|---|---|

## P0 <Phase>

| AP | Was | Wer | Ergebnis (fertig, wenn) | Hängt an | spätestens | LP |
|---|---|---|---|---|---|---|

## Laufend

| Was | Wer | Takt |
|---|---|---|
| ADR je Designentscheidung mit Literaturstelle in `docs/adr/` | Claude Entwurf, Nutzer Abnahme | je Arbeitspaket |
| Leseeintrag zu Beginn des Pakets ausgeben und lesen | Claude gibt aus, Nutzer liest | je Arbeitspaket |
| Erklär-Check nach jedem Gate, der Nutzer erklärt | Nutzer, Claude prüft gegen das Kapitel | je Gate |
| Rückfluss in den Hub (Lernkarte, Framework, Case Study) | Claude schlägt vor, Nutzer gibt frei | je Gate |
