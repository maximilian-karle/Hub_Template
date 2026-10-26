# Lesepfad DK1 Python und Softwarehandwerk

Kern-Lesepfad des Moduls, gilt für alle Projekte im Modul. Angelegt mit
`/advisor` am `<TT.MM.JJJJ>`. Die Abschnitte gehen von Python über
Softwarehandwerk (Tests, fremder Code, Git, SQL, Dienste) und reichen mit
DK1-K08 bis zum ersten Aufruf eines Sprachmodells.

Quellen nur aus der Bibliothek im Hub (`02_bibliothek/`), Seiten vor dem
Eintragen im PDF geprüft. Keine Zusammenfassung der Bücher, die Lektüre
bleibt beim Nutzer. Fehlt ein Werk, steht die Lücke als Empfehlung da.

Marker bei Kernaussagen. G heißt am Text der Bibliothek geprüft, L heißt aus
dem Lesepfad übernommen und noch nicht gegen den Text geprüft. Seiten PDF
beziehen sich auf die Dateien in `02_bibliothek/`, gedruckte Seiten stehen
nur, wo geprüft (ISLP gedruckt = PDF minus 10, Feathers gedruckt = PDF
minus 23).

Rolle. Kern heißt Pflicht im Modul, in `modul.md` einem Block der Reihenfolge
zugeordnet.

Wo es steckt. Je Abschnitt steht, wo der Stoff in den Spuren geübt wird.
Spur A meint ein Projekt im Arbeits-Ast, Spur U eines im Unternehmens-Ast,
Spur Ö öffentliche Daten als Ersatz, wenn kein Ast passt. Die Beispiele sind
allgemein gehalten und werden beim Übernehmen durch die eigenen Projekte
ersetzt.

## Übersicht

| ID | Thema | Minuten | Rolle | Block |
|---|---|---|---|---|
| DK1-K01 | Python lesen, Funktionen und Code nachverfolgen | 45 | Kern | K1 |
| DK1-K02 | Datenstrukturen, NumPy, Daten laden | 50 | Kern | K2 |
| DK1-K03 | Klassen, Fehler, Tests und Rückmeldung | 40 | Kern | K3 |
| DK1-K04 | Fremden Code verstehen, Characterization Tests | 60 | Kern | K4 |
| DK1-K05 | Relationales Modell und Abfragen | 45 | Kern | K5 |
| DK1-K06 | Git, Versionsgeschichte und Zusammenarbeit | 30 | Kern | K6 |
| DK1-K07 | Dienste, REST und Authentifizierung | 40 | Kern | K7 |
| DK1-K08 | Strukturierte Ausgabe und Tools | 40 | Kern | K8 |

Summe Pflichtminuten 350 (45 + 50 + 40 + 60 + 45 + 30 + 40 + 40, rund
5,8 h). Der Rest des Kerns sind Übungen ohne KI und Kontrollfragen.

## DK1-K01 Python lesen, Funktionen und Code nachverfolgen

Kern, 45 Min. Pflicht, Block K1.

| Werk | Kapitel oder Abschnitt | Seiten PDF | gedruckt |
|---|---|---|---|
| James u. a., ISLP | Kap. 2.3.1 Getting Started, 2.3.2 Basic Commands | 50 bis 52 | 40 bis 42 |
| James u. a., ISLP | Kap. 2.3.5 Sequences and Slice Notation, 2.3.8 For Loops | 61, 69 bis 71 | 51, 59 bis 61 |

Lücke. Ein Python-Lehrbuch, das Funktionen, Parameter, Standardwerte und
Gültigkeitsbereiche von Grund auf erklärt, ist nicht in der mitgelieferten
Bibliothek. Empfehlung, eines zu beschaffen und mit `/add-literature`
einzutragen. Bis dahin trägt ISLP nur die Syntax.

**Worum es geht.** Wie man ein kurzes Programm Zeile für Zeile im Kopf
ausführt, bevor man es laufen lässt.

**Warum jetzt.** Funktion, Parameter und Rückgabe sind die Grundbegriffe,
an denen Anfänger am häufigsten scheitern (etwa an der Probefrage zum
Standardwert einer Liste). Alles Weitere baut darauf.

**Worauf achten.** Unterschied zwischen Definieren und Aufrufen einer
Funktion, Listen als veränderbare Objekte, Einrückung als Blockgrenze.

**Kernaussagen.**
- (G) Listen, Tupel und Zeichenketten sind Sequenzen, Listen entstehen mit
  eckigen Klammern (ISLP Kap. 2.3.2, S. 51 PDF).
- (L) Ein Standardwert eines Parameters entsteht einmal beim Definieren der
  Funktion und nicht bei jedem Aufruf.

