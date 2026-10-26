"""Muster für Lebenslauf und Anschreiben im Stil der Vorlage.

Erfundene Person, erfundene Firmen. Zeigt Aufbau, Länge und Ton nach
`05_werkstatt/karriere/Profil/Bewerbungsstil.md`. Bauen mit

    python3 07_handwerk/Bewerbung_PDF/render.py 07_handwerk/Bewerbung_PDF/muster/cv_inhalt_muster.py 07_handwerk/Bewerbung_PDF/muster
"""

CV = {
    "sprache": "de",
    "dateiname": "Muster_Lebenslauf.pdf",
    "person": {
        "name": "Alex Beispiel",
        "titel": "M.Sc. Wirtschaftsingenieurwesen",
        "kontakt": ["Musterstraße 1, 12345 Musterstadt", "+49 170 0000000", "alex.beispiel@example.com"],
        "adresse_brief": ["Musterstraße 1", "12345 Musterstadt", "+49 170 0000000", "alex.beispiel@example.com"],
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
    "zusammenfassung": (
        "Als Wirtschaftsingenieur mit Stationen in Handel, Maschinenbau und Beratung verbinde ich "
        "Supply-Chain-Praxis mit Datenanalyse. Bei der Musterwerk GmbH verantworte ich das Reporting "
        "der Lieferantentermintreue und die Disposition für zwei Produktlinien."
    ),
    "reihenfolge": ["erfahrung", "ausbildung"],
    "erfahrung": [
        {"zeit": "04/2025\nheute",
         "kopf": "**Musterwerk GmbH, MUSTERSTADT:** Supply Chain Analyst",
         "punkte": [
             "Monatliches Reporting zur Termintreue von rund 120 Lieferanten aufgebaut, Grundlage der "
             "quartalsweisen Lieferantengespräche im Einkauf",
             "Disposition von zwei Produktlinien mit rund 4.000 Materialien, Reichweite um ein Fünftel gesenkt",
             "Datenmodell aus ERP-Exporten in Python und SQL, Dashboard für Einkauf und Produktion",
         ]},
        {"zeit": "09/2023\n03/2025",
         "kopf": "**Beratung Nord GmbH, HAMBURG:** Werkstudent Operations Consulting",
         "punkte": [
             "Ist-Analyse von Lagerprozessen bei zwei Mittelständlern, Ergebnisse im Lenkungskreis vorgestellt",
             "Angebots- und Projektcontrolling, Auswertungen in Excel und Power BI",
         ]},
        {"zeit": "10/2021\n08/2023",
         "kopf": "**Handelshaus Süd KG, MUSTERSTADT:** Werkstudent Disposition",
         "punkte": [
             "Bestellvorschläge für Filiale und Lager geprüft, Kennzahlen zur Warenverfügbarkeit berichtet",
         ]},
    ],
    "ausbildung": [
        {"zeit": "10/2023\n03/2025",
         "kopf": "**Hochschule Musterstadt, MUSTERSTADT** M.Sc. Wirtschaftsingenieurwesen [Note: 1,7]",
         "beschreibung": [
             "Schwerpunkte Supply Chain Planning und Data Analytics",
             "**Masterarbeit:** Lieferantenbewertung auf Basis von ERP-Bewegungsdaten [Note: 1,3]",
         ]},
        {"zeit": "10/2019\n09/2023",
         "kopf": "**Technische Hochschule Beispielstadt, BEISPIELSTADT** B.Eng. Wirtschaftsingenieurwesen [Note: 2,1]",
         "beschreibung": [
             "Auslandssemester an einer Partnerhochschule in Lissabon, Schwerpunkt Logistik",
         ]},
    ],
    "skills": {
        "kompetenzen": [
            "Disposition und Bestandsmanagement",
            "Lieferantenbewertung und Einkaufscontrolling",
            "Datenanalyse (Python, SQL, Power BI)",
            "KPI-Systeme und Reporting",
        ],
        "zertifikate": [
            ("Mai 2024", "Professional Scrum Master I", "Scrum.org"),
            ("Nov 2022", "Grundlagen Lean Management", "Industrie- und Handelskammer"),
        ],
        "sprachen": [("Deutsch", "Muttersprache"), ("Englisch", "verhandlungssicher"),
                     ("Portugiesisch", "Grundkenntnisse")],
    },
}

BRIEF = {
    "dateiname": "Muster_Anschreiben.pdf",
    "dokument": "Anschreiben",
    "empfaenger": ["Frau Dr. Erika Muster", "Personalabteilung", "Zielfirma AG", "Hauptstraße 10",
                   "54321 Zielstadt"],
    "datum": "01.12.2026",
    "betreff": "Bewerbung als Supply Chain Planner",
    "betreff_zusatz": "Kennziffer 4711, Zielstadt",
    "anrede": "Sehr geehrte Frau Dr. Muster,",
    "absaetze": [
        "auf Ihre Anzeige bin ich über Ihre Karriereseite gestoßen. Mich spricht besonders an, dass "
        "die Stelle Bedarfsplanung und Lieferantensteuerung in einer Hand verbindet, denn genau an "
        "dieser Schnittstelle arbeite ich heute.",
        "Seit April 2025 bin ich Supply Chain Analyst bei der Musterwerk GmbH. Dort habe ich ein "
        "monatliches Reporting zur Termintreue unserer rund 120 Lieferanten aufgebaut, das der Einkauf "
        "heute in jedem Quartalsgespräch nutzt. In der Disposition von zwei Produktlinien haben wir die "
        "Reichweite um ein Fünftel gesenkt, ohne dass die Lieferfähigkeit gelitten hat. Die Daten dafür "
        "führe ich in einem eigenen Datenmodell aus den ERP-Exporten zusammen.",
        "Meinen Master in Wirtschaftsingenieurwesen habe ich im März 2025 an der Hochschule Musterstadt "
        "abgeschlossen, mit einer Masterarbeit zur Lieferantenbewertung aus Bewegungsdaten. Aus meinen "
        "Stationen in der Disposition eines Händlers und in einer Beratung kenne ich außerdem den Blick "
        "auf die Filiale und den Blick des Kunden auf ein Projekt.",
        "Die Zielfirma AG baut nach Ihrem letzten Geschäftsbericht ein zweites Werk auf. Den Hochlauf "
        "der Planung dort mitzugestalten, reizt mich mehr als jede fertige Struktur.",
        "Meine Kündigungsfrist beträgt drei Monate. Über eine Einladung zu einem persönlichen Gespräch "
        "freue ich mich sehr.",
    ],
    "gruss": "Mit freundlichen Grüßen",
    "anlagen_titel": "ANLAGEN",
    "anlagen": ["Lebenslauf", "Zeugnisse", "Zertifikate"],
}
