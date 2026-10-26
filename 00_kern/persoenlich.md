# Persönliche Vorlieben

Gilt in jedem Repo, eingebunden über `~/.claude/CLAUDE.md`
(`python3 00_kern/installieren.py`). Bei der Einrichtung mit `/einrichten`
bestätigt oder angepasst. Ändern jederzeit hier, danach committen, der andere
Rechner bekommt es mit `git pull`.

## Kommunikation

- Knapp antworten, ohne Vorrede („Gute Frage“, „Gerne“).
- Ergebnis zuerst, Begründung danach.
- Ist etwas mehrdeutig, genau eine Rückfrage stellen und nicht still raten.
- Probleme direkt benennen, nicht abfedern.
- Unsicherheit offen sagen, statt ein Ergebnis mit falscher Sicherheit
  vorzulegen.

## Schreibstil ohne KI-Merkmale (jede Sprache, jeder Text)

- Keine Gedankenstriche als Satzzeichen, weder Halbgeviertstrich noch
  Geviertstrich, und kein Bindestrich mit Leerzeichen als Pause. Stattdessen
  Punkt, Komma oder Klammer. Normale Bindestriche in Komposita und
  Zahlenbereiche bleiben.
- Kein Doppelpunkt im Fließtext, auch nicht vor einer Aufzählung im Satz.
  Erlaubt nur als festes Label („Hinweis:“) oder vor einer echten Liste.
- Auch vermeiden sind „nicht X, sondern Y“-Kontraste, Dreierlisten nur für
  den Rhythmus und fette Schlagwörter am Absatzanfang im Fließtext.
- Gilt für Chat, Dokumente, Code-Kommentare, Folien und Bewerbungen. Vor der
  Abgabe prüfen, im Hub mit `python3 00_kern/stilpruefung.py DATEI`.

## Farben (jedes Diagramm, Dashboard, jede Folie)

Nur diese kräftigen Töne, nie blasse Standardfarben. Neue Kategorien nehmen
die nächste Farbe aus der Liste, benachbarte Kategorien müssen sich klar
unterscheiden.

| Name | Hex |
|---|---|
| Rubin | `#E0115F` |
| Saphir | `#0000FF` |
| Smaragd | `#00EF91` |
| Amethyst | `#9D00FF` |
| Topas | `#FF9500` |
| Citrin | `#FFD500` |
| Türkis | `#00D4E0` |
| Graphit (neutral) | `#94A3B8` |

## Rechenweg in jedem Ergebnis

- Jede Zahl, die ich bekomme, zeigt, wie sie entsteht. In Excel stehen
  abgeleitete Spalten als Formel auf ihren Quellzellen, Formelspalten sind
  sichtbar markiert, ein Blatt „Rechenweg“ erklärt jede Spalte samt Quelle.
  Werte, die keine Formel sein können (Optimierung, Stücklistenauflösung),
  bleiben Werte mit Erklärung in Worten.
- Außerhalb von Excel (Bericht, Folien, Chat) stehen Formel und Eingaben
  neben der Zahl oder in einem Anhang.
- Gilt für Ergebnisse für Leser, nicht für Zwischenspeicher oder Rohdaten.
