# Handbuch

Wie du mit dem Hub arbeitest und lernst. Die `README.md` sagt, wie du ihn
einrichtest und was wo liegt. Dieses Handbuch erklärt, wie die Teile
zusammenspielen, mit einem Beispiel, das sich durch alle Kapitel zieht. Lies
es einmal ganz, danach reicht der Spickzettel am Ende.

## Inhalt

1. Die Idee in fünf Sätzen
2. Stamm und Äste
3. Was in welchem Ordner passiert
4. Lernen mit ALTER
5. Dein Rhythmus
6. Ein Beispiel von der Aufgabe bis zur Case Study
7. Bewerben mit dem Hub
8. Regeln, die immer gelten
9. Wenn etwas schiefgeht
10. Spickzettel

## 1. Die Idee in fünf Sätzen

Der Hub ist ein privates Git-Repo, in dem du mit Claude Code arbeitest, lernst
und deine Entwicklung belegst. Jede Aufgabe aus der Arbeit oder der
Selbständigkeit wird zugleich zu Lernstoff, weil die Theorie dazu einmal im
Hub liegt und in deinen Projekten angewendet wird. Was du lernst, behältst
du über ein Karteisystem mit verteilter Wiederholung, und was du kannst,
weist du mit Erklärungen, Artefakten und Case Studies nach. Claude übernimmt
dabei das Planen, Prüfen, Rechnen und Dokumentieren, das Urteil und die
Verantwortung bleiben bei dir. Weil alles in Dateien steht, weiß jede neue
Sitzung, wer du bist, woran du arbeitest und wie du arbeiten willst.

## 2. Stamm und Äste

```
                 ┌──────────────────────────────┐
                 │             Hub              │   privat, dir gehört alles
                 │ Regeln · Bibliothek · Lernen │
                 │ Werkstatt · Wissen · Werkzeug│
                 └──────┬───────────────┬───────┘
          Kern der      │               │      Kern der
          Module ↓      │               │      ↓ Module
                 ┌──────┴─────┐  ┌──────┴──────┐
                 │  AT_FIRMA  │  │  ST_FIRMA   │  je ein eigenes privates Repo
                 │  Spur A    │  │  Spur U     │  Daten bleiben dort
                 └──────┬─────┘  └──────┬──────┘
                        └───────┬───────┘
          zurück nur anonymisiert ↑  Lernkarte · Framework · Case Study
```

Der Hub ist der Stamm. Dort liegen deine Regeln, deine Bücher, dein
Lernsystem, deine Werkzeuge und alles, was nur dir gehört (Lernprojekte,
private Anliegen, Bewerbungen).

Ein Ast ist ein eigenes privates Repo für etwas, das jemand anderem gehört,
also die Arbeit bei deinem Arbeitgeber, deine eigene Firma, ein Verein oder
ein Kunde. Jeder Ast hat eine Spur, einen Buchstaben, unter dem du dort
übst. Üblich sind A für die Arbeit und U für das eigene Unternehmen. Ö heißt
öffentliche Daten und ist der Ersatz, wenn kein Ast passt. Einen neuen Ast
hängst du mit `/ast-anlegen` an.

Die Grenze ist streng. Daten eines Asts bleiben im Ast. In den Hub fließt nur
zurück, was über einen von drei Wegen läuft, und das immer anonymisiert und
von dir freigegeben.

| Weg zurück | Was im Hub ankommt |
|---|---|
| Lernkarte | ein Begriff oder eine Methode, die du behalten willst |
| Framework | eine Registerzeile, wenn sich ein Ansatz im Ast bewährt |
| Case Study | die Geschichte eines abgeschlossenen Vorhabens, ohne interne Zahlen |

Wechselst du den Job, legst du einen neuen Ast an. Dein Wissen, deine Module
und deine Case Studies bleiben im Hub und gehen mit.

## 3. Was in welchem Ordner passiert

Die Ordner sind nummeriert, weil sie eine Schleife bilden.

