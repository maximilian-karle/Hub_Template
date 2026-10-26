# Darstellung im Chat

Gilt für `/alter`, `/heute`, `/tutor` und `/editor`. Der Chat ist für den
Lernenden gebaut, nicht für das Skript. Lernen ist anstrengend, jede Nachricht
soll sich mit einem Blick erfassen lassen.

## 1. Klartext statt Kürzel

- Das Modul heißt mit seinem Titel aus der ersten Zeile von `modul.md`, ohne
  ID (aus `# XY2 Datenmodellierung` wird „Datenmodellierung“).
- Das Kapitel heißt mit der Überschrift aus dem Lesepfad, ohne ID (aus
  `## XY2-K00 Gesamtbild und Problemstellung` wird „Gesamtbild und
  Problemstellung“), dazu Werk und Kapitel in Klammern, etwa „(Autor, Kap. 1)“.
- Einen Abschnitt ohne Lesepfad (Karten aus anderen Lernprojekten) nennt der
  Kopf nach dem Lernprojekt und nach Werk und Kapitel der `quelle`.
- Rollen stehen ausgeschrieben (Advisor, Librarian, Tutor, Editor, Roommate),
  nicht als Kürzel. Blöcke (K1, K2) und Abschnitts-IDs (XY2-K00) kommen im
  Chat nicht vor, ebenso keine Befehlsnamen und Dateipfade, außer der Lernende
  soll eine Datei öffnen.
- In Dateien, Skripten und Commit-Meldungen bleiben die IDs, sie sind dort
  technisch nötig.

## 2. Der Kopf

Jede Nachricht, die eine Frage oder Aufgabe stellt, beginnt mit dieser Tabelle,
damit sich der Lernende jederzeit zurechtfindet.

```
| | |
|---|---|
| **Thema** | Datenmodellierung |
| **Kapitel** | Gesamtbild und Problemstellung (Autor, Kap. 1) |
| **Heute** | Wiederholung, Karte 2 von 5 |
```

- „Heute“ nennt Tätigkeit und Fortschritt in Worten (Wiederholung, Test,
  Erklärung prüfen, Lesen), bei Fragen mit „Frage i von n“ oder „Karte i
  von n“.
- Zu Beginn einer Tätigkeit und beim Wechsel des Kapitels kommt eine vierte
  Zeile **Worum es geht** dazu, der Satz stammt aus dem Lesepfad. Fehlt er,
  schreibt ihn der Assistent einmal und trägt ihn dort nach.
- Eine Zeile „Wie geprüft wird“ steht beim Beginn, kurz, etwa „5 Fragen, ich
  bewerte, keine Hilfe“.

## 3. Die Frage

Unter dem Kopf steht die Frage fett, darunter in einer Zeile, was der
Lernende tun soll („Zuversicht in Prozent, dann deine Antwort“). Nichts
anderes in dieser Nachricht.

## 4. Die Rückmeldung

Nach einer Antwort eine Tabelle, danach direkt der Kopf der nächsten Frage.

```
| | |
|---|---|
| **Richtig wäre** | Kurzantwort in ein bis zwei Sätzen |
| **Bei dir** | was fehlte oder falsch war, in einem Satz |
| **Note** | 2 von 5, Kern fehlt |
| **Quelle** | Werk, Kapitel, Seite |
```

Lange Musterantworten stehen nicht im Fließtext, sondern in der ersten Zeile
der Tabelle, auf das Wesentliche gekürzt.

## 5. Bilanz und Ende

Die Bilanz ist eine Tabelle mit den Zahlen links und der Einordnung rechts
(Trefferquote, Zuversicht, Fehler mit Seite, nächster Schritt). Der Stand am
Ende heißt „Heute gelaufen“ und „Als Nächstes“.

## 6. Zeichen

Hervorhebung läuft über Fett, Tabellen und Zitatblöcke. Keine Emojis. Für
Richtung und Ergebnis genügen ↑ ↓ → Σ Δ. Die Schreibregeln aus
`00_kern/regeln.md` gelten unverändert.
