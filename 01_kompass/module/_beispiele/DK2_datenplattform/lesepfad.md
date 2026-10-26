# Lesepfad DK2 Datenplattform und Datenmodellierung

Kern-Lesepfad des Moduls, gilt für alle Projekte im Modul. Quellen, Seiten,
Kernaussagen und allgemeine Kontrollfragen stehen hier. Fragen, die Interna
eines Arbeitgebers berühren würden (Tabellen, Werkzeuge, Datenfallen eines
bestimmten Systems), sind allgemein formuliert. Die Fassung mit den Interna
und die Zuordnung zu den Arbeitspaketen bleiben im Lesebegleiter des
Projekts im Ast.

Marker bei Kernaussagen. G heißt am Text der Bibliothek geprüft, L heißt aus
dem Lesepfad übernommen und noch nicht gegen den Text geprüft. Seiten PDF
beziehen sich auf die Dateien in `02_bibliothek/`, gedruckte
Seiten stehen nur, wo geprüft.

Rolle. Kern heißt Pflicht im Modul, in `modul.md` einem Block der Reihenfolge
zugeordnet. Vertiefung heißt projektnah, gelesen, wenn ein Projekt den Schritt
braucht.

## Übersicht

| ID | Thema | Minuten | Rolle | Block |
|---|---|---|---|---|
| DK2-K00 | Gesamtbild und Problemstellung | 55 | Kern | K1 |
| DK2-K01 | Baseline und Kennzahlen des Pflegeaufwands | 40 | Vertiefung, Spur A | A1 |
| DK2-K02 | Vierstufiger Entwurf und Bus-Matrix | 50 | Kern | K2, K7 |
| DK2-K03 | Pull-Vertrag und Landing | 50 | Kern | K6 |
| DK2-K04 | Batch-Denkmodell, unveränderliche Eingaben | 60 | Kern | K6 |
| DK2-K05 | Datenfallen und Staging | 55 | Kern | K8 |
| DK2-K06 | Parquet und DuckDB, spaltenorientierte Speicherung | 60 | Kern | K5 |
| DK2-K07 | Fakten für Bestand, Verbrauch, Bedarf | 40 | Kern | K3 |
| DK2-K08 | Dimensionen und Historie | 50 | Kern | K4 |
| DK2-K09 | Betrieb, Tagesmarker, Sperrdatei | 60 | Vertiefung, Spur A | A2 |
| DK2-K10 | Golden Master und Umzug eines Konsumenten | 55 | Vertiefung, Spur A | A2 |
| DK2-K11 | Konsumentenvertrag und Schema-Evolution | 45 | Kern | K8 |
| DK2-K12 | Kennzahlenkatalog und Beförderungsregel | 50 | Vertiefung, Spur A | nach Bedarf |
| DK2-K13 | Auftragskette und Fertigung | 45 | Vertiefung, Hauptort ein Modul zu Auftragsabwicklung oder Fertigung | keiner |
| DK2-K14 | Weitere Werke und Tochtergesellschaften | 40 | Kern | K3 |
| DK2-K15 | Quellenablösung und Abschaltung des Altwerkzeugs | 45 | Vertiefung, Spur A | nach Bedarf |
| DK2-K16 | Entscheidungen begründen | 45 | Kern | K5 |

Summe Pflichtminuten 845 (rund 14,1 h), davon Kern 550 (rund 9,2 h).

## DK2-K00 Gesamtbild und Problemstellung

Kern, 55 Min. Pflicht, Block K1.

| Werk | Kapitel oder Abschnitt | Seiten PDF | gedruckt |
|---|---|---|---|
| Kimball/Ross, The Data Warehouse Toolkit | Kap. 1, Alternative DW/BI Architectures (Independent Data Mart, Hub-and-Spoke, Hybrid, fünf Mythen) | 62 bis 68 |  |
| Reis/Housley, Fundamentals of Data Engineering | Kap. 2, Lebenszyklus von der Datenerzeugung bis zur Auslieferung | 59 bis 74 |  |

**Worum es geht.** Warum getrennte Auswertungen verschiedene Zahlen liefern und wie die Schichten einer Plattform das lösen.

**Warum jetzt.** Bevor modelliert wird, muss klar sein, welches Problem die Architektur löst und wo die Schichten liegen.

