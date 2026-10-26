# Ralph, autonome Iterationsschleife (optional, je Projekt)

Quelle ist https://github.com/snarktank/ralph. Die Skills `/prd` (PRD
erzeugen) und `/ralph` (PRD in prd.json umwandeln) kommen aus dem Plugin
`ralph-skills` des Marketplace `ralph-marketplace` und werden einmal global
installiert. Dieser Ordner enthält nur den zweiten Teil, die eigentliche
Bash-Schleife (`ralph.sh`). Sie wird NICHT global installiert, sondern
bewusst je Projekt kopiert und von Hand gestartet.

## Warnung, vor dem ersten Start lesen

`ralph.sh` ruft im Claude-Modus `claude --dangerously-skip-permissions` auf.
Jede Iteration läuft also ganz ohne Rückfragen, mit Schreib- und
Löschzugriffen, Git-Commits und beliebigen Bash-Befehlen. Kein Werkzeugaufruf
wird einzeln bestätigt.

Nur in einem Ordner starten, der
- ein echtes Softwareprojekt mit Tests oder Typecheck ist (Ralphs
  Fertig-Kriterium ist „Typecheck und Tests bestehen“ je User Story),
- unter Versionskontrolle steht (Ralph arbeitet auf einem eigenen Branch),
- keine unveröffentlichten Rohdaten aus einem Quellsystem oder vertrauliche
  Inhalte enthält, die nicht versehentlich verändert oder committet werden
  dürfen (siehe `00_kern/vertraulichkeit.md` im Hub).

Für reine Excel-, Power-BI- oder Analyseprojekte ist Ralph in der Regel nicht
das richtige Werkzeug. Dort fehlt ein Typecheck- oder Testkriterium, an dem
die Schleife erkennen könnte, ob eine Iteration gelungen ist.

## Einrichtung in einem Projekt

Voraussetzungen sind `jq` (auf macOS `brew install jq`) und die Claude Code
CLI im Pfad.

```bash
# im Hub, in einem Ast heißt der Zielordner projekte/<projekt>/ralph
cp -r 07_handwerk/project_scaffold/ralph 03_projekte/<projekt>/ralph
cd 03_projekte/<projekt>/ralph
chmod +x ralph.sh
```

1. Mit `/prd` in Claude Code eine PRD für das nächste Feature erzeugen (sie
   landet in `tasks/prd-*.md`).
2. Mit `/ralph` die PRD in `ralph/prd.json` umwandeln.
3. Schleife starten.
   ```bash
   ./ralph.sh --tool claude 10   # höchstens 10 Iterationen
   ```
4. Der Fortschritt steht in `progress.txt`. Abgeschlossene oder alte Läufe
   wandern automatisch nach `archive/`, sobald sich der Branch ändert.

## Enthaltene Dateien

- `ralph.sh`, die Schleife selbst
- `prompt.md`, Prompt für den Modus `amp`
- `CLAUDE.md`, Anweisungen für den Modus `claude` (wird bei `--tool claude`
  als stdin an `claude --print` gegeben)
- `prd.json.example`, Referenzformat für die Liste der Stories
