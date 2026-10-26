---
argument-hint: [projekt | lernen | trimester]
description: Fasst Wochenfortschritt zusammen und aktualisiert den Projekt-Status, mit Lernteil und Trimesterreview
---
Wähle nach `$1` den Teil.

- Ein Projektordner unter `03_projekte/` führt Teil A aus.
- `lernen` führt Teil B aus. Ein Lernprojekt (Ordner unter `03_projekte/` mit
  `lernlog.md`) führt ebenfalls Teil B aus, danach Teil A für dessen Ordner.
- `trimester` führt Teil C aus.
- Ohne Argument führst du Teil B aus. Gibt es noch kein Lernprojekt, keine
  Karte und kein Modul, sag das in einem Satz und verweise auf `/aufnahme`
  oder `/advisor` (und auf `/einrichten`, falls `00_kern/einstellungen.json`
  noch `"eingerichtet": false` zeigt).

Für alles, was entsteht, gelten die Schreibregeln aus `00_kern/regeln.md`.

## Teil A, Projektstatus

Für 03_projekte/$1/:

1. Ermittle, was sich seit der letzten Ausführung geändert hat
   (geaenderte/neue Dateien in data/, analysis/, kpis/, dashboards/;
   falls Git genutzt wird: `git log --since="7 days ago" --stat`).
2. Fasse in max. 5 Bulletpoints zusammen: was wurde fertiggestellt, was
   ist in Arbeit, was ist blockiert (und warum).
3. Liste offene Befunde aus data/output/data_quality_log.md, die noch
   nicht adressiert wurden.
4. Aktualisiere den Abschnitt "Aktueller Status" in
   03_projekte/$1/CLAUDE.md mit dem neuen Stand (Datum + Kurzfassung).
5. Prüfe, ob unter den fertiggestellten Ergebnissen aus Schritt 2 etwas
   ist, das noch nicht in
   05_werkstatt/karriere/Profil/Leistungsdokumentation.md (falls es
   diese Datei gibt) steht (neues quantifiziertes Ergebnis, neuer Meilenstein, neue
   Eigeninitiative). Falls ja: Ergänzungsvorschlag machen (welcher
   Abschnitt, welcher Wortlaut) statt automatisch reinzuschreiben, der
   Nutzer bestätigt, da das Dokument vertraulich und zeugnisrelevant ist.
6. Ausgabe: kurze Statusmeldung, kein Fliesstext-Report.

## Teil B, Lernteil der Woche

Gerechnet wird nie von dir. Die Zahlen liefert `04_gedaechtnis/wochenlage.py`,
die Regeln dazu stehen im Kopf des Skripts.

```bash
git pull --ff-only && python3 04_gedaechtnis/wochenlage.py --merken
```

Scheitert der Pull, nicht mergen, in zwei Zeilen sagen, was los ist, und den
Nutzer entscheiden lassen. Hat der Hub noch kein Remote, entfällt der Pull. `--merken` schreibt den Messpunkt des Tages in
`04_gedaechtnis/rueckstau.json`, ohne ihn gäbe es nie einen Trend.

Ausgabe als Stand, höchstens acht Zeilen, jede Zahl mit ihrer Rechnung
(Rechenweg aus `~/.claude/CLAUDE.md`).

| Größe | Quelle und Rechnung | Lesart |
|---|---|---|
| Ist-Stunden | `ist_minuten.minuten` aus den Lernlogs unter `03_projekte/`, gegen `budget_min` (`lernen.deep_dive_h_woche` aus `00_kern/einstellungen.json` mal 60, ohne Eintrag 300 Minuten) | Stand, kein Soll-Ist. Je Projekt aufschlüsseln, je Kern und Spur des Moduls, wenn das Lernlog sie nennt |
| Wiederholung | `abrufquote.wiederholung_min_geschaetzt`, Abrufe mal Zeitkosten aus `heute.KOSTEN` | Schätzung, `/heute` führt kein Zeitlog. Als Schätzung kennzeichnen |
| Abrufquote | `richtig` durch `abrufe` im Fenster, erster Kontakt ausgenommen | Korridor 60 bis 70 %. Darüber oder darunter als Beobachtung nennen, nicht als Urteil. Mit Kalibrierung, wenn `kalibrierung` gefüllt ist (Make It Stick, Kap. 5) |
| Rückstau | `rueckstau.last_tagesbudgets` (Zeit der fälligen Karten durch das Tagesbudget `lernen.wiederholung_min_tag`, ohne Eintrag 20 Minuten), Bremse ab 1,5 | Trend gegen den Messpunkt, der mindestens sechs Tage alt ist. Fehlt er, sag „erster Messpunkt“ |
| Nächster Block | `abschnitte.naechster` (erster Abschnitt mit gesperrten Karten) und `abschnitte.aktiv`, dazu der nächste offene Abschnitt in `lesepfad.md` des Moduls und die offene Meilensteinzeile in `modul.md` | Ein Vorschlag, kein Pensum |