**Worauf achten.**
- (L) Mehrere Auswertungen mit je eigenem Zugriff auf dieselben Exporte sind, was Kimball die Architektur unabhängiger Data Marts nennt.
- (L) Das Ziel ist eine Engine mit Schichten, die Quelle, Aufbereitung und Auslieferung trennt.
- (L) Bei Reis laufen die Undercurrents (Datenmanagement, DataOps, Orchestrierung) quer durch alle fünf Stufen des Lebenszyklus.

**Kontrollfragen.**
1. Welchem der fünf Mythen über dimensionale Modelle begegnest du am ehesten, und was entgegnet Kimball?
2. Ordne Landing, Staging, Mart und Konsumenten den fünf Stufen des Lebenszyklus bei Reis zu. Welche Stufe fehlt im Bild?

**Spur U, Daten der eigenen Firma.** Welche Architektur nach Kimball haben die heutigen Auswertungen deiner Firmendaten (z. B. Umsatz oder Kunden), eigene Zugriffe je Skript oder eine gemeinsame Schicht?

## DK2-K01 Baseline und Kennzahlen des Pflegeaufwands

Vertiefung, Spur A, 40 Min. Pflicht, Block A1.

| Werk | Kapitel oder Abschnitt | Seiten PDF | gedruckt |
|---|---|---|---|
| Werner, Supply Chain Controlling | Kap. 5.1 und Beginn 5.3, Kennzahlentypologie Input, Throughput, Output, Payment | 60 bis 64 und 72 bis 76 |  |

**Worum es geht.** Wie man misst, wie aufwendig die heutige Pflege der Auswertungen ist, als Ausgangswert für später.

**Warum jetzt.** Ohne gemessenen Ausgangswert lässt sich die Wirkung einer Plattform später nicht belegen.

**Worauf achten.**
- (L) Werner trennt Eingangsgrößen (Aufwand) von Ergebnisgrößen.
- (L) Eine Kennzahl ohne Zielwert und Messregel steuert nichts.

**Kontrollfragen.**
1. Ist ein Pflegeaufwand in Stunden eine Input-, Throughput- oder Output-Kennzahl nach Werner, und was wäre das Gegenstück auf der Output-Seite?
2. Was muss eine Baseline-Messung trennen, damit nach einem Umbau ein fairer Vorher-nachher-Vergleich möglich ist?

## DK2-K02 Vierstufiger Entwurf und Bus-Matrix

Kern, 50 Min. Pflicht, Block K2, K7.

| Werk | Kapitel oder Abschnitt | Seiten PDF | gedruckt |
|---|---|---|---|
| Kimball/Ross, The Data Warehouse Toolkit | Kap. 3, die vier Schritte Geschäftsprozess, Granularität, Dimensionen, Fakten | 105 bis 108 |  |
| Kimball/Ross, The Data Warehouse Toolkit | Kap. 2, Conformed Dimensions und Bus-Matrix | 73 bis 76 und 86 bis 89 |  |
| Kimball/Ross, The Data Warehouse Toolkit | Kap. 4, Bus Architecture am Beispiel Bestand | 159 bis 166 |  |
| Reis/Housley, Fundamentals of Data Engineering | Kap. 8, Kimball gegen Inmon und Data Vault (Vertiefung, Grundlage der Modellwahl) | 320 bis 334 |  |

**Worum es geht.** In welcher Reihenfolge ein Datenmodell entworfen wird und wie die Bus-Matrix zeigt, was gemeinsam gebaut wird.

**Warum jetzt.** Die Granularität ist die erste Entscheidung jedes Modells, alles Weitere hängt an ihr.

**Worauf achten.**
- (L) Die Granularität wird festgelegt, bevor Dimensionen und Fakten gewählt werden. Ein Fehler dort lässt sich durch keine spätere Wahl reparieren.
- (L) Die Bus-Matrix legt fest, welche Dimension zuerst gebaut wird und wer welchen Prozess besitzt.

**Kontrollfragen.**
1. Auf welcher Granularität würdest du Bestandsfakten deklarieren (Material, Werk, Lagerort, Tag), und welche Frage eines Konsumenten könnte dann nicht mehr beantwortet werden?
2. Welche Dimension taucht in den meisten Zeilen deiner Bus-Matrix auf, und warum ist sie damit die erste, die gebaut wird?

