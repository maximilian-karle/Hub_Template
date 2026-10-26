---
description: Ein Befehl für das ganze Lernsystem ALTER. Wählt aus Karten, Modulplan und Verlauf die nächste Tätigkeit (Behalten, Tutor, Editor, Lesen, Meilenstein) und führt sie aus, bis ich stoppe
argument-hint: [optional: minimal]
disable-model-invocation: true
---
Du führst mich durch das Lernsystem ALTER. Ich tippe nur `/alter`, du sagst,
was als Nächstes dran ist, und machst es mit mir. Antworte auf Deutsch. Für
alles, was entsteht, gelten die Schreibregeln aus `00_kern/regeln.md`.

Was dran ist, entscheidet nie du, sondern `04_gedaechtnis/alter.py`. Die
Regeln stehen im Kopf der Datei, die Schwellen in `04_gedaechtnis/methodik.md`.
Die Tätigkeiten selbst führst du nach den bestehenden Befehlsdateien aus
(`/heute`, `/tutor`, `/editor`, `/advisor`). Diese lassen sich nicht als
Befehl aufrufen, du liest die Datei und folgst ihr, als hätte ich sie mit den
Argumenten aus dem Vorschlag aufgerufen.

Die Darstellung im Chat folgt `04_gedaechtnis/darstellung.md`, also Klartext
statt Kürzel, ein Kopf als Tabelle über jeder Frage, Rückmeldung und Bilanz
als Tabelle. Rollen stehen ausgeschrieben (Advisor, Librarian, Tutor, Editor,
Roommate), IDs wie XY2-K00 und Befehlsnamen kommen im Chat nicht vor.

$ARGUMENTS

## 1. Lage holen

```bash
git pull --ff-only && python3 04_gedaechtnis/alter.py
```

Steht oben `minimal`, mit `--minimal`. Scheitert der Pull, nicht mergen und
nicht weitermachen, in zwei Zeilen sagen, was los ist. Hat der Hub noch kein
Remote, lässt du den Pull weg.

Zeigt `00_kern/einstellungen.json` noch `"eingerichtet": false`, sag das in
einem Satz und schlag `/einrichten` vor, bevor es weitergeht. Ist der
Vorschlag `advisor`, weil es noch kein Modul gibt (`grund` nennt das), endet
`/alter` hier mit einem Satz. Eine neue Aufgabe beginnt mit `/aufnahme`, ein
Modul aus dem Studienplan plant `/advisor`.

## 2. Ansagen und loslegen

Eine Tabelle mit vier Zeilen, dann sofort beginnen, ohne Rückfrage. Titel von
Modul und Kapitel holst du aus `modul.md` und `lesepfad.md`, den Satz zu
„Worum es geht“ aus dem Lesepfad.

```
| | |
|---|---|
| **Thema** | {Modultitel ohne ID} |
| **Kapitel** | {Kapitelüberschrift ohne ID} ({Werk, Kapitel}) |
| **Heute** | {Rolle ausgeschrieben}, {Tätigkeit in Worten} |
| **Worum es geht** | {Satz aus dem Lesepfad} |
```

Darunter eine Zeile, warum genau das jetzt dran ist (aus `grund`, in
Alltagssprache), und eine Zeile, wie geprüft wird. Die `hinweise` nennst du
beim ersten Vorschlag der Sitzung in einer Zeile darunter, ausgeführt werden
sie nur, wenn ich es sage. Sage ich „später“ oder „stopp“, endet die Sitzung
mit Abschnitt 5.

## 3. Ausführen je Schritt

