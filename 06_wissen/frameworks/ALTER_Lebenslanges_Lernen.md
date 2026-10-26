# ALTER, lebenslanges Lernen im Hub

| Feld | Wert |
|---|---|
| Status | In trial |
| Testprojekt | das erste Lernprojekt unter `03_projekte/`, Start mit `/alter`, sobald ein Modul geplant ist |
| Angelegt | |
| Zuletzt geprüft | |
| Quellen | Swadia, zwei Videos (2026), Brown, Roediger, McDaniel, *Make It Stick* (2014), Betriebsregeln aus der Sprachlernpraxis (Nation, Lewis, Corder). Details in Abschnitt 6 |

## 1. Kernidee

Berufsbegleitendes Lernen scheitert selten am Stoff. Es scheitert daran,
dass Planung, Quellen, Verstehen, Behalten und Vorzeigen an niemandem hängen
und deshalb im Alltag wegfallen. ALTER verteilt diese Aufgaben auf fünf
Rollen (Advisor, Librarian, Tutor, Editor, Roommate), und der Hub gibt jeder
Rolle einen festen Ort und ein Werkzeug. Der tragende Gedanke kommt aus der
Lernforschung. Gelernt wird durch Abruf aus dem Gedächtnis, verteilt über
die Zeit und gemischt, also durch Anstrengung, die sich langsam anfühlt.
Die neun Grundsätze (`01_kompass/lerngrundsaetze.md`) sorgen dafür, dass
dieses System mit einem festen Wochenbudget dauerhaft läuft und bei
Unterbrechungen nicht zusammenbricht. Das Budget steht unter `lernen` in
`00_kern/einstellungen.json` (Vorschlag 5 h Deep Dive je Woche und 20 Min.
Wiederholung je Tag).

## 2. Wann anwenden und wann nicht

- **Anwenden bei** einem Lernprojekt im Hub mit Ziel über mehrere Monate,
  bei dem Können am Ende nachgewiesen werden soll (Mathematik, ML, Sprache,
  Finanzen). Ebenso bei Lernstoff, der aus einem Ast zurückfließt (Lernkarte
  aus der Arbeit).
- **Nicht anwenden bei** einer einmaligen Frage, die ein Nachschlagen
  beantwortet, bei einem Anliegen, dessen Ziel ein Ergebnis im eigenen Leben
  ist (Steuer, Kochbuch), und bei Wissen, das nur für eine Woche gebraucht
  wird. Dort ist die Wiederholungslast teurer als der Nutzen.

## 3. Das Modell

Die Lernschleife des Hub und die Rolle an jeder Station.

`01_kompass → 02_bibliothek → 03_projekte (und Äste) → 04_gedaechtnis → 05_werkstatt → 06_wissen → 01_kompass`

| Rolle | Leitfrage | Ort im Hub | Werkzeug | Grundsätze | Evidenz |
|---|---|---|---|---|---|
| Advisor | Was lerne ich als Nächstes, was lasse ich weg, wie viel Zeit habe ich? | `01_kompass/` | `/advisor`, Studienplan | 3, 4, 5 | Swadia V1 4:45 (fünf Entscheidungen), Budget als Setzung in `00_kern/einstellungen.json` |
| Librarian | Welches Werk und welches Kapitel tragen den Block? | `02_bibliothek/` | Literatur-Index, `literature-scout`, `/add-literature` | 7 | Swadia V1 9:39 (Regal aus wenigen Quellen), V2 0:25 (drei Tore) |
| Tutor, Verstehen | Habe ich es verstanden oder nur wiedererkannt? | Lernprojekt | `/tutor` mit `sokrates`, `feynman`, `test` | 6 | Swadia V1 14:02, MIS Kap. 4 (erwünschte Schwierigkeiten, Generierung), Kap. 5 (Illusion des Wissens, Kalibrierung) |
| Tutor, Behalten | Kann ich es in drei Monaten noch abrufen? | `04_gedaechtnis/` | SM-2-Engine, `/heute` | 2, 3, 4, 5 | MIS Kap. 2 (Abruf), Kap. 3 (Verteilen und Mischen) |
| Editor | Hält mein Ergebnis einer fremden Prüfung stand? | `05_werkstatt/` | `/editor`, Transcript | 6 | Swadia V1 16:44, MIS Kap. 8 (Reflexion, Kalibrierung) |
| Roommate | Womit aus einem fernen Fach hängt das zusammen? | `06_wissen/verbindungen/` | `/roommate`, monatlich | 1 | Swadia V1 18:34, MIS Kap. 8 (Elaboration) |

V1 und V2 sind die beiden Videos von Swadia mit Zeitmarke, MIS ist Make It
Stick (Abschnitt 6).