`01_kompass → 02_bibliothek → 03_projekte und Äste → 04_gedaechtnis → 05_werkstatt → 06_wissen → zurück zu 01_kompass`

| Ordner | Was dort passiert | Typischer Befehl |
|---|---|---|
| `00_kern/` | Regeln, Vorlieben, Einstellungen, Skripte. Hier änderst du, wie Claude arbeitet | `/einrichten` |
| `01_kompass/` | Ziele, Kompetenzprofil, Studienplan, Module, Aufnahmen neuer Aufgaben | `/aufnahme`, `/advisor` |
| `02_bibliothek/` | Fachbücher als PDF mit Index und Inhaltsverzeichnissen, Methodenkoffer | `/add-literature` |
| `03_projekte/` | Lernprojekte und private Anliegen | `/new-project` |
| `04_gedaechtnis/` | Karten und Wiederholung über alle Lernprojekte | `/heute`, `/alter` |
| `05_werkstatt/` | Case Studies, Transcript deiner Nachweise, Bewerbungen | `/editor`, `/job-apply` |
| `06_wissen/` | eigene Frameworks, Verbindungen zwischen Fächern | `/framework-next`, `/roommate` |
| `07_handwerk/` | Projektvorlage, Definition of Done, Decks, Dashboards, Lebenslauf | wird von den Befehlen genutzt |

Ein paar Begriffe, die überall vorkommen.

| Begriff | Bedeutung |
|---|---|
| Modul | ein Kompetenzfeld, etwa Datenmodellierung. Es hat einen Plan, einen Kern-Lesepfad und ein Register aller Projekte, in denen du es angewendet hast. Es läuft über Jahre und sammelt Belege |
| Kern | die Theorie eines Moduls, einmal im Hub, für alle Projekte gleich |
| Spur | wo du den Kern anwendest, also in welchem Ast |
| Lesepfad | je Arbeitspaket ein Abschnitt mit Werk, Kapitel, Seiten, Minuten, warum jetzt, worauf achten und zwei Kontrollfragen |
| Block | ein Arbeitsschritt im Modulplan mit Termin als Obergrenze, Stunden und Nachweis |
| Gate | ein Meilenstein mit Kriterium, nach dem du in einem Erklär-Check zeigst, dass du verstanden hast |
| ADR | eine Entscheidung im Projekt mit Begründung und Literaturstelle |
| `/xx-next` | ein eigener Befehl je Projekt, der genau ein Arbeitspaket abarbeitet |

## 4. Lernen mit ALTER

ALTER ist das Lernsystem des Hubs. Der Name steht für die fünf Rollen, die
Claude für dich übernimmt (Advisor, Librarian, Tutor, Editor, Roommate). Die
Idee dahinter ist einfach. Berufsbegleitendes Lernen scheitert selten am
Stoff, sondern daran, dass niemand plant, prüft und nachhält. Hier hat jede
dieser Aufgaben einen Ort und einen Befehl.

| Rolle | Frage, die sie beantwortet | Wie |
|---|---|---|
| Advisor | Was lerne ich als Nächstes, was lasse ich weg, wie viel Zeit habe ich? | `/advisor` plant einen Durchlauf eines Moduls in fünf Entscheidungen (Ziel, Ausgangslage, Reihenfolge, Cut List, Meilensteine) |
| Librarian | Welches Buch und welches Kapitel tragen diesen Schritt? | Bibliothek mit Index, Agent `literature-scout`, Lesepfade |
| Tutor | Habe ich es verstanden, und kann ich es in drei Monaten noch? | `/tutor` prüft Verstehen, `/heute` sorgt fürs Behalten |
| Editor | Hält mein Ergebnis einer fremden Prüfung stand? | `/editor` prüft eine Erklärung, einen Text oder Code auf Logik, Argument, Struktur und Präzision |
| Roommate | Womit aus einem fernen Fach hängt das zusammen? | `/roommate` einmal im Monat |

### Was die Lernforschung dazu sagt

Das System stützt sich auf Brown, Roediger und McDaniel, *Make It Stick*,
das in deiner Bibliothek liegt. Drei Befunde tragen alles.

