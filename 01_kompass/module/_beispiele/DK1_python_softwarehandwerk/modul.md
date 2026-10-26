# DK1 Python und Softwarehandwerk

> **Beispiel.** Dieses Modul ist ein ausgearbeitetes Muster und gehört
> niemandem. So übernimmst du es.
> 1. Den Ordner `DK1_python_softwarehandwerk/` nach `01_kompass/module/`
>    kopieren (eine Ebene höher, sonst sieht `/alter` ihn nicht).
> 2. Die ID an dein eigenes Bereichskürzel aus `01_kompass/entwicklung/profil.md`
>    anpassen, im Ordnernamen, im Titel und in allen IDs `DK1-Knn` im
>    Lesepfad. Verweise auf andere Module (`DK2`, `DK3` usw.) zeigen auf
>    Module eines Musterplans und werden durch deine eigenen ersetzt oder
>    gestrichen.
> 3. Mit `/advisor` den ersten Durchlauf planen. Ziel, Ausgangslage,
>    Termine und Spuren unten sind Beispiele, der Advisor ersetzt sie im
>    Interview durch deine. Alle Platzhalter `<...>` müssen vor dem ersten
>    `/alter` gefüllt sein, Termine im Format TT.MM.JJJJ.

| Feld | Wert |
|---|---|
| Bereich | `<Kürzel> <Bereich aus dem eigenen Kompetenzprofil>`, im Muster DK Daten und KI (Kürzel und Name aus `profil.md` übernehmen) |
| Lernziel | `<Lernziel aus profil.md>` |
| Erster Durchlauf | `<Trimester>`, seit `<TT.MM.JJJJ>` |
| Kern-Lesepfad | [lesepfad.md](lesepfad.md), DK1-K01 bis DK1-K08 |
| Projekte | [projekte.md](projekte.md) |
| Lernprojekt | `03_projekte/<kurzname>/`, Lernlog dort |

Das Modul ist ein Kompetenzfeld. Es läuft über den ersten Durchlauf hinaus
weiter, jedes Projekt, in dem Code selbst geschrieben, gelesen oder als
Dienst bereitgestellt wird, kommt hierher, nutzt den Kern-Lesepfad und
hinterlässt eine Case Study im Register. Ein Durchlauf ist ein Abschnitt
dieser Datei, geplant mit `/advisor`, neuester unten.

## Durchlauf 1 (`<Trimester>`, 26 h)

Stand `<TT.MM.JJJJ>`, geplant mit /advisor. Spuren A Bestandscode verstehen
im Arbeits-Ast (ein bestehendes Skript oder Modul, Wahl in der ersten
Modulwoche), U kleiner Datendienst im Unternehmens-Ast. Alle Termine sind
Obergrenzen, gearbeitet wird so schnell wie möglich.

**Ziel.** Am Ende schreibe, teste und debugge ich ohne KI-Assistenz ein
kleines Python-Programm mit Funktionen, Datenstrukturen, einer Klasse und
Tests mit pytest. Code, den Claude gebaut hat, erkläre ich Zeile für Zeile
und ändere ihn gefahrlos, nachdem ich sein Verhalten mit Characterization
Tests festgeschrieben habe. Ich arbeite mit Git über Branch, Merge und einen
selbst gelösten Konflikt und schreibe SQL-Abfragen mit Joins und Gruppierung
ohne Vorlage. Ich rufe eine REST-API auf, stelle selbst einen Endpunkt mit
API-Key bereit und erkläre Authentifizierung mit Schlüssel und Token. Ich baue
einen LLM-Aufruf mit Structured Output und einem Tool als Brücke zu einem
späteren Modul über Sprachmodelle. Ohne dieses Fundament bleibt jedes
spätere Modell ein Werk von Claude.

**Ausgangslage.** Beispiel einer typischen Ausgangslage. Python und Git
laufen produktiv, aber weitgehend über Claude. Ohne KI beginnen Python und
SQL bei null, es fehlen Grundbegriffe (Funktion, Parameter, Standardwert),
das Nachverfolgen von Code sowie Joins und Gruppieren. Git sitzt im Kern,
die Folgen eines Push sind aber nicht benannt. Probefragen `<n>`, davon
richtig `<k>`, Zuversicht im Mittel `<x>` %, Treffer `<y>` %.

**Reihenfolge.** Der Kern geht von Python über Softwarehandwerk (Tests,
fremder Code, Git, SQL, Dienste) bis zum ersten LLM-Aufruf und liest die
Abschnitte des Kern-Lesepfads [lesepfad.md](lesepfad.md). Jeder Kernblock
wird möglichst am selben Abend in Spur U oder A nachgezogen.

