# Beispielmodule

Drei vollständig ausgearbeitete Module als Muster. Sie zeigen, wie Plan,
Kern-Lesepfad und Register eines Moduls aussehen, und verweisen auf Werke aus
der mitgelieferten Bibliothek. `/alter` zählt sie nicht als eigene Module,
solange sie in diesem Ordner liegen.

| Beispiel | Kompetenzfeld | Kern-Lesepfad |
|---|---|---|
| [BE2_bewerbungsgespraech](BE2_bewerbungsgespraech/modul.md) | Bewerbungsgespräch und Fachinterview, dazu Arbeitshilfen zu MECE, Pyramidenprinzip und SCQA | Rolle des Beraters, Selbstvorstellung, Antworten strukturieren, Lücken erzählen |
| [DK1_python_softwarehandwerk](DK1_python_softwarehandwerk/modul.md) | Python und Softwarehandwerk | Code schreiben, lesen, testen, bereitstellen |
| [DK2_datenplattform](DK2_datenplattform/modul.md) | Datenplattform und Datenmodellierung | Fakten und Dimensionen, Granularität, Historisierung, Ingestion, Datenqualität |

## Übernehmen

1. Ordner nach `01_kompass/module/` kopieren.
2. ID an das eigene Bereichskürzel anpassen (Ordnername, IDs im Lesepfad,
   Kopf von `modul.md`), Bereiche stehen in `00_kern/einstellungen.json`.
3. Mit `/advisor <ID>` den ersten Durchlauf planen. Der Advisor übernimmt den
   Kern, setzt Termine nach dem eigenen Budget und schreibt die Spurblöcke für
   die eigenen Äste neu.
4. Zeile in `01_kompass/module/README.md` und im Studienplan ergänzen.
