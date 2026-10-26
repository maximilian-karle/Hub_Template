# Kern-Regeln

Gelten im Hub und in jedem Ast. Eingebunden über `~/.claude/CLAUDE.md`
(`python3 00_kern/installieren.py`). Was nur für ein Repo gilt, steht in
dessen eigener `CLAUDE.md`. Schreibstil, Farben und Rechenweg stehen in
`00_kern/persoenlich.md` und werden hier nicht wiederholt. Persönliche
Parameter (Name, Äste, Budgets) liegen in `00_kern/einstellungen.json`.

## 1. Sprache und Schrift

- Der Chat folgt `sprache.chat` in `00_kern/einstellungen.json`. Dateien
  folgen der Sprache des Repos (Hub nach `sprache.hub`, jeder Ast nach seinem
  Eintrag unter `aeste`).
- Deutscher Text mit echten Umlauten (ä, ö, ü, ß). Ausnahme sind Bezeichner,
  die technisch ASCII bleiben müssen (Variablen, Funktionen, Dateinamen,
  Ordner, Schlüssel).
- Keine Emojis in Ergebnissen. Status zeigen Text, Farbe und schlichte
  Zeichen wie ↑ ↓ → Σ Δ.
- Werden ich und Kollegen in einem gemeinsamen Dokument genannt, wechselt die
  Reihenfolge, oder es stehen Rollen statt Namen.

## 2. Denken und Darstellen

- Pyramid Principle, Ergebnis zuerst, Begründung danach. Executive Summary
  vor dem Detail.
- MECE gliedern, also überschneidungsfrei und vollständig.
- Argumente (Gespräch, Pitch, Text, Empfehlung) baut Claude nach
  `00_kern/argumentation_weisse_rhetorik.md`. Den Begründungsstrang wähle
  ich, Claude schlägt zwei bis drei vor.
- Ist etwas mehrdeutig, genau eine Rückfrage. Unsicherheit offen benennen.
- Rückfrage auch dann, wenn eine Annahme älter als drei Monate und nicht neu
  bestätigt ist oder eine Aufgabe nicht klar ins Delegationsmodell passt.

## 3. Quellen und Lesepfad

- Vor jeder Methodenwahl zuerst die Bibliothek im Hub (`02_bibliothek/`)
  befragen, aus einem Ast heraus über den Agenten `literature-scout`. Die
  Bibliothek ist Anregung, keine Checkliste.
- Danach eigenes Denken ergänzen. Eine Methode wird angepasst, kombiniert
  oder ersetzt, nie unverändert weitergereicht.
- Jede Quelle mit Werk und Kapitel nennen. Wörtliche Zitate höchstens 15
  Wörter.
- Ein Ansatz, der über ein Projekt hinaus trägt, wird Framework-Kandidat
  (`06_wissen/frameworks/README.md`).
- Jedes Projekt bekommt einen Lesepfad, damit ich die Tiefe selbst
  wiedergeben kann und nicht nur mit Claude gebaut habe. Er hat drei Teile.
  - Lesepfad entlang des Arbeitsplans, je Arbeitspaket ein bis zwei
    Abschnitte zu 30 bis 60 Min. mit Werk und Kapitel. Je Abschnitt warum
    jetzt, worauf achten, wo es im eigenen Code oder in der eigenen
    Entscheidung steckt, zwei Kontrollfragen. Fehlt ein Werk, wird die Lücke
    als Empfehlung genannt.
  - Entscheidungsprotokoll (ADR) mit Literaturstelle je Entscheidung,
    zugleich Rohmaterial für die Case Study.
  - Erklär-Check nach jedem Gate, ich erkläre (Feynman).
  Gehört das Projekt zu einem Modul, liegen die Kern-Abschnitte einmal im
  Modulordner im Hub (`01_kompass/module/`), das Projekt führt nur eigene
  Abschnitte. Neue Aufgaben beginnen im Hub mit `/aufnahme`, das Projekt
  entsteht mit `/new-project`.

## 4. Qualität

- Plausibilität. Jede berichtete Zahl gegen die Vorperiode halten. Eine
  Abweichung über 15 % wird ausdrücklich markiert und nie still
  durchgereicht.
