# Präsentationsstandard für Lenkungskreis und Workshop

Gilt für jedes Deck unter `reports/steering_committee/` eines Projekts, im
Hub unter `03_projekte/<projekt>/`, in einem Ast unter `projekte/<projekt>/`.
Die Kern-Regeln für Decks stehen in `00_kern/regeln.md`, Abschnitt 6. Diese
Datei führt sie für den Bau mit `deck_toolkit` aus.

## Folienaufbau (Situation, Komplikation, Lösung)

1. **Cover** mit Projekt, Datum, Anlass
2. **Executive Summary** auf einer Folie, Regel siehe unten
3. **Situation**, die Ausgangslage auf einer Folie
4. **Komplikation**, was sich geändert hat oder welches Problem ansteht
5. **Lösung und Empfehlung**, die Kernaussage mit Zahlen, samt Vergleich mit
   Vorperiode oder Ziel (Qualitätsregeln in `00_kern/regeln.md`, Abschnitt 4)
6. **Optionen und Zielkonflikte**, nur wenn eine Entscheidung ansteht, samt
   der durchdachten Gegenposition (siehe `/steering-prep`)
7. **Nächste Schritte und Bitte**, was konkret vom Gremium gebraucht wird
8. **Anhang** mit Detailtabellen und Verweis auf die Methodik
   (`methodology/*.md` verlinken, statt sie im Hauptteil zu doppeln)

Keine andere Blockstruktur ohne Absprache. Jedes Deck soll an seinem Aufbau
sofort erkennbar sein. Wird ein Deck live gezeigt und soll ein Gespräch
steuern, ist es ein Pitch mit höchstens etwa fünf Folien (Kern-Regeln,
Abschnitt 6).

## Sprache

Die Sprache folgt dem Repo, im Hub Deutsch, in einem Ast die Sprache aus
`00_kern/einstellungen.json`. Das ganze Deck bleibt in einer Sprache, auch
wenn das Publikum gemischt ist. Zahlen und Einheiten sind so geschrieben,
dass sie international lesbar sind (EUR, %, keine stillen Annahmen über das
Dezimaltrennzeichen).

## Executive Summary, Längenregel

- Höchstens fünf Punkte auf einer Folie
- Der erste Punkt ist die Kernaussage (Pyramid Principle, Ergebnis zuerst,
  Begründung danach)
- Keine Zahl ohne Bezug, immer mit Vorperiode oder Ziel

## Methode, jedes Deck ist gebaut wie Beratungsarbeit

Ein Deck ist kein gerenderter Bericht, sondern ein Argument. Sechs Regeln, in
der Reihenfolge, in der sie beim Bau greifen.

### 1. Die Methode je Folie wählen, nicht abdrucken

Bevor eine Folie entsteht, in der Bibliothek (`02_bibliothek/`, Methodenkoffer
und Werke) die Methode suchen, die zur Aufgabe der Folie passt, und sie auf
den Fall zuschneiden. Die Methode formt die Folie, steht aber nicht auf ihr.
Die Fußzeile trägt nur Quellenhinweise, keine Zeile „Methode …“. Bewährte
Paarungen sind

| Aufgabe der Folie | Methode | Kategorie |
|---|---|---|
| Executive Summary | Pyramid Principle, Management Summary | Statusberichte |
| Roter Faden des Decks | SCQA | Informationsanalyse |
| Komplikation, was fehlt | Gap-Analyse, Ist/Ist-nicht | Zieldefinition |
| Optionen gegeneinander ordnen | Paarvergleich, gewichtete Bewertung | Optionsbewertung |
| Zielkonflikte zwischen Parteien | Force Field Analysis | Systemanalyse |
| Rollen und Publikum | Stakeholder Map, Zwiebelmodell | Stakeholderanalyse |
| Verantwortung für Ergebnisse | RACI-Matrix | Prozessanalyse |
| Abschluss, Abnahme | Definition of Done, Abnahmeprotokoll | Projektabschluss |

Wer die Methode zuerst wählt, muss eine Form finden, die zum Argument passt.
Eine Methode wird nie unverändert aus dem Index weitergereicht, sondern
angepasst (Kern-Regeln, Abschnitt 3).

Ist eine Folie ein **Arbeitsinstrument** statt einer Aussage (ein
Paarvergleich, der live gefüllt wird, eine Matrix zum Korrigieren), wird sie
leer gebaut, und die Sprechernotizen sagen, dass sie im Raum gefüllt wird.
Ein vorab gefülltes Instrument ist ein präsentiertes Ergebnis, und das ist
ein anderes (meist das falsche) Treffen.

### 2. Jede Folie auf eine grafische Form prüfen

Die Aufzählung ist der Rückfall, nicht der Normalfall. Vor dem ersten
Aufzählungspunkt fragen, welche Gestalt der Inhalt wirklich hat.

| Gestalt des Inhalts | Form | `deck_toolkit` |
|---|---|---|
| Ablauf, Prozess, Zeitleiste | Kästen mit Pfeilen | `flow_box` + `arrow` |
| Kontrast, vorher und nachher, zwei Lücken | zwei Felder, farbig unterschieden | `flow_box` |
| Hierarchie, Ebenen, Zielgruppen | waagerechte Bänder mit Beschriftung | `band` + `chip` |
| Vergleich über Optionen | Matrix | `table` + Zellfarbe |
| Gegensatzpaare | Kasten ↔ Kasten mit Doppelpfeil | `flow_box` + `arrow(direction="both")` |
| Größenordnungen, die Leitzahlen | Kennzahlkacheln | `kpi_card` |

Überblick schlägt Vollständigkeit. Eine Folie, die der Raum in fünf Sekunden
erfasst und dann diskutiert, schlägt eine vollständige Folie, die vorgelesen
werden muss.