| Block | spätestens | Inhalt | Quelle | Spur | h max | Nachweis |
|---|---|---|---|---|---|---|
| K1 | <TT.MM.JJJJ> | Variablen, Typen, Funktionen, Parameter, Rückgabe, Code nachverfolgen | DK1-K01, ISLP Kap. 2.3.1, 2.3.2, 2.3.5, 2.3.8, Python-Lehrbuch offen | Kern | 3 | Probefrage 1 richtig, fünf Aufgaben zum Nachverfolgen |
| K2 | <TT.MM.JJJJ> | Listen, Dictionaries, Sets, NumPy, Daten laden und indizieren | DK1-K02, ISLP Kap. 2.3.3, 2.3.6, 2.3.7 | Kern | 2 | Übungen ohne KI |
| K3 | <TT.MM.JJJJ> | Klassen, Module, Fehlerbehandlung, Debugging, pytest | DK1-K03, Feathers Kap. 2, Python-Lehrbuch offen | Kern | 2,5 | Programm mit Klasse und drei Tests ohne KI |
| K4 | <TT.MM.JJJJ> | fremden Code verstehen, Characterization Tests | DK1-K04, Feathers Kap. 13, 16, 19 | Kern | 2 | Kontrollfragen |
| K5 | <TT.MM.JJJJ> | relationales Modell, Joins, Gruppieren, HAVING | DK1-K05, Kleppmann Kap. 2, SQL-Übungswerk offen | Kern | 2 | Probefrage 2 richtig |
| K6 | <TT.MM.JJJJ> | Commit, Branch, Merge, Konflikt, Remote | DK1-K06, Git-Werk offen | Kern | 1 | Probefrage 3 vollständig |
| K7 | <TT.MM.JJJJ> | HTTP, REST, Authentifizierung mit API-Key und Token | DK1-K07, Kleppmann Kap. 4 (Modes of Dataflow), Werk zu Authentifizierung offen | Kern | 1,5 | Kontrollfragen |
| K8 | <TT.MM.JJJJ> | LLM-Aufruf mit Structured Output und Tool | DK1-K08, Alammar/Grootendorst Kap. 6 (Output Verification), Kap. 7 (Agents) | Kern | 1 | Kontrollfragen |
| U1 | <TT.MM.JJJJ> | kleine Datenstrecke im Unternehmens-Ast von Hand geschrieben (laden, prüfen, speichern) | wie K1 bis K3 | U | 2 | Tests grün, ohne KI geschrieben, Zeile für Zeile erklärt |
| U2 | <TT.MM.JJJJ> | Kennzahl aus den eigenen Daten mit SQL abfragen und als REST-Endpunkt mit API-Key bereitstellen | wie K5, K7 | U | 3 | Abfrage ohne Vorlage, Aufruf mit und ohne Schlüssel getestet |
| U3 | <TT.MM.JJJJ> | Case Study U | | U | 1 | Case Study |
| A1 | <TT.MM.JJJJ> | bestehendes Skript im Arbeits-Ast wählen, Verhalten mit Characterization Tests festschreiben, eigene Änderung über Branch und Merge | wie K4, K6 | A | 3,5 | Tests grün, Merge ohne KI, Erklär-Check |
| A2 | <TT.MM.JJJJ> | Case Study A, anonymisiert | | A | 1,5 | Case Study |

Summe Kern 15 h (3 + 2 + 2,5 + 2 + 2 + 1 + 1,5 + 1), Spur U 6 h (2 + 3 + 1),
Spur A 5 h (3,5 + 1,5), zusammen 26 h.

**Cut List.** Weg fallen Python-Vertiefungen wie Decorators, Generatoren,
async und strenge Typisierung (bei Bedarf in einem späteren Modul zu
Machine Learning oder Datenplattformen), ISLP Kap. 2.3.4 und 2.3.9
(Statistikmodul), Feathers Teil III und Kap. 5, Kleppmann Kap. 5 bis 9
(Datenplattformen), OAuth-Abläufe im Detail, Docker, CI/CD und Cloud,
Agentenschleife und Chains aus Alammar/Grootendorst Kap. 7 und RAG (beides
späteres Modul über Sprachmodelle). Im Minimalbetrieb fällt zuerst der
Endpunkt in U2 weg (nur die Abfrage bleibt), dann läuft die Änderung in A1
nur über Kontrollfragen. K1 bis K5 und die Case Study U bleiben immer.

**Meilensteine.**

| spätestens | Output | Prüfung |
|---|---|---|
| Start, <TT.MM.JJJJ> | K1 und K2 | Probefrage 1 richtig, fünf Aufgaben zum Nachverfolgen ohne Ausführen |
| Aufbau, <TT.MM.JJJJ> | K3 bis K7, U1, A1 | Probefragen 2 und 3 richtig, Datenstrecke einem Fachfremden Zeile für Zeile erklärt |
| Abschluss, <TT.MM.JJJJ> | K8, U2, Case Study U und A (anonymisiert) | Prüfung ohne System mit drei Teilen, nämlich 60 Min. Programm mit Klasse und drei Tests plus SQL-Abfrage ohne KI, zehn Fragen zu K1 bis K8 (bestanden ab 8), Endpunkt in fünf Minuten einem Fachfremden erklärt und verteidigt |

**Annahmen.** Last Validated `<TT.MM.JJJJ>`. Stunden sind Obergrenzen und
gegen das Wochenbudget aus `00_kern/einstellungen.json`
(`lernen.deep_dive_h_woche`) zu prüfen. Arbeitsdaten bleiben im Arbeits-Ast,
in den Hub kommt nur die anonymisierte Case Study.

**Offen.** Vier Lücken in der mitgelieferten Bibliothek, die du beschaffst
und mit `/add-literature` einträgst, nämlich ein Python-Lehrbuch (trägt K1
und K3), ein SQL-Übungswerk (K5), ein Werk zu Git (K6) und eines zu
Authentifizierung (K7). Bis dahin tragen ISLP, Feathers und Kleppmann allein.
Prüfungen stehen im Lernlog, die nächste Tätigkeit wählt `/alter`.