- Rohdaten vor Aussage. Für Mengen und Werte gilt das Quellsystem (ERP,
  Bankauszug, Export), für Einordnung und Risiko das Gespräch. Widersprechen
  sich beide, wird das als offener Punkt geführt und nicht selbst aufgelöst.
- Ablauffrist. Jede Annahme in einer Methodikdatei trägt ein Datum „Last
  Validated“. Ist es älter als drei Monate, wird das vor dem Ergebnis
  gemeldet.
- Fertig ist ein Ergebnis erst, wenn die Definition of Done für seinen Typ
  erfüllt ist (`07_handwerk/Definition_of_Done.md`).

## 5. Delegationsmodell

Prüffrage je Aufgabe ist, ob sie Urteil unter Unsicherheit mit Folgen für
andere Menschen verlangt oder nur bekannte Informationen korrekt verarbeitet.

| Wer | Was |
|---|---|
| Bleibt bei mir | Beziehungen und politische Abstimmung, letztes Urteil bei unklaren Zahlen, Prüfung von Interviewaussagen mit der Fachabteilung, die Empfehlung vertreten |
| Claude im Gespräch | Framework auf einen Fall anwenden, erste Struktur, Argument auf MECE prüfen, Rohdaten zur Management-Erzählung, Advocatus Diaboli, erste Entwürfe |
| Claude Code und Automatisierung | Exporte einlesen und normalisieren, Neuberechnung bei neuen Inputs, Dashboard-Refresh, Abgleich Rohdaten gegen Dashboard, Versionierung und Doku im Repo |

Passt eine Aufgabe nicht eindeutig, fragen.

## 6. Decks

- Jede Folie bekommt eine Methode, die ihre Aufgabe trägt (Pyramid für die
  Zusammenfassung, SCQA für den roten Faden, Gap-Analyse für die
  Komplikation, Paarvergleich für ein Ranking, Stakeholder Map für Rollen).
- Vor dem Text die grafische Form prüfen. Ablauf wird Flussbild, Kontrast
  wird zwei Felder, Hierarchie wird Bänder, Vergleich wird Matrix.
- Quellen in die Fußzeile, mit Marker an der Aussage.
- Mein voller Name (`person.name`) steht auf dem Cover.
- Keine internen Projektartefakte auf Folien (Arbeitspaketnummern,
  Dateinamen, Repo-Pfade).
- Ein Deck, das live ein Gespräch steuern soll, ist ein Pitch mit höchstens
  fünf Folien, am Ende steht, was heute entschieden werden soll.
- Das fertige Deck als Bilder rendern und ansehen, bevor es übergeben wird.
- Standard und Werkzeug in `07_handwerk/Praesentationsstandard.md` und
  `07_handwerk/deck_toolkit.py`.

## 7. Excel und Dashboards

- Ergebnis-Excel ohne erklärende Unterzeilen und Fußhinweise im Blatt. Ein
  schlichter Titel je Blatt mit Stichdatum, Legenden und Einschränkungen ins
  Readme-Blatt.
- Dashboards nach dem Bausatz in `07_handwerk/dashboard_template/`. Weiße
  Karten, Diagrammtitel linksbündig, kein Gitternetz.
- Animationen nur, wo sie etwas hervorheben, und mit Rücksicht auf
  `prefers-reduced-motion`.

## 8. Code

- Quellcode könnte jeder sehen. In Kommentaren, Docstrings und
  Konsolenmeldungen deshalb keine Personennamen, keine Projekthistorie, keine
  Datumsstempel.
- Erhalten bleibt das Warum, also Geschäftsregeln, Invarianten, Eigenheiten
  der Datenquelle, Herleitungen und Literaturstellen. Entscheidungshistorie
  gehört ins ADR des Projekts.

## 9. Git

- Sage ich „commit“, geht der Commit direkt auf `main`, ohne Feature-Branch
  und ohne PR. Vor jedem `git push` einmal bestätigen lassen.
- Historie umschreiben, Force-Push, Löschen und Umbenennen von Repos oder
  Ordnern nur nach einem ausdrücklichen Ja im Chat, jedes Mal neu.
- Commit nur des eigenen Projektordners, wenn mehrere Projekte offen sind
  (`git add -- 03_projekte/<projekt>`), nie pauschal `git add -A`.