**Spur U, Daten der eigenen Firma.** Welche Granularität hat die Faktentabelle deiner Umsätze, und warum nicht Tag je Kunde?

## DK2-K03 Pull-Vertrag und Landing

Kern, 50 Min. Pflicht, Block K6.

| Werk | Kapitel oder Abschnitt | Seiten PDF | gedruckt |
|---|---|---|---|
| Reis/Housley, Fundamentals of Data Engineering | Kap. 7, Ingestion, Batch-Ingestion, Schemaänderungen | 261 bis 274 | 235 bis 247 |
| Kimball/Ross, The Data Warehouse Toolkit | Kap. 19, Anforderungen sammeln und Extraktion | 480 bis 491 | etwa 444 bis 455 |

**Worum es geht.** Was eine Quelle liefern muss, damit die Plattform die Daten abholen kann, und wann eine Lieferung als unvollständig gilt.

**Warum jetzt.** Bevor Daten verarbeitet werden, muss feststehen, was die Quelle liefern muss und wann eine Lieferung unvollständig ist.

**Worauf achten.**
- (G) Ein täglicher Zug nach Zeitintervall ist das übliche Muster der Berichts-ETL (Reis, gedruckt S. 244).
- (G) Vollständige Snapshots sind wegen ihrer Einfachheit weit verbreitet, Differenzabzüge sparen Übertragung und Speicher (Reis, gedruckt S. 246).
- (G) Schemaänderungen im Quellsystem brechen Pipelines. Man braucht automatische Erkennung, Alarm bei nicht auffangbaren Änderungen und Absprache mit den Betroffenen (Reis, gedruckt S. 243). Das ist der Grund, warum der Lauf bei geänderter Spalte laut abbrechen soll.

**Kontrollfragen.**
1. Wann ist ein täglicher vollständiger Export einem Differenzabzug vorzuziehen, und welche Eigenschaft einer Quelle macht den Differenzabzug unsicher?
2. Was muss ein Pull-Vertrag festhalten, damit der Lauf eine unvollständige Lieferung erkennt?

**Spur U, Daten der eigenen Firma.** Woran erkennt deine Ladestrecke, dass ein Export aus Shop, Buchhaltung oder CRM unvollständig ist oder sein Schema geändert hat?

## DK2-K04 Batch-Denkmodell, unveränderliche Eingaben

Kern, 60 Min. Pflicht, Block K6.

| Werk | Kapitel oder Abschnitt | Seiten PDF | gedruckt |
|---|---|---|---|
| Kleppmann, Designing Data-Intensive Applications | Kap. 10, Unix-Philosophie und was ein Batch-Job ist | 411 bis 419 |  |
| Kleppmann, Designing Data-Intensive Applications | Kap. 10, Ausgabe von Batch-Abläufen, Philosophie des Batch-Verarbeitens, Fehlertoleranz | 433 bis 436 | gedruckt 412 bis 413 |

**Worum es geht.** Warum Rohdaten nie überschrieben werden und wie jeder Lauf dadurch wiederholbar bleibt.

**Warum jetzt.** Unveränderliche Eingaben machen jeden Lauf wiederholbar, das ist die Grundlage der Idempotenz.

**Worauf achten.**
- (G) Wer Eingaben als unveränderlich behandelt und keine Seiteneffekte zulässt, kann einen Lauf beliebig oft wiederholen.
- (G) Bei einem Fehler im Code nimmt man die Version zurück und rechnet neu. Kleppmann nennt das human fault tolerance. Eine Datenbank mit Schreibzugriffen kann das nicht.
- (G) Automatischer Neustart ist nur sicher, weil Eingaben unveränderlich sind und halbe Ausgaben verworfen werden.

**Kontrollfragen.**
1. Was geht verloren, wenn jemand eine Datei im Landing nachträglich von Hand korrigiert?
2. Warum liegen Annotationen der Nutzer außerhalb des Kern-Marts, wenn man den Gedanken der abgeleiteten Daten ernst nimmt?

**Spur U, Daten der eigenen Firma.** Was bedeutet Idempotenz für deine Ladestrecke, und wie prüft ein Test sie?