Querschnitt, gilt für alle Rollen. Der volle Wortlaut der Grundsätze steht
in `01_kompass/lerngrundsaetze.md`.

| Grundsatz | Wirkung im Modell |
|---|---|
| 1 Jede Erfahrung ist Lernstoff | Äste melden über drei feste Wege zurück (Lernkarte, Framework-Beförderung, Case Study) |
| 2 Ein Gedächtnis für alle Quellen | Eine Wiederholungsschlange über alle Lernprojekte. Ein Lernprojekt mit eigener Engine steht im Studienplan als ausgenommen |
| 3 Zufluss nach Wiederholungslast | Neue Karten nur, wenn die fälligen Wiederholungen des Tages ins Budget passen |
| 4 Minimalbetrieb statt Abbruch | Schalter auf 10 Min. nur Wiederholung |
| 5 Kein Schuldaufbau | Keine Rückstandszahl, Plan als Blockliste mit Obergrenzen statt Kalender |
| 6 Jeder Block endet mit Nachweis | Prüfung ohne System plus Artefakt im Transcript |
| 7 Werk und Kapitel | Jede Karte und jede Bewertung trägt das Feld `quelle` |
| 8 Arbeitsdaten bleiben im Ast | Kern im Hub, Übung in der Spur des Asts (siehe `00_kern/einstellungen.json`), öffentliche Daten (Spur Ö) nur als Ersatz, Rückfluss nur anonymisiert |
| 9 Keine Lektüre ohne Arbeitspaket | Ein Kern-Abschnitt wird erst zu Beginn des zugehörigen Arbeitspakets gelesen, in dem er angewendet wird. Der Lesepfad hängt am Arbeitsplan, nicht an einer Kapitelliste (Kern-Regeln, Abschnitt 3) |

## 4. Anwendung

Je Lernprojekt, im Raum sind der Nutzer und Claude.

1. **Ziel klären (Advisor).** Input sind Kompetenzprofil
   (`01_kompass/entwicklung/profil.md`) und Wochenbudget. `/advisor` fragt
   genau fünf Entscheidungen ab (Ziel, Ausgangslage, Reihenfolge, Cut List,
   Meilensteine). Artefakt ist der Abschnitt des Durchlaufs in `modul.md` des
   Modulordners unter `01_kompass/module/`.
2. **Quelle wählen (Librarian).** Input ist der nächste Block. Ergebnis ist
   ein Werk mit Kapiteln aus dem Index, höchstens drei bis vier Quellen je
   Block. Fehlt ein Werk, beschafft es der Nutzer. Ein neues Werk muss
   vorher eines der drei Tore passieren (ändert es, wie ich denke, greift es
   eine Überzeugung an, verhindert es einen selbstsicheren Fehler). Artefakt
   ist der Blockeintrag im `lernlog.md` mit Quelle.
3. **Block erarbeiten (Tutor, Verstehen).** Input ist das Kapitel. Vor dem
   Lesen eine Frage zu beantworten versuchen (Generierung), beim Arbeiten
   `sokrates`. Artefakt sind eigene Notizen und gelöste Aufgaben.
4. **Block abschließen (Tutor, Verstehen).** Vor dem Test schätzt der
   Nutzer seine Zuversicht je Frage (0 bis 100 %), danach wird sie gegen das
   Ergebnis gehalten (Kalibrierung). `feynman` bewertet die eigene Erklärung
   gegen das Kapitel, gerichtet an einen Fachfremden, denn wo er stocken
   würde, liegt die Lücke. `test` stellt Fragen aus dem Lehrplan. Lücken
   werden zu Karten, Ausrutscher nicht. Artefakt sind neue Karten mit
   `quelle` und eine Bewertung samt Kalibrierung im `lernlog.md`.
5. **Behalten (Tutor, Behalten).** Täglich `/heute`, 15 bis 30 Min. über alle
   Projekte, gemischt. Zielkorridor 60 bis 70 % Trefferquote. Artefakt ist der
   Lernzustand in `04_gedaechtnis/`.
6. **Nachweisen (Editor).** Am Blockende eine Prüfung ohne System, das
   Artefakt (Erklärung, Code, Analyse) prüft `/editor` auf Logik, Schwächen
   im Argument, Wiederholung, Struktur und Präzision. Der Nutzer bleibt Autor
   und entscheidet über jede Änderung. Artefakt ist ein Eintrag in
   `05_werkstatt/transcript.md`.
7. **Verbinden (Roommate).** Monatlich ein laufendes Thema mit einem fernen
   Fach verknüpfen. Artefakt ist eine Notiz in `06_wissen/verbindungen/`,
   eine tragfähige Idee wird Framework-Kandidat.