| Befund | Was der Hub daraus macht |
|---|---|
| Wiederlesen fühlt sich nach Lernen an, bringt aber wenig. Wer aus dem Gedächtnis abruft, behält (Kap. 1 und 2) | Karten fragen ab, statt zu zeigen. Vor dem Lesen versuchst du, eine Frage zu beantworten |
| Verteilt und gemischt üben wirkt stärker als am Stück (Kap. 3) | eine Wiederholungsschlange über alle Projekte, Abstände rechnet der SM-2-Algorithmus |
| Wir halten uns oft für sicherer, als wir sind (Kap. 5) | vor jedem Test schätzt du deine Zuversicht in Prozent, danach wird sie gegen das Ergebnis gehalten |

### Die drei Prüfmodi des Tutors

| Modus | Was passiert | Wann |
|---|---|---|
| `sokrates` | Claude fragt nach, bis die Lücke sichtbar ist, und erklärt nicht vor | beim Erarbeiten, oder wenn eine Karte immer wieder scheitert |
| `feynman` | du erklärst einem Fachfremden, Claude bewertet gegen das Kapitel auf Korrektheit, Vollständigkeit, Klarheit und Blindstellen | am Blockende, nach einem Gate, mit Abstand nach Wochen |
| `test` | Fragen aus dem Lehrplan, vorher Zuversicht je Frage | am Blockende |

Lücken werden zu Karten, Ausrutscher nicht. Sonst verstopft die Schlange mit
Dingen, die du eigentlich weißt.

### Die Regeln, die das System am Laufen halten

Der volle Text steht in `01_kompass/lerngrundsaetze.md`. Die wichtigsten
drei für den Alltag.

- Fällt eine Woche aus, wird nichts nachgeholt. Es gibt keine
  Rückstandszahl, der Plan läuft vom Stand weiter.
- Statt abzubrechen, schaltest du in den Minimalbetrieb. Zehn Minuten nur
  Wiederholung mit `/heute minimal` halten das Gedächtnis warm.
- Kein Kapitel wird auf Vorrat gelesen. Ein Abschnitt kommt erst, wenn das
  Arbeitspaket dran ist, in dem du ihn anwendest.

### Du musst dir das nicht merken

Im Alltag tippst du `/alter`. Das Skript `04_gedaechtnis/alter.py` schaut auf
deine Karten, deinen Modulplan und deinen Verlauf und wählt genau eine
nächste Tätigkeit. Die Reihenfolge der Regeln ist fest, das Modell
entscheidet nicht selbst.

| Was das System sieht | Was es vorschlägt |
|---|---|
| fällige Karten, heute noch nicht wiederholt | Behalten mit `/heute` |
| eine Karte scheitert zweimal in Folge | Sokrates am Abschnitt, denn die Lücke liegt im Verstehen |
| zwei falsche Antworten trotz hoher Zuversicht | Feynman, weil das eine Illusion des Wissens ist |
| ein Abschnitt sitzt seit Wochen | Feynman mit Abstand, danach Editor |
| ein begonnener Block | der nächste Schritt dieses Blocks |
| ein Meilenstein ist fällig | Erklär-Check über alle Abschnitte bis dahin |
| sonst | der nächste Block nach Termin |
| alles erledigt oder noch kein Modul | Advisor plant den nächsten Durchlauf |

## 5. Dein Rhythmus

Das Budget legst du in `/einrichten` fest (Vorschlag 5 Stunden Deep Dive je
Woche und 20 Minuten Wiederholung je Tag). Termine sind immer Obergrenzen.

