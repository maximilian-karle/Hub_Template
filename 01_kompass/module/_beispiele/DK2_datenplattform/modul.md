> Dies ist ein Beispielmodul. Es zeigt, wie ein ausgearbeitetes Modul
> aussieht, mit vollem Kern-Lesepfad und einem geplanten ersten Durchlauf.
> Zum Übernehmen den Ordner nach `01_kompass/module/` kopieren, die ID (hier
> `DK2`, im Ordnernamen, im Titel und in allen Abschnitts-IDs wie `DK2-K00`)
> an ein eigenes Bereichskürzel aus `01_kompass/entwicklung/profil.md`
> anpassen und danach mit `/advisor` den ersten Durchlauf planen. Der
> Advisor ersetzt die Platzhalter in spitzen Klammern, passt Spuren, Blöcke
> und Stunden an das eigene Budget an und streicht diesen Hinweis.

# DK2 Datenplattform und Datenmodellierung

| Feld | Wert |
|---|---|
| Bereich | <Kürzel> <Bereich aus dem eigenen Kompetenzprofil>, z. B. DK Daten und KI |
| Lernziel | <Lernziel aus profil.md> |
| Erster Durchlauf | <Trimester>, seit <TT.MM.JJJJ> |
| Kern-Lesepfad | [lesepfad.md](lesepfad.md), DK2-K00 bis DK2-K16 |
| Projekte | [projekte.md](projekte.md) |
| Lernprojekt | `03_projekte/<kurzname>/`, Lernlog dort |

Das Modul ist ein Kompetenzfeld. Es läuft über das erste Trimester hinaus
weiter, jedes neue Projekt mit Datenmodellierung oder Datenplattform kommt
hierher, nutzt den Kern-Lesepfad und hinterlässt eine Case Study im Register.
Ein Durchlauf ist ein Abschnitt dieser Datei, geplant mit `/advisor`,
neuester unten.

## Durchlauf 1 (<Trimester>, 70 h)

Stand <TT.MM.JJJJ>, geplant mit /advisor. Spuren A Data Mart im Arbeits-Ast,
U Sternschema der Daten der eigenen Firma. Alle Termine sind Obergrenzen,
gearbeitet wird so schnell wie möglich.

**Ziel.** Am Ende kann ich einen Geschäftsprozess nach Kimballs vier
Schritten in ein Sternschema übersetzen, eine Ladestrecke von der Quelle über
Staging bis zum Mart idempotent bauen und begründen, die Datenqualität mit
Prüfregeln messen und als Zahl berichten und meine Modellwahl gegen Inmon und
Data Vault verteidigen.

**Ausgangslage.** <Was schon da ist, etwa Praxis aus Projekten oder erste
Theorie, in zwei bis drei Sätzen.> Probefragen <n>, davon richtig <k>,
Zuversicht im Mittel <x> %, Treffer <y> %. <Die ersten Lücken, z. B.
Granularität und Idempotenz.>

**Reihenfolge.** Der Kern liest die Abschnitte des Kern-Lesepfads
[lesepfad.md](lesepfad.md), jeweils zu Beginn des passenden Arbeitspakets im
Projekt der Spur A. Spur U zieht denselben Schritt an den eigenen
Firmendaten nach. Wer keinen Ast hat, übt in Spur Ö mit öffentlichen Daten,
etwa einem offenen Verkaufs- oder Mobilitätsdatensatz.

