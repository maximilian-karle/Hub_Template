# BE2 Bewerbungsgespräch und Fachinterview

> **Beispiel.** Dieses Modul ist ein ausgearbeitetes Muster und wird von
> `/alter` nicht gelesen, solange es unter `_beispiele/` liegt. Zum Übernehmen
> den Ordner nach `01_kompass/module/` kopieren, die ID `BE2` (im Ordnernamen,
> im Titel und in den Abschnitts-IDs `BE2-Knn` des Lesepfads) an ein eigenes
> Bereichskürzel aus `00_kern/einstellungen.json` anpassen und mit `/advisor`
> den ersten Durchlauf planen. Der Kern-Lesepfad bleibt, der Durchlauf unten
> zeigt nur, wie ein geplanter Durchlauf aussieht, und wird ersetzt.

| Feld | Wert |
|---|---|
| Bereich | `<Kürzel>` <Bereich aus dem eigenen Kompetenzprofil>, im Beispiel BE für Beratung |
| Lernziel | <Lernziel aus profil.md> |
| Erster Durchlauf | <Trimester>, seit <TT.MM.JJJJ> |
| Kern-Lesepfad | [lesepfad.md](lesepfad.md), BE2-K00 bis BE2-K07 |
| Projekte | [projekte.md](projekte.md) |
| Lernprojekt | `03_projekte/<kurzname>/`, Lernlog dort |

Das Modul ist ein Kompetenzfeld. Es läuft über das erste Trimester hinaus
weiter, jede beworbene Stelle mit Gespräch kommt als Projekt hierher, nutzt
den Kern-Lesepfad und hinterlässt eine Case Study im Register. Der Kern
trägt, was für jedes Gespräch gleich bleibt (Rolle des Beraters,
Selbstvorstellung, Antworten strukturieren, Lücken ehrlich erzählen, KI in
der Beratung). Fachlich Stellenspezifisches steht im Lesepfad des Projekts.
Ein Durchlauf ist ein Abschnitt dieser Datei, geplant mit `/advisor`,
neuester unten. Die vertiefte Fallmethodik für Case-Interviews gehört in ein
eigenes Modul, hier steht nur das Mindestniveau für das Gespräch.

## Durchlauf 1 (<Trimester>, 26 h)

Stand <TT.MM.JJJJ>, geplant mit /advisor. Spur A ist die Bewerbung auf eine
Stelle in der Beratung, geführt als Lernprojekt im Hub, weil eine Bewerbung
nicht in den Arbeits-Ast gehört. Belege aus der Arbeit kommen nur
anonymisiert ins Briefing. Spur Ö sind Übungsfälle aus den Casebooks der
Bibliothek. Spur U entfällt im Beispiel, ein Gegenstück wäre ein Pitch oder
Erstgespräch mit einem Kunden des eigenen Unternehmens. Alle Termine sind
Obergrenzen, gearbeitet wird so schnell wie möglich.

**Ziel.** Am Ende kann ich mich in 90 Sekunden schlüssig vorstellen, fünf
Belege nach dem STAR-Muster frei erzählen, meine größten Lücken laut Anzeige
in je einer ehrlichen Antwort mit Lernpfad benennen und die Fachthemen der
Stelle so erklären, dass ein Manager aus dem Fachbereich folgt. Dazu löse ich
drei Übungsfälle laut mit Struktur in der ersten Minute und einer Empfehlung
zuerst.

**Ausgangslage.** Lebenslauf und Abgleich von Anzeige und Lebenslauf liegen
vor, ein geübtes Gespräch nicht. Die Theorie beginnt bei null. Probefragen
<n>, davon richtig <k>, Zuversicht im Mittel <x> %, Treffer <y> %. Die
Bibliothek hat nichts zu den Fachthemen der Stelle, wenn diese sehr speziell
sind (Lücke im Lesepfad des Projekts).

**Reihenfolge.** Der Kern liest die Abschnitte des Kern-Lesepfads
[lesepfad.md](lesepfad.md), das Projekt zieht jeden Schritt am Gespräch
nach. Das Briefing und die Karten entstehen im Projekt.

