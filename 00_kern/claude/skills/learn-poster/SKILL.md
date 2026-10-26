---
name: learn-poster
argument-hint: [thema] [optional: zielordner]
description: Erstellt zu einem Thema einen kompakten Hilfszettel (A4) und eine handgezeichnete Mind Map als Poster (A3)
---
Ziel: zu $1 ein Lernpaar bauen. Der Hilfszettel erklärt jeden Begriff dicht
in fünf Spalten. Die Mind Map zeigt alle Begriffe und ihre Zusammenhänge auf
einem Blatt, gezeichnet wie von Hand. Beide entstehen aus derselben
Themendatei, nie getrennt.

Werkzeug: `{{HUB}}/07_handwerk/learning_poster/build_poster.py`
Muster: `{{HUB}}/07_handwerk/learning_poster/beispiel/ki_beratung.json`. Das Feld
`author` kommt aus `person.name` in `{{HUB}}/00_kern/einstellungen.json`.

1. **Auftrag spiegeln.** In drei Sätzen zurückgeben, was das Thema umfasst
   und wofür es gebraucht wird (Interview, Projekt, Prüfung). Eine Rückfrage,
   falls der Umfang unklar ist, sonst weiter.
2. **Begriffe erheben.** Zuerst den Information Hub prüfen
   (`{{HUB}}/02_bibliothek/Literatur_Index.md`, Methodenkoffer), dann im Netz
   recherchieren, welche Begriffe aktuell tatsächlich fallen
   (Stellenanzeigen, Herstellerdokumentation, Fachglossare). Nicht aus dem
   Gedächtnis auffüllen, was sich prüfen lässt.
3. **Felder bilden.** Die Begriffe in höchstens acht Felder ordnen (mehr
   Farben hat die Palette nicht). Jedes Feld bekommt eine Leitfrage und,
   außer dem letzten, ein Verb zum nächsten Feld (`next`). Die Felder
   ergeben in dieser Reihenfolge einen Satz, das ist der Lesepfad auf dem
   Poster. Richtwert sind 60 bis 80 Begriffe, je Feld 8 bis 14.
4. **Themendatei schreiben** nach dem Muster, je Begriff
   - `t` Begriff im Original, wie er im Gespräch fällt
   - `s` Kurzform für das Poster, höchstens 66 Zeichen
   - `e` Erklärung in ein bis zwei Sätzen, ohne Fachwort, das nicht selbst
     auf dem Blatt steht
   - `x` Beispiel oder Einsatz, möglichst aus der eigenen Arbeit
   - `l` zwei bis vier verwandte Begriffe, exakt wie in `t` geschrieben,
     bevorzugt aus anderen Feldern
   - `lv` Stand: `nutze`, `kenne` oder `neu`. Als Einschätzung
     kennzeichnen, der Nutzer korrigiert sie.
   Dazu vier bis sechs Merksätze, die über einzelne Begriffe hinausgehen
   (sie hängen als Notizzettel in der Mitte des Posters). Farben je Feld aus
   der Edelstein-Palette.
5. **Bauen und ansehen.**
   `python {{HUB}}/07_handwerk/learning_poster/build_poster.py <datei.json> --preview <scratchpad>`
   Jede Vorschauseite ansehen. Abgeschnittene Zeilen, Text über dem
   Blattrand oder Notizzettel auf einem Ast sind Fehler, auch wenn der Bau
   durchläuft. Hinweise „check on the poster" und „check on the sketch" aus
   dem Protokoll einzeln prüfen. Ein geöffnetes PDF wird nicht überschrieben,
   das Protokoll sagt es.
6. **Übergeben.** Beide PDFs nennen, die Zahl der Begriffe je Stand, und
   was bei der Recherche nicht belegt werden konnte.

Ablage: ohne Angabe von $2 in
`{{HUB}}/01_kompass/entwicklung/Lernposter/`, bei
Projektthemen im jeweiligen Projektordner unter `docs/`.

Sprache: Erklärungen auf Deutsch mit echten Umlauten, Fachbegriffe im
Original. Keine Gedankenstriche, kein Doppelpunkt als Satzverbinder, keine
Emojis.