**Eine Tabelle ist richtig, wenn das Publikum sie Zelle für Zelle
korrigieren soll**, etwa eine Rollenübersicht zur Bestätigung oder ein
Detailanhang. Dann bleibt sie, und die Sprechernotizen sagen warum, damit die
Wahl sichtbar bewusst ist.

### 3. Quellen in die Fußzeile, Marker an die Aussage

Dafür gibt es `deck_toolkit.Sources`.

```python
src = Sources()
bullets(ph, [f"Die Zielgrößen laufen gegeneinander{src.ref(QUELLE)}."])
footnote_sources(slide, src)
```

`src.ref()` liefert den hochgestellten Marker und merkt sich die Quelle,
`footnote_sources()` setzt die nummerierte Liste an den Folienfuß. Dasselbe
Werk zweimal auf einer Folie behält einen Marker.

Der Grund ist, dass eine Quellenzeile ohne Marker formal jede Aussage der
Folie stützt und tatsächlich keine. Der Leser kann nicht erkennen, welche
Aussage auf Literatur ruht und welche eigene ist, und genau darum geht es
beim Zitieren. Mehr als neun Quellen auf einer Folie sind kein
Nummerierungsproblem, sondern ein Zeichen, dass die Folie zu viel trägt.

### 4. Titel müssen tatsächlich passen

Der Cover-Titelplatzhalter der neutralen Vorlage ist **7,4 Zoll** breit und
1,7 Zoll hoch, unten verankert, der Untertitel steht 0,15 Zoll darunter. Ein
zu langer Cover-Titel wird deshalb nicht abgeschnitten. Er wächst nach oben
aus seiner Fläche und bringt das Cover aus dem Gleichgewicht. Eine feste
Zeichengrenze fängt das nicht, weil sie an einem 11,5 Zoll breiten
Inhaltstitel gemessen wurde.

Cover entstehen mit `deck_toolkit.cover()`. Es prüft Titel und Untertitel
gegen die echte Geometrie des Platzhalters und nennt bei einem Befund die
Schriftgröße, die passen würde. `head()` prüft Inhaltstitel entsprechend.
Eine eigene Vorlage unter `07_handwerk/deck_vorlage.pptx` braucht dieselbe
Geometrie, sonst die Konstanten `COVER_*` in `deck_toolkit` anpassen.

### 5. Das gerenderte Deck ansehen

Überlappende Formen, verschobene Spalten und halb leere Kästen erscheinen
nicht im Build-Log. Der Bau ist „sauber“, und die Folie ist trotzdem falsch.
Das Deck als Bilder rendern und ansehen, bevor es übergeben wird. Auf macOS
geht das mit Keynote oder mit LibreOffice
(`soffice --headless --convert-to pdf`), auf Windows mit PowerPoint per
COM-Automatisierung. Eine schon geöffnete Anwendung dabei **nicht** beenden.

### 6. Der volle Name auf jeder Folie

Der volle Name aus `00_kern/einstellungen.json` (Feld `person.name`), nie die
Kurzform, steht auf dem Cover und als kleiner Stempel am Fuß jeder
Inhaltsfolie. Die neutrale Vorlage setzt ihn aus `deck_toolkit.AUTHOR`, ein
Deck-Skript tippt ihn nie selbst ein. Der Grund ist, dass einzelne Folien
weitergereicht werden und ihre Herkunft tragen sollen. Für gemeinsame
Abteilungsdokumente gilt die Ausnahme aus den Kern-Regeln, Abschnitt 1.

## Publikumstreue, keine internen Projektartefakte

Das Publikum eines Decks ist nicht die Person, die das Projekt führt. Nummern
aus dem Arbeitsplan („Arbeitspaket 1.1 und 1.2“), Phasennummern, interne
Dateinamen (`CLAUDE.md`, `Arbeitsplan.md`) und Repo-Pfade (`00_Charter/`,
`03_projekte/...`) sind der eigene Verwaltungsapparat. Ein externer Leser
(Lenkungskreis, Workshopteilnehmer, Kunde) hat keinen Kontext dafür, und ihn
auf der Folie nachzuliefern ist nicht ihr Zweck. Genannt wird die Sache, für
die der Verwaltungsbezug steht, nicht der Bezug selbst.

| Statt | Besser |
|---|---|
| „Arbeitspaket 1.1 und 1.2“ | „welche Ziele am höchsten stehen und wer welche Entscheidung trägt“ |
| „siehe Stakeholder_Map.md“ | (der Inhalt selbst, auf der Folie oder im Anhang) |
| „gibt Phase 4 frei (4.2, 4.3)“ | „gibt den Bau der Abteilungsseite frei“ |

**Nicht betroffen** sind Literaturzitate mit Autor, Werk und Kapitel oder
Abschnitt (etwa „Werner, *Supply Chain Controlling*, Abschn. 5.1“). Das sind
veröffentlichte Quellen, die das Publikum selbst nachschlagen kann. Methode
und Grundlage zu zitieren ist Erwartung dieses Standards, kein Verstoß.

**Durchsetzung.** `save()` in `07_handwerk/deck_toolkit.py` durchsucht den
sichtbaren Text jeder Folie (nicht die Sprechernotizen, die nur der
Vortragende sieht und die interne Bezüge tragen dürfen) nach den typischen
Mustern (Arbeitsplan, Dateinamen auf `.md`, nummerierte Repo-Ordner,
„Phase n.n“) und warnt je Treffer. Eine Warnung beim Bau heißt, dass die
Formulierung vor dem Versand noch geändert werden muss. Löst ein Zitat sie
zufällig aus, wird das Zitat umformuliert, nicht die Prüfung abgeschaltet.
