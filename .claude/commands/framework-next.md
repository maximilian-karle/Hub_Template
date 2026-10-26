---
description: Arbeitet genau den nächsten offenen Punkt des Framework-Scans (06_wissen/frameworks) ab
---
Wir scannen die Bibliothek nach Frameworks. Arbeite in dieser Session genau
EINEN Punkt aus `06_wissen/frameworks/Scan_Workplan.md` ab und hör danach auf.
Antworte in `sprache.chat`, Dateien in `sprache.hub` (beides in
`00_kern/einstellungen.json`).

Ist die Bibliothek noch leer oder der Workplan ohne Punkte, sag das und
schlag vor, zuerst Werke abzulegen (`/add-literature`) und dann Punkt A1 zu
starten.

## 1. Einlesen, bevor du etwas änderst

- `06_wissen/frameworks/Scan_Workplan.md` vollständig
- `06_wissen/frameworks/README.md` (Lebenszyklus, Aufnahmekriterien, Tabellen)
- `06_wissen/frameworks/_Template_Framework.md`
- `CLAUDE.md` der Wurzel, Abschnitt 6 (Bibliothek und Frameworks)
- `git log --oneline -10 -- 06_wissen/frameworks 02_bibliothek`

## 2. Den nächsten Punkt bestimmen

$ARGUMENTS

- Ist oben eine Punktnummer angegeben (z. B. `C3`), nimm diesen Punkt.
- Sonst der erste Punkt in der Reihenfolge A → B → C → D, dessen Status-Zelle
  nicht mit `**Done` beginnt. Ein Punkt mit `**Waiting (user: …)**` wird nicht
  bearbeitet. Sag mir, welche Entscheidung fehlt, und stopp.
- Nenne mir in höchstens zehn Zeilen: Punkt, Akzeptanzkriterien, welche Kapitel
  du lesen wirst. Dann fang an.

## 3. Umsetzen

- Kapitel im Volltext lesen: Text per pypdf aus dem PDF ins Scratchpad ziehen,
  Seitenbereiche über die Lesezeichen bestimmen (`get_destination_page_number`).
  Nicht aus dem Inhaltsverzeichnis auf den Inhalt schließen.
- Keine Aussage über ein Kapitel, das nicht gelesen wurde. Was offen bleibt,
  kommt in Abschnitt 8 der Framework-Datei.
- Quellen immer mit Werk und Kapitel, kein wörtliches Zitat über 15 Wörter.
- Eigenständig denken (CLAUDE.md Abschnitt 6, Schritt 2): Die Synthese muss
  mehr sein als die Summe der Quellen. Widersprüche zwischen den Quellen
  benennen, nicht glätten.
- Eine Datei nur, wenn die Aufnahmekriterien aus dem README erfüllt sind.
  Fehlt das Testprojekt, bleibt es eine Kandidatenzeile.
- Frameworks, deren Testprojekt in einem Ast liegt, stehen im Hub nur als
  Registereintrag in `README.md` mit dem Namen des Asts in der Spalte Ort, die
  Datei selbst liegt dort unter `01_frameworks/`. Die Erprobung läuft im Ast,
  im Hub wird danach nur die Registerzeile nachgezogen.
- Entscheidungen, die meine sind (Testprojekt, Reihenfolge, Zusammenlegen,
  Ausmustern): vorbereiten, als `**Waiting (user: …)**` markieren, stoppen.
- Ein Nebenbefund (fehlender Index-Eintrag, falsche Kapitelangabe) wird nicht
  nebenbei groß umgebaut: kleine Korrektur ja, sonst als offener Punkt melden.

## 4. Dokumentieren

- `Scan_Workplan.md`: die Status-Zelle des Punkts beginnt mit
  `**Done <dd.mm.yyyy>.**` und einem Satz Ergebnis. Neue C-Punkte aus B1 dort
  anlegen.
- `README.md`: Tabellen nachziehen (Datei, Status, Testprojekt).
- `02_bibliothek/Literatur_Index.md`: bei den genutzten Werken auf die
  Framework-Datei verweisen.

## 5. Abschluss

Kurze Zusammenfassung. Was entstanden ist, was nicht gelesen wurde,
welche Entscheidung von mir offen ist und welcher Punkt als Nächstes dran ist.
Frag mich, ob committet und gepusht werden soll (direkt auf `main`). Danach
keine weitere Arbeit in dieser Session.