## DK2-K05 Datenfallen und Staging

Kern, 55 Min. Pflicht, Block K8.

| Werk | Kapitel oder Abschnitt | Seiten PDF | gedruckt |
|---|---|---|---|
| Kimball/Ross, The Data Warehouse Toolkit | Kap. 19, Cleaning and Conforming, Fehlerereignis-Tabelle, Audit-Dimension | 491 bis 499 |  |
| Kimball/Ross, The Data Warehouse Toolkit | Kap. 2, Audit Dimension und Error Event Schemas | 102 bis 104 |  |
| Reis/Housley, Fundamentals of Data Engineering | Kap. 2, Undercurrents Datenmanagement und DataOps, Datenqualität (Vertiefung) | 74 bis 96 |  |

**Worum es geht.** Wo typische Fehler der Quelldaten auffallen und wo über sie entschieden wird, bevor sie in Kennzahlen landen.

**Warum jetzt.** Staging ist der Ort, an dem Fehler der Quelle gefunden und entschieden werden, bevor sie in Kennzahlen wandern.

**Worauf achten.**
- (L) Ein gefundener Fehler wird festgehalten und der Lauf geht weiter, wenn er nicht kritisch ist. Bei kritischen Fehlern stoppt der Lauf.
- (L) Das Register muss je Falle festlegen, ob abgebrochen oder gewarnt wird.

**Kontrollfragen.**
1. Eine Datenfalle verfälscht Mittelwerte, eine andere nur die Einheit eines Preises. Welche bricht den Lauf ab, welche markiert nur, und woran machst du das fest?
2. Warum zählt eine Falle erst als kontrolliert, wenn es auch einen Test gibt, der die Prüfung auf die Falle ansetzt?

**Spur U, Daten der eigenen Firma.** Nenne drei Datenfallen in deinen Exporten und entscheide je Falle zwischen Abbruch und Warnung.

## DK2-K06 Parquet und DuckDB, spaltenorientierte Speicherung

Kern, 60 Min. Pflicht, Block K5.

| Werk | Kapitel oder Abschnitt | Seiten PDF | gedruckt |
|---|---|---|---|
| Kleppmann, Designing Data-Intensive Applications | Kap. 3, Transaktionsverarbeitung gegen Analytik, spaltenorientierte Speicherung, Kompression | 112 bis 126 | gedruckt 90 bis 98 |
| Reis/Housley, Fundamentals of Data Engineering | Anhang A, Serialisierungsformate, Parquet, Kompression | 417 bis 424 | gedruckt 392 bis 393 |

**Worum es geht.** Wie Daten gespeichert werden, damit Abfragen schnell sind, und warum sich dieses Format schwer umkehren lässt.

**Warum jetzt.** Das Speicherformat entscheidet, ob Analyseabfragen schnell genug sind, und ist eine der wenigen schwer umkehrbaren Wahlen.

**Worauf achten.**
- (G) Eine Analyseabfrage liest wenige Spalten über viele Zeilen. Im Spaltenformat liest sie nur die Spalten, die sie braucht (Kleppmann, gedruckt S. 95).
- (G) Gleichartige Werte einer Spalte liegen nebeneinander und lassen sich gut komprimieren (Kleppmann, gedruckt S. 97 bis 98).
- (G) Spaltenformate sind schlecht für viele kleine Einzelzeilen-Änderungen. Ein Lauf, der je Tabelle einmal vollständig schreibt, ist davon nicht betroffen (Reis, Anhang A).
- (G) Beide Bücher sagen nichts zum Netzlaufwerk. Dass es schnell genug ist, muss der Lasttest zeigen.

**Kontrollfragen.**
1. Wieso liest eine Abfrage wie Bestandswert je Werk und Monat aus einem Spaltenformat weniger Daten als aus einer zeilenorientierten Tabelle?
2. Welches Ergebnis eines Lasttests würde dich zu einem Datenbankserver statt Parquet bewegen, und ab welcher Abfragezeit?

**Spur U, Daten der eigenen Firma.** Lohnt sich Parquet beim Volumen deiner Daten, oder reicht eine einzelne DuckDB-Datei?

## DK2-K07 Fakten für Bestand, Verbrauch, Bedarf