| Block | spätestens | Inhalt | Quelle | Spur | h max | Nachweis |
|---|---|---|---|---|---|---|
| K1 | <TT.MM.JJJJ> | Rolle des Beraters, Guidelines | BE2-K00, BE2-K01, Aichele/Schönberger Kap. 1, 6 | Kern | 3 | Kontrollfragen |
| K2 | <TT.MM.JJJJ> | Selbstvorstellung, Antworten strukturieren | BE2-K02, BE2-K03, Aichele/Schönberger Kap. 8.12, Methodenkoffer | Kern | 3 | 90-Sekunden-Vorstellung gesprochen |
| K3 | <TT.MM.JJJJ> | Beraterprofil und Lücken erzählen | BE2-K04, Bodenstein u. a. Kap. 2.3, 2.4 | Kern | 2 | Lückenantwort gesprochen |
| K4 | <TT.MM.JJJJ> | Berater und Kunde | BE2-K05, Bodenstein u. a. Kap. 3 | Kern | 1,5 | Kontrollfragen |
| K5 | <TT.MM.JJJJ> | KI in der Beratung | BE2-K06, Arica/Freye Kap. 5, 6 | Kern | 1,5 | Kontrollfragen |
| K6 | <TT.MM.JJJJ> | Wiederholung der Karten, Erklär-Check | alle K | Kern | 1 | Erklär-Check G1 |
| A1 | <TT.MM.JJJJ> | Anzeige, Firma und Rolle lesen, Briefing anlegen, Selbstvorstellung und fünf STAR-Belege | wie K2, K3, dazu Stellenanzeige | A | 4 | Briefing Teil 1, Belege gesprochen |
| A2 | <TT.MM.JJJJ> | Antworten auf Lücken und Motivfragen, Fachthemen der Stelle, zwei Probegespräche mit Claude als Interviewer | wie K3, K4, dazu Projektlesepfad | A | 6 | Probegespräch 2 mit Rückmeldung |
| Ö1 | <TT.MM.JJJJ> | Case-Training, drei Übungsfälle laut lösen, mit Tutor und Editor durchgearbeitet | BE2-K07, MIT-Casebook Kap. 1, 2.3, Accenture-Workbook | Ö | 4 | drei Fälle gelöst, Raster erfüllt |

Summe Kern 12 h (3 + 3 + 2 + 1,5 + 1,5 + 1), Spur A 10 h (4 + 6), Spur Ö
4 h, zusammen 26 h. Die Lesezeit von BE2-K07 liegt in Ö1. Die Stunden sind
Richtwerte, die Zeiten der Spur A sind Bewerbungsarbeit und laufen privat,
nicht in der Arbeitszeit.

**Cut List.** Weg fallen Aichele/Schönberger Kap. 2 bis 5 (Akquise und
Projektsteuerung, späteres Modul zur Projektarbeit), Kap. 8.2 bis 8.11
(Methodenkompendium, späteres Methodenmodul) und Bodenstein u. a. Kap. 4 bis
15. Die vertiefte Fallmethodik steht in einem eigenen Modul, hier nur das
Mindestniveau für das Gespräch. Liegt das Fachinterview deutlich nach dem
ersten Gespräch, rückt der Fachteil von A2 dahinter. Im Minimalbetrieb fällt
zuerst Ö1 weg, dann der Fachteil von A2, dann schrumpft A2 auf die
Lückenantworten.

**Meilensteine.**

| spätestens | Output | Prüfung |
|---|---|---|
| G1, <TT.MM.JJJJ> | Kern gelesen, Selbstvorstellung, STAR-Belege und Lückenantworten stehen | Erklär-Check G1 (BE2-K00 bis BE2-K06), Probefragen richtig |
| G2, <TT.MM.JJJJ> | Fachantworten, drei Übungsfälle, zwei Probegespräche | Erklär-Check G2, Probegespräch 2 mit Rückmeldung |
| Gespräch, <TT.MM.JJJJ> | erstes Gespräch geführt | Nachbereitung im Lernlog innerhalb von zwei Tagen |
| Abschluss | nach dem letzten Gespräch oder der Absage | Case Study A (anonymisiert), Prüfung ohne System mit zehn Fragen (bestanden ab 8) |

**Annahmen.** Last Validated <TT.MM.JJJJ>. Stunden sind Obergrenzen und
geschätzt, nach dem Gespräch werden sie durch die Ist-Stunden ersetzt. In
vielen Beratungen prüft das erste Gespräch Personal Fit und Soft Skills mit
einem Manager aus dem Fachbereich, das zweite den technischen Fit. Das wird
beim Recruiting erfragt und als Angabe geführt, solange es nicht schriftlich
bestätigt ist. Führt den ersten Termin der Fachbereich, wird die Technik
schon dafür vorbereitet. Arbeitsdaten bleiben im Arbeits-Ast, das Briefing
nennt nur anonymisierte Belege.

**Offen.** Prüfungen stehen im Lernlog, Nachweise im Transcript
(`05_werkstatt/transcript.md`), die Karten liegen in `04_gedaechtnis/`.
Welche Tätigkeit als Nächstes dran ist, entscheidet `/alter`. Offen ist,
was aus gesperrten oder vertraulichen Arbeiten im Gespräch gesagt werden
darf, und ob ein Bewerbungsprojekt eine Case Study in der üblichen Form
hinterlässt.