| Takt | Was | Dauer | Befehl |
|---|---|---|---|
| täglich | Karten wiederholen | 15 bis 30 Min. | `/heute`, oder `/alter`, das damit beginnt |
| zwei bis drei Mal je Woche | Deep Dive, ein Schritt im Modul | 1 bis 2 h | `/alter` |
| je Arbeitspaket im Ast | Paket abarbeiten, Leseeintrag zuerst | wie das Paket | `/<kurz>-next` im Ast |
| wöchentlich | Projektstand und Lernlage der Woche | 15 Min. | `/weekly-review` |
| monatlich | ein Thema mit einem fernen Fach verbinden | 30 Min. | `/roommate` |
| nach jedem Gate | Erklär-Check, danach Rückfluss in den Hub | 30 Min. | `/tutor feynman`, `/ast-stand` |
| je Trimester | Profil, Studienplan und Budget prüfen | 1 h | `/weekly-review trimester` |
| wenn neue Aufgaben kommen | aufnehmen und einordnen | 20 Min. | `/aufnahme` |

## 6. Ein Beispiel von der Aufgabe bis zur Case Study

Angenommen, du arbeitest im Einkauf eines Industrieunternehmens, dein Ast
heißt `AT_FIRMA` (Spur A). Daneben baust du eine kleine Beratung auf, Ast
`ST_FIRMA` (Spur U). In deinem Kompetenzprofil steht unter anderem der
Bereich DK Daten und KI.

### Woche 1, die Aufgabe kommt

Dein Chef will ein monatliches Reporting zur Termintreue der Lieferanten.
Bisher gibt es nur Excel-Listen aus dem ERP.

Du öffnest Claude Code im Hub und tippst

```
/aufnahme Reporting Lieferantentermintreue aus ERP-Exporten
```

Claude liest dein Profil, deinen Studienplan und die vorhandenen Module und
fragt in kurzen Runden nach Auftrag, Ast, Termin und Theorie. Ergebnis ist
ein Vorschlag. Die Aufgabe berührt den Bereich Daten und KI, ein Modul
Datenplattform gibt es noch nicht, aber als Beispiel unter
`01_kompass/module/_beispiele/DK2_datenplattform/`. Du kopierst es nach
`01_kompass/module/`. Claude prüft dann einen Zwilling in Spur U. Deine
Beratung hat Rechnungs- und Kundendaten, an denen dasselbe Modell geübt
werden kann. Alle vier Kriterien passen (gleicher Kern, Daten verfügbar,
Nutzen für die Firma, Umfang im Budget). Das Aufnahmeblatt landet in
`01_kompass/aufnahmen/`, ohne eine einzige Firmenzahl.

### Woche 1, der Plan

```
/advisor DK2
```

Der Advisor fragt dich fünf Dinge. Was soll am Ende stehen, was kannst du
schon, in welcher Reihenfolge, was lässt du bewusst weg und woran misst du
den Fortschritt? Daraus entsteht in `modul.md` ein Durchlauf mit Kern-Blöcken
(K1 Fakten und Dimensionen, K2 Granularität, ...), Spurblöcken für die Arbeit
(A1, A2) und für die Beratung (U1, U2), je mit Stunden, Termin als
Obergrenze und Nachweis.

### Woche 1, das Projekt im Ast

Du wechselst nach `~/AT_FIRMA` und tippst

```
/new-project lieferantentermintreue
```

`/new-project` findet das Aufnahmeblatt und füllt daraus vor. Dann führt
es dich durch ein Interview wie bei einem Berater (Anlass, Ziele, Scope,
Rolle, Team, Termine, Daten, Kennzahlen, Risiken, Vertraulichkeit,
Arbeitsplan). Am Ende stehen Charter, Arbeitsplan mit Arbeitspaketen, ein
projekteigener Lesepfad, ein Ordner für ADRs und ein neuer Befehl
`/lt-next`, der genau ein Paket abarbeitet.

### Ein normaler Dienstag

Morgens, 20 Minuten im Hub.

```
/heute
```

Eine Karte je Nachricht, du antwortest, schätzt deine Zuversicht, bewertest
dich von 0 bis 5. Der Algorithmus legt fest, wann die Karte wiederkommt.

Abends, eine Stunde im Hub.

```
/alter
```

