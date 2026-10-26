"""Basisinhalt Lebenslauf und Anschreiben.

Quelle der Fakten ist `05_werkstatt/karriere/Profil/Master_CV_Daten.md`. Jede
Station, jeder Titel, jeder Zeitraum und jede Note wird gegen
`Profil/Nachweise_Index.md` geprüft. `/einrichten` (Schritt karriere) füllt
diese Datei als `Profil/cv_inhalt_basis.py`, `/job-apply` kopiert die Basis
in den Bewerbungsordner und schneidet dort Zusammenfassung, Reihenfolge der
Punkte und das Anschreiben auf die Anzeige zu. Fakten werden dabei nie
verändert, nur ausgewählt und umformuliert.

Kopfzeile je Station als "**Firma, ORT:** Rolle", Zeitraum zweizeilig
"von\\nbis". **x** wird fett gesetzt. Text in [eckigen Klammern] ist ein
Platzhalter, `render.py --final` bricht ab, solange einer offen ist.
"""

CV = {
    "sprache": "de",
    "dateiname": "Lebenslauf_[Vorname_Nachname].pdf",
    "person": {
        "name": "[Vorname Nachname]",
        "titel": "[Abschluss oder Berufsbezeichnung]",
        "kontakt": ["[Straße Nr., PLZ Ort]", "[Telefon]", "[E-Mail]", "[LinkedIn, optional]"],
        "adresse_brief": ["[Straße Nr.]", "[PLZ Ort]", "[Telefon]", "[E-Mail]"],
    },
    "ueberschriften": {
        "dokument": "Lebenslauf",
        "zusammenfassung": "Zusammenfassung",
        "erfahrung": "Praktische Erfahrung",
        "ausbildung": "Akademische Ausbildung",
        "skills": "Skills",
        "kompetenzen": "Kompetenzfelder",
        "zertifikate": "Zertifikate",
        "sprachen": "Sprachen",
    },
    # Optional, verdichtet einen ausführlichen Lebenslauf, etwa "7.8pt".
    # "schriftgroesse": "7.8pt",
    "zusammenfassung": "[Drei Sätze. Wer ich bin, was ich kann, was ich suche.]",
    "reihenfolge": ["erfahrung", "ausbildung"],
    "erfahrung": [
        {"zeit": "[MM/JJJJ]\nheute",
         "kopf": "**[Firma], [ORT]:** [Rolle]",
         "punkte": [
             "[Ergebnis mit Zahl, Verb am Anfang]",
             "[Ergebnis mit Zahl]",
         ]},
    ],
    "ausbildung": [
        {"zeit": "[MM/JJJJ]\n[MM/JJJJ]",
         "kopf": "**[Hochschule], [ORT]** [Abschluss] [Note: x,x]",
         "beschreibung": ["[Schwerpunkte]", "**Abschlussarbeit:** [Titel] [Note: x,x]"]},
    ],
    "skills": {
        "kompetenzen": ["[Kompetenz 1]", "[Kompetenz 2]", "[Kompetenz 3]"],
        "zertifikate": [("[Mon JJJJ]", "[Zertifikat]", "[Aussteller]")],
        "sprachen": [("Deutsch", "Muttersprache"), ("Englisch", "[Niveau]")],
    },
}

BRIEF = {
    "dateiname": "Anschreiben_[Vorname_Nachname].pdf",
    "dokument": "Anschreiben",
    "empfaenger": ["[Ansprechperson]", "[Abteilung]", "[Firma]", "[Straße Hausnummer]", "[PLZ Ort]"],
    "datum": "[TT.MM.JJJJ]",
    "betreff": "Bewerbung als [Position]",
    "betreff_zusatz": "[Kennziffer, Ort]",
    "anrede": "[Anrede nach Profil/Bewerbungsstil.md]",
    "absaetze": [
        "[Einstieg, warum diese Stelle bei dieser Firma, konkret und ohne Floskel]",
        "[Zwei bis drei belegte Ergebnisse, die am stärksten zur Anzeige passen]",
        "[Was ich in den ersten Monaten beitrage, Abschluss mit Gesprächswunsch]",
    ],
    "gruss": "Mit freundlichen Grüßen",
    "anlagen_titel": "ANLAGEN",
    "anlagen": ["Lebenslauf", "Zeugnisse"],
}