Kern, 40 Min. Pflicht, Block K3.

| Werk | Kapitel oder Abschnitt | Seiten PDF | gedruckt |
|---|---|---|---|
| Kimball/Ross, The Data Warehouse Toolkit | Kap. 2, Faktentabellen (additiv, semi-additiv, Nullwerte, Transaktion, Periodic und Accumulating Snapshot) | 77 bis 80 |  |
| Kimball/Ross, The Data Warehouse Toolkit | Kap. 4, Bestandsmodelle, die drei Typen von Faktentabellen | 147 bis 158 |  |

**Worum es geht.** Welche Arten von Zahlen es gibt (Bestand, Verbrauch, Bedarf) und welche sich addieren lassen.

**Warum jetzt.** Erst mit den Faktentypen ist klar, welche Größen sich addieren lassen und welche nicht.

**Worauf achten.**
- (L) Bestände lassen sich über die Zeit nicht addieren (semi-additiv), Verbräuche schon.
- (L) Kimball behandelt Nullwerte in Faktentabellen ausdrücklich. Das ist die fachliche Grundlage für Monate ohne Verbrauch.

**Kontrollfragen.**
1. Warum ist der Durchschnittsbestand eines Quartals nicht die Summe der drei Monatsbestände, und was passiert mit der Reichweite, wenn man es so rechnet?
2. Ist ein Monat ohne Verbrauch ein fehlender Wert oder eine echte Null im Sinne Kimballs, und welche Folge hat das für den Mittelwert?

**Spur U, Daten der eigenen Firma.** Welche Fakten deiner Umsätze oder Bestände sind additiv, welche semi-additiv?

## DK2-K08 Dimensionen und Historie

Kern, 50 Min. Pflicht, Block K4.

| Werk | Kapitel oder Abschnitt | Seiten PDF | gedruckt |
|---|---|---|---|
| Kimball/Ross, The Data Warehouse Toolkit | Kap. 5, Beschaffungs-Bus-Matrix, Slowly Changing Dimensions Typ 1, 2, 3 und Hybride | 178 bis 195 |  |

**Worum es geht.** Wie sich Stammdaten wie Material oder Lieferant über die Zeit ändern und ob man den alten Stand braucht.

**Warum jetzt.** Dimensionen ändern sich über die Zeit, und das Modell muss entscheiden, ob die alte Fassung gebraucht wird.

**Worauf achten.**
- (L) Typ 2 hält die Historie und braucht dafür einen Ersatzschlüssel.
- (L) Man prüft je Merkmal eines Stammsatzes, ob die alte Fassung wirklich gebraucht wird.

**Kontrollfragen.**
1. Welche drei Attribute eines Materialstamms würdest du als Typ 2 führen, welche als Typ 1, und welche Frage eines Konsumenten entscheidet das?
2. Wie lässt sich Tage im Status aus einer Typ-2-Dimension und einem Snapshot berechnen, ohne eine eigene Tabelle je Werkzeug?

**Spur U, Daten der eigenen Firma.** Ein Kunde wechselt die Preisgruppe. Typ 1 oder Typ 2, und welche Auswertung entscheidet das?

## DK2-K09 Betrieb, Tagesmarker, Sperrdatei

Vertiefung, Spur A, 60 Min. Pflicht, Block A2.

| Werk | Kapitel oder Abschnitt | Seiten PDF | gedruckt |
|---|---|---|---|
| Kleppmann, Designing Data-Intensive Applications | Kap. 8, unzuverlässige Uhren, Prozesspausen, Leases, Fencing Tokens | 309 bis 326 |  |
| Reis/Housley, Fundamentals of Data Engineering | Kap. 3, Prinzipien, darunter Plan for failure | 103 bis 106 |  |
| Kimball/Ross, The Data Warehouse Toolkit | Kap. 19, Job Scheduler, Backup und Recovery (Vertiefung) | 519 bis 525 |  |

**Worum es geht.** Wie ein täglicher Lauf auf mehreren Rechnern sauber abläuft, ohne dass zwei gleichzeitig schreiben.

**Warum jetzt.** Ein täglicher Lauf auf mehreren Rechnern braucht Schutz davor, zweimal gleichzeitig zu schreiben.