Das System sagt dir, was dran ist, etwa „Tutor, Kapitel Granularität aus
Kimball und Ross, *The Data Warehouse Toolkit*, Kap. 3“. Es zeigt den
Abschnitt aus dem Lesepfad mit Seiten, warum jetzt und worauf du achten
sollst. Du liest im Buch aus deiner Bibliothek und sagst „gelesen“. Danach
erklärst du in eigenen Worten, was Granularität ist, Claude prüft im Modus
`feynman` gegen das Kapitel. Was fehlt, wird nach deinem Ja zu Karten mit
Werk und Kapitel. Morgen fragt `/heute` sie ab.

### Am Donnerstag im Ast

```
/lt-next
```

Der Befehl sagt in der ersten Zeile, welches Arbeitspaket heute dran ist,
erklärt es in einfachen Worten und gibt zuerst den Leseeintrag aus. Dann
baut ihr das Paket, etwa die Faktentabelle der Wareneingänge auf
Positionsebene. Die Designentscheidung („eine Zeile je Bestellposition und
Wareneingang“) wird ein ADR mit Begründung und Literaturstelle. Tests laufen
grün, bevor das Paket als erledigt gilt. Am Ende steht die Vorbereitung für
das nächste Paket als Datei bereit, damit du vorher lesen kannst.

### Das Gate

Nach vier Wochen ist das erste Gate erreicht, das Datenmodell steht. Du
erklärst in fünf Minuten einem Fachfremden, was entschieden wurde und warum,
vorher nennst du deine Zuversicht. Claude prüft gegen die Kapitel. Danach
schreibst du eine kurze Erklärung, und `/editor` prüft sie auf Logik,
Argument und Präzision, ohne sie für dich umzuschreiben. Hält sie, kommt eine
Zeile ins Transcript unter `05_werkstatt/`.

### Der Rückfluss

Zurück im Hub tippst du

```
/ast-stand AT_FIRMA
```

Claude liest über GitHub nur die freigegebenen Dateien des Asts (Charter,
Methodik, ADRs, Kennzahlendefinitionen), nie Daten oder Berichte, und schlägt
vor, was in den Hub darf. Etwa eine Lernkarte „Granularität vor Kennzahl
festlegen“ und ein Framework-Kandidat für den Aufbau eines Lieferanten-Marts.
Jede Übernahme passiert erst nach deinem Ja.

### Das Ende

Das Reporting läuft. Du misst nach drei Monaten, was sich verändert hat, und
`/new-project` hatte die Kennzahl dafür schon im Interview festgelegt. Daraus
wird eine Case Study in `05_werkstatt/case_studies/` nach Situation, Task,
Approach und Result, mit relativen statt internen Zahlen. Im Register des
Moduls steht jetzt ein Projekt mit Case Study. Beim nächsten Projekt mit
Datenmodellierung nutzt du denselben Kern, und das Register wächst.

## 7. Bewerben mit dem Hub

Einmal in `/einrichten` (Schritt 8) erfasst du deine Lebenslaufdaten, deine
Präferenzen und deinen Stil. Danach reicht

```
/job-apply <PDF, Link oder Text der Anzeige>
```

| Schritt | Was passiert |
|---|---|
| Fit-Check | die Anzeige wird gegen deine Zielrollen, Region, Gehalt und Ausschlüsse gehalten |
| Keyword-Abgleich | jede Anforderung gegen deine belegten Erfahrungen, Lücken offen benannt |
| Skill-Gap-Log | jede Lücke wird gezählt. Nach vier Wochen siehst du, was bei Stellen, die dir gefallen, am häufigsten fehlt. Daraus wird ein Modul |
| Lebenslauf | aus deiner Basis zugeschnitten, Formulierungen der Anzeige, wo deine Erfahrung sie deckt, nie erfunden |
| Anschreiben | nach deinem Ton, deiner Anrede und deinen Wörtern, mit zwei bis drei Belegen aus deinen Case Studies |
| Prüfung | eine Seite, keine offenen Platzhalter, jede Angabe gegen deine Zeugnisse, Vertraulichkeit |

Das Beispielmodul Bewerbungsgespräch
(`01_kompass/module/_beispiele/BE2_bewerbungsgespraech/`) bereitet dich auf
die Gespräche vor, mit Arbeitshilfen zu MECE, Pyramidenprinzip und SCQA.

