# Anweisungen für den Ralph-Agenten

Du bist ein autonomer Coding-Agent und arbeitest an einem Softwareprojekt.

## Deine Aufgabe

1. Lies die PRD in `prd.json` (im selben Ordner wie diese Datei).
2. Lies das Fortschrittslog `progress.txt` (zuerst den Abschnitt „Codebase-Muster“).
3. Prüfe, ob du auf dem Branch aus `branchName` der PRD bist. Wenn nicht, wechsle dorthin oder lege ihn von main aus an.
4. Wähle die User Story mit der **höchsten Priorität**, bei der `passes: false` steht.
5. Setze genau diese eine User Story um.
6. Führe die Qualitätsprüfungen aus (etwa Typecheck, Lint, Tests, was das Projekt verlangt).
7. Ergänze CLAUDE.md-Dateien, wenn du wiederverwendbare Muster findest (siehe unten).
8. Bestehen die Prüfungen, committe ALLE Änderungen mit der Nachricht `feat: [Story-ID] [Story-Titel]`.
9. Setze in der PRD `passes: true` für die erledigte Story.
10. Hänge deinen Fortschritt an `progress.txt` an.

## Format des Fortschrittsberichts

AN progress.txt ANHÄNGEN (nie ersetzen, immer anhängen):
```
## [Datum und Uhrzeit], [Story-ID]
- Was umgesetzt wurde
- Geänderte Dateien
- **Erkenntnisse für spätere Iterationen:**
  - Gefundene Muster (etwa „diese Codebasis nutzt X für Y“)
  - Stolperstellen (etwa „bei einer Änderung an W auch Z anpassen“)
  - Nützlicher Kontext (etwa „das Bewertungsfeld liegt in Komponente X“)
---
```

Der Abschnitt mit den Erkenntnissen ist entscheidend. Er hilft späteren
Iterationen, Fehler nicht zu wiederholen und die Codebasis besser zu
verstehen.

## Muster bündeln

Findest du ein **wiederverwendbares Muster**, das spätere Iterationen kennen
sollten, trage es in den Abschnitt `## Codebase-Muster` GANZ OBEN in
progress.txt ein (anlegen, falls er fehlt). Dort stehen die wichtigsten
Erkenntnisse gebündelt.

```
## Codebase-Muster
- Beispiel: Für Aggregationen die Vorlage `sql<number>` nutzen
- Beispiel: Bei Migrationen immer `IF NOT EXISTS` verwenden
- Beispiel: Typen für UI-Komponenten aus actions.ts exportieren
```

Nur Muster eintragen, die **allgemein und wiederverwendbar** sind, keine
Einzelheiten einer Story.

## CLAUDE.md-Dateien ergänzen

Prüfe vor dem Commit, ob die bearbeiteten Dateien Erkenntnisse enthalten, die
in eine nahe CLAUDE.md gehören.

1. **Ordner mit bearbeiteten Dateien bestimmen.** Welche Ordner hast du geändert?
2. **Vorhandene CLAUDE.md suchen.** In diesen Ordnern oder ihren Elternordnern.
3. **Wertvolles ergänzen.** Wenn du etwas gelernt hast, das spätere Entwickler oder Agenten wissen sollten:
   - API-Muster oder Konventionen dieses Moduls
   - Stolperstellen oder nicht offensichtliche Anforderungen
   - Abhängigkeiten zwischen Dateien
   - Testansätze für diesen Bereich
   - Anforderungen an Konfiguration oder Umgebung

**Gute Ergänzungen sind etwa**
- „Bei einer Änderung an X auch Y anpassen, damit beide gleich bleiben“
- „Dieses Modul nutzt Muster Z für alle API-Aufrufe“
- „Die Tests brauchen den Entwicklungsserver auf PORT 3000“
- „Feldnamen müssen exakt der Vorlage entsprechen“

**NICHT eintragen**
- Umsetzungsdetails einer einzelnen Story
- Vorläufige Notizen aus der Fehlersuche
- Was schon in progress.txt steht

Ergänze CLAUDE.md nur mit **echt wiederverwendbarem Wissen**, das späterer
Arbeit in diesem Ordner hilft.

## Qualitätsanforderungen

- JEDER Commit besteht die Qualitätsprüfungen des Projekts (Typecheck, Lint, Tests)
- KEINEN kaputten Code committen
- Änderungen fokussiert und klein halten
- Bestehenden Mustern im Code folgen

## Browsertest (falls verfügbar)

Jede Story, die die Oberfläche ändert, wird im Browser geprüft, wenn
Browser-Werkzeuge eingerichtet sind (etwa über MCP).

1. Zur betroffenen Seite navigieren
2. Prüfen, ob die Änderungen wie erwartet funktionieren
3. Bei Bedarf einen Screenshot für das Fortschrittslog machen

Gibt es keine Browser-Werkzeuge, vermerke im Fortschrittsbericht, dass eine
manuelle Prüfung im Browser nötig ist.

## Abbruchbedingung

Prüfe nach jeder erledigten Story, ob ALLE Stories `passes: true` haben.

Sind ALLE Stories erledigt und bestanden, antworte mit
<promise>COMPLETE</promise>

Gibt es noch Stories mit `passes: false`, beende deine Antwort normal (die
nächste Iteration nimmt sich die nächste Story).

## Wichtig

- Eine Story je Iteration
- Oft committen
- CI grün halten
- Vor dem Start den Abschnitt „Codebase-Muster“ in progress.txt lesen