**Wo es steckt.** Spur U in der kleinen Datenstrecke, die von Hand entsteht.
Spur A in jedem bestehenden Skript, das später mit Characterization Tests
gelesen wird.

**Kontrollfragen.**
1. Was gibt eine Funktion zurück, die kein `return` hat?
2. Warum verändert `liste.append(x)` in einer Funktion auch die Liste des
   Aufrufers?

## DK1-K02 Datenstrukturen, NumPy, Daten laden

Kern, 50 Min. Pflicht, Block K2.

| Werk | Kapitel oder Abschnitt | Seiten PDF | gedruckt |
|---|---|---|---|
| James u. a., ISLP | Kap. 2.3.3 Introduction to Numerical Python | 52 bis 58 | 42 bis 48 |
| James u. a., ISLP | Kap. 2.3.6 Indexing Data, 2.3.7 Loading Data | 61 bis 69 | 51 bis 59 |

**Worum es geht.** Welche Behälter Python für Daten hat und wie man eine
Tabelle lädt und gezielt Zeilen und Spalten herausgreift.

**Warum jetzt.** pandas und NumPy laufen in fast jedem Datenprojekt, oft
aber über Claude. Ohne Indexieren bleibt jede Auswertung fremder Code.

**Worauf achten.** Unterschied zwischen Liste und NumPy-Array, Indexierung ab
null, Zugriff über Position gegen Zugriff über Namen.

**Kernaussagen.**
- (L) NumPy-Arrays rechnen elementweise, Listen nicht.
- (L) Ein geladener Datensatz wird vor der Auswertung auf fehlende Werte
  geprüft.

**Wo es steckt.** Spur U beim Laden der eigenen Daten in die Datenstrecke.
Spur A beim Lesen der Tabellen im gewählten Skript.

**Kontrollfragen.**
1. Was ergibt `[1, 2] * 2` und was ergibt dasselbe mit einem NumPy-Array?
2. Wie wählst du in einem DataFrame alle Zeilen mit einem Wert über 50 in
   einer Spalte `menge` aus?

## DK1-K03 Klassen, Fehler, Tests und Rückmeldung

Kern, 40 Min. Pflicht, Block K3.

| Werk | Kapitel oder Abschnitt | Seiten PDF | gedruckt |
|---|---|---|---|
| Feathers, Working Effectively with Legacy Code | Kap. 2 Working with Feedback | 32 bis 43 | 9 bis 20 |

Lücke. Klassen, Module, Fehlerbehandlung und pytest in Python stehen in
keinem Werk der mitgelieferten Bibliothek. Dasselbe Python-Lehrbuch wie in
DK1-K01 schließt sie.

**Worum es geht.** Warum ein Test, der in Sekunden läuft, mehr Sicherheit
gibt als sorgfältiges Hinsehen.

**Warum jetzt.** Bevor eigener Code wächst, braucht er Tests. Sonst ist jede
Änderung ein Risiko.

**Worauf achten.** Feathers unterscheidet zwischen Ändern mit Sorgfalt und
Ändern mit Rückmeldung durch Tests. Was macht einen Test zum Unit Test?

**Kernaussagen.**
- (L) Unit Tests laufen schnell und lokalisieren einen Fehler, große Tests
  tun beides nicht.
- (L) Rückmeldung durch Tests ersetzt das Prinzip, nur mit Vorsicht zu
  ändern.

**Wo es steckt.** Spur U mit den Tests der Datenstrecke. Spur A mit den
Tests, die A1 vorbereitet.

**Kontrollfragen.**
1. Woran erkennst du, dass ein Test kein Unit Test ist?
2. Wozu braucht eine Klasse eine Methode `__init__`?

## DK1-K04 Fremden Code verstehen, Characterization Tests

Kern, 60 Min. Pflicht, Block K4.

| Werk | Kapitel oder Abschnitt | Seiten PDF | gedruckt |
|---|---|---|---|
| Feathers, Working Effectively with Legacy Code | Kap. 13 I Need to Make a Change, but I Don't Know What Tests to Write | 208 bis 219 | 185 bis 196 |
| Feathers, Working Effectively with Legacy Code | Kap. 16 I Don't Understand the Code Well Enough to Change It | 232 bis 237 | 209 bis 214 |
| Feathers, Working Effectively with Legacy Code | Kap. 19 My Project Is Not Object Oriented | 254 bis 267 | 231 bis 244 |

**Worum es geht.** Wie man Code, den man nicht selbst geschrieben hat, erst
festhält und dann sicher ändert.

**Warum jetzt.** Wer mit Claude arbeitet, hat schnell viel Code, den er
nicht selbst geschrieben hat. Ihn erklären und ändern zu können ist der
Nachweis, der in einem Fachgespräch zählt.