8. **Steuern (Advisor).** Wöchentlich Ist-Stunden, Abrufquote und Rückstau
   gegen Budget, je Trimester ein Review. Artefakt ist der aktualisierte
   Studienplan `01_kompass/studienplan/studienplan.md`.

**Automatischer Ablauf.** Statt die Schritte einzeln aufzurufen, tippt der
Nutzer `/alter`. Das Skript `04_gedaechtnis/alter.py` wählt aus Karten,
Modulplan und Verlauf genau eine nächste Tätigkeit, das Modell entscheidet
nicht selbst. Die Regeln gelten in dieser Reihenfolge, die erste zutreffende
gewinnt.

| Regel | Auslöser | Tätigkeit |
|---|---|---|
| 1 | Fällige Karten, heute noch kein `/heute` | Behalten |
| 2 | Problemkarte, zweimal in Folge unter Note 3 | Tutor `sokrates` am Abschnitt |
| 3 | Illusion des Wissens, zwei falsche Abrufe mit Zuversicht ab 70 % in 14 Tagen | Tutor `feynman` |
| 4 | Abschnitt sitzt (mindestens drei Karten, alle ab 21 Tagen Intervall) | Tutor `feynman` mit Abstand, danach Editor |
| 5 | Begonnener Block | nächster Schritt des Blocks |
| 6 | Meilenstein fällig | Erklär-Check über die Abschnitte |
| 7 | Nächster Block nach Termin, Spur-Blöcke warten auf den gelesenen Kern-Block | Block beginnen |
| 8 | Alles erledigt oder noch kein Modul geplant | Advisor plant den nächsten Durchlauf, ohne Modul zuerst `/aufnahme` oder `/advisor` |

Die Schwellen der Regeln 2 bis 4 sind Setzungen (Last Validated in
`04_gedaechtnis/methodik.md`) und werden in den ersten Wochen am eigenen
Verlauf geprüft. Die Regel 3 stützt sich auf Make It Stick, Kap. 5, Regel 4
auf Kap. 3.

## 5. Eigene Anpassung

- **Bibliothek statt NotebookLM.** Swadia bindet die KI an ein Regal aus
  wenigen Quellen in NotebookLM (V1 9:39). Der Hub hat dieses Regal in
  `02_bibliothek/` mit Index und Kapitelangaben, der `literature-scout` liest
  nur dort. Die drei Tore aus V2 werden zur Eintrittsprüfung für neue Werke.
- **Kalibrierung als Brücke.** Das Entscheidungsjournal aus V2 (Zuversicht in
  Prozent, später gegen das Ergebnis gehalten) und die Kalibrierung aus MIS
  Kap. 5 meinen dasselbe. Beides zusammen wird zur Zuversichtsschätzung vor
  jedem Blocktest (Schritt 4).
- **Nicht übernommen aus Swadia.** Den Plan per Zapier in Kalender und
  Erinnerungen zu schreiben (V1 7:25, gesponsert) widerspricht Grundsatz 5,
  der Plan bleibt eine Blockliste mit Obergrenzen. Podcasts aus NotebookLM
  zählen nur als Input, nie als Lernen, weil Zuhören wie Wiederlesen
  Vertrautheit ohne Abruf erzeugt (MIS Kap. 1).
- **Tutor geteilt.** Swadia führt einen Tutor. Hier gibt es zwei Aufgaben
  mit verschiedenen Werkzeugen, Verstehen im Gespräch und Behalten in einer
  deterministischen Engine. Grund ist, dass Make It Stick Abruf und
  Verteilen als eigene Wirkung belegt (Kap. 2 und 3), die ein Gespräch allein
  nicht leistet. Das Intervall rechnet Python, nie das Modell.
- **Ein Gedächtnis statt vieler.** Alle Projekte teilen eine Schlange, damit
  das Mischen aus Kap. 3 von selbst entsteht und die Tageslast an einer Stelle
  begrenzt werden kann.
- **Betriebsregeln aus der Sprachlernpraxis.** Kein Schuldaufbau, Blockliste
  statt Kalender, Korridor 60 bis 70 % Trefferquote und Prüfung ohne System je
  Abschnitt sind Regeln, wie sie beim täglichen Sprachenlernen mit
  Karteikasten üblich sind. Neu ist, dass der Zufluss neuer Karten an der
  Wiederholungslast hängt (Grundsatz 3).
- **Fehler gegen Ausrutscher (nach Corder).** Nur echte Wissenslücken kommen
  in die Schlange, sonst verstopft sie. Die Unterscheidung stammt aus der
  Fehleranalyse beim Sprachenlernen und wird hier auf alle Fächer übertragen.
- **Karten als Zusammenhang (nach Lewis).** Im Sprachenlernen werden Chunks
  statt Einzelwörter gelernt. Übertragen heißt das, Karten fragen nach
  Anwendung und Rechnung und nicht nur nach Begriffen (Kartentypen Begriff,
  Anwendung, Rechnung).