## 8. Regeln, die immer gelten

Die Regeln stehen in zwei Dateien und gelten über `~/.claude/CLAUDE.md` in
jedem Repo, auch in den Ästen. Du kannst sie jederzeit ändern, danach
committen.

| Datei | Inhalt |
|---|---|
| `00_kern/persoenlich.md` | wie Claude mit dir spricht, Schreibstil ohne KI-Merkmale, Farbpalette, Rechenweg in jedem Ergebnis |
| `00_kern/regeln.md` | Sprache, Ergebnis zuerst, Quellen und Lesepfad, Qualität, Delegation, Decks, Excel, Code, Git |
| `00_kern/vertraulichkeit.md` | was aus einem Ast nie und wie es anonymisiert in den Hub darf |

Vier Regeln, deren Sinn sich nicht sofort erschließt.

| Regel | Warum |
|---|---|
| Delegationsmodell | Claude verarbeitet bekannte Informationen. Urteil unter Unsicherheit mit Folgen für andere Menschen bleibt bei dir. So weißt du immer, was du vertreten musst |
| Rechenweg | jede Zahl zeigt Formel und Quelle. Du kannst sie verteidigen, und Fehler fallen auf |
| Plausibilität 15 % | jede Zahl gegen die Vorperiode, größere Sprünge werden markiert und nie still durchgereicht |
| Ablauffrist drei Monate | Annahmen tragen ein Datum. Ist es alt, fragt Claude nach, statt mit veralteten Werten zu rechnen |

## 9. Wenn etwas schiefgeht

| Lage | Was du tust |
|---|---|
| eine Woche keine Zeit | nichts nachholen, `/heute minimal` genügt, danach `/alter` |
| Claude behauptet etwas über ein Buch | nach Werk, Kapitel und Seite fragen. Der Lesepfad markiert, was am Text geprüft ist und was nicht |
| `/alter` schlägt etwas vor, das gerade nicht passt | „stopp“ sagen und den gewünschten Befehl selbst aufrufen |
| ein neues Buch | als `Autor_Titel.pdf` in den passenden Ordner unter `02_bibliothek/`, beim nächsten Start meldet ein Hook es, `/add-literature` trägt es ein |
| ein zweiter Rechner | vor der Arbeit `git pull --ff-only`. Das Claude-Gedächtnis überträgt `python3 00_kern/gedaechtnis_sync.py export` und `import` |
| neuer Job | `/ast-anlegen` für den neuen Arbeitgeber, der alte Ast bleibt als Archiv. Module und Case Studies bleiben im Hub |
| eine Einstellung ändern | `/einrichten <schritt>`, etwa `/einrichten stil` oder `/einrichten karriere` |
| die Vorlage hat eine neue Fassung | siehe Abschnitt „Vorlage aktualisieren“ in der README |

## 10. Spickzettel

| Ich will | Befehl |
|---|---|
| meine Karten wiederholen | `/heute` |
| lernen, ohne zu überlegen, was dran ist | `/alter` |
| eine neue Aufgabe einordnen | `/aufnahme <Aufgabe>` |
| ein Modul planen | `/advisor <ID>` |
| ein Projekt anlegen | `/new-project <kurzname>` |
| das nächste Arbeitspaket | `/<kurz>-next` |
| prüfen, ob ich es verstanden habe | `/tutor feynman <Abschnitt>` |
| ein Ergebnis gegenlesen lassen | `/editor <Datei>` |
| die Woche abschließen | `/weekly-review` |
| sehen, was in einem Ast passiert ist | `/ast-stand <Ast>` |
| mich bewerben | `/job-apply <Anzeige>` |
| ein Thema auf eine Seite bringen | `/learn-poster <Thema>` |
| ein Buch eintragen | `/add-literature` |
| eigene Frameworks aus der Bibliothek entwickeln | `/framework-next` |
| einen neuen Ast | `/ast-anlegen` |
| etwas an der Einrichtung ändern | `/einrichten <schritt>` |