**Worauf achten.**
- (L) Eine Sperre mit Ablaufzeit schützt nur, wenn der Besitzer seine Ablaufzeit nicht überschreitet.
- (L) Fencing Tokens lösen das, wenn der geschützte Speicher einen alten Token ablehnt. Ein Netzlaufwerk kann das nicht, die Tragfähigkeit einer Sperrdatei bleibt dort offen.
- (L) Eigene Überlegung, nicht aus dem Buch. Den Mart atomar in eine neue Version schreiben und umbenennen.

**Kontrollfragen.**
1. Was geschieht im schlimmsten Fall, wenn Rechner A nach einem Ruhezustand weiterschreibt, obwohl Rechner B die Sperre inzwischen übernommen hat?
2. Welche zwei Uhren sind an der Ablaufzeit beteiligt, und warum kann ihre Abweichung die Sperre unwirksam machen?

## DK2-K10 Golden Master und Umzug eines Konsumenten

Vertiefung, Spur A, 55 Min. Pflicht, Block A2.

| Werk | Kapitel oder Abschnitt | Seiten PDF | gedruckt |
|---|---|---|---|
| Feathers, Working Effectively with Legacy Code | Kap. 2, Arbeiten mit Rückmeldung, Legacy Code Change Algorithm | 32 bis 43 |  |
| Feathers, Working Effectively with Legacy Code | Kap. 13, Characterization Tests und Heuristik zum Schreiben | 208 bis 218 |  |

**Worum es geht.** Wie man beweist, dass ein neues Werkzeug dieselben Zahlen liefert wie das alte.

**Warum jetzt.** Wer ein bestehendes Werkzeug ablöst, braucht einen Beweis, dass die neuen Zahlen den alten entsprechen.

**Worauf achten.**
- (L) Ein Characterization Test hält fest, was der Code tut, nicht was er tun sollte.
- (L) Auf ein ganzes Werkzeug angewendet ergibt das den zellgenauen Abgleich gegen das Altwerkzeug.
- (L) Eine Abweichung ist kein Fehler an sich, sondern eine Entscheidung. Welche Rechnung stimmt, wird fachlich entschieden.

**Kontrollfragen.**
1. Das Altwerkzeug rechnet eine Kennzahl nach einer anderen Regel. Ist die Abweichung im Abgleich ein Fehler der neuen Engine?
2. Welche Abweichung müsste im Abgleich erklärt sein, bevor du umschalten darfst, und welche darfst du als erweiterte Grundgesamtheit stehen lassen?

## DK2-K11 Konsumentenvertrag und Schema-Evolution

Kern, 45 Min. Pflicht, Block K8.

| Werk | Kapitel oder Abschnitt | Seiten PDF | gedruckt |
|---|---|---|---|
| Kleppmann, Designing Data-Intensive Applications | Kap. 4, Formate, Rückwärts- und Vorwärtskompatibilität, Avro und Schemaunterschiede über Feldnamen | 134 bis 136 und 142 bis 150 |  |
| Reis/Housley, Fundamentals of Data Engineering | Kap. 5, Datenverträge zwischen Quelle und Verbraucher | 208 bis 209 |  |

**Worum es geht.** Wie man das Datenmodell ändert, ohne die Verbraucher der Daten zu überraschen.

**Warum jetzt.** Sobald ein zweiter Verbraucher den Mart liest, muss jede Änderung am Schema gegen ihn geprüft werden.

**Worauf achten.**
- (L) Kleppmann behandelt das Format, nicht die Bedeutung. Dieselbe Spalte mit neuer Bedeutung bleibt für einen Formattest unsichtbar.

**Kontrollfragen.**
1. Eine neue Spalte kommt in den Mart. Ist das rückwärts- oder vorwärtskompatibel für einen bestehenden Konsumenten, und warum?
2. Welche Änderung am Mart würde ein Vertragstest nicht entdecken, obwohl sich die Zahlen eines Konsumenten ändern?

**Spur U, Daten der eigenen Firma.** Welche Spalten wird eine spätere Auswertung (z. B. ein Dashboard) aus dem Mart lesen, und wie hält ein Vertragstest sie stabil?

## DK2-K12 Kennzahlenkatalog und Beförderungsregel