Regeln für den Ton, übernommen aus `/heute`.

- Kein Schuldaufbau. Nie „verpasst“, nie „im Rückstand“ in Bezug auf Tage oder
  Stunden. Eine Woche unter dem Budget ist ein Stand. Der Rückstau meint nur
  die Last fälliger Karten, und die steht neben der Bremse, nicht über dem
  Nutzer.
- Stunden sind Obergrenzen. Über dem Budget ist keine gute Woche, über 90
  Minuten an einem Tag in einem Block ein Warnzeichen.
- Fehlt ein Lernlog oder ist es leer, sag das in einem Satz. Nichts schätzen.

Danach Erinnerung an Prüfungen. Liegt der letzte Trimesterreview (Teil C) mehr
als drei Monate zurück oder gibt es keinen, nenne das in einem Satz mit dem
Verweis auf `/weekly-review trimester`.

Den Messpunkt committen, nur diese Datei:

```bash
git add -- 04_gedaechtnis/rueckstau.json && git commit -m "Gedächtnis: Messpunkt Rückstau {datum}"
```

Frag einmal, ob gepusht werden soll, und push erst nach dem Ja.

## Teil C, Trimesterreview

Einmal je Trimester (drei Monate ab `lernen.trimester_start` in
`00_kern/einstellungen.json`), nicht nachholen,
wenn eines ausfällt. Die Prüfung läuft ohne System, also ohne Karten, Chat und
Skripte, auf Papier oder im leeren Dokument. Sie misst, was ohne Gerüst bleibt
(Make It Stick, Kap. 2, Abruf als Prüfung).

1. **Stoff bestimmen.** Nimm aus `engine.py stats` und den Karten alle, die
   sitzen (Intervall ab 21 Tagen), dazu die Meilensteine der Module im
   laufenden Trimester aus `01_kompass/module/*/modul.md`. Zu einer Frage
   gehört nur Material, das schon eine Karte oder einen Lesepfad-Abschnitt
   hat. Nie ein Stoff, der nie vorkam.
2. **Prüfung bauen.** 12 bis 20 Fragen, verteilt über die Module, ein Drittel
   Begriff, ein Drittel Anwendung auf einen Fall, ein Drittel Rechnung oder
   Erklärung in eigenen Worten, 60 Minuten. Zwei Dateien nach
   `04_gedaechtnis/pruefungen/`, die Prüfung `YYYY-MM_trimester.md` und der
   Schlüssel `YYYY-MM_trimester_loesung.md` mit Punkten je Frage und Quelle
   (Werk und Kapitel). Der Schlüssel wird dem Nutzer erst nach der Abgabe
   gezeigt. Wer die Prüfung als Word-Datei haben will, kann sie mit
   `python-docx` rendern, nötig ist das nicht.
3. **Der Nutzer schreibt sie allein.** Du beantwortest keine Frage, gibst
   keinen Hinweis und rechnest nichts vor.
4. **Auswerten.** Mit dem Schlüssel Punkte vergeben, die Quote ausrechnen
   (Punkte durch Maximum) und zeigen. Schwelle für „bestanden“ ist 70 %
   (Annahme aus `04_gedaechtnis/methodik.md`, nach dem ersten Lauf prüfen). Falsche
   Antworten gehen als neue oder zurückgesetzte Karten in den Kasten, erst
   nach dem Ja des Nutzers (`engine.py add`, `review`).
5. **Transcript.** Ab 70 % eine Zeile in `05_werkstatt/transcript.md` je
   geprüftem Modul und Spur, mit der Prüfung als Nachweis und dem Pfad der
   Datei als Artefakt. Unter 70 % kein Eintrag, dafür die Lücken als
   Wiederholungsplan und eine zweite Prüfung auf Wunsch. Stunden trägst du
   aus dem Lernlog ein, nie geschätzt.
6. **Kalibrierung.** Frag vor der Auswertung nach der geschätzten Quote und
   nenne sie neben der echten (Make It Stick, Kap. 8).

Danach nur die berührten Dateien committen (`04_gedaechtnis/pruefungen`,
`05_werkstatt/transcript.md`, Karten) und einmal nach dem Push fragen.
