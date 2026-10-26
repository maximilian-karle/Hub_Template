# Module

Ein Modul ist ein Kompetenzfeld aus dem Studienplan. Es startet in einem
Trimester (erster Durchlauf) und läuft danach weiter. Jede neue Aufgabe aus
einem Ast, die zum Modul passt, kommt als Projekt hierher, nutzt denselben
Kern-Lesepfad und hinterlässt eine Case Study. Am Ende belegt das Register,
wie oft eine Fähigkeit angewendet wurde.

Je Modul ein Ordner `<ID>_<kurzname>/` mit drei Dateien. Die ID ist das
Bereichskürzel aus dem Kompetenzprofil plus laufende Nummer (Liste in
`00_kern/einstellungen.json` unter `profil.bereiche`).

| Datei | Inhalt | wer schreibt |
|---|---|---|
| `modul.md` | Kopf, je Durchlauf Ziel, Ausgangslage, Reihenfolge, Cut List, Meilensteine, Blocktabelle | `/advisor` |
| `lesepfad.md` | Kern-Lesepfad mit IDs `<ID>-K00` und folgende, für alle Projekte gleich, Vorlage `07_handwerk/project_scaffold/00_Charter/Lesepfad.md` | `/aufnahme`, `/advisor`, wächst mit jedem Projekt |
| `projekte.md` | Register der Projekte mit Ast, Spur, Ort, Gate, Case Study, Prüfung | `/aufnahme`, `/new-project` (Status), Gate-Abschluss |

Durch ein laufendes Modul führt `/alter`. Der Befehl liest `modul.md` und
`lesepfad.md` und wählt den nächsten Block und Schritt.

Neue Aufgaben beginnen mit `/aufnahme`. Gibt es das Modul schon, kommt das
Projekt ins Register. Ist es nur im Studienplan geplant, wird es sofort mit
`/advisor` ausgearbeitet. Passt keines, wird eines im Gespräch entwickelt.

| Modul | Bereich | erster Durchlauf | Projekte | Case Studies |
|---|---|---|---|---|