| `schritt` | Was du tust | `--ergebnis` beim Eintragen |
|---|---|---|
| `heute` | `.claude/commands/heute.md` von vorn, ohne dessen Commit am Ende | Trefferquote und Zahl der Karten |
| `feynman_start` | `.claude/commands/tutor.md` mit `feynman` und den Abschnitten, als Ausgangswert vor dem Lesen | Punkte von 12 und Zuversicht |
| `lesen` | Aus `01_kompass/module/<modul>_*/lesepfad.md` den Abschnitt zeigen (Werk, Seiten, Warum jetzt, Worauf achten). Dann wartest du, bis ich „gelesen“ sage. Ist es heute nicht mehr drin, endet die Sitzung, der Schritt bleibt offen. | Minuten, falls ich sie nenne |
| `sokrates`, `sokrates_luecke` | `tutor.md` mit `sokrates`. Bei `sokrates_luecke` zuerst die gescheiterten Karten des Abschnitts mit `engine.py zeige` lesen, dort setzt die Suche nach der Lücke an | die gefundene Lücke in einem Satz |
| `abschluss` mit Modus `test` oder `feynman` | `tutor.md` im Modus aus dem Vorschlag | Treffer oder Punkte und Zuversicht |
| `feynman_illusion` | `tutor.md` mit `feynman`. Sag vorher in einem Satz, dass hohe Zuversicht und falsche Antworten zusammenfielen | Punkte und Zuversicht |
| `feynman_abstand` | `tutor.md` mit `feynman`, ausdrücklich ohne vorheriges Nachlesen. Geprüft wird, ob das Verständnis nach Wochen hält | Punkte und Zuversicht |
| `editor`, `editor_abstand` | Ich schreibe eine Erklärung des Abschnitts für einen Fachfremden, fünf bis zehn Sätze, im Chat. Dann `.claude/commands/editor.md` mit `chat erklaerung` | hält oder hält nicht, Zahl der Befunde A |
| `abschluss` mit Modus `editor` | Frag nach dem Pfad zum Artefakt im Ast oder im Hub, dann `editor.md` mit diesem Pfad | hält oder hält nicht |
| `arbeiten` | Sag, wo die Arbeit liegt, also im Ast der Spur des Blocks (siehe `befehl` und `00_kern/einstellungen.json`, dort meist über das `/xx-next` des Projekts) oder bei Spur Ö mit öffentlichen Daten im Lernprojekt, und was der Block liefern soll (`inhalt`, `nachweis`). Die Arbeit passiert dort. Die Sitzung endet, bis ich „fertig“ melde | kurz, was entstanden ist |
| `lernlog` | Eine Frage nach den Minuten des Blocks. Dann eine Zeile in `lernlog.md` des Lernprojekts aus `modul.md` (Datum, Block, Minuten, Prüfung aus den Ergebnissen im Verlauf, Nachweis). Gibt es eine langweiligste Stelle, kommt sie in die Spalte Notiz | Minuten |
| `gate` | `tutor.md` mit `feynman` über alle Abschnitte des Vorschlags als Erklär-Check. Was in `pruefung` darüber hinaus steht (etwa ADR verteidigen), danach in derselben Runde | Punkte und Zuversicht |
| `advisor` | `.claude/commands/advisor.md` für das nächste Modul | geplantes Modul |
| `pause` | nichts, Minimalbetrieb, die Sitzung endet | |

Karten aus Lücken entstehen so, wie `tutor.md` es sagt, nach meinem Ja. Eine
Zeile im Transcript entsteht so, wie `editor.md` es sagt.

## 4. Eintragen und weiter

Nach jeder abgeschlossenen Tätigkeit:

```bash
python3 04_gedaechtnis/alter.py erledigt --ergebnis "{ergebnis}"
```

Das trägt den Vorschlag in `04_gedaechtnis/alter_verlauf.json` ein, schaltet
nach `lesen` die Karten frei und gibt den nächsten Vorschlag aus. Mit ihm geht
es bei Abschnitt 2 weiter, ohne Rückfrage. Bricht eine Tätigkeit ab, bevor sie
fertig ist, trägst du nichts ein, der Schritt kommt beim nächsten `/alter`
wieder.

Du überspringst keinen Vorschlag und tauschst keine Reihenfolge. Will ich
etwas anderes, sage ich es, dann endet `/alter` und ich rufe den Befehl
selbst auf.

## 5. Ende

Ende ist, wenn ich stoppe, ein Schritt Zeit außerhalb braucht (`lesen`,
`arbeiten`) oder der Vorschlag `pause` ist. Dann eine Tabelle mit höchstens
fünf Zeilen als Stand, ohne Rückstand:

| | |
|---|---|
| **Heute gelaufen** | je Tätigkeit die Rolle ausgeschrieben, das Kapitel und das Ergebnis |
| **Als Nächstes** | was beim nächsten Mal dran ist, in Worten |

Danach committen, nur was die Sitzung geändert hat:

```bash
git add -- 04_gedaechtnis/karten 04_gedaechtnis/alter_verlauf.json && git commit -m "ALTER: {datum}, {Tätigkeiten}"
```

Lernlog und Transcript kommen mit `git add --` auf ihren Pfad dazu, wenn sie
sich geändert haben. Frag einmal, ob gepusht werden soll, und push erst nach
meinem Ja.
