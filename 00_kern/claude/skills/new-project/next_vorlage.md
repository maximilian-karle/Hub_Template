---
description: Arbeitet genau das nächste offene Arbeitspaket von <Projektname> ab und gibt dazu den Leseeintrag aus
argument-hint: [optional: Paketnummer, z. B. AP-1.1]
---
Wir arbeiten an <Projektname>. Arbeite in dieser Session genau EIN
Arbeitspaket ab und hör danach auf. Antworte im Chat auf Deutsch. Sag in der
ersten Zeile, welches Paket diese Session bearbeitet. Termine im Arbeitsplan
sind Obergrenzen, gearbeitet wird so schnell wie möglich.

## 1. Einlesen, bevor du etwas änderst

- `<Projektordner>/CLAUDE.md`
- `<Projektordner>/00_Charter/Arbeitsplan.md` vollständig, mit den Entscheidungen
- `<Projektordner>/00_Charter/Offene_Punkte.md`
- `<Projektordner>/00_Charter/Lesepfad.md` und der Kern-Lesepfad im Hub
  `<Hub>/01_kompass/module/<Modul-ID>_<kurzname>/lesepfad.md`, falls das Projekt
  einem Modul zugeordnet ist
- `git status` und `git log --oneline -10`. Uncommittete Änderungen einer
  anderen Session fasst du nicht an, nenn sie und stopp.

## 2. Das nächste Paket bestimmen

$ARGUMENTS

- Ist oben eine Paketnummer angegeben, nimm dieses Paket.
- Sonst das erste Paket in der Reihenfolge der Tabellen, dessen Zelle „Was“
  nicht mit `**Erledigt` beginnt und dessen Abhängigkeiten erledigt sind.
  Liegt ein Paket nur bei mir oder einer anderen Person, nenn es als offen
  und nimm das nächste, das diese Session bearbeiten kann.
- Ist das Paket blockiert (Entscheidung, Zugang, fehlende Daten), sag das und
  stopp.

## 3. Paket erklären und Leseeintrag ausgeben, vor jeder Änderung

- **Worum es geht.** Zwei bis vier Sätze in einfachen Worten, Fachwörter beim
  ersten Auftreten in einem Halbsatz erklärt. Paketnummern allein genügen nie.
- **Lektüre als Tabelle** je Abschnitt der Spalte LP (Werk, Kapitel, Seiten,
  Minuten, Pflicht oder Vertiefung), darunter unverändert Warum jetzt, Worauf
  achten, Wo es steckt und die Kontrollfragen. Eine ID `<Modul-ID>-Knn` liest
  du aus dem Kern-Lesepfad im Hub, `LP-nn` aus dem Lesepfad des Projekts.
- Kam ein Abschnitt schon bei einem früheren Paket, nur die Kontrollfragen
  und der Hinweis, wo er vollständig stand.
- „kein Eintrag“ sagst du ausdrücklich mit Grund. Passt der Eintrag nicht zum
  Paket, meld das als Lücke und schlag einen Abschnitt vor.
- Steht ein Erklär-Check in der Spalte, gib die Aufgabe aus dem Abschnitt
  „Erklär-Check nach jedem Gate“ aus.

## 4. Plan nennen und umsetzen

- In höchstens zehn Zeilen Paket, Ergebnis „fertig, wenn“, Plan und Dateien.
  Dann fang an. Rückfragen nur bei einer Entscheidung, die laut Arbeitsplan
  bei mir liegt.
- Regeln aus der `CLAUDE.md` des Projekts und des Repos gelten vollständig.
- Tests laufen grün, bevor du fertig meldest.
- Gehört eine Designentscheidung zum Paket, entsteht das ADR in `docs/adr/`
  nach `ADR-000_Vorlage.md`, mit Literaturstelle.
- Ändert das Paket, was ein Leseeintrag unter „Wo es steckt“ beschreibt, zieh
  den Eintrag im Lesepfad des Projekts nach. Den Kern-Lesepfad im Hub änderst
  du nicht, eine nötige Änderung nennst du als Vorschlag.

## 5. Dokumentieren

- `Arbeitsplan.md`, die Zelle „Was“ beginnt mit `**Erledigt TT.MM.JJJJ.**`
  und einem Satz Ergebnis.
- `Offene_Punkte.md` nachziehen.
- Ein Befund außerhalb des Pakets wird nicht nebenbei behoben, sondern als
  neues Paket vorgeschlagen.
- Ist ein Gate erreicht, schlag den Rückfluss in den Hub vor (Lernkarte,
  Framework, Case Study), anonymisiert nach `vertraulichkeit.md`. Gehört das
  Projekt zu einem Modul, nennst du die Zeile im Register
  `<Hub>/01_kompass/module/<Modul-ID>_<kurzname>/projekte.md`, die nachzuziehen
  ist (Gate, Case Study, Prüfung).

## 6. Abschluss

Ergebnis, Teststand und das nächste Paket, danach die Kontrollfragen des
Leseeintrags ohne Antwort. Frag, ob committet werden soll, und nenn die
Dateien. Für das nächste Paket schreibst du nach
`<Projektordner>/00_Charter/Vorbereitung/Vorbereitung_<AP>.md` die
Kurzerklärung, die Lektüre als Tabelle mit Minuten und Summe und die
Kontrollfragen, damit ich vorher lesen kann. Danach keine weitere Arbeit in
dieser Session.
