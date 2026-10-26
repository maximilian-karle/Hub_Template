---
argument-hint: [projekt]
description: Führt die drei Qualitätsprüfungen für ein Projekt aus
---
Führe für das Projekt $1 (im Hub `03_projekte/$1/`, in einem Ast
`projekte/$1/`) folgende Prüfungen aus und fasse die Befunde als kurze
Liste zusammen, nicht als Fließtext.

1. PLAUSIBILITÄT. Vergleiche die aktuellen Werte in
   `data/output/consolidated_master.xlsx` mit der Vorperiode (falls eine
   frühere Fassung im selben Ordner liegt oder in `data_quality_log.md`
   dokumentiert ist). Markiere jede Abweichung über 15 %.

2. VORRANGKONFLIKTE. Gleiche Aussagen aus `data/input/interviews/` gegen
   die Mengen und Werte aus den Quellsystem-Exporten in
   `data/input/exporte/` ab (zum Beispiel SAP, Bankauszug, Backend-Export).
   Liste jeden erkennbaren Widerspruch als offenen Punkt, ohne ihn selbst
   aufzulösen.

3. ABLAUF VON ANNAHMEN. Prüfe in jeder Datei unter `methodology/` das Feld
   „Letzte Validierung“. Liste alle Dateien, deren Validierung mehr als
   drei Monate vor dem heutigen Datum liegt.

Ergebnis ist eine Tabelle mit den Spalten Kategorie, Befund und
Empfehlung, kein Fließtext. Trage neue Befunde zusätzlich in
`data/output/data_quality_log.md` ein.