Vertiefung, Spur A, 50 Min. Pflicht, Block nach Bedarf des Projekts.

| Werk | Kapitel oder Abschnitt | Seiten PDF | gedruckt |
|---|---|---|---|
| Werner, Supply Chain Controlling | Kap. 5.2, Arten von Kennzahlen | 64 bis 72 |  |
| Werner, Supply Chain Controlling | Kap. 5.4.1, Werttreiberbaum | 105 bis 112 |  |
| Consulting Methodenkoffer | Kategorie Data Structure (Glossary, Data Dictionary) |  |  |

**Worum es geht.** Wie eine Kennzahl einmal verbindlich definiert wird, damit alle dieselbe rechnen.

**Warum jetzt.** Dieselbe Kennzahl wird in mehreren Werkzeugen verschieden gerechnet, der Katalog legt eine Definition fest.

**Worauf achten.**
- (L) Der Werttreiberbaum zerlegt eine Kennzahl und zeigt, an welchem Zweig sich zwei Tools tatsächlich unterscheiden.

**Kontrollfragen.**
1. Zeichne den Werttreiberbaum einer Kennzahl, die zwei Werkzeuge verschieden rechnen. An welchem Zweig liegt die Abweichung?
2. Was gehört in einen Katalogeintrag, damit er den Rechenweg zeigt, aus dem jede berichtete Zahl entsteht?

## DK2-K13 Auftragskette und Fertigung

Vertiefung, Hauptort ein Modul zu Auftragsabwicklung oder Fertigung, 45 Min. Pflicht, Block keiner.

| Werk | Kapitel oder Abschnitt | Seiten PDF | gedruckt |
|---|---|---|---|
| Kimball/Ross, The Data Warehouse Toolkit | Kap. 6, Auftragstransaktionen mit Kopf und Position | 204 bis 215 |  |
| Kimball/Ross, The Data Warehouse Toolkit | Kap. 6, Accumulating Snapshot für die Auftragsabwicklung | 230 bis 237 |  |

**Worum es geht.** Wie Aufträge in Ebenen aufgebaut sind und wie man diese Ebenen nicht verwechselt.

**Warum jetzt.** Aufträge haben mehrere Ebenen, und viele Fehler entstehen, wenn Ebenen verwechselt werden.

**Worauf achten.**
- (L) Aufträge haben mehrere Ebenen (Kopf, Position, Einteilung). Viele Datenfallen bei Aufträgen sind im Kern eine Verwechslung der Ebene.
- (L) Der Accumulating Snapshot bildet ab, wie ein Auftrag durch Meilensteine läuft.

**Kontrollfragen.**
1. Auf welcher Ebene würdest du die Lieferfähigkeit eines Kundenauftrags als Fakt führen, und was passiert bei der Summe über die Positionen?
2. Welche Meilensteine wären die Spalten eines Accumulating Snapshots für einen Fertigungsauftrag?

## DK2-K14 Weitere Werke und Tochtergesellschaften

Kern, 40 Min. Pflicht, Block K3.

| Werk | Kapitel oder Abschnitt | Seiten PDF | gedruckt |
|---|---|---|---|
| Kimball/Ross, The Data Warehouse Toolkit | Kap. 4, Conformed Dimensions | 166 bis 174 |  |
| Kimball/Ross, The Data Warehouse Toolkit | Kap. 2, mehrere Währungen und Mengeneinheiten | 96 bis 97 |  |

**Worum es geht.** Wie weitere Werke und Gesellschaften dieselben Stammdaten nutzen.

**Warum jetzt.** Kommen weitere Werke, Standorte oder Gesellschaften dazu, müssen die Dimensionen für alle gleich sein.

**Worauf achten.**
- (L) Eine Dimension ist conformed, wenn alle Fakten sie mit denselben Schlüsseln und Attributen teilen.
- (L) Eine zweite Währung oder Mengeneinheit gehört ins Faktendesign und lässt sich später nur mit Aufwand nachrüsten.

**Kontrollfragen.**
1. Welche Attribute einer Werks- oder Standortdimension müssen für alle Gesellschaften gleich sein, damit zwei Einheiten vergleichbar sind?
2. Wo steht in deinen Fakten, in welcher Währung ein Betrag vorliegt?