**Worauf achten.** Der Test hält fest, was der Code tut, nicht was er tun
sollte. Kap. 19 ist das passende Kapitel für prozedurale Skripte, die
Beispiele sind in C und müssen auf Python übertragen werden.

**Kernaussagen.**
- (G) Ein Characterization Test beschreibt das tatsächliche Verhalten eines
  Codestücks, nicht das gewünschte (Kap. 13, S. 209 PDF).
- (G) Vorgehen in vier Schritten, nämlich Code in einen Test einbinden, eine
  Erwartung schreiben, die scheitert, aus dem Fehler das Verhalten ablesen
  und die Erwartung darauf ändern (Kap. 13, S. 209 PDF).
- (L) Notizen, Skizzen und probeweises Umbauen helfen, Code zu verstehen
  (Kap. 16).

**Wo es steckt.** Spur A in A1 am gewählten Skript im Arbeits-Ast. Spur U,
sobald die eigene Datenstrecke umgebaut wird.

**Kontrollfragen.**
1. Warum sucht ein Characterization Test keine Fehler?
2. Was tust du, wenn der festgehaltene Ist-Wert offensichtlich falsch ist?

## DK1-K05 Relationales Modell und Abfragen

Kern, 45 Min. Pflicht, Block K5.

| Werk | Kapitel oder Abschnitt | Seiten PDF | gedruckt |
|---|---|---|---|
| Kleppmann, Designing Data-Intensive Applications | Kap. 2 Relational Model Versus Document Model | 50 bis 63 | |
| Kleppmann, Designing Data-Intensive Applications | Kap. 2 Query Languages for Data, Declarative Queries on the Web | 64 bis 67 | |

Lücke. Ein Übungswerk zu SQL mit Joins, Gruppieren und HAVING ist nicht in
der mitgelieferten Bibliothek. Kleppmann erklärt das Modell, das Schreiben
von Abfragen übt er nicht. Empfehlung, eines zu beschaffen und mit
`/add-literature` einzutragen.

**Worum es geht.** Warum Daten in Tabellen mit Schlüsseln liegen und wie eine
Abfrage beschreibt, was man will, statt wie es berechnet wird.

**Warum jetzt.** Jede Auswertung über mehrere Tabellen braucht Joins und
Gruppieren, und ein späteres Modul zu Datenmodellen (etwa ein Sternschema)
setzt beides voraus.

**Worauf achten.** Viele-zu-eins-Beziehungen und warum sie Joins brauchen.
Deklarativ gegen imperativ.

**Kernaussagen.**
- (L) Viele-zu-eins- und Viele-zu-viele-Beziehungen sprechen für das
  relationale Modell (Kap. 2, S. 55 PDF).
- (L) Eine deklarative Abfrage nennt das Ergebnis, die Datenbank wählt den
  Weg.
- (L) WHERE filtert Zeilen vor dem Gruppieren, HAVING Gruppen danach.

**Wo es steckt.** Spur U in U2 mit einer Kennzahl aus den eigenen Daten,
etwa in DuckDB oder SQLite abgefragt.

**Kontrollfragen.**
1. Warum braucht eine Abfrage der Menge je Standortname einen Join, wenn
   die Bewegungen nur die Standortnummer tragen?
2. Wann gehört eine Bedingung in WHERE und wann in HAVING?

## DK1-K06 Git, Versionsgeschichte und Zusammenarbeit

Kern, 30 Min. Pflicht, Block K6.

Lücke. Kein Werk der mitgelieferten Bibliothek behandelt Git. Empfehlung,
ein Werk zu Versionsverwaltung mit Git zu beschaffen und mit
`/add-literature` einzutragen. Bis dahin trägt nur die Übung in A1.

**Worum es geht.** Wie Git Stände festhält, Zweige trennt und wieder
zusammenführt.

**Warum jetzt.** Git läuft täglich im Hub, oft aber über Claude. Wer die
Folgen eines Push nicht benennen kann, verliert die Kontrolle über den
eigenen Stand.

**Worauf achten.** Commit lokal, Push öffentlich, Merge und Konflikt als
normaler Vorgang.

**Kernaussagen.**
- (L) Ein Commit hält einen Stand lokal fest und lässt sich leicht
  zurücknehmen, ein Push macht ihn für andere sichtbar.
- (L) Ein Konflikt entsteht, wenn zwei Zweige dieselbe Stelle ändern, und
  wird von Hand entschieden.

**Wo es steckt.** Spur A in A1 mit einer Änderung über Branch und Merge. Im
Hub bei jedem Commit auf `main`.

**Kontrollfragen.**
1. Warum steht vor jedem Push eine Bestätigung, vor jedem Commit nicht?
2. Was passiert bei einem Merge, wenn beide Zweige dieselbe Zeile geändert
   haben?