| Block | spätestens | Inhalt | Quelle | Spur | h max | Nachweis |
|---|---|---|---|---|---|---|
| K1 | <TT.MM.JJJJ> | Fakten, Dimensionen, Architektur | DK2-K00, Kimball/Ross Kap. 1, Reis/Housley Kap. 2 | Kern | 4 | Kontrollfragen |
| K2 | <TT.MM.JJJJ> | vierstufiger Entwurf, Granularität, Bus-Matrix | DK2-K02, Kimball/Ross Kap. 3, 2, 4 | Kern | 4 | Probefrage 1 richtig |
| K3 | <TT.MM.JJJJ> | Faktentypen, Conformed Dimensions | DK2-K07, DK2-K14, Kimball/Ross Kap. 2, 4 | Kern | 3 | Kontrollfragen |
| K4 | <TT.MM.JJJJ> | Slowly Changing Dimensions | DK2-K08, Kimball/Ross Kap. 5 | Kern | 3 | Kontrollfragen |
| K5 | <TT.MM.JJJJ> | spaltenorientierte Speicherung, umkehrbare Entscheidungen | DK2-K06, DK2-K16, Kleppmann Kap. 3, Reis/Housley Kap. 3, 4, Anhang A | Kern | 3 | Kontrollfragen |
| K6 | <TT.MM.JJJJ> | Ingestion, Idempotenz, unveränderliche Eingaben | DK2-K03, DK2-K04, Reis/Housley Kap. 7, Kleppmann Kap. 10 | Kern | 3 | Probefrage 2 richtig |
| K7 | <TT.MM.JJJJ> | Kimball gegen Inmon und Data Vault | DK2-K02, Reis/Housley Kap. 8 | Kern | 2 | eigene Modellwahl als ADR verteidigt |
| K8 | <TT.MM.JJJJ> | Datenqualität, Konsumentenvertrag, typische Fehler | DK2-K05, DK2-K11, Kimball/Ross Kap. 19, 16 (Schluss), Kleppmann Kap. 4 | Kern | 3 | Kontrollfragen |
| A1 | <TT.MM.JJJJ> | Spur A im Arbeits-Ast, z. B. ein Data Mart aus ERP-Exporten. Architektur, Granularität, Dimensionen mit Historie und Modellwahl | wie K1, K2, K4, K7, dazu DK2-K01 | A | 12 | Erklär-Check |
| A2 | <TT.MM.JJJJ> | Ladestrecke mit Staging, Prüfregeln und Abgleich gegen das bisherige Werkzeug, danach Case Study anonymisiert | wie K6, K8, dazu DK2-K09, DK2-K10 | A | 13 | Case Study |
| U1 | <TT.MM.JJJJ> | Spur U, z. B. Umsatz- oder Kundendaten der eigenen Firma. Granularität, Bus-Matrix und Dimensionen mit SCD | wie K2, K3, K4 | U | 10 | Schema in DuckDB |
| U2 | <TT.MM.JJJJ> | Ladestrecke Export, Staging, Mart mit Prüfregeln und Qualitätsbericht, danach Case Study | wie K6, K8 | U | 10 | Test, zwei Läufe gleiche Zeilenzahl |

Summe Kern 25 h (4 + 4 + 3 + 3 + 3 + 3 + 2 + 3), Spur A 25 h (12 + 13),
Spur U 20 h (10 + 10), zusammen 70 h. Die Stunden sind Richtwerte und werden
mit `/advisor` gegen das eigene Wochenbudget gehalten.

**Cut List.** Weg fallen Kimball/Ross Kap. 7 bis 16 (außer dem Schluss von
Kap. 16) und Kap. 21, Kleppmann Kap. 5, 6, 9, 11 und Reis/Housley Kap. 9,
10, 11 und Anhang B. Sie gehören in spätere Module, etwa zu Analytik und
Dashboards oder zu verteilten Systemen. Der Accumulating Snapshot wandert in
ein Modul zur Auftragsabwicklung oder Fertigung, Data Vault bleibt beim
Vergleich. Im Minimalbetrieb schrumpft U2 auf drei Prüfregeln, dann laufen
die A-Blöcke nur über ihre Kontrollfragen. Kern und Case Studies bleiben.

**Meilensteine.**

| spätestens | Output | Prüfung |
|---|---|---|
| G1, <TT.MM.JJJJ> | U1 fertig, erster Durchstich der Ladestrecke in Spur A | Erklär-Check G1 (DK2-K00 bis DK2-K11), Modellwahl erklärt und verteidigt, Probefragen 1 und 2 richtig |
| Aufbau, <TT.MM.JJJJ> | U2 mit Qualitätsbericht, Conformed Dimensions im Projekt der Spur A | Erklär-Check des Mart-Modells mit SCD |
| Abschluss, <TT.MM.JJJJ> | Case Study A (anonymisiert) und U | Erklär-Check G2, Prüfung ohne System mit zehn Fragen (bestanden ab 8), Sternschema der eigenen Daten in fünf Minuten einem Fachfremden erklärt |

**Annahmen.** Last Validated <TT.MM.JJJJ>. Stunden sind Obergrenzen. Die
Lesezeit der Kern-Abschnitte liegt bei rund 9 h (550 Min. laut
[lesepfad.md](lesepfad.md)), der Rest des Kerns sind Kontrollfragen und
Übungen. Die Termine der Spur A folgen dem Arbeitsplan des Projekts im Ast.
Arbeitsdaten bleiben im Ast, in den Hub kommt nur die anonymisierte Case
Study.

**Offen.** Prüfungen stehen im Lernlog, Nachweise im Transcript
(`05_werkstatt/transcript.md`), die Karten liegen in `04_gedaechtnis/`. Welche
Tätigkeit als Nächstes dran ist, entscheidet `/alter`.
