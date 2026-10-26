---
name: job-apply
argument-hint: [stellenanzeige: pfad-zu-pdf | url | eingefügter-text] [firma] [rolle]
description: Liest eine Stellenanzeige ein und erzeugt daraus einen zugeschnittenen Lebenslauf und ein Anschreiben im eigenen Stil, mit Keyword-Abgleich, Fit-Check und Lückenlog
---

Ziel ist, aus der Stellenanzeige $1 (Firma $2, Rolle $3, falls angegeben,
sonst aus der Anzeige abgeleitet) eine vollständige, auf die Anzeige
zugeschnittene Bewerbung im eigenen Stil zu erzeugen. Für jeden Text gelten
`{{HUB}}/00_kern/persoenlich.md` und `{{HUB}}/00_kern/regeln.md`.

Kontext `{{HUB}}/05_werkstatt/karriere/CLAUDE.md`. Alle Pfade unten ohne
Präfix liegen unter `{{HUB}}/05_werkstatt/karriere/`.

## 0. Bereit?

Prüfe still, ob `Profil/Master_CV_Daten.md`, `Profil/Bewerbungsstil.md`,
`Profil/Zielfirmen_Praeferenzen.md` und `Profil/cv_inhalt_basis.py` gefüllt
sind (keine `<Platzhalter>` mehr in den Kernfeldern). Fehlt etwas, sag es in
zwei Zeilen und biete `/einrichten karriere` an. Ohne Master-CV-Daten keine
Bewerbung, denn erfundene Fakten sind schlimmer als eine Lücke.

## 1. Stellenanzeige einlesen

- PDF extrahieren, URL abrufen, Text direkt übernehmen.
- Firma und Rolle aus der Anzeige ableiten, falls nicht mitgegeben.
- Ordner `Bewerbungen/<Firma>_<Rolle>_<JJJJ-MM-TT>/` anlegen, Anzeige dort
  als `Stellenanzeige.md` mit Quelle (Dateiname oder URL).

## 2. Fit-Check

- Gegen `Profil/Zielfirmen_Praeferenzen.md` prüfen (Zielrolle, Branche,
  Region, Remote, Gehalt, Ausschlusskriterien). Ist „Last Validated“ älter als
  drei Monate, kurz nachfragen, ob die Präferenzen noch stimmen.
- Passt die Stelle klar nicht, das kurz sagen und fragen, ob trotzdem weiter.
  Auch bei Abbruch die Stelle mit Gewicht C ins Skill-Gap-Log (Schritt 4).

## 3. Keyword-Abgleich

- Anforderungen aus der Anzeige ziehen (Fachwissen, Werkzeuge, Methoden,
  Soft Skills, Formulierungen), je als Muss oder Wunsch.
- Abgleich gegen `Profil/Master_CV_Daten.md` und
  `Profil/Leistungsdokumentation.md`. Welche eigene Erfahrung deckt welches
  Keyword?
- **Keine Erfindung.** Nur aufgreifen, was durch echte Erfahrung gedeckt ist.
  Lücken offen benennen.
- Ergebnis als `Keyword_Matching.md` im Bewerbungsordner, Tabelle
  Anzeige-Keyword, Muss oder Wunsch, eigene Erfahrung, Quelle (Datei und
  Abschnitt).

## 4. Lücken ins Skill-Gap-Log

Jede Lücke in `{{HUB}}/01_kompass/entwicklung/Skill_Gap_Log.md`. Stelle in die
Stellenliste (Gewicht A Unterlagen erstellt, B nur gesichtet, C Fit-Check
negativ), je Skill die Zählung erhöhen und M oder W mit Stellennummer
vermerken. Neue Skills als neue Zeile im passenden Cluster.

## 5. Lebenslauf

- `Profil/cv_inhalt_basis.py` nach `Bewerbungen/<Ordner>/inhalt.py`
  kopieren. Ist die Anzeige in einer anderen Sprache als die Basis, den
  Inhalt dort übersetzen und `"sprache"` setzen, Überschriften mit.
- In `inhalt.py` nur auswählen und umformulieren, nie Fakten ändern. Titel im
  Kopf auf die Zielrolle, Zusammenfassung auf die Anzeige, Reihenfolge der
  Kompetenzen und der Punkte je Station nach den Keywords aus Schritt 3,
  Wortlaut der Anzeige übernehmen, wo er fachlich gedeckt ist.
- Alle Vorgaben aus `Profil/Bewerbungsstil.md` (Länge, Foto, Reihenfolge,
  Form der Punkte, was immer drin sein muss und was nie).

## 6. Anschreiben

- Nur, wenn `Bewerbungsstil.md` es als Standard vorsieht oder die Anzeige es
  verlangt. Sonst `BRIEF` aus `inhalt.py` entfernen.
- `BRIEF` füllen. Empfänger, Betreff mit Kennziffer, Datum, Anrede und Gruß
  nach `Bewerbungsstil.md`. Einstieg und Motivation für genau diese Firma, kein
  Textbaustein. Zwei bis drei belegte Ergebnisse aus Schritt 3, die am
  stärksten zur Anzeige passen. Ton, Aufbau und Wortliste nach
  `Bewerbungsstil.md`.
- Gehalt und Kündigungsfrist nur, wenn die Anzeige danach fragt, Werte aus
  `Zielfirmen_Praeferenzen.md`, die Zahl je Stelle mit mir festlegen.

## 7. Rendern und ansehen

```bash
python3 {{HUB}}/07_handwerk/Bewerbung_PDF/render.py <ordner>/inhalt.py <ordner> --final
```

`--final` bricht bei offenen `[Platzhaltern]` ab, Gestaltung und Seitenzahl
kommen aus `Profil/stil.json`. Meldet das Skript „ZU LANG“, kürzen, nicht die
Schrift verkleinern, außer `Bewerbungsstil.md` erlaubt es. Die PDFs als Bild
ansehen, bevor du fertig meldest.

## 8. Vertraulichkeit und Belege

- Was aus `Leistungsdokumentation.md` kommt und interne Namen oder Zahlen
  enthalten könnte, nach `{{HUB}}/00_kern/vertraulichkeit.md` prüfen, sensible
  Stellen mit `[ANONYMISIEREN: ...]` markieren statt sie zu übernehmen.
- Jede Station, jeden Titel, jeden Zeitraum, jede Note und jedes
  Sprachniveau gegen `Profil/Nachweise_Index.md` prüfen. Ein Titel, der vom
  Zeugnis abweicht, kostet mehr als ein fehlendes Keyword.
- Anlagen aus `Profil/Nachweise/00_Bewerbungsmappe/`, falls vorhanden, sonst
  Hinweis auf `mappe.py`.

## 9. Status und Ausgabe

- In `Profil/Zielfirmen_Praeferenzen.md` die Firma auf „beworben“ setzen oder
  die Zeile ergänzen.
- Kurze Zusammenfassung im Chat. Firma, Rolle, stärkste Keyword-Treffer,
  Lücken, offene Punkte, Pfad zum Ordner. Keine vollen Dateiinhalte. Den
  Versand macht die Person selbst.