## DK1-K07 Dienste, REST und Authentifizierung

Kern, 40 Min. Pflicht, Block K7.

| Werk | Kapitel oder Abschnitt | Seiten PDF | gedruckt |
|---|---|---|---|
| Kleppmann, Designing Data-Intensive Applications | Kap. 4 Modes of Dataflow, Dataflow Through Services: REST and RPC | 150 bis 158 | |

Lücke. Authentifizierung mit API-Key und Token steht in keinem Werk der
mitgelieferten Bibliothek. Empfehlung, ein Werk zu API-Design und
Sicherheit zu beschaffen.

**Worum es geht.** Wie zwei Programme über das Netz Daten austauschen und wie
ein Dienst prüft, wer anfragt.

**Warum jetzt.** U2 stellt einen eigenen Endpunkt bereit, und DK1-K08 lässt
ein Sprachmodell einen solchen Endpunkt als Tool nutzen. Ohne Verständnis
von Anfrage und Antwort bleibt beides Magie.

**Worauf achten.** Client und Server, GET und POST, warum ein Dienst nur
vorgegebene Eingaben erlaubt.

**Kernaussagen.**
- (G) Server stellen eine API über das Netz bereit, Clients stellen Anfragen
  daran, die bereitgestellte API heißt Dienst (Kap. 4, S. 153 PDF).
- (G) Anders als eine Datenbank erlaubt ein Dienst nur Ein- und Ausgaben, die
  seine Geschäftslogik vorgibt (Kap. 4, S. 154 PDF).
- (G) REST ist eine Entwurfshaltung auf den Prinzipien von HTTP und kein
  eigenes Protokoll, mit URLs für Ressourcen und HTTP-Funktionen unter
  anderem für Authentifizierung (Kap. 4, S. 155 PDF).

**Wo es steckt.** Spur U in U2 mit dem Endpunkt für die eigene Kennzahl.

**Kontrollfragen.**
1. Warum gibt ein Dienst nicht einfach direkten Zugriff auf die Datenbank?
2. Was antwortet ein Endpunkt, wenn der API-Key fehlt, und warum?

## DK1-K08 Strukturierte Ausgabe und Tools

Kern, 40 Min. Pflicht, Block K8.

| Werk | Kapitel oder Abschnitt | Seiten PDF | gedruckt |
|---|---|---|---|
| Alammar/Grootendorst, Hands-On Large Language Models | Kap. 6 Output Verification, Providing Examples, Grammar: Constrained Sampling | 213 bis 220 | |
| Alammar/Grootendorst, Hands-On Large Language Models | Kap. 7 Agents: Creating a System of LLMs, nur der Teil zu Tools | 240 bis 242 | |

**Worum es geht.** Wie man ein Sprachmodell dazu bringt, in einem festen
Format zu antworten und für eine Frage ein Werkzeug aufzurufen.

**Warum jetzt.** Das ist die Brücke vom Softwarehandwerk zu Anwendungen mit
Sprachmodellen. Ein eigener Endpunkt wird damit zum Werkzeug für ein Modell.

**Worauf achten.** Beispiele im Prompt garantieren das Format nicht,
Einschränkung und Prüfung der Ausgabe schon. Die Agentenschleife selbst
gehört in ein späteres Modul über Sprachmodelle.

**Kernaussagen.**
- (G) Beispiele im Prompt verbessern die Struktur der Ausgabe, ob das Modell
  sich daran hält, bleibt aber ihm überlassen (Kap. 6, S. 216 PDF).
- (G) Gegen diesen Nachteil gibt es Pakete, die die Ausgabe einschränken und
  prüfen (Kap. 6, S. 216 PDF).
- (G) Tools geben einem Modell Fähigkeiten, die es allein nicht hat, etwa
  einen Taschenrechner (Kap. 7, S. 240 PDF).

**Wo es steckt.** Spur U, sobald ein Modell den Endpunkt aus U2 als Tool
aufruft (im Muster außerhalb des Durchlaufs, Kandidat für den nächsten).

**Kontrollfragen.**
1. Warum reicht ein Beispiel im Prompt nicht, wenn ein Programm die Antwort
   weiterverarbeitet?
2. Wer führt das Tool aus, das Modell oder dein Code?

## Erklär-Check nach jedem Gate

Der Nutzer erklärt in fünf Minuten einem Fachfremden, was das Gate
entschieden hat und warum. Vorher nennt er seine Zuversicht in Prozent. Claude
prüft gegen die Kapitel auf Korrektheit, Vollständigkeit, Klarheit und
Blindstellen. Lücken werden zu Karten, Ausrutscher nicht.