**Spur U, Daten der eigenen Firma.** Welche Attribute braucht die Standort- oder Kanaldimension, damit zwei Geschäftsbereiche oder Vertriebswege vergleichbar sind?

## DK2-K15 Quellenablösung und Abschaltung des Altwerkzeugs

Vertiefung, Spur A, 45 Min. Pflicht, Block nach Bedarf des Projekts.

| Werk | Kapitel oder Abschnitt | Seiten PDF | gedruckt |
|---|---|---|---|
| Kleppmann, Designing Data-Intensive Applications | Kap. 12, Datenintegration, abgeleitete Daten, Neuverarbeitung | 511 bis 522 |  |
| Kleppmann, Designing Data-Intensive Applications | Kap. 12, Beginn von Aiming for Correctness, Ende-zu-Ende-Argument | 537 bis 545 |  |

**Worum es geht.** Wie man ein Altwerkzeug abschaltet, nachdem seine Zahlen als korrekt belegt sind.

**Warum jetzt.** Vor dem Abschalten eines Altwerkzeugs muss die Korrektheit über die ganze Kette belegt sein.

**Worauf achten.**
- (L) Korrektheit lässt sich nicht in einer einzelnen Schicht beweisen, sondern wird am Ende der Kette geprüft.
- (L) Das stützt den zellgenauen Abgleich gegenüber Einzeltests der Schichten.

**Kontrollfragen.**
1. Genügt ein grüner Test jeder Schicht, um ein Altwerkzeug abzuschalten? Begründe mit dem Ende-zu-Ende-Argument.
2. Was prüft ein Abdeckungstest, was ein Golden-Master-Abgleich nicht prüft?

## DK2-K16 Entscheidungen begründen

Kern, 45 Min. Pflicht, Block K5.

| Werk | Kapitel oder Abschnitt | Seiten PDF | gedruckt |
|---|---|---|---|
| Reis/Housley, Fundamentals of Data Engineering | Kap. 3, Prinzipien guter Architektur, darunter umkehrbare Entscheidungen | 103 bis 113 | Prinzip 7 auf gedruckt 83 |
| Reis/Housley, Fundamentals of Data Engineering | Kap. 4, dauerhafte gegen vergängliche Technologien, Build gegen Buy, Monolith gegen modular, Server gegen serverless | 146 bis 149 und 158 bis 169 | Immutable gegen Transitory auf gedruckt 120 bis 121 |

**Worum es geht.** Wie man Entscheidungen so begründet, dass ein Außenstehender sie nachvollziehen kann.

**Warum jetzt.** Jede Entscheidung braucht eine Begründung, die ein externer Leser nachvollziehen kann.

**Worauf achten.**
- (G) Man soll umkehrbare Entscheidungen anstreben, Zwei-Wege-Türen (Reis, Prinzip 7, gedruckt S. 83).
- (G) Beständige und vergängliche Technologien unterscheidet der Lindy-Effekt. Je länger etwas besteht, desto länger bleibt es (Reis, Kap. 4, gedruckt S. 121).
- (L) Reis denkt cloud-orientiert. Die Kriterien sind übertragbar, die Werkzeugbeispiele nicht.

**Kontrollfragen.**
1. Welche deiner Architekturentscheidungen ist umkehrbar und welche nicht? Was kostet die Umkehr jeweils?
2. Welche Angabe in einem ADR würde einen externen Leser überzeugen, dass die Entscheidung nicht nur Bequemlichkeit war?

**Spur U, Daten der eigenen Firma.** Welche Entscheidung in deiner Ladestrecke ist eine Zwei-Wege-Tür, welche nicht?

## Erklär-Check nach jedem Gate

Der Nutzer erklärt in fünf Minuten einem Fachfremden, was das Gate
entschieden hat und warum. Vorher nennt er seine Zuversicht in Prozent. Claude
prüft gegen die Kapitel auf Korrektheit, Vollständigkeit, Klarheit und
Blindstellen. Lücken werden zu Karten, Ausrutscher nicht.

## Lücken

- Für den Betrieb mit Continuous Integration und für Coding Agents hat die
  Bibliothek kein Werk. Empfehlung, bei Bedarf ein Werk dazu über
  `/add-literature` aufnehmen.
