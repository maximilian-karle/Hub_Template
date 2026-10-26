---
name: add-literature
argument-hint: [titel] [autor] [dateiname.pdf]
description: Trägt eine neue Quelle samt Inhaltsverzeichnis in Literatur_Index.md ein
---
1. Prüfe, ob $3 unter {{HUB}}/02_bibliothek/ liegt (Hauptordner oder
   Themenordner). Liegt die Datei noch im Hauptordner, verschiebe sie in den
   passenden Themenordner (Tabelle „Ordnerstruktur“ oben im Index). Ordner,
   die mit „_“ beginnen, führen einen eigenen Unterindex und gehören nicht
   hierher.
2. Liegen die ersten 20 Seiten schon als Kontext vor (vom SessionStart-Hook
   geliefert), nutze sie, um Titel, Autor und Inhaltsverzeichnis
   vorzuschlagen. Sonst lies die ersten 20 Seiten von $3 selbst.
3. Ergänze in {{HUB}}/02_bibliothek/Literatur_Index.md einen neuen Abschnitt
   im bestehenden Format, Autor vor Titel:
   ## [Autor], [Titel]
   - **Autor:**
   - **Ordner:** (Themenordner in Backticks)
   - **Datei:**
   - **Relevanz:**
   - **Inhaltsverzeichnis:** (als Liste, so wie im PDF-Auszug erkennbar)
4. Keine Dubletten. Prüfe vorher, ob Titel oder Datei schon im Index stehen.
5. Zeige der Person den Entwurf zur Bestätigung, bevor er gespeichert wird.
   Geratene Kapitelangaben sind schlimmer als keine.
