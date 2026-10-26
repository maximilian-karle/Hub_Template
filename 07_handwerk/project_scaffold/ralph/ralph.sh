#!/bin/bash
# Ralph Wiggum, lang laufende Schleife für einen KI-Agenten
# Aufruf: ./ralph.sh [--tool amp|claude] [max_iterationen]

set -e

# Argumente lesen
TOOL="amp"  # Standard bleibt amp, wie im Original
MAX_ITERATIONS=10

while [[ $# -gt 0 ]]; do
  case $1 in
    --tool)
      TOOL="$2"
      shift 2
      ;;
    --tool=*)
      TOOL="${1#*=}"
      shift
      ;;
    *)
      # Eine Zahl gilt als Höchstzahl der Iterationen
      if [[ "$1" =~ ^[0-9]+$ ]]; then
        MAX_ITERATIONS="$1"
      fi
      shift
      ;;
  esac
done

# Werkzeugwahl prüfen
if [[ "$TOOL" != "amp" && "$TOOL" != "claude" ]]; then
  echo "Fehler, unbekanntes Werkzeug '$TOOL'. Erlaubt sind 'amp' oder 'claude'."
  exit 1
fi
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PRD_FILE="$SCRIPT_DIR/prd.json"
PROGRESS_FILE="$SCRIPT_DIR/progress.txt"
ARCHIVE_DIR="$SCRIPT_DIR/archive"
LAST_BRANCH_FILE="$SCRIPT_DIR/.last-branch"

# Vorigen Lauf archivieren, wenn sich der Branch geändert hat
if [ -f "$PRD_FILE" ] && [ -f "$LAST_BRANCH_FILE" ]; then
  CURRENT_BRANCH=$(jq -r '.branchName // empty' "$PRD_FILE" 2>/dev/null || echo "")
  LAST_BRANCH=$(cat "$LAST_BRANCH_FILE" 2>/dev/null || echo "")
  
  if [ -n "$CURRENT_BRANCH" ] && [ -n "$LAST_BRANCH" ] && [ "$CURRENT_BRANCH" != "$LAST_BRANCH" ]; then
    # Vorigen Lauf archivieren
    DATE=$(date +%Y-%m-%d)
    # Präfix "ralph/" für den Ordnernamen entfernen
    FOLDER_NAME=$(echo "$LAST_BRANCH" | sed 's|^ralph/||')
    ARCHIVE_FOLDER="$ARCHIVE_DIR/$DATE-$FOLDER_NAME"
    
    echo "Archiviere vorigen Lauf $LAST_BRANCH"
    mkdir -p "$ARCHIVE_FOLDER"
    [ -f "$PRD_FILE" ] && cp "$PRD_FILE" "$ARCHIVE_FOLDER/"
    [ -f "$PROGRESS_FILE" ] && cp "$PROGRESS_FILE" "$ARCHIVE_FOLDER/"
    echo "   Archiviert nach $ARCHIVE_FOLDER"
    
    # Fortschrittsdatei für den neuen Lauf zurücksetzen
    echo "# Ralph Progress Log" > "$PROGRESS_FILE"
    echo "Started: $(date)" >> "$PROGRESS_FILE"
    echo "---" >> "$PROGRESS_FILE"
  fi
fi

# Aktuellen Branch merken
if [ -f "$PRD_FILE" ]; then
  CURRENT_BRANCH=$(jq -r '.branchName // empty' "$PRD_FILE" 2>/dev/null || echo "")
  if [ -n "$CURRENT_BRANCH" ]; then
    echo "$CURRENT_BRANCH" > "$LAST_BRANCH_FILE"
  fi
fi

# Fortschrittsdatei anlegen, falls sie fehlt
if [ ! -f "$PROGRESS_FILE" ]; then
  echo "# Ralph Progress Log" > "$PROGRESS_FILE"
  echo "Started: $(date)" >> "$PROGRESS_FILE"
  echo "---" >> "$PROGRESS_FILE"
fi

echo "Starte Ralph mit $TOOL, höchstens $MAX_ITERATIONS Iterationen"

for i in $(seq 1 $MAX_ITERATIONS); do
  echo ""
  echo "==============================================================="
  echo "  Ralph, Iteration $i von $MAX_ITERATIONS ($TOOL)"
  echo "==============================================================="

  # Gewähltes Werkzeug mit dem Ralph-Prompt ausführen
  if [[ "$TOOL" == "amp" ]]; then
    OUTPUT=$(cat "$SCRIPT_DIR/prompt.md" | amp --dangerously-allow-all 2>&1 | tee /dev/stderr) || true
  else
    # Claude Code läuft mit --dangerously-skip-permissions autonom, --print liefert die Ausgabe
    OUTPUT=$(claude --dangerously-skip-permissions --print < "$SCRIPT_DIR/CLAUDE.md" 2>&1 | tee /dev/stderr) || true
  fi
  
  # Auf das Abschlusssignal prüfen
  if echo "$OUTPUT" | grep -q "<promise>COMPLETE</promise>"; then
    echo ""
    echo "Ralph hat alle Aufgaben erledigt."
    echo "Fertig in Iteration $i von $MAX_ITERATIONS"
    exit 0
  fi
  
  echo "Iteration $i fertig, weiter."
  sleep 2
done

echo ""
echo "Ralph hat die Höchstzahl ($MAX_ITERATIONS) erreicht, ohne alle Aufgaben zu erledigen."
echo "Stand in $PROGRESS_FILE prüfen."
exit 1