- **Vier Stränge als Hypothese (nach Nation).** Für Sprache verteilt Nation
  die Zeit auf Input, Output, Sprachtraining und Flüssigkeit. Für ein Fach
  wie ML lautet die ungeprüfte Übertragung Lesen, eigenes Anwenden an Daten,
  Abruf und Rechnen unter Zeit. Der erste Lauf prüft, ob das trägt.
- **Keine Lerntypen.** Make It Stick findet keinen Beleg dafür, Unterricht an
  einen bevorzugten Lernstil anzupassen (Kap. 6). Das System richtet Formate
  deshalb nach dem Stoff aus.

## 6. Quellen

| Werk | Kapitel oder Abschnitt | Beitrag |
|---|---|---|
| Swadia, „Harvard in a Box“ (YouTube, 2026) | 2:41 bis 18:34, je Rolle ein Kapitel | die fünf Rollen, fünf Entscheidungen des Advisors, Regal aus wenigen Quellen, Tutor gegen vorgetäuschtes Verständnis, Prüfkriterien des Editors, Breite durch den Roommate |
| Swadia, „The Only 7 Books You Need to Educate Yourself Like the Top 1%“ (YouTube, 2026) | 0:25 (drei Tore), 5:23 (Erklären vor Fachfremden), 8:26 (Entscheidungsjournal) | Eintrittsprüfung für Werke, Feynman an Fachfremde gerichtet, Zuversichtsschätzung |
| Brown, Roediger, McDaniel, *Make It Stick* (2014) | Kap. 1 (S. 1) | Wiederlesen und massiertes Üben erzeugen Vertrautheit, keine Beherrschung |
| dito | Kap. 2 (S. 23) | Abruf als Lernhandlung, Feedback nach dem Abruf |
| dito | Kap. 3 (S. 46) | Verteilen, Mischen, Variieren der Übung |
| dito | Kap. 4 (S. 67) | erwünschte Schwierigkeiten, Generierung vor der Lösung |
| dito | Kap. 5 (S. 102) | Illusion des Wissens, Kalibrierung durch Tests |
| dito | Kap. 6 (S. 131) | keine Evidenz für Lerntypen, Struktur aufbauen, dynamisches Testen |
| dito | Kap. 7 (S. 162) | Wachstumsdenken, gezieltes Üben, Mnemotechniken |
| dito | Kap. 8 (S. 200) | Praxisregeln für Lernende und lebenslang Lernende, Elaboration, Reflexion |
| Nation, Four Strands; Lewis, Lexical Approach; Corder, Fehler gegen Ausrutscher | nur aus zweiter Hand, Werke nicht in der Bibliothek | siehe Abschnitt 5 |

Notizen zu den Videos und Make It Stick gehören, sobald erfasst, in
`02_bibliothek/` und in den Literatur-Index.

## 7. Erprobungslog

Ein Eintrag je Anwendung, neuester oben. Der erste Lauf beginnt mit `/alter`,
sobald ein Modul mit `/advisor` geplant ist. Ausgewertet wird nach vier
Wochen gegen die Schwellen in `04_gedaechtnis/methodik.md`.

| Datum | Projekt | Was funktioniert hat | Was sich ändern musste |
|---|---|---|---|
| | | | |

## 8. Grenzen und offene Fragen

- Die Videos von Swadia sind praxisnahe Empfehlungen, keine Forschung. Ihre
  Zahlen (88 % Abbruch offener Kurse, Blooms Zwei-Sigma-Befund, Stanford-Studie)
  sind nicht gegen die Primärquellen geprüft und tragen hier keine Aussage.
- Nation, Lewis und Corder kommen nur aus zweiter Hand. Die Werke selbst
  sind nicht gelesen und stehen nicht in der Bibliothek.
- Make It Stick ist eine Zusammenfassung der Forschung für ein breites
  Publikum. Die Primärstudien in den Anmerkungen sind nicht geprüft.
- Die Übertragung der vier Stränge auf andere Fächer ist eine Hypothese.
- Der Korridor 60 bis 70 % ist eine Setzung aus der Sprachlernpraxis, kein
  Wert aus der Literatur.
- Teilen sich mehrere Lernprojekte das Wochenbudget, entscheidet der
  Studienplan über die Verteilung. Ein Lernprojekt mit eigener Engine kann
  dort ausgenommen werden, seine Zeit zählt dann nicht in `/heute`.
- Ob die Teilung des Tutors (Verstehen im Gespräch, Behalten in der Engine)
  im Alltag hält, zeigt erst der erste Lauf.

## 9. Interview-Pitch

Bleibt leer, solange der Status „In trial“ ist.
