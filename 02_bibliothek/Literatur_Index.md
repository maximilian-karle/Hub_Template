# Literatur-Index

Ein Eintrag je Werk mit Inhaltsverzeichnis, damit ein Blick in diese Datei
reicht, um zu wissen, ob und wo sich ein Nachschlagen lohnt. Neue PDFs
erkennt ein Hook beim Sitzungsstart (SessionStart), `/add-literature` trägt
sie hier mit Inhaltsverzeichnis ein. Ordner, die mit `_` beginnen, überspringt
der Hook (etwa `_Skripte` für Vorlesungsunterlagen mit eigenem Index).

Urheberrechtlich geschützte Werke gehören nur in ein privates Repo.

---

## Ordnerstruktur

Die Werke liegen in Themenordnern, der Index bleibt eine Datei. Jeder
Eintrag nennt seinen Ordner in der Zeile „Ordner". Ein neues PDF kann im
Hauptordner oder direkt im Themenordner abgelegt werden, der
SessionStart-Hook findet beides.

| Ordner | Inhalt |
|---|---|
| `Supply_Chain_und_Operations/` | SCM, Produktion, Logistik, Einkauf, Standortplanung, Supply Chain Controlling |
| `Finance_und_Controlling/` | Bilanzanalyse, Corporate Finance, Erfolgsrechnung |
| `Consulting/` | Beratungsprozess, Beratungsmethoden, Szenariotechnik |
| `Transformation_OpEx_und_Change/` | Transformation, Restrukturierung, Operational Excellence, Change Management |
| `KI_und_Daten/` | KI und Digitalisierung in der Supply Chain, Machine Learning, Sprachmodelle, KI-Regulierung |
| `Mathematik_und_Informatik/` | Mathematik, Stochastik und Logik als Fundament für Machine Learning |
| `Software_Engineering/` | Softwarehandwerk für die eigene Pipeline: Testen, Refactoring, Arbeiten mit bestehendem Code |
| `Lernen_und_Wissensarbeit/` | Lernforschung und Kognitionspsychologie als Grundlage für das Lernsystem nach ALTER |
| `Curricula/` | Modulhandbücher als Landkarte für das eigene Lernzielbild |
| `Sprachen/` | Englisch (IELTS) und Italienisch als Prüfungs- und Lernliteratur |
| `Forschungsmethodik/` | Fallstudien- und Design-Science-Methodik für wissenschaftliches Arbeiten |

---

## Global Supply Chain and Operations Management
- **Autor:** Ivanov, Tsipoulanidis, Schoenberger, 4th Edition (2025), Springer
  Texts in Business and Economics
- **Ordner:** `Supply_Chain_und_Operations/`
- **Datei:** Ivanov_Global Supply Chain and Operations Management.pdf
- **Relevanz:** Footprint-Entscheidungen, Netzwerk-Design, methodische
  Grundlage für die Forecast-Bias-Berechnung. Kap. 5 ist eine Quelle für die
  Segmentierung von Beschaffungsstrategien. Kap. 11 (Gütemaße, Bias vor
  minimalem Fehler in Sect. 11.2.3) und Sect. 12.5 (eingefrorener Plan,
  rollierende Planung) tragen die Steuerung von Prognoserevisionen. Revisionen
  zwischen Meldungen behandelt das Kapitel selbst nicht, auch Tracking-Signal
  und Lewis-Skala stehen nicht darin. Kap. 12 (Sect. 12.4 Produktmix als
  lineares Programm mit Komponentenbestand als Nebenbedingung, Sect. 12.6
  Stücklistenauflösung und Nettobedarf) ist die Hauptquelle für
  Baubarkeitsprüfungen beim Auslauf von Produkten.
- **Inhaltsverzeichnis:**
  - Part I Introduction to SCOM (Ch. 1 Basics, Ch. 2 Industry Examples,
    Ch. 3 Analytics & Model-Based Decision-Making)
  - Part II Designing Operations and Supply Network, Strategic (Ch. 4
    Strategy, Facility Location, Network Design, Sourcing/Procurement,
    Process Design, Capacity, Ch. 5 bis 9)
  - Part III Planning and Executing, Tactical/Operational (Ch. 11 Demand
    Forecasting, Ch. 12 MRP, Ch. 13 Inventory Management, Ch. 14
    Scheduling/Routing)
  - Part IV Advanced Topics (Ch. 15 SC Risk Management & Resilience,
    Ch. 16 Digital SC/Industry 4.0, Ch. 17 Pricing/Revenue Management,
    Ch. 18 Yield Management)

## Introduction to Supply Chain Analytics
- **Autor:** Dmitry Ivanov (2024, Springer, Classroom Companion: Business)
- **Ordner:** `Supply_Chain_und_Operations/`
- **Datei:** Ivanov_Introduction to Supply Chain Analytics.pdf
- **Relevanz:** methodische Grundlage für Optimierung, Simulation
  (AnyLogic/anyLogistix), Bestandssteuerung. Sect. 2.1 deckt sich fast
  wörtlich mit Kap. 11 des großen Ivanov-Bandes und bringt zur Steuerung von
  Prognoserevisionen nichts Eigenes. Sect. 1.4 und 2.3 (lineares Programm für
  den Produktmix, als Solver-Beispiel) sind Nebenquelle für
  Baubarkeitsprüfungen beim Produktauslauf.
- **Inhaltsverzeichnis:**
  - Ch. 1 Analytics and Model-Based Decision-Making Support
  - Ch. 2 Demand Forecasting, Production Planning, and Inventory Control
  - Ch. 3 Discrete Event Simulation of Manufacturing Processes and
    Inventory Control (Queuing Theory, Little's Law, Bottleneck
    Analysis/Theory of Constraints)
  - Ch. 4 Facility Location Planning and Network Optimization (anyLogistix)
  - Ch. 5 Supply Chain Risk and Resilience Analytics (Sect. 5.4 Digital
    Twin-Based Supply Chain Analytics)

## Computational Intelligence in Logistik und Supply Chain Management
- **Autor:** Thomas Hanne, Rolf Dornberger (2023, Springer Gabler)
- **Ordner:** `Supply_Chain_und_Operations/`
- **Datei:** Hanne_Computational Intelligence in Logistik und Supply Chain Management.pdf
- **Relevanz:** Metaheuristiken/KI-Methoden für Standort-, Routing- und
  Losgrößenprobleme, Ergänzung zu quantitativer Optimierung im
  Network Design
- **Inhaltsverzeichnis:**
  - Kap. 2 Grundlagen Computational Intelligence
  - Kap. 3 Transportprobleme (Travelling-Salesman-Problem, Vehicle-Routing-Problem)
  - Kap. 4 Bestandsplanung und Losgrößenbestimmung
  - Kap. 5 Scheduling
  - Kap. 6 Standortplanung (Weber-Problem, Location-Routing, Hub-Standorte,
    Multi-Echelon-Netzwerkgestaltung)
  - Kap. 7 Intelligente Software für die Logistik

## KI in der Supply Chain
- **Autor:** Heiko Ziegeler (2026, Springer Gabler)
- **Ordner:** `KI_und_Daten/`
- **Datei:** Ziegeler_KI in der Supply-Chain.pdf
- **Relevanz:** Management- und Impulsbuch, bewusst ohne Formeln, nützlich
  für die Argumentationsseite von KI-Vorhaben (Nutzen identifizieren,
  Scheiterngründe, Regulatorik), nicht als Methodenquelle. Für die
  quantitative Bewertung bleibt Goudz/Erdogan der Einstieg, dort steht
  Wirtschaftlichkeit je Anwendungsfall. Eigenständiger Beitrag gegenüber
  jenem Titel ist Kap. 6 (Scheiternsmuster).
- **Inhaltsverzeichnis:**
  - Kap. 1 Lieferketten am Limit
  - Kap. 2 Mind the Gap
  - Kap. 3 Die Supply Chain als strategisches Asset
  - Kap. 4 KI konkret: Nutzen für die eigene Supply Chain identifizieren
  - Kap. 5 Hausaufgaben: das Unternehmen fit für KI machen
  - Kap. 6 Die Kunst des Scheiterns, wie man eine Supply Chain mit KI ruiniert
  - Kap. 7 Spielregeln: Regulation, Datenschutz, Nachhaltigkeit
  - Kap. 8 Lieferketten neu denken: strategische Vision

## Künstliche Intelligenz im Supply Chain Management, Potenziale und Grenzen der KI
- **Autor:** Alexander Goudz, Sibel Erdogan (2024, Springer, Reihe IT kompakt)
- **Ordner:** `KI_und_Daten/`
- **Datei:** Goudz_Künstliche Intelligenz im Supply Chain Management, Potenziale und Grenzen der KI.pdf
- **Relevanz:** KI-Anwendungsfelder Beschaffung/Lagerung/Planung mit
  Kosten-Zeit-Qualität-Quantifizierung je Konzept
- **Inhaltsverzeichnis:**
  - Kap. 2 Grundlagen der KI (Industrie 4.0, Historie, neuronale Netze,
    Machine Learning, Deep Learning)
  - Kap. 3 Digitalisierung der Supply Chain
  - Kap. 4 Anwendungsgebiete: Beschaffung, Lagerung & Kommissionierung,
    Planung/Bestandsmanagement, je mit Ist-Analyse, Konzept, Wirtschaftlichkeit, KPIs

## Logistische Modelle der innerbetrieblichen Lieferkette
- **Autor:** Peter Nyhuis, Matthias Schmidt (2025, Springer)
- **Ordner:** `Supply_Chain_und_Operations/`
- **Datei:** Nyhuis_Logistische Modelle der innerbetrieblichen Lieferkette.pdf
- **Relevanz:** Trichtermodell, Durchlaufdiagramm, Bestandskennlinien.
  Grundlage für Engpassanalyse und Losgrößenbestimmung in der
  Produktionslogistik. Kap. 1.5 (Zielsystem mit veränderlicher Gewichtung,
  Entkopplungspunkt-Logik) stützt Kennzahlensysteme mit konkurrierenden
  Zielen.
- **Inhaltsverzeichnis:**
  - Kap. 4 Das Arbeitssystem, Trichtermodell, Durchlaufelement
  - Kap. 6 Der Produktionsbereich, Engpassorientierte Logistikanalyse
    (Ressourcensicht)
  - Kap. 7 Das Lager, Lagerdurchlaufdiagramm, Lagerkennlinie,
    Servicegradkennlinie
  - Kap. 8 Losgrößenbestimmung (durchlauforientiert, multikriteriell,
    fremdbeschafftes Material)
  - Kap. 9 Ausgewählte Modellierungsgrundlagen

## Mehrstufige Standortplanung unter ökonomisch-ökologischen Nachhaltigkeitsaspekten
- **Autor:** Jens Christian (2026, Dissertation, Springer, Reihe Produktion
  und Logistik)
- **Ordner:** `Supply_Chain_und_Operations/`
- **Datei:** Christian_Mehrstufige Standortplanung unter ökonomisch-ökologischen Nachhaltigkeitsaspekten.pdf
- **Relevanz:** Standortplanung unter CBAM/Emissionszöllen mit
  stochastischem/CVaR-Ansatz, direkt relevant für
  Netzwerk-Design-Entscheidungen unter regulatorischer Unsicherheit
- **Inhaltsverzeichnis:**
  - Kap. 3 Mathematisches Modell für die mehrstufige Standortplanung mit
    Emissionszöllen (SND-CT-CP)
  - Kap. 4 Numerische Untersuchungen zum SND-CT-CP
  - Kap. 6 Numerische Ergebnisse der Fix&Optimize-Heuristik
  - Kap. 7 Mathematische Modellformulierungen unter stochastischen
    Emissionsobergrenzen (S-SND-CT-CP)

## Operational Excellence für die Logistik
- **Autor:** Thomas Liebetruth (2026, Springer Gabler, Reihe essentials;
  OTH Regensburg), Praxisimpuls zu Führung und Kultur von Maj-Britt Pohlmann
- **Ordner:** `Transformation_OpEx_und_Change/`
- **Datei:** Liebetruth_Operational Excellence für die Logistik.pdf
- **Relevanz:** Vier-Perspektiven-Rahmen (Prozesse & Qualität, People &
  Culture, Finanzen & Steuerung, Technologie & Innovation), der Lean, SCM und
  Change Management unter einem Dach zusammenführt. Eignet sich als
  Abnahmetest für ein Transformationsraster. Kap. 3.3 (Transparenz und
  Effizienz) ist anschlussfähig an Werner, Supply Chain Controlling, Kap. 5.
  Kap. 2.3 ergänzt Lauer um die Umsetzungsseite. Kompakt (57 Seiten), daher
  Strukturgeber statt Nachschlagewerk.
- **Inhaltsverzeichnis:**
  - Kap. 1 Perspektiven der Operational Excellence (Prozesse & Qualität,
    People & Culture, Finanzen & Steuerung, Technologie & Innovation,
    Zusammenspiel der Perspektiven)
  - Kap. 2 Konzepte für Exzellenz (Lean Management/KVP, Supply Chain
    Management, Change Management, Design Thinking, Unternehmenskultur &
    Führungsverständnis, Zwischenfazit: kein Konzept wirkt allein)
  - Kap. 3 Toolbox, Instrumente für die Praxis, gegliedert nach den vier
    Perspektiven
  - Kap. 4 Organisatorische Verankerung von Operational Excellence
  - Kap. 5 Fazit und Ausblick

## Optimierungen und Cost Savings im Supply Chain Management
- **Autor:** Marc Helmold (2025, Springer Gabler)
- **Ordner:** `Supply_Chain_und_Operations/`
- **Datei:** Helmold_Optimierungen und Cost Savings im Supply Chain Management.pdf
- **Relevanz:** Cost-Saving-Systematik (Design-/Non-Design-/Prozess-Cost
  Savings), Working Capital, Lieferantenmanagement, direkt anwendbar für
  Cost-to-Serve-Analysen. Sect. 1.3.4 liefert die engste der gängigen
  Working-Capital-Definitionen (nur Verbindlichkeiten aus L+L, nicht alle
  kurzfristigen Verbindlichkeiten). Kap. 9 ist eine Quelle für die
  Segmentierung von Beschaffungsstrategien. Kap. 3 (Sect. 3.6 brutto/netto,
  Sect. 3.8 Cost Reduction gegen Cost Avoidance) trägt die Bewertung von
  Komplettierungskäufen beim Produktauslauf.
- **Inhaltsverzeichnis:**
  - Kap. 1 SCM-Grundlagen und Finanzkennzahlen (ROI, Working Capital)
  - Kap. 3 Arten von Cost Savings (Design/Non-Design/Prozess, brutto/netto,
    Cost Reduction vs. Cost Avoidance)
  - Kap. 5 Market-Test/Benchmarking/Landed-Cost-Analysen/Global Sourcing
  - Kap. 9 Upstream Supply Chain Management/Lieferantenmanagement
  - Kap. 13 Verhandlungen: Tipps und Techniken

## Produktionsplanung und -steuerung im Hannoveraner Lieferkettenmodell
- **Autor:** Matthias Schmidt, Peter Nyhuis (2021, Springer Vieweg)
- **Ordner:** `Supply_Chain_und_Operations/`
- **Datei:** Schmidt_Produktionsplanung und -steuerung im Hannoveraner Lieferkettenmodell.pdf
- **Relevanz:** HaLiMo-Rahmenmodell, Zielsysteme (Kap. 2.4) und
  Wirkzusammenhänge zwischen PPS-Hauptaufgaben und logistischen Zielgrößen
  (Kap. 4). Kap. 2.4 und Kap. 4 stützen Kennzahlensysteme mit konkurrierenden
  Zielen.
- **Inhaltsverzeichnis:**
  - Kap. 2 Das Hannoveraner Lieferkettenmodell (HaLiMo)
  - Kap. 4 Wirkzusammenhänge zwischen PPS-Hauptaufgaben und logistischen
    Zielgrößen
  - Kap. 5 Beeinflussung logistischer Zielgrößen durch die PPS (u. a.
    Sekundärbedarfsplanung, Fremdbezugsplanung, Bestandsmanagement und
    Produktionscontrolling)
  - Kap. 6 Standardisierte Beschreibung der PPS-Aufgaben (Steckbriefe)

## Supply Chain Controlling
- **Autor:** Hartmut Werner (2. Auflage 2022, Springer Gabler)
- **Ordner:** `Supply_Chain_und_Operations/`
- **Datei:** Werner_Supply Chain Controlling.pdf
- **Relevanz:** direkte Grundlage für Kennzahlensysteme, Cost Tracking,
  Working Capital/Cash-to-Cash-Cycle im Controlling-Alltag. Kap. 8 liefert
  eine der gängigen Working-Capital-Definitionen. Kap. 5.1 bis 5.3, 5.4.1 und
  Kap. 6 stützen Kennzahlensysteme mit konkurrierenden Zielen.
- **Inhaltsverzeichnis:**
  - Kap. 3 Digitales Supply Chain Controlling
  - Kap. 4 Resilientes Supply Chain Controlling
  - Kap. 5 Kennzahlenmanagement in der Supply Chain (Input/Throughput/
    Output/Payment-Typologie, Werttreiberbaum Abschn. 5.4.1)
  - Kap. 6 Supply Chain Performance und Supply Chain Scorecard
    (Strategy Map)
  - Kap. 7 Supply Chain Cost Tracking und Hard-(Soft)-Analyse
  - Kap. 8 Working Capital Management in der Supply Chain (nur fünf
    Seiten, Cash-to-Cash-Cycle)
  - Kap. 9 Strategisches Kostenmanagement (Target Costing,
    Prozesskostenrechnung, Lifecycle Costing/TCO)

## Supply Management Research, Aktuelle Forschungsergebnisse 2019
- **Autor:** Bode, Bogaschewsky, Eßig, Lasch, Stölzle (Hrsg.), Springer
  Gabler, Tagungsband 12. Wissenschaftliches Symposium Supply Management
  (BME)
- **Ordner:** `Supply_Chain_und_Operations/`
- **Datei:** Bode_Supply Management Research.pdf
- **Relevanz:** aktuelle Forschungsbeiträge zu Buyer-Supplier-Verhandlungen,
  Lieferantenintegration Industrie 4.0, Data Literacy in der Supply Chain
- **Inhaltsverzeichnis (Auswahl Beiträge):**
  - Dangerous Deception? Advancing the Knowledge on Buyer-Supplier
    Negotiations
  - Politics in Internal Integration for Supply Chain Management
  - Data Literacy in the Supply Chain, Groundwork for Big Data Potentials
  - Lieferantenintegration im Kontext von Industrie 4.0

## Grundlagen des Einkaufs
- **Autor:** Bundesverband Materialwirtschaft, Einkauf und Logistik e.V.
  (BME); Vorwort Dr. Christoph Feldmann
- **Ordner:** `Supply_Chain_und_Operations/`
- **Datei:** BME_Grundlagen des Einkaufs.pdf (Scan ohne Textebene, nur als Bild lesbar)
- **Relevanz:** Praxisleitfaden Einkaufsorganisation, Sourcing-Strategien,
  Einkaufsprozess. Grundlagenreferenz für die Beschaffungsseite von
  Supply-Chain-Projekten. S. 13 bis 16 (Sourcing-Strategie,
  Warengruppenportfolio) sind eine Quelle für die Segmentierung von
  Beschaffungsstrategien.
- **Inhaltsverzeichnis:**
  - Einkauf, Grundlagen und Begriffsabgrenzung (Definition/Abgrenzung,
    Einkaufsportfolio, Direkter vs. Indirekter Einkauf)
  - Die Einkaufsorganisation (strategisch vs. operativ, Projekt- vs.
    Serieneinkauf, zentrale/dezentrale/hybride Organisationsformen)
  - Die Sourcing-Strategie (Anzahl Lieferanten: Single/Dual/Multiple
    Sourcing; Komplexität: Unit/Modular/System Sourcing; Ort:
    Local/Regional/National/Global Sourcing)
  - Der Einkaufsprozess (Strategiedefinition inkl. Warengruppenportfolio
    mit Hebel-, Strategischen, Standard- und Engpassmaterialien, S. 15 bis 16, Kernprozesse:
    Bedarfserkennung, Beschaffungsmarktforschung, Lieferantenauswahl, Sourcing,
    Beauftragung, Abwicklung, Unterstützungsprozesse: Lieferantenmanagement,
    Einkaufscontrolling, Risikomanagement)

## Change Management, Grundlagen und Erfolgsfaktoren
- **Autor:** Thomas Lauer (3., vollständig überarbeitete Auflage 2019,
  Springer Gabler; TH Aschaffenburg)
- **Ordner:** `Transformation_OpEx_und_Change/`
- **Datei:** Lauer_Change Management.pdf
- **Relevanz:** Leitwerk für Change Management, deckt die Themen ab, die in
  Lehre und Prüfung typischerweise erwartet werden, und ergänzt den gängigen
  Kanon (Lewin, Kotter, ADKAR). Methodische Grundlage für die Widerstands- und
  Kommunikationsseite von Transformationsprojekten (etwa Verlagerungen oder
  die Einführung eines neuen Reportings) über das Erfolgsfaktoren-Modell auf
  Basis der Feldtheorie Lewins. Kap. 5, 8 und 9 liefern das psychologische
  Fundament für die People-Seite eines Transformationsrasters (Feldtheorie,
  neun Erfolgsfaktoren, Gleicher-Formel, VIE-Theorie).
- **Inhaltsverzeichnis:**
  - **Teil I Grundlagen**
    - Kap. 1 Change Management, Begriff, Gegenstand, Ansatzpunkte
    - Kap. 2 Auslöser von Unternehmenswandel (Unternehmen als offene
      Systeme, Umweltdynamik, Lebenszyklusmodelle, „Burn-out-Syndrom")
    - Kap. 3 Hemmnisse des Wandels (Verhalten in Krisensituationen,
      individuelle/kollektive/wirtschaftliche Ursachen, Komplexität)
    - Kap. 4 Ursachen gescheiterten Wandels (Widerstandsarten,
      Erscheinungsformen, Sach- vs. Machtwiderstände, Nährböden auf
      Unternehmens- und Mitarbeiterebene, falscher Umgang mit Widerständen)
    - Kap. 5 Erfolgsfaktorenmodell des Change Managements (Feldtheorie
      Lewins, Drei-Phasen-Modell, Bausteine Orientierung, Start-,
      Prozess- und Zielmotivation)
  - **Teil II Erfolgsfaktoren** (je Kapitel: Begriff, Erfolgsbeitrag,
    Voraussetzungen, ausgewählte Methoden, Praxis-Check)
    - Kap. 6 Person, transaktionale vs. transformatorische Führung,
      optimale Mischung der Führungsstile, Rollenbilder (Visionär, Coach,
      Vorbild, Wohltäter), emotionale Intelligenz
    - Kap. 7 Vision, Voraussetzungen wirksamer Visionen, Visionsarbeit,
      Visions-Review
    - Kap. 8 Kommunikation, Kommunikation in Start- und
      Durchführungsphase, Kommunikationsplanung und Stakeholder-Analyse,
      Gesprächsführung, World Café, Projektinformationsmarkt
    - Kap. 9 Partizipation, Gruppenmoderation, Mitarbeiterbefragung,
      Open Space, Partizipationsplan
    - Kap. 10 Integration, Integration on the job / off the job
    - Kap. 11 Re-Edukation, Personalentwicklung, seminargestütztes Coaching
    - Kap. 12 Projektorganisation, Projektaufbauorganisation, strategische
      Projektauswahl, Projektteambildung, Motivationserhalt, Agiles
      Projektmanagement/Scrum
    - Kap. 13 Konsultation, Beratertrends, Prozessberatung, Inhouse-Beratung
    - Kap. 14 Evolution, organisationales Lernen, Lernen von der Natur,
      Sensor-Teams, Ideenolympiade, internes Crowdsourcing,
      Intrapreneurship-Programme, Kulturmanagement (Schein)

## Systematischer Ansatz zur kennzahlenbasierten Analyse und Bewertung von indirekten Prozessen im Kontext von Operational Excellence
- **Autor:** Patrick Eichenseer (2023, Springer Gabler, Reihe BestMasters, mit Höchstnote ausgezeichnete Master-Abschlussarbeit)
- **Ordner:** `Transformation_OpEx_und_Change/`
- **Datei:** Eichenseer_Systematischer Ansatz zur kennzahlenbasierten Analyse und Bewertung von indirekten Prozessen im Kontext von Operational Excellence.pdf
- **Relevanz:** Einer der wenigen Titel, die OpEx für *indirekte*
  (administrative) Prozesse quantifizieren statt nur für die Fertigung:
  fünf relative Kennzahlen (Zeiteffizienz, Wertschöpfungsproduktivität,
  Wertschöpfungskostenratio, kundenorientierter Qualitätsfaktor,
  Simplizitätswert) plus Prozesskosten als absolute Kennzahl, jeweils mit
  hergeleiteten Zielwerten. Dazu: PE-Radar und PE-Index zur Visualisierung,
  ein indirektes Prozessportfolio zur Priorisierung und ein bewerteter
  Methodenkoffer zur Datenerhebung (Wertstromanalyse, Tätigkeitsstrukturanalyse,
  MTM-Office-System, Process Mining u. a.). Macht Liebetruths Perspektive
  „Finanzen & Steuerung" (Kap. 3.3) messbar und ergänzt Werner,
  Supply Chain Controlling, Kap. 5 um die Prozesssicht. Anwendbar auf
  Dispositions- und Einkaufsprozesse sowie als Baustein für Transformations-
  und OpEx-Vorhaben. Kap. 3.1 dient als Methodenvergleich bestehender
  Prozessanalyse-Verfahren.
- **Inhaltsverzeichnis:**
  - Kap. 1 Einleitung und Zielsetzung (Fokus auf indirekte Prozesse,
    Problemstellung, Forschungsfrage)
  - Kap. 2 Anforderungen an die Analyse- und Bewertungsmethodik (allgemeine
    und fallspezifische Anforderungen, Bewertungskriterien)
  - Kap. 3 Stand der Wissenschaft (Beschreibung und Bewertung vorhandener
    Methoden zur Prozessanalyse, u. a. WSA, Makigami, Process Turtle,
    Waste Walk, TSA, Prozesskostenrechnung, SIPOC, MOS, REFA, BPMN 2.0)
  - Kap. 4 Ableitung eines neuen kennzahlenbasierten Ansatzes
    - 4.2 Kennzahlen: Effizienz, Produktivität, Kosten, Qualität + Kunde
      (kundenorientierter Qualitätsfaktor, Simplizitätswert),
      Prozesskosten als absolute Kennzahl
    - 4.3 Bewertungsmaßstäbe: Durchlaufzeit, Aktionszeit,
      Prozesskostensatz, Rolled Throughput Yield, Häufigkeit pro Jahr,
      Beschwerdequote, Schnittstellen- und Medienkontinuität
    - 4.4 Methoden zur Datenerhebung (Beschreibung, Gegenüberstellung,
      Bewertung)
    - 4.5 Visualisierung (Kennzahlen: PE-Radar, PE-Index,
      Prozessportfolio; Prozessablauf: Datenkästen, Notationen)
  - Kap. 5 Handlungsempfehlung zur Methodenanwendung (Methodenauswahl,
    Ablaufbeschreibung)
  - Kap. 6 Schlussbetrachtung (Anforderungserfüllung, kritische Würdigung,
    Ausblick)

## The Palgrave Handbook of Supply Chain and Disruptive Technologies
- **Autor:** Nachiappan Subramanian, Yasanur Kayikci, Atanu Chaudhuri,
  Michael Bourlakis (Hrsg.) (2025, Palgrave Macmillan / Springer Nature)
- **Ordner:** `KI_und_Daten/`
- **Datei:** Subramanian_The Palgrave Handbook of Supply Chain and Disruptive Technologies.pdf
- **Relevanz:** Forschungs-Sammelband (29 Beiträge, ~750 Seiten) zu
  digitalen Technologien entlang der Supply Chain, Nachschlagewerk
  kapitelweise, nicht zum Durchlesen. Direkt anschlussfähig: Kap. 6
  (Beschaffungsdigitalisierung), Kap. 11 (Deep Learning im
  Bestandsmanagement), Kap. 22 (Lean Digitalization), Kap. 14
  (Industrie 5.0). Ergänzt Ziegeler und Goudz/Erdogan um die
  internationale Forschungsseite; viele Beiträge sind Literaturreviews
  oder empirische Studien, daher Belegquelle für Aussagen, keine
  Methodenanleitung. Blockchain-, Agrar- und Last-Mile-Kapitel sind für
  die Fertigungs-/Controllingpraxis nachrangig.
- **Inhaltsverzeichnis:**
  - Kap. 1 Mapping the Supply Chain with Disruptive Technologies: Parts and Overview
  - Part I Supply Chain Digitalization, Key Barriers, Enablers, and
    Capabilities (Kap. 2 3D Printing in Supply Chains, Kap. 3 IoT and Big
    Data in SC Processes, Kap. 4 Disruptive Technologies and SDGs,
    Kap. 5 Digital SC Activities and Sustainable Performance)
  - Part II Technological Effort vs. Value in Supply Chains (Kap. 6
    Procurement Digitalisation, Kap. 7 Customer Switching Behaviour,
    Kap. 8 Chief Privacy Officer in Digital SCs, Kap. 9 Social Implications
    of Autonomous Vehicles, Kap. 10 Digitalization and Innovation
    Performance During the Pandemic)
  - Part III Transformational Models and Processes (Kap. 11 Deep Learning
    in Inventory Management, Kap. 12 Smart Farming/Distribution/Retailing
    in Agri-Food, Kap. 13 Blockchain and IoT for SC Security, Kap. 14
    Industry 5.0 and the Future of Supply Chains)
  - Part IV Digital Design Capabilities (Kap. 15 bis 18 Blockchain:
    Traceability, Trust Design, Vaccine SC, Process Industries; Kap. 19
    Social Media in Container Logistics)
  - Part V Digital Manufacturing Capabilities (Kap. 20 AI & Digital Twins
    in Bioproduction, Kap. 21 Predictive Maintenance with Digital Twins,
    Kap. 22 Smart Production Through Lean Digitalization, Kap. 23 Additive
    Manufacturing and Industry 4.0)
  - Part VI Digital Delivery and Use Capabilities (Kap. 24 UAV Automation
    in Inbound/Warehousing, Kap. 25 Physical Internet and Urban Logistics,
    Kap. 26 Blockchain for Hydrogen SC, Kap. 27 bis 28 Last Mile Delivery)
  - Part VII Conclusion (Kap. 29 Final Thoughts and Future Research Directions)

## Basiswissen Bilanzanalyse, Schneller Einstieg in Jahresabschluss, Bilanz und GuV
- **Autor:** Bernd Heesen, Michelle Julia Heesen (5. Auflage 2026, Springer Gabler)
- **Ordner:** `Finance_und_Controlling/`
- **Datei:** Heesen_Basiswissen Bilanzanalyse.pdf
- **Relevanz:** Schnellweg zur Analyse eines fremden Abschlusses mit wenigen
  Kennzahlen, durchgehend an einem realen, leicht veränderten Fall (Bauco).
  Kern ist die Kennzahlen-Checkliste in drei Analyseblöcken, die mit einem
  Executive Summary endet (Kap. 3). Einsatzfelder sind der Bonitäts- und
  Stabilitätsblick auf Lieferanten und das Lesen des Abschlusses eines kleinen
  Unternehmens. Kap. 3.3.8 bis 3.3.9 (Cash Cycle vs. Cash Conversion Cycle)
  ist eine Working-Capital-Quelle, der "Cash Cycle" ist dabei eine
  eigenständige Liquiditätspuffer-Prüfung, keine zweite CCC-Definition.
  **Maßgeblicher Heesen-Band** für den aktuellen Einstieg, der ältere Band
  „Bilanzanalyse und Kennzahlen" (2018) nur für die Detailanalyse und die
  Bilanzoptimierung heranziehen.
- **Inhaltsverzeichnis:**
  - Kap. 1 GuV und Bilanz
  - Kap. 2 Das zu analysierende Zahlenwerk der Bauco (Schritt 1 bis 4:
    Vereinfachung und erste Betrachtung von GuV und Bilanz)
  - Kap. 3 Analyse mit Kennzahlen-Checkliste (1. Analyseblock Vermögen und
    langfristige Finanzierung, 2. Liquidität & Cash Flow, 3. Ertragskraft und
    operative Stärke, Executive Summary)
  - Kap. 4 Abschlusswürdigung

## Bilanzanalyse und Kennzahlen, Fallorientierte Bilanzoptimierung
- **Autor:** Bernd Heesen, Wolfgang Gruber (6. Auflage 2018, Springer Gabler)
- **Ordner:** `Finance_und_Controlling/`
- **Datei:** Heesen_Bilanzanalyse und Kennzahlen.pdf
- **Relevanz:** Vertiefung zu „Basiswissen Bilanzanalyse" desselben
  Erstautors: mehrperiodische Vollanalyse eines Falls (GH Mobile) mit
  Struktur-Bilanz/Struktur-GuV und Kennzahlen je Analysefeld. Eigenständiger
  Beitrag ist Kap. 7, die schrittweise Bilanzoptimierung mit Kennzahlen
  vorher/nachher, anschlussfähig an Werner, Supply Chain Controlling, Kap. 8
  (Working Capital). **Rechtsstand September 2017** (BilMoG, BilRUG), für
  aktuelle Rechtsfragen nicht maßgeblich.
- **Inhaltsverzeichnis:**
  - Kap. 1 Der Jahresabschluss (Funktionen, Bestandteile, Gliederung)
  - Kap. 2 Gewinn- und Verlustrechnung (Aufbauprinzipien, internationale
    Bilanzierung, Gesamt- vs. Umsatzkostenverfahren)
  - Kap. 3 Das BilRUG (wichtigste Änderungen, GuV, Pensionsrückstellungen,
    Beteiligungen/Ausschüttungen, Änderungen zum 01.01.2018)
  - Kap. 4 Einstieg in die Bilanzanalyse am Beispiel der GH Mobile
  - Kap. 5 Reduktion der Komplexität (Struktur-Bilanz und Struktur-GuV)
  - Kap. 6 Detailanalysen (Kennzahlen, Vorgehensweise, Analysefelder)
  - Kap. 7 Analyse des optimierten Zahlenwerkes (Annahmen, Ergebnisse,
    Kennzahlen zu Vermögen, Kapital, Liquidität/Finanzkraft, Erfolgsstruktur,
    Rentabilität nach Optimierung)
  - Anhang: Ausgangsdaten und Berechnungen (Excel-Tool über Verlag/IFAK)

## Business Transformation, Praxisorientierter Leitfaden zur erfolgreichen Neuausrichtung von Unternehmen und Geschäftsfeldern
- **Autor:** Jörg Klasen (2019, Springer Gabler)
- **Ordner:** `Transformation_OpEx_und_Change/`
- **Datei:** Klasen_Business Transformation.pdf
- **Relevanz:** Durchgängiger Transformationsprozess aus Praxissicht
  (Ex-Berater, Geschäftsführer Energiebranche), jedes Kapitel endet mit einer
  Checkliste. Deckt die Management- und Prozessseite ab, die Lauer (Change
  Management) von der Verhaltensseite her beschreibt. Direkt nutzbar sind Kap.
  7 (Mitbestimmung/Betriebsrat) für Verlagerungsvorhaben, Kap. 8 (Stakeholder,
  Kommunikationsplanung) und Kap. 9 (Verankerung per Gremienbeschluss und
  Wissensübergabe). Kap. 10 beschreibt die Rolle des Chief Transformation
  Officer und ist damit Referenz für eine Laufbahn Richtung Transformation &
  OpEx. Kap. 4 bis 8 liefern zusammen mit Dogan, Lauer und Liebetruth die
  Phasen-Achse eines Transformationsrasters (Sect. 2.3) sowie die konkreten
  Werkzeuge für Strategie, Prozessredesign und Kommunikation.
- **Inhaltsverzeichnis:**
  - Kap. 1 Einleitung (Begriffsabgrenzung, Ergänzung zur Literatur)
  - Kap. 2 Business Transformation, ein ganzheitlicher Managementprozess
  - Kap. 3 Das Problem erkennen (exogene/endogene Faktoren, Werttreiber)
  - Kap. 4 Strategie entwickeln (Fähigkeiten, Where to play, Value
    Proposition/Why we will win, How to play, Business Model Canvas)
  - Kap. 5 Transformationsprojekt starten und managen (Phasen,
    Projektleiter/Team, Projektantrag/-auftrag/-handbuch, Projektsteuerung)
  - Kap. 6 Vom Konzept bis zur Umsetzung (Konzeptplanung,
    Wachstumsinitiativen, Initiativen zur Effizienzsteigerung)
  - Kap. 7 Einbeziehung der Arbeitnehmervertretung (Mitbestimmung auf
    Unternehmens-, Tarif- und Betriebsebene, Europa)
  - Kap. 8 Marketing und Kommunikation (Stakeholder, Kommunikationsplanung)
  - Kap. 9 Verankerung (Projektdokumentation, Gremienbeschlüsse,
    Wissensübergabe)
  - Kap. 10 Anforderungen an einen erfolgreichen Chief Transformation Officer

## Corporate Finance, Theorie und Anwendungsbeispiele
- **Autor:** Enzo Mondello (2022, Springer Gabler)
- **Ordner:** `Finance_und_Controlling/`
- **Datei:** Mondello_Corporate Finance.pdf
- **Relevanz:** Umfangreiches Lehrbuch (~1.260 Seiten, CFA-Hintergrund,
  Beispiele Schweiz/Deutschland, HGB/OR und IFRS), Nachschlagewerk
  kapitelweise, modular aufgebaut. Direkt anschlussfähig ist Kap. 6 Working
  Capital Management inkl. Geldumschlagsdauer (Kap. 6.4) als finanzielle
  Fundierung der Cash-Conversion-Cycle-Kennzahl in einem Management-Dashboard
  und Ergänzung zu Werner Kap. 8. Sect. 6.2 bis 6.4 enthalten auch das
  Optimum-NWC-Modell (Sect. 6.3), das Werners und Helmolds "je weniger, desto
  besser"-Lesart korrigiert. Kap. 3 (WACC) und Kap. 4 bis 5
  (Investitionsrechnung, Unsicherheit, Realoptionen) für Business Cases bei
  Verlagerungs- und Footprint-Entscheidungen. Teil III (Aktien, Anleihen,
  Derivate) für die Controllingpraxis nachrangig. Lösungen zu den Aufgaben
  liegen in einem separaten Band (nicht abgelegt).
- **Inhaltsverzeichnis:**
  - Teil I Grundlagen (Kap. 1 Einführung: Ziele, Agency-Theorie, Corporate
    Governance, Rolle des CFO; Kap. 2 Erwartete Rendite und Risiko; Kap. 3
    Kapitalkostensatz/WACC)
  - Teil II Sachinvestitionen und Working Capital Management (Kap. 4
    dynamische und statische Investitionsrechnung; Kap. 5 weiterführende
    Konzepte: Cashflow-Projektion, Unsicherheit, Realoptionen,
    Performancebeurteilung; Kap. 6 Working Capital Management:
    wertorientierte NWC-Optimierung, Geldumschlagsdauer, Management der
    Positionen, Finanzierung des Umlaufvermögens)
  - Teil III Finanzinvestitionen (Kap. 7 Aktien, Kap. 8 Anleihen, Kap. 9
    Derivate)
  - Teil IV Finanzierung (Kap. 10 Außenfinanzierung, Kap. 11
    Innenfinanzierung/Private Equity/Venture Capital, Kap. 12
    Kapitalstruktur und Dividendenpolitik)
  - Teil V Spezialthemen (Kap. 13 Realoptionen, Kap. 14 Fusionen und
    Akquisitionen, Kap. 15 Risikomanagement und Derivate)

## Einführung in die Cross-Impact-Bilanzanalyse (CIB), Wege zur qualitativen System- und Szenarioanalyse
- **Autor:** Wolfgang Weimer-Jehle (2023, Springer Gabler; ZIRIUS,
  Universität Stuttgart)
- **Ordner:** `Consulting/`
- **Datei:** Weimer-Jehle_Einführung in die Cross-Impact-Bilanzanalyse (CIB).pdf
- **Relevanz:** **Achtung Titel: keine Bilanzanalyse im Sinne des
  Jahresabschlusses**, sondern eine Methode der qualitativen Szenarioanalyse.
  Aus Deskriptoren, ihren Ausprägungen und einer Cross-Impact-Matrix werden
  in sich konsistente Szenarien bestimmt („Bilanz" meint die Wirkungssummen
  je Deskriptor). Macht die „Scenario Technique" aus dem Methodenkoffer
  (Option Evaluation) formal nachvollziehbar und ergänzt die quantitative
  Unsicherheitsbetrachtung bei Christian (Standortplanung unter
  Emissionszöllen) um die qualitative Seite, z. B. für Szenarien zu Zöllen,
  Lieferketten-Risiken oder Auslandsstandorten. Kap. 8.4 (ungeeignete
  Anwendungsfälle) vor jedem Einsatz prüfen. Die Praxisfälle in Kap. 7
  stammen aus Politik, Energie und Gesundheit, nicht aus der Supply Chain.
- **Inhaltsverzeichnis:**
  - Kap. 1 Einleitung
  - Kap. 2 Das Anwendungsfeld der CIB (Szenarien, Szenarien und
    Entscheidungen, die CIB im Methodenfeld)
  - Kap. 3 Grundlagen der CIB (Deskriptoren, Ausprägungen, Cross-Impact-Matrix,
    Bestimmung konsistenter Szenarien, Darstellungsformate, Kennwerte,
    Datenunsicherheit und Signifikanz)
  - Kap. 4 Portfolioanalyse (Ordnen des Portfolios, Szenario-Logik,
    Konsistenzsicherung, Interventions- und Dissensanalyse,
    Storyline-Entwicklung)
  - Kap. 5 Was tun, wenn … (zu wenige/zu viele Szenarien, monotones oder
    bipolares Portfolio, unterbestimmte Deskriptoren, Vakanzen,
    kontextsensitive Einflüsse)
  - Kap. 6 Daten (Dossiers Deskriptoren, Ausprägungen, Cross-Impact-Daten,
    Datenerhebung)
  - Kap. 7 Die CIB in der Praxis (Iran-Atomabkommen, Energie und
    Gesellschaft, Gesundheitsprävention, IPCC Storylines)
  - Kap. 8 Methodenreflexion (Stärken, Grenzen, Checkliste ungeeigneter
    Anwendungsfälle)
  - Anhang, Glossar

## Erfolgsrechnung, Wertsteigerung durch Wertschöpfung. Grundlagen, Konzeption, Instrumente
- **Autor:** Jürgen Reim (2., aktualisierte und erweiterte Auflage 2022,
  Springer Gabler; Hochschule RheinMain, Wiesbaden Business School)
- **Ordner:** `Finance_und_Controlling/`
- **Datei:** Reim_Erfolgsrechnung, Wertsteigerung durch Wertschöpfung.pdf
- **Relevanz:** Umfassendes Controlling-Lehrbuch (~980 Seiten) zur internen
  Erfolgsrechnung von der Kostenrechnung bis zum Unternehmenswert, Nachschlagewerk kapitelweise. Direkt anschlussfähig: Kap. 10
  (Abweichungsanalyse in der flexiblen Plankostenrechnung) für Plan-Ist-
  Vergleiche; Kap. 12.3 (effizienzorientierte Kennzahlen, Wertstrom-Methode)
  verbindet Produktionskennzahlen mit der Erfolgsrechnung, anschlussfähig an
  Werner Kap. 5 und Eichenseer; Kap. 17 (Prozesskostenrechnung, Gemeinkosten
  in indirekten Bereichen) liefert die Kostenseite zu Eichenseers
  Prozesskosten; Kap. 21 (Verrechnungspreise) für intercompany-Beziehungen
  mit Auslandswerken. Kap. 14 (Szenario-Technik und Simulation) ist die
  quantitative Ergänzung zur CIB (Weimer-Jehle).
- **Inhaltsverzeichnis:**
  - Teil I Grundlagen (Kap. 1 Gegenstand und Abgrenzung, digitale
    Wertschöpfung; Kap. 2 wertschöpfungsorientierte Erfolgsrechnung)
  - Teil II Kosten- und Leistungsrechnung als Dokumentationsrechnung
    (Kap. 3 Informationsgrundlage und Kostenrechnungssysteme; Kap. 4 Kosten-
    und Leistungsartenrechnung; Kap. 5 Kostenstellenrechnung; Kap. 6
    Kostenträgerrechnung: Kalkulation, kalkulatorische Periodenerfolgsrechnung)
  - Teil III Operative Erfolgsrechnung (Kap. 7 Plan-Kosten- und
    Leistungsrechnung; Kap. 8 Systeme der Plankostenrechnung, u. a.
    Grenzplankostenrechnung; Kap. 9 Kostenplanung; Kap. 10 Kostenkontrolle und
    Abweichungsanalyse; Kap. 11 operative Plan-Erfolgsrechnung,
    Deckungsbeitragsrechnung; Kap. 12 Wertschöpfung und Erfolgsrechnung in
    der Industrie 4.0, effizienzorientierte Kennzahlen, Erlösmodelle)
  - Teil IV Strategische Erfolgsrechnung (Kap. 13 Grundlagen; Kap. 14
    Szenario-Technik und Szenario-Rechnung; Kap. 15 strategische Planungs-
    und Kontrollrechnung auf Basis Free Cash Flow und Residualgewinn;
    Kap. 16 Erfahrungskurve, Produktlebenszyklus, Target Costing; Kap. 17
    Prozesskostenrechnung)
  - Teil V Unternehmenserfolgsrechnung (Kap. 18 Grundlagen; Kap. 19
    kapitalmarktorientierte Erfolgsziele, Gesamtkapitalkostensatz; Kap. 20
    Gestaltung des Unternehmensportfolios, Realoptionen; Kap. 21
    Verrechnungspreise; Kap. 22 Unternehmenswert über FCF und EVA,
    Residualgewinne)

## Kernanalysen der Financial Due Diligence
- **Autor:** Thomas Pomp (2024, Springer Gabler, Reihe essentials)
- **Ordner:** `Finance_und_Controlling/`
- **Datei:** Pomp_Kernanalysen der Financial Due Diligence.pdf
- **Relevanz:** Kurzer Leitfaden (53 Seiten) zu den drei Kernanalysen der
  Financial Due Diligence, Quality-of-Earnings-Analyse, Nettoverschuldung,
  Working Capital, mit der Überleitung Unternehmenswert zu Eigenkapitalwert
  nach Working-Capital-Anpassung (Abb. 1.1). Füllt die Lücke „Financial Due
  Diligence als Handwerk" und ergänzt Heesen/Heesen sowie Heesen/Gruber um die
  transaktionsspezifische Bereinigungslogik für das Prüffeld Financial einer
  Unternehmensübernahme.
- **Inhaltsverzeichnis:**
  - Kap. 1 Einleitung
  - Kap. 2 Analyse der nachhaltigen historischen Ergebnisentwicklung
    (2.1 Überblick, 2.2 Normalisierungen, 2.3 Pro-forma-Anpassungen)
  - Kap. 3 Analyse der Nettoverschuldung (3.1 Überblick, 3.2 Liquide
    Mittel, 3.3 Finanzvermögen, 3.4 Finanzverbindlichkeiten, 3.5
    Finanzähnliche Vermögenspositionen, 3.6 Schuldenähnliche Positionen,
    3.7 Nicht bilanzierte schuldenähnliche Positionen, 3.8 Wechselwirkung
    zwischen EBIT(DA)-Bereinigungen und Nettoverschuldung anhand von
    Praxisbeispielen)
  - Kap. 4 Analyse des Working Capital (4.1 Überblick, 4.2 Bereinigung
    des Trade Working Capital, 4.3 Bereinigung des Other Working Capital,
    4.4 Trade-Working-Capital-Kennzahlen, 4.5 Herleitung des normalen
    Working-Capital-Niveaus, 4.6 Schwankungsbreite des Working Capital)

## Besonderheiten bei der Bewertung von KMU
- **Autor:** Susann Ihlau, Hendrik Duscha (2., aktualisierte Auflage 2019,
  Springer Gabler)
- **Ordner:** `Finance_und_Controlling/`
- **Datei:** Ihlau_Besonderheiten bei der Bewertung von KMU.pdf
- **Relevanz:** Behandelt genau die Punkte, an denen die
  kapitalmarktorientierte Lehrbuchmethode (Mondello, Reim) bei der Übernahme
  eines kleinen Unternehmens scheitert, Abgrenzung des Bewertungsobjekts,
  Abhängigkeit vom Inhaber (Kap. 4.3.1, übertragbare Ertragskraft bei
  personenbezogenen Unternehmen), Unternehmerlohn (Kap. 4.3.1.2), Zuschläge im
  Kapitalisierungszinssatz (Kap. 4.4.2, Insolvenzrisiko, mangelnde
  Diversifikation/Fungibilität, Size Premium), Bezug zu IDW S 1 (Kap. 1).
  Direkte Quelle für das Prüffeld Bewertung einer Unternehmensübernahme.
- **Inhaltsverzeichnis:**
  - Kap. 1 Einführung
  - Kap. 2 Spezifische Merkmale und Besonderheiten von KMU (2.1
    Definition von KMU: quantitative/qualitative Merkmale, 2.2 Bedeutung
    von KMU)
  - Kap. 3 Grundlagen der Unternehmensbewertung (Wert und Preis,
    Bewertungsanlässe, Bewertungszweck und Wertkategorien, Grundsätze
    ordnungsmäßiger Unternehmensbewertung, Bewertungsverfahren:
    kapitalwertorientiert/marktpreisorientiert/Einzelbewertung/
    vereinfachend, Bewertungsprozess inkl. Kapitalisierung der
    finanziellen Überschüsse mit CAPM, Basiszinssatz, Risikozuschlag,
    Phasenmethode)
  - Kap. 4 Besonderheiten bei der Bewertung von KMU (Abgrenzung des
    Bewertungsobjekts, Auswahl des Bewertungsverfahrens, Prognose der
    finanziellen Überschüsse bei personenbezogenen Unternehmen und
    eingeschränkten Informationsquellen, Berücksichtigung von Steuern,
    Kapitalisierung: CAPM-Anwendbarkeit und Anpassungen des
    Kapitalisierungszinssatzes bei KMU)
  - Kap. 5 Zusammenfassung
  - Tabellarische Zusammenfassung, Sachverzeichnis

## Unternehmensnachfolge, Praxishandbuch für Familienunternehmen
- **Autor:** Andreas Wiesehahn (Hrsg.) (2., aktualisierte und erweiterte
  Auflage 2020, Springer Gabler)
- **Ordner:** `Finance_und_Controlling/`
- **Datei:** Wiesehahn_Unternehmensnachfolge.pdf
- **Relevanz:** Herausgeberband mit 23 Fachbeiträgen und 12 Interviews zu
  nahezu allen Aspekten der Unternehmensnachfolge, mit Schwerpunkt Nachfolge
  in der Familie. Für eine Übernahme direkt anschlussfähig sind Kap. 8
  (familieninterne Lösungen), Kap. 20/22 (Finanzierung mit
  Fremdmitteln/Private Equity), Kap. 24 (Nachfolgecontrolling), Kap. 25
  (Nachfolge als betriebswirtschaftliches Problem), Kap. 29 (psychologische
  Aspekte), Kap. 31/32 (rechtliche Grundlagen, Übertragung zu Lebzeiten).
  Liefert den Rahmen für Neuaufstellung und Zielbild nach einer Nachfolge.
  Kap. 28 (Nachfolgebesteuerung) ist Hintergrund für Fragen an die
  Steuerberatung, ersetzt sie nicht, Rechtsstand 2020 vor Verwendung prüfen.
- **Inhaltsverzeichnis:**
  - Teil I Bedeutung, Situation und Formen der Unternehmensnachfolge
    (Kap. 1 Entwicklung und volkswirtschaftliche Bedeutung, Kap. 2
    Aktuelle Situation Region Bonn/Rhein-Sieg, Kap. 3 Empirische Studie:
    Erwartungen an die Unternehmensnachfolge, Kap. 4 Frauen in der
    Unternehmensnachfolge, Kap. 5/7 Interviews, Kap. 6 Überblick über die
    Formen der Unternehmensnachfolge)
  - Teil II Familieninterne und -externe Nachfolge (Kap. 8 Familieninterne
    Lösungen als Nachfolgestrategie, Kap. 9/11/13 Interviews, Kap. 10
    Verkauf als Nachfolgestrategie, Kap. 12 Wert- und Preisfindung bei
    einem Unternehmensverkauf)
  - Teil III MBO, MBI, Stiftung und Liquidation (Kap. 14 MBO/MBI als
    Nachfolgestrategie, Kap. 15/17 Interviews, Kap. 16 Stiftungen in der
    Nachfolgegestaltung, Kap. 18 Liquidation als Strategie)
  - Teil IV Finanzierung und Unternehmensnachfolge (Kap. 19/21/23
    Interviews, Kap. 20 Finanzierungslösungen mit Fremdmitteln, Kap. 22
    Private Equity und Unternehmensnachfolge)
  - Teil V Ausgewählte sachliche und emotionale Aspekte der
    Unternehmensnachfolge (Kap. 24 Nachfolgecontrolling, Kap. 25
    Nachfolge als betriebswirtschaftliches Problem, Kap. 26 Organisation
    des Nachfolgeprozesses, Kap. 27 Interview, Kap. 28
    Nachfolgebesteuerung, Kap. 29 Psychologische Aspekte der
    Unternehmensnachfolge, Kap. 30 Der freiwillige Beirat als Instrument
    der Unternehmensnachfolge)
  - Teil VI Unternehmensnachfolge zu Lebzeiten und im Todesfall des
    Unternehmers (Kap. 31 Rechtliche Grundlagen, Kap. 32
    Unternehmensübertragung zu Lebzeiten, Kap. 33 Unternehmensnachfolge
    bei Tod des Unternehmers, Kap. 34 Interview, Kap. 35 Möglichkeiten
    der Testamentsvollstreckung)

## Seven Building Blocks of a Successful Corporate Restructuring, A Practical Guide
- **Autor:** Dino Dogan (2024, Springer; Luxembourg School of Business), Übersetzung von „Sieben Bausteine einer erfolgreichen
  Unternehmensrestrukturierung" (2024), mit KI-Unterstützung übersetzt und
  inhaltlich redigiert; das deutsche Original ist nicht abgelegt
- **Ordner:** `Transformation_OpEx_und_Change/`
- **Datei:** Dogan_Seven Building Blocks of a Successful Corporate Restructuring.pdf
- **Relevanz:** Kompaktes Restrukturierungsmodell „7P" (Plan, People,
  Partitioning, Processes, Platforms, Portfolio, Performance) auf ~150 Seiten,
  von der Früherkennung bis zur Fortschrittsmessung. Kandidat als
  Strukturgeber neben Liebetruths vier Perspektiven und Klasens
  Transformationsprozess, alle drei lassen sich zu einem Transformationsraster
  verbinden. Kap. 5.2 (Einsatz von Beratern) liefert die Auftraggebersicht auf
  Beratung. Englisch, für Zitate in deutschen Dokumenten auf den Originaltitel
  verweisen oder übersetzen.
- **Inhaltsverzeichnis:**
  - Kap. 1 Introduction
  - Kap. 2 Restructuring
  - Kap. 3 Overview of the Seven Building Blocks (7P)
  - Kap. 4 Building Block 1: Plan (Early Detection, Motivation of the
    Clients, Feasibility and Profitability, Strategic Plan, Operational Plan,
    Success Control, Prudent and Forward-Looking Solutions)
  - Kap. 5 Building Block 2: People (Assembling Strong Teams, Use of
    Consultants, Human Communication)
  - Kap. 6 Building Block 3: Partitioning
  - Kap. 7 Building Block 4: Processes
  - Kap. 8 Building Block 5: Platforms (IT, Communication and Collaboration
    Platforms)
  - Kap. 9 Building Block 6: Portfolio (Composition, Pricing)
  - Kap. 10 Building Block 7: Performance (Strategic, Operational,
    Restructuring Progress)
  - Kap. 11 Summary

## Supply Chain Transformation
- **Autor:** Chopra & Sodhi
- **Datei:** [noch nicht abgelegt] (PDF nicht mitgeliefert)
- **Relevanz:** strategische Neuaufstellung
- **Inhaltsverzeichnis:** [TODO, nach Ablage per /add-literature einlesen]

## Operations Management (Facility Location Kapitel)
- **Autor:** Heizer & Render
- **Datei:** [noch nicht abgelegt] (PDF nicht mitgeliefert)
- **Relevanz:** quantitative Standortwahl
- **Inhaltsverzeichnis:** [TODO, nach Ablage per /add-literature einlesen]

## Business Consulting, Methoden, Techniken und Einblicke
- **Autor:** Christian Aichele, Marius Schönberger (Hrsg.) (2025, Springer Vieweg)
- **Ordner:** `Consulting/`
- **Datei:** Aichele_Business Consulting, Methoden, Techniken und Einblicke.pdf
- **Relevanz:** Ergiebige Consulting-Quelle für den Rahmen eines
  Beratungsmandats. Vollständiger Beratungsprozess-Leitfaden von der
  Akquisition bis zum Projektabschluss, dazu ein umfangreiches
  Methoden-Kompendium (Kap. 8) mit konkret benannten Werkzeugen. Kap. 1, 3, 4,
  6 (Added Values, Beraterpyramide, Phasen des Beratungsprozesses,
  Projektakquisition, Projektauftrag/-design/-planung, Guidelines für
  erfolgreiche Berater) sind die direkte Vorlage für einen Mandats-Charter.
  Kap. 5 (kennzahlenbasierte Projektsteuerung, Earned Value) liefert das
  Modell für eine Steering-Kadenz. Kap. 8.2 Strategieentwicklung (SWOT,
  PESTEL, Five Forces, McKinsey 7S, Szenariotechnik) und Kap. 8.3
  Organisationsentwicklung mit Reifegradmodellen (Maturity Models) sind
  anschlussfähig an die Frage nach dem OpEx-Reifegrad eines Unternehmens und
  die vier Liebetruth-Perspektiven. Kap. 8.7 Finanz-/Controllingberatung
  (Working Capital Management, Business Valuation, Liquiditätsplanung) für die
  Finanzdiagnose. Kap. 7 Insights, u. a. "Kein Plan überlebt die Realität",
  als nüchterner Realitätscheck aus echten Projekten.
- **Inhaltsverzeichnis:**
  - Kap. 1 Einführung in die Unternehmensberatung (Added Values der
    Unternehmensberater, Anforderungen an die Berater, Strukturierung und
    Klassifikation der Beratung, Historie der Beratung, Die Beraterpyramide,
    Die Phasen des Beratungsprozesses)
  - Kap. 2 Beratungsmarketing (klassische und digitale Ansätze)
  - Kap. 3 Projektakquisition (Kontaktaufnahme und Akquisitionstermin,
    Angebotserstellung, Vorgehensmodelle, Projektauftrag)
  - Kap. 4 Das Beratungsprojekt (Definitionen Projekt/Projektmanagement,
    Projektvorbereitung, -design, -planung, Projektziele, -mittel,
    -information und -dokumentation, Die Kunst Beratungsprojekte zu führen)
  - Kap. 5 Das Projektcontrolling (kennzahlenbasierte Projektsteuerung,
    Earned Value Analysis, Kostentrendanalyse, Business Object Management)
  - Kap. 6 Guidelines für erfolgreiche Berater (High Priority Consulting
    Guidelines: technische und menschliche Konfiguration; Low Priority
    Project Management Guidelines)
  - Kap. 7 Insights (Fallstudien u. a. Energiewirtschaft, IT-Outsourcing,
    Projekt Grow, S/4HANA-Implementierungen, Großhandel/SAP,
    Digitalisierung und KI im Beratungsumfeld, "Kein Plan überlebt die
    Realität", Porzellanhersteller-Fallstudie)
  - Kap. 8 Kompendium der Methoden und Techniken: 8.2 Strategieentwicklung
    und -beratung (SWOT, PESTEL, Five Forces, Balanced Scorecard,
    BCG-Matrix, McKinsey 7S, Szenariotechnik, Business Model Canvas, Blue
    Ocean Strategy, Frühwarnsysteme, Benchmarking, Marktsegmentierung,
    OKR), 8.3 Organisationsentwicklung (Organisationsdiagnose,
    Reifegradmodelle/Maturity Models, Change-Management-Modelle,
    Kulturdiagnosen, Stakeholderanalyse, RACI, Prozesslandkarten,
    Zielsystemanalyse), 8.4 Prozessberatung/Business Process Management
    (IST-/SOLL-Analyse, Wertstromanalyse, BPMN, Six Sigma/DMAIC,
    Lean/Kaizen/KVP, Time-Driven ABC, Prozessreifegradanalysen, Service
    Blueprinting), 8.5 Projektmanagement und -umsetzung (klassisch, agil,
    Design Thinking, Rapid Prototyping, User Story Mapping, Business Case,
    Earned Value, Risikoanalyse, Portfoliomanagement), 8.6 IT- und
    Technologieberatung, 8.7 Finanz- und Controllingberatung
    (Deckungsbeitragsrechnung, Break-Even, Investitionsrechnung,
    Budgetierung/Forecasting, Business Valuation, Financial Risk
    Assessment, Liquiditätsplanung, Working Capital Management), 8.8
    Personal- und HR-Beratung, 8.9 Marketing- und Vertriebsberatung, 8.10
    Innovations- und Kreativitätstechniken (Brainstorming, Morphologischer
    Kasten, TRIZ, SCAMPER, 6-3-5-Methode, Innovation Canvas, Open
    Innovation, Lead User), 8.11 Diagnose-, Analyse- und
    Visualisierungstools (GAP-Analyse, Ishikawa-Diagramme,
    Entscheidungsbaum/-matrix, Heatmaps, Mindmaps, Affinitätsdiagramme,
    Balanced-Scorecard-Dashboards, KPI-Cockpits), 8.12 Kommunikation,
    Moderation und Coaching (Moderationstechniken, Konfliktmoderation,
    Systemisches Coaching, Fragetechniken, Storytelling, Elevator
    Pitching, Stakeholder-Kommunikationspläne)

## Exzellenz in der Unternehmensberatung
- **Autor:** Robert Bodenstein, Ilse Andrea Ennsfellner, Josef Herget
  (Hrsg.) (2. Auflage 2022, Springer Gabler)
- **Ordner:** `Consulting/`
- **Datei:** Bodenstein_Exzellenz in der Unternehmensberatung.pdf
- **Relevanz:** Kernquelle für das Rollenverständnis in einem Beratungsmandat.
  Kap. 3 (Consulting Governance) beschreibt Beratung explizit als gemeinsame
  Leistung von Berater UND Kunde inkl. Rollenverschmelzung, anschlussfähig an
  Fälle, in denen eine Person gleichzeitig Kunde bzw. intern Wissender und
  Teil des Beraterteams ist. Kap. 8 (Beratersystem), Kap. 9 (Kundensystem,
  Beratungsreife und Nachhaltigkeit) und Kap. 10 (Exzellenzmodell zur
  Beratungsqualität) liefern ein Reifegradmodell für die Beratungsleistung
  selbst, nicht nur fürs beratene Unternehmen, also eine Meta-Ebene für die
  eigene Arbeitsweise. Kap. 12 (Match, wie Kunden und Berater zusammenkommen)
  für die Kick-off- und Anbahnungsphase.
- **Inhaltsverzeichnis:**
  - Kap. 1 Unternehmensberatung, Entwicklung und Relevanz einer neuen
    Profession
  - Kap. 2 Unternehmensberatung, Typologie, Felder und Rollen
  - Kap. 3 Unternehmensberatung und Consulting Governance, eine Leistung
    von Beratern und Kunden
  - Kap. 4 Qualität in der digitalisierten Welt
  - Kap. 5 Normen und Standards in der Unternehmensberatung
  - Kap. 6 Die Beratungsnorm ISO 20700
  - Kap. 7 Exzellenz in der Unternehmensberatung
  - Kap. 8 Das Beratersystem, Potenziale und Resultate
  - Kap. 9 Kundensystem, Beratungsreife und Nachhaltigkeit
  - Kap. 10 Beratungssystem, ein Exzellenzmodell zur Beratungsqualität
  - Kap. 11 Die Profession, Legitimation, Stakeholder und Reifegrad
  - Kap. 12 Match, Wie Kunden und Berater zusammenkommen
  - Kap. 13 Trends der Unternehmensberatung, mit systematischen
    Werkzeugen am Puls der Zeit bleiben
  - Kap. 14 Zukunftsperspektiven der Unternehmensberatung
  - Kap. 15 Ressourcen für Unternehmensberatung

## Digital Consulting
- **Autor:** Mahmut Arica, Christine Freye (Hrsg.) (2026, Springer Gabler)
- **Ordner:** `Consulting/`
- **Datei:** Arica_Digital Consulting.pdf
- **Relevanz:** Methodische Selbstreflexion für ein KI-gestütztes
  Berater-Setup. Kap. 5 (KI als digitale Beratungsassistenz, Mehrwerte und
  Grenzen) und Kap. 6 (Einsatz von KI-gesteuerten Tools im Consulting,
  Chancen, Restriktionen und die unverzichtbare Rolle der Experten) gehören in
  die Methodik- und Limitations-Diskussion eines Berichts. Kap. 1 (Wege zur
  digitalen Transformation der Unternehmensberatung, "Consulting
  4.0"-Stufenmodell) taugt zur Selbsteinordnung, wo das eigene Vorgehen auf
  dieser Skala steht.
- **Inhaltsverzeichnis:**
  - Teil I Überblick über das Digital Consulting (Kap. 1 Wege zur
    digitalen Transformation der Unternehmensberatung, Kap. 2
    KI-gestützte Beratung zur Stärkung der zielführenden Transformation
    von Unternehmen)
  - Teil II Methoden und Ansätze im Digital Consulting (Kap. 3 Scrum als
    Beispiel für Beratung 4.0, Kap. 4 Zukunft navigieren: Strategische
    KI-Integration in Organisationen mit KI Design Sprints)
  - Teil III Werkzeuge im Digital Consulting (Kap. 5 KI als digitale
    Beratungsassistenz: Mehrwerte und Grenzen, Kap. 6 Einsatz von
    KI-gesteuerten Tools im Consulting: Chancen, Restriktionen und die
    unverzichtbare Rolle der Experten)
  - Teil IV Fallbeispiele im Digital Consulting (Kap. 7 Das Verschwimmen
    der Grenzen zwischen Beratungs- und Softwareindustrie, Kap. 8 Building
    the Future of Digital Procurement Through Corporate Foresight, Kap. 9
    Cyberangriffe als Gefahr der Digitalisierung, Kap. 10 Berechnung und
    digitaler Vertrauensnachweis eines Palettenpreisindex)

## 77 Keywords Consulting
- **Autor:** Springer Fachmedien Wiesbaden (Hrsg.); Beiträge u. a. von
  Johann Engelhard, Rolf-Dieter Reineke, Gerhard Schewe, Jürgen Weber,
  Klaus Wübbenhorst (2. Auflage, Springer Gabler)
- **Ordner:** `Consulting/`
- **Datei:** Springer Fachmedien_77 Keywords Consulting.pdf
- **Relevanz:** Lexikon der 77 Kernbegriffe der Unternehmensberatung, nützlich
  für eine präzise Terminologie im Mandat (Mandat vs. Engagement vs. Case,
  Beratungsprodukt, Beraterausbildung/-einsatz/-karriere) und für die
  Berufsverbände als Qualitätsreferenz (BDU, AMCF, ASCO). Wichtigster
  Einzeleintrag ist **Advocacy Consulting**. Gefälligkeitsgutachten, die
  vorgegebene Ergebnisse liefern, verletzen die Beraterethik. Das wird
  relevant, sobald dieselbe Person zugleich Mitarbeiter des untersuchten
  Unternehmens und Berater ist, die Unabhängigkeit der Analyse also
  ausdrücklich adressiert werden muss.
- **Inhaltsverzeichnis:** Lexikonformat A bis Z, keine klassischen Kapitel;
  nur die ersten 20 Seiten gescreent, daher unvollständig. Gescreente
  Stichworte (A bis B): Ablauforganisation, Advocacy Consulting, Ambition
  Driven Strategy, AMCF, ASCO, Aufbauorganisation, Balanced Scorecard,
  BDU, Benchmarking, Beraterausbildung, Beratereinsatz, Beraterkarriere,
  Beraternutzen, Beratung, Beratungsförderung, Beratungsprodukt, Best
  Practice, Betriebsvergleich. Insgesamt 77 Stichworte von A bis Z.

## Modulhandbuch „Künstliche Intelligenz und Robotik" (B.Sc.), SPO 2026
- **Autor:** Technische Hochschule Augsburg, Fakultät für Informatik
  (Entwurf WS 2026/27, Stand 07.10.2026; rechtlich verbindlich ist nur die
  Studien- und Prüfungsordnung)
- **Ordner:** `Curricula/`
- **Datei:** TH Augsburg_Modulhandbuch Künstliche Intelligenz und Robotik.pdf (Druck aus der THA-Nextcloud als
  Bild ohne Textebene, 106 Seiten, per OCR gelesen)
- **Relevanz:** Kein Lehrbuch, sondern eine Landkarte für ein eigenes
  Lernzielbild in KI und Robotik. Je Modul stehen Inhalte, Lernziele,
  Prüfungsform und eine Literaturliste, die sich je Modul übernehmen und nach
  Bezugsweg sortieren lässt. Drei Grenzen: Das Handbuch nennt keine
  Studiengangsziele und keine Berufsfelder (die stehen nur auf der
  THA-Website), es beschreibt die Wahlpflichtmodule nicht (rund 27 der 210
  CP), und fünf Module nennen keine Literatur (Maschinelles Lernen,
  Robotikpraktikum 1 bis 4). Gewichtung nach CP der beschriebenen Module:
  Robotik und Hardware 55, KI-Kern 30, Informatik und Software 30, Mathematik
  und Statistik 15.
- **Inhaltsverzeichnis:**
  - 1 Orientierungsphase (je 5 CP): 1.1 Grundlagen der Programmierung (C),
    1.2 Grundlagen der Elektrotechnik, 1.3 Grundlagen der Informatik
    (Automaten, Petri-Netze, Algorithmen, Python), 1.4 Mathematik 1,
    1.5 Physik, 1.6 Robotikpraktikum 1, 1.7 Datenkommunikation, 1.8 KI und
    Robotik (Suche, symbolische KI, Agenten, Reinforcement Learning),
    1.9 Mathematik 2, 1.10 Objektorientierte Programmierung (C++),
    1.11 Robotermechanik, 1.12 Robotikpraktikum 2 (ROS)
  - 2 Vertiefungsphase: 2.1 Echtzeitsysteme, 2.2 Effiziente KI-Software
    (KI-Hardware, CUDA, Quantisierung, Pruning), 2.3 Maschinelles Lernen,
    2.4 Robotikpraktikum 3, 2.5 Software-Engineering, 2.6 Statistik,
    2.7 Angewandte Regelungstechnik, 2.8 Maschinelle Sprachverarbeitung,
    2.9 Mensch-Maschine-Interaktion, 2.10 Robotikpraktikum 4, 2.11 Seminar
    Wissenschaftliches Arbeiten, 2.12 Sensordatenfusion, 2.13 Angewandte
    Generative KI, 2.14 Computer Vision und 3D-Datenverarbeitung,
    2.15 Projektarbeit (10 CP), 2.16 Simulation von Robotersystemen,
    2.17 Praktische Tätigkeit (20 CP), 2.18 Praxisseminar (3 CP),
    2.19 Bachelorarbeit (12 CP), 2.20 Bachelorseminar (3 CP)

## Large Language Models in Cybersecurity, Threats, Exposure and Mitigation
- **Autor:** Andrei Kucharavy, Octave Plancherel, Valentin Mulder, Alain
  Mermoud, Vincent Lenders (Hrsg.) (2024, Springer, Open Access CC BY 4.0;
  Cyber-Defence Campus, armasuisse)
- **Ordner:** `KI_und_Daten/`
- **Datei:** Kucharavy_Large Language Models in Cybersecurity.pdf
- **Relevanz:** Sammelband mit 27 kurzen Beiträgen (rund 250 Seiten). Teil I
  (Kap. 1 bis 6) ist eine kompakte, technisch saubere Einführung in
  Sprachmodelle samt ihrer grundsätzlichen Grenzen (Kap. 5) und ihrer
  Evaluierung (Kap. 6) und damit Begleitlektüre zu Modulen wie Maschinelle
  Sprachverarbeitung und Angewandte Generative KI. Praktisch nutzbar für eine
  eigene agentische Arbeitsumgebung sind Kap. 9 (Schwachstellen durch
  Code-Vorschläge), Kap. 10 (Übernahme des Ausführungsflusses, also Prompt
  Injection), Kap. 7 (Abfluss privater Daten) und Kap. 23 (Betrieb im eigenen
  Haus). Für die Limitations-Diskussion KI-gestützter Beratung ergänzt es
  Arica/Freye, Digital Consulting, Kap. 5 bis 6 um die Risikoseite. Stand
  2024, bei Modellfamilien (Kap. 3) und Marktdaten (Kap. 13 bis 14) schnell
  veraltet. Kein Supply-Chain-Bezug.
- **Inhaltsverzeichnis:**
  - Part I Introduction (Kap. 1 From Deep Neural Language Models to LLMs,
    Kap. 2 Adapting LLMs to Downstream Applications, Kap. 3 Overview of
    Existing LLM Families, Kap. 4 Conversational Agents, Kap. 5 Fundamental
    Limitations of Generative LLMs, Kap. 6 Tasks for LLMs and Their
    Evaluation)
  - Part II LLMs in Cybersecurity (Kap. 7 Private Information Leakage,
    Kap. 8 Phishing and Social Engineering, Kap. 9 Vulnerabilities
    Introduced by LLMs Through Code Suggestions, Kap. 10 LLM Controls
    Execution Flow Hijacking, Kap. 11 LLM-Aided Social Media Influence
    Operations, Kap. 12 Deep(er) Web Indexing with LLMs)
  - Part III Tracking and Forecasting Exposure (Kap. 13 LLM Adoption Trends
    and Associated Risks, Kap. 14 The Flow of Investments in the LLM Space,
    Kap. 15 Insurance Outlook for LLM-Induced Risk, Kap. 16
    Copyright-Related Risks, Kap. 17 Monitoring Emerging Trends in LLM
    Research)
  - Part IV Mitigation (Kap. 18 Security Awareness and Education, Kap. 19
    Privacy Preserving LLMs Training, Kap. 20 Adversarial Evasion, Kap. 21
    Robust and Private Federated Learning, Kap. 22 LLM Detectors, Kap. 23
    On-Site Deployment of LLMs, Kap. 24 LLMs Red Teaming, Kap. 25 Standards
    for LLM Security)
  - Part V Conclusion (Kap. 26 The Dual Role of LLMs in Cybersecurity,
    Kap. 27 Towards Safe LLMs Integration)

## The EU AI Act, Answers to Frequently Asked Questions
- **Autor:** Paul Voigt, Nils Hullen (2024, Springer; Übersetzung von
  „Handbuch KI-Verordnung", das deutsche Original ist nicht abgelegt)
- **Ordner:** `KI_und_Daten/`
- **Datei:** Voigt_The EU AI Act.pdf
- **Relevanz:** Juristisches Praxishandbuch im Frage-Antwort-Format (rund
  240 Seiten), Stand August 2024. Maßgebliche Quelle für die
  Regulierungsseite jedes KI-Vorhabens und damit die belastbare Vertiefung
  zu Ziegeler, KI in der Supply Chain, Kap. 7. Für die eigene Praxis zählt
  vor allem die Rollenfrage in Kap. 1.3 (Anbieter oder Betreiber, ein
  Unternehmen mit selbst gebauten KI-Auswertungen ist in der Regel
  Betreiber), die Risikoklassen in Kap. 1.2 und 3 sowie die
  Transparenzpflichten in Kap. 4. Kap. 7 ordnet DSGVO, Produktsicherheit,
  Haftung und Normen ein. In der Beratung „AI in Operations" ist das die
  Grundlage, um eine Compliance-Frage einzuordnen, nicht um sie zu
  beantworten. Kein Rechtsrat. Leitlinien und Fristen nach 08/2024 fehlen,
  vor einer Aussage zum geltenden Stand gegenprüfen. Englisch: in deutschen
  Dokumenten auf den Originaltitel verweisen.
- **Inhaltsverzeichnis:**
  - Kap. 1 Scope and General Requirements (New Legislative Framework,
    erfasste KI-Arten: AI System, AI Model, verbotene Praktiken,
    Hochrisiko, Transparenzpflichten, GPAI-Modelle, Ausnahmen; erfasste
    Akteure: Provider, Deployer, Importer u. a.)
  - Kap. 2 What AI Practices Are Prohibited?
  - Kap. 3 Which Requirements Apply to High-Risk AI Systems? (u. a. 3.2
    Anforderungen an die Systeme, 3.3 Pflichten der Anbieter)
  - Kap. 4 Which AI Systems Are Subject to Specific Transparency
    Obligations?
  - Kap. 5 Which Requirements Apply to GPAI Models?
  - Kap. 6 How Is the AI Act Implemented and Enforced?
  - Kap. 7 What Other Legislation Is Particularly Relevant with Regard to
    AI? (7.2 Datenschutz, 7.3 allgemeine Produktsicherheit, 7.4 Haftung,
    7.5 internationale Regelwerke, 7.6 technische Normen und Standards)
  - Unterabschnitte unterhalb der genannten Ebene nicht einzeln erfasst

## Public Governance and Emerging Technologies, Values, Trust, and Regulatory Compliance
- **Autor:** Jurgen Goossens, Esther Keymolen, Antonia Stanojević (Hrsg.)
  (2025, Springer, Open Access CC BY 4.0; Utrecht und Tilburg, gefördert
  vom niederländischen Forschungsrat NWO)
- **Ordner:** `KI_und_Daten/`
- **Datei:** Goossens_Public Governance and Emerging Technologies.pdf
- **Relevanz:** Rechts- und verwaltungswissenschaftlicher Sammelband (16
  Beiträge, rund 390 Seiten) über den Einsatz von Algorithmen, KI und
  Blockchain in der öffentlichen Verwaltung. Für Supply Chain und Controlling
  nachrangig, nur kapitelweise heranziehen. Übertragbar sind drei Beiträge:
  „Explainable AI Is No Silver Bullet" (angemessenes Vertrauen in
  KI-Empfehlungen, anschlussfähig an Erklärbarkeit im Maschinellen Lernen und
  an jedes Dashboard mit Modellvorschlag), „Algorithmic Impact Assessments"
  (Folgenabschätzung als Instrument, neben Voigt/Hullen zu lesen) und
  „Learning-Loop Bureaucracies" (KI, Recht und Organisation als Konfiguration,
  Bezug zur Organisationsseite bei Liebetruth). Belegquelle für Aussagen,
  keine Methodenanleitung.
- **Inhaltsverzeichnis:** Beiträge ohne Kapitelnummern
  - Einleitung: Governance by Technology, Governance of Technology
  - Part I Governance: By and of Technology (Municipalities Enacting
    Algorithms; The Role of Technology in Citizens' Right to Good
    Administration; Explainable AI Is No Silver Bullet; European Digital
    Infrastructure Consortium (EDIC); Privacy-By-Design in the Belgian
    Public Sector; Our Stakes in Data)
  - Part II Regulatory Compliance (Regulatory Equivalence in Blockchain
    Systems; Algorithmic Impact Assessments (AIAs) as Instruments for
    Accountability and Social Control; Quantum Computing with Fiduciary
    Law; The Rule of Tech? Submitting Legislation to Digital Constraints;
    The Shaping of AI Policies in Latin America)
  - Part III Public Trust and Values (Empathy as a Public Value; Civic Vice
    in Digital Governance; Algorithmic Governance and Social Vulnerability;
    The Frameworks of Trust and Trustlessness Around Algorithmic Control
    Technologies; Learning-Loop Bureaucracies)

## Modulhandbuch M.Sc. „Artificial Intelligence for Connected Industries" (AI4CI)
- **Autor:** Universität Ulm, Fakultät für Ingenieurwissenschaften,
  Informatik und Psychologie (Stand Wintersemester 2025/2026, erzeugt
  24.07.2026)
- **Ordner:** `Curricula/`
- **Datei:** Universität Ulm_Modulhandbuch Artificial Intelligence for Connected Industries.pdf
- **Relevanz:** Zweite Landkarte neben dem THA-Bachelor für ein Lernzielbild
  in KI. Berufsbegleitend, Blended Learning, überwiegend englisch, Module mit
  je 6 ECTS und eigener Prüfung. Pflicht sind laut Handbuch nur das Modul
  AI/ML (6 ECTS) und die Master Thesis (30 ECTS), der Rest wird aus drei
  Wahlpflichtbereichen und freien Wahlmodulen belegt. Wie viele ECTS je
  Bereich Pflicht sind, steht nicht im Handbuch, sondern in der
  Prüfungsordnung. Für ein Profil zwischen Supply Chain und Daten trägt vor
  allem der Bereich „Processes and Data Management" (Data and Process Mining
  mit Celonis, Business Process Management, Numerische Methoden für Data
  Science, Project Management nach PMBOK), dazu AI/ML und Pattern Recognition
  and Deep Learning. Die Bereiche „Systems and Networks" und „Automatics and
  Robots" sind Embedded, Regelungstechnik und Robotik. Generative KI,
  Sprachverarbeitung, Cloud und Betrieb von Modellen kommen nicht vor.
- **Inhaltsverzeichnis:**
  - Pflicht: 1 Artificial Intelligence and Machine Learning for Connected
    Systems, 2 Master Thesis
  - Wahlpflicht Systems and Networks: 3 Design of Embedded Real-Time
    Systems, 4 Management Aspects of Systems Engineering I,
    5 Systemtechnik, 6 Wireless Sensor Networks, 7 Module der
    Partneruniversitäten
  - Wahlpflicht Automatics and Robots: 8 Control System Theory and Control
    Engineering, 9 Learning Robots, 10 Modeling and Identification of
    Dynamic Systems, 11 Pattern Recognition and Deep Learning, 12 Robot
    Operating Systems (3 ECTS), 13 Signals and Systems, 14 Module der
    Partneruniversitäten
  - Wahlpflicht Processes and Data Management: 15 Big (Social) Data
    Analytics, 16 Business Process Management, 17 Data and Process Mining,
    18 Numerische Methoden für Data Science, 19 Project Management,
    20 Module der Partneruniversitäten
  - Freie Wahlmodule: 21 aus Sensor Systems Engineering, 22 aus Business
    Analytics (empfohlen: Machine Learning with Python, Advanced Python
    Programming), 23 der Partneruniversitäten (u. a. Operations Research,
    Federated and Distributed Learning, Industrial Internet of Things)

## An Introduction to Statistical Learning, with Applications in Python (ISLP)
- **Autor:** Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani,
  Jonathan Taylor (2023, Springer Texts in Statistics; von den Autoren frei
  bereitgestellt über statlearning.com)
- **Ordner:** `KI_und_Daten/`
- **Datei:** James_An Introduction to Statistical Learning with Applications in Python.pdf
- **Relevanz:** Grundlagenwerk für Maschinelles Lernen. Das THA-Modulhandbuch
  nennt dort keine Literatur, das Ulmer Handbuch führt genau diesen Titel im
  Pflichtmodul AI/ML. Jedes Kapitel endet mit einem Python-Lab. Erste Wahl für
  einen eigenen Lernblock, weil es Statistik und ML in einem Zug behandelt
  (Kap. 2 bis 6 decken auch ein Statistikmodul weitgehend). Anschlussfähig an
  die Gütemaße in Ivanov, Global SCOM, Kap. 11.
- **Inhaltsverzeichnis:**
  - Kap. 1 Introduction
  - Kap. 2 Statistical Learning
  - Kap. 3 Linear Regression
  - Kap. 4 Classification
  - Kap. 5 Resampling Methods
  - Kap. 6 Linear Model Selection and Regularization
  - Kap. 7 Moving Beyond Linearity
  - Kap. 8 Tree-Based Methods
  - Kap. 9 Support Vector Machines
  - Kap. 10 Deep Learning
  - Kap. 11 Survival Analysis and Censored Data
  - Kap. 12 Unsupervised Learning
  - Kap. 13 Multiple Testing

## Speech and Language Processing
- **Autor:** Daniel Jurafsky, James H. Martin (Entwurf der 3. Auflage,
  Fassung vom 19.08.2026; von den Autoren frei bereitgestellt über
  web.stanford.edu/~jurafsky/slp3)
- **Ordner:** `KI_und_Daten/`
- **Datei:** Jurafsky_Speech and Language Processing.pdf
- **Relevanz:** Literaturangabe des THA-Moduls Maschinelle Sprachverarbeitung
  und das Standardlehrbuch des Fachs. Teil I führt von N-Grammen über
  Embeddings und neuronale Netze bis zu Transformern und liefert damit die
  Theorie, um Generative AI als Lösung zu bauen. Kap. 11 (Retrieval) und Kap.
  12 (Agents) sind die Grundlage für ein eigenes RAG- oder Agentenprojekt.
  Teil III (linguistische Annotation) ist für Anwender nachrangig. Entwurf,
  die Kapitelnummern ändern sich zwischen den Fassungen, deshalb immer mit
  Fassungsdatum zitieren.
- **Inhaltsverzeichnis:**
  - Part I Large Language Models (Kap. 1 Introduction, Kap. 2 Words and
    Tokens, Kap. 3 N-gram Language Models, Kap. 4 Logistic Regression,
    Kap. 5 Embeddings, Kap. 6 Neural Networks, Kap. 7 Transformers and
    Pretraining, Kap. 8 Post-training)
  - Part II Advanced LLM Topics and Tools (Kap. 9 Masked Language Models,
    Kap. 10 Interpretability, Kap. 11 Retrieval-based Models, Kap. 12
    Agents, Kap. 13 Machine Translation, Kap. 14 RNNs and LSTMs, Kap. 15
    Phonetics and Speech Feature Extraction, Kap. 16 Automatic Speech
    Recognition, Kap. 17 Text-to-Speech)
  - Part III Annotating Linguistic Structure (Kap. 18 Sequence Labeling,
    Kap. 19 Context-Free Grammars and Constituency Parsing, Kap. 20
    Dependency Parsing, Kap. 21 Information Extraction, Kap. 22 Semantic
    Role Labeling, Kap. 23 Lexicons for Sentiment, Affect, and Connotation,
    Kap. 24 Coreference Resolution and Entity Linking, Kap. 25 Discourse
    Coherence, Kap. 26 Conversation and its Structure)

## Deep Learning
- **Autor:** Ian Goodfellow, Yoshua Bengio, Aaron Courville (2016, MIT Press,
  Reihe Adaptive Computation and Machine Learning)
- **Ordner:** `KI_und_Daten/`
- **Datei:** Goodfellow_Deep Learning.pdf (801 Seiten, Satz der Webfassung von
  deeplearningbook.org, Seitenzahlen weichen von der Druckausgabe ab, deshalb
  nach Kapitel und Abschnitt zitieren)
- **Relevanz:** Das theoretische Standardwerk und Literaturangabe des
  THA-Moduls Angewandte Generative KI. Schließt die Lücke, die beide
  Modulhandbücher lassen, nämlich ein eigenes Fundament für Deep Learning.
  Teil I (Kap. 2 bis 5) ist zugleich die knappste Zusammenfassung der Mathematik,
  die ML braucht, und damit der Prüfstein, ob Hartmann und Kurt reichen.
  Teil II (Kap. 6 bis 12) ist der Kern für die Praxis. Teil III ist
  Forschungsstand 2016 und für das Zielbild nachrangig. Grenze: Das Buch
  endet vor dem Transformer, Attention und Sprachmodelle fehlen. Dafür
  Jurafsky/Martin, Kap. 7 bis 8, und Alammar/Grootendorst lesen. Keine
  Programmierbeispiele, also immer mit ISLP, Kap. 10, oder einem
  Framework-Kurs kombinieren.
- **Inhaltsverzeichnis:**
  - Kap. 1 Introduction
  - Part I Applied Math and Machine Learning Basics (Kap. 2 Linear Algebra,
    Kap. 3 Probability and Information Theory, Kap. 4 Numerical Computation,
    Kap. 5 Machine Learning Basics)
  - Part II Deep Networks: Modern Practices (Kap. 6 Deep Feedforward
    Networks, Kap. 7 Regularization for Deep Learning, Kap. 8 Optimization
    for Training Deep Models, Kap. 9 Convolutional Networks, Kap. 10
    Sequence Modeling: Recurrent and Recursive Nets, Kap. 11 Practical
    Methodology, Kap. 12 Applications)
  - Part III Deep Learning Research (Kap. 13 Linear Factor Models, Kap. 14
    Autoencoders, Kap. 15 Representation Learning, Kap. 16 Structured
    Probabilistic Models for Deep Learning, Kap. 17 Monte Carlo Methods,
    Kap. 18 Confronting the Partition Function, Kap. 19 Approximate
    Inference, Kap. 20 Deep Generative Models)

## Hands-On Large Language Models, Language Understanding and Generation
- **Autor:** Jay Alammar, Maarten Grootendorst (1. Auflage 09/2024, O'Reilly)
- **Ordner:** `KI_und_Daten/`
- **Datei:** Alammar_Hands-On Large Language Models.pdf
- **Relevanz:** Das Praxisbuch, um Generative AI als Lösung zu bauen, und
  Literaturangabe des THA-Moduls Angewandte Generative KI. Durchgehend mit
  lauffähigem Python-Code und vielen Abbildungen, kaum Formeln. Für ein
  eigenes Supply-Chain-Projekt tragen Kap. 8 (semantische Suche und RAG), Kap.
  7 (Ketten, Gedächtnis, Agenten), Kap. 6 (Prompt Engineering) und Kap. 4 bis
  5 (Klassifikation und Clustering von Texten, etwa Lieferantenkorrespondenz
  oder Reklamationen). Teil III (Feinabstimmung) erst bei Bedarf. Die Theorie
  dahinter steht in Jurafsky/Martin, Teil I. Stand 2024, Modellnamen und
  Bibliotheksversionen veralten schnell, die Konzepte nicht. Evaluierung wird
  nur am Rand behandelt und muss aus anderer Quelle kommen.
- **Inhaltsverzeichnis:**
  - Part I Understanding Language Models (Kap. 1 An Introduction to Large
    Language Models, Kap. 2 Tokens and Embeddings, Kap. 3 Looking Inside
    Large Language Models)
  - Part II Using Pretrained Language Models (Kap. 4 Text Classification,
    Kap. 5 Text Clustering and Topic Modeling, Kap. 6 Prompt Engineering,
    Kap. 7 Advanced Text Generation Techniques and Tools, Kap. 8 Semantic
    Search and Retrieval-Augmented Generation, Kap. 9 Multimodal Large
    Language Models)
  - Part III Training and Fine-Tuning Language Models (Kap. 10 Creating
    Text Embedding Models, Kap. 11 Fine-Tuning Representation Models for
    Classification, Kap. 12 Fine-Tuning Generation Models)

## Mathematik für Informatiker, Ein praxisbezogenes Lehrbuch
- **Autor:** Peter Hartmann (7. Auflage 2019, Springer Vieweg; Hochschule
  Landshut)
- **Ordner:** `Mathematik_und_Informatik/`
- **Datei:** Hartmann_Mathematik für Informatiker.pdf
- **Relevanz:** Literaturangabe der THA-Module Mathematik 1 und 2 und ein
  Mathematikbuch, das für Maschinelles Lernen reicht, weil es lineare Algebra,
  Analysis und Statistik in einem Band führt. Für ML zählen Kap. 6 bis 10
  (Vektorräume bis Eigenwerte und Skalarprodukt), Kap. 15
  (Differenzialrechnung) und Teil III. Kap. 11 (Graphentheorie) ist Grundlage
  für Netzwerk- und Routingfragen und anschlussfähig an Hanne/Dornberger, Kap.
  3. Mehrdimensionale Analysis (Gradient) ist knapp, dafür
  Oberguggenberger/Ostermann, Kap. 15, heranziehen. Ein weiteres
  Grundlagenbuch wie Teschl ist damit entbehrlich.
- **Inhaltsverzeichnis:**
  - Teil I Diskrete Mathematik und lineare Algebra (Kap. 1 Mengen und
    Abbildungen, Kap. 2 Logik, Kap. 3 Natürliche Zahlen, vollständige
    Induktion, Rekursion, Kap. 4 Etwas Zahlentheorie, Kap. 5 Algebraische
    Strukturen, Kap. 6 Vektorräume, Kap. 7 Matrizen, Kap. 8 Gauß'scher
    Algorithmus und lineare Gleichungssysteme, Kap. 9 Eigenwerte,
    Eigenvektoren und Basistransformationen, Kap. 10 Skalarprodukt und
    orthogonale Abbildungen, Kap. 11 Graphentheorie)
  - Teil II Analysis (Kap. 12 Die reellen Zahlen, Kap. 13 Folgen und
    Reihen, Kap. 14 Stetige Funktionen, Kap. 15 Differenzialrechnung,
    Kap. 16 Integralrechnung, Kap. 17 Differenzialgleichungen, Kap. 18
    Numerische Verfahren)
  - Teil III Wahrscheinlichkeitsrechnung und Statistik (Kap. 19
    Wahrscheinlichkeitsräume, Kap. 20 Zufallsvariable, Kap. 21 Wichtige
    Verteilungen, stochastische Prozesse, Kap. 22 Statistische Verfahren)

## Analysis für Informatiker, Grundlagen, Methoden, Algorithmen
- **Autor:** Michael Oberguggenberger, Alexander Ostermann (3. Auflage 2025,
  Springer; Universität Innsbruck)
- **Ordner:** `Mathematik_und_Informatik/`
- **Datei:** Oberguggenberger_Analysis für Informatiker.pdf
- **Relevanz:** Steht in keinem der beiden Modulhandbücher, ergänzt Hartmann
  aber genau dort, wo dieser knapp ist, mit Funktionen mehrerer Veränderlicher
  samt Gradient und Extrema (Kap. 15 bis 16) als Voraussetzung für
  Gradientenabstieg, dazu Kap. 18 (lineare Regression aus Sicht der Analysis
  hergeleitet, Brücke zu ISLP, Kap. 3). Algorithmisch angelegt, mit
  begleitender Software. Kap. 19 bis 21 (Differentialgleichungen) nur für
  Regelungstechnik und Simulation nötig, also nachrangig. Als Nachschlagewerk
  kapitelweise nutzen, nicht durcharbeiten.
- **Inhaltsverzeichnis:**
  - Kap. 1 Zahlen, Kap. 2 Reellwertige Funktionen, Kap. 3 Trigonometrie,
    Kap. 4 Komplexe Zahlen, Kap. 5 Folgen und Reihen, Kap. 6 Grenzwerte und
    Stetigkeit von Funktionen
  - Kap. 7 Die Ableitung einer Funktion, Kap. 8 Anwendungen der Ableitung,
    Kap. 9 Fraktale und L-Systeme
  - Kap. 10 Stammfunktionen, Kap. 11 Bestimmte Integrale, Kap. 12
    Taylorreihen, Kap. 13 Numerische Integration, Kap. 14 Kurven
  - Kap. 15 Skalarwertige Funktionen in zwei Veränderlichen, Kap. 16
    Vektorwertige Funktionen in zwei Veränderlichen, Kap. 17
    Integralrechnung in zwei Veränderlichen, Kap. 18 Lineare Regression
  - Kap. 19 Differentialgleichungen, Kap. 20 Systeme von
    Differentialgleichungen, Kap. 21 Numerik von Differentialgleichungen
  - Anhang A Vektorrechnung, B Matrizen, C Ergänzungen zur Stetigkeit,
    D Beschreibung der ergänzenden Software

## Stochastik für Informatiker, Eine Einführung in einheitlich strukturierten Lerneinheiten
- **Autor:** Noemi Kurt (2020, Springer Vieweg; TU Berlin)
- **Ordner:** `Mathematik_und_Informatik/`
- **Datei:** Kurt_Stochastik für Informatiker.pdf
- **Relevanz:** Literaturangabe des THA-Moduls Statistik. Kompakt (rund 250
  Seiten) und in gleich aufgebauten Lerneinheiten, damit gut für das
  Selbststudium in kurzen Blöcken. Teil I und II sind das Fundament für
  ISLP und Goodfellow, Kap. 3. Mit direktem Bezug zur eigenen Praxis:
  Kap. 14 (Warteschlangenmodelle, anschlussfähig an Ivanov, Supply Chain
  Analytics, Kap. 3) und Kap. 15 (Monte-Carlo-Simulation, anschlussfähig an
  die Szenariorechnung bei Reim, Kap. 14). Regression und multivariate
  Verfahren fehlen, die stehen in ISLP.
- **Inhaltsverzeichnis:**
  - Teil I Grundlagen der Wahrscheinlichkeitstheorie (Kap. 1 Endliche
    Wahrscheinlichkeitsräume, Kap. 2 Bedingte Wahrscheinlichkeiten und
    Unabhängigkeit, Kap. 3 Diskrete Zufallsvariablen und Verteilungen,
    Kap. 4 Gemeinsame Verteilung, Unabhängigkeit von Zufallsvariablen,
    Kap. 5 Kenngrößen für Zufallsvariablen, Kap. 6 Zufallsvariablen mit
    Dichte, Kap. 7 Grenzwertsätze)
  - Teil II Einführung in die Statistik (Kap. 8 Parameterschätzung, Kap. 9
    Konfidenzbereiche, Kap. 10 Hypothesentests)
  - Teil III Markov-Ketten und stochastische Algorithmen (Kap. 11
    Markov-Ketten, Kap. 12 Randomisierte Algorithmen, Kap. 13
    Verzweigungsprozesse und erzeugende Funktionen, Kap. 14
    Warteschlangenmodelle und Markov-Ketten in stetiger Zeit, Kap. 15
    Simulation von Zufallsvariablen, Monte-Carlo-Methode)

## Quantenlogik, Eine Einführung für Ingenieure und Informatiker
- **Autor:** Günther Wirsching, Matthias Wolff, Ingo Schmitt (2023, Springer;
  KU Eichstätt-Ingolstadt, BTU Cottbus-Senftenberg)
- **Ordner:** `Mathematik_und_Informatik/`
- **Datei:** Wirsching_Quantenlogik.pdf
- **Relevanz:** Steht in keinem Modulhandbuch und hat keinen Bezug zu Supply
  Chain oder Controlling. Reines Interessensthema. Mittelbar nutzbar sind zwei
  Teile, Kap. 1 und 3 als gründliche Einführung in klassische Logik
  (Hintergrund zur symbolischen KI im THA-Modul KI und Robotik) und Kap. 5 als
  zweite Darstellung der linearen Algebra. Kap. 7 zeigt Anwendungen in
  Datenbankabfragen und Psychologie. Kein Buch über Quantencomputer.
- **Inhaltsverzeichnis:**
  - Kap. 1 Einführung in die Logik
  - Kap. 2 Grundlegende mathematische Strukturen
  - Kap. 3 Klassische Logiken
  - Kap. 4 Logik der Überlagerungen
  - Kap. 5 Lineare Algebra
  - Kap. 6 Logik der Orthogonalprojektoren
  - Kap. 7 Anwendungen in Datenbanken und Psychologie

## Working Effectively with Legacy Code
- **Autor:** Michael C. Feathers (2005, Prentice Hall, Robert C. Martin
  Series; Erstdruck 09/2004)
- **Ordner:** `Software_Engineering/`
- **Datei:** Feathers_Working Effectively with Legacy Code.pdf
- **Relevanz:** Standardwerk für das sichere Ändern von Code ohne Tests. Kein
  Supply-Chain-Bezug, aber direkt nutzbar für eine eigene Python-Pipeline.
  Kap. 2 (Legacy Code Change Algorithm) und Kap. 13 (Characterization Tests)
  liefern das Vorgehen, um bestehendes Verhalten vor einem Umbau
  festzuschreiben, anschlussfähig an Vergleichsläufe zwischen alter und neuer
  Pipeline und an den Neuaufbau einer Input-Schicht. Kap. 4 (Seam Model) und
  Kap. 6 (Sprout und Wrap) für Änderungen unter Zeitdruck. Kap. 19 behandelt
  nicht objektorientierten Code und ist damit für prozedurale Skripte das
  passendste Kapitel. Teil III ist ein Katalog zum Nachschlagen, nicht zum
  Durchlesen. Grenze: Beispiele in Java, C++ und C#, Werkzeugstand 2004 (Kap.
  5 veraltet), die Techniken müssen auf Python übertragen werden.
- **Inhaltsverzeichnis:**
  - Part I The Mechanics of Change (Kap. 1 Changing Software, Kap. 2
    Working with Feedback, Kap. 3 Sensing and Separation, Kap. 4 The Seam
    Model, Kap. 5 Tools)
  - Part II Changing Software (Kap. 6 I Don't Have Much Time and I Have to
    Change It, Kap. 7 It Takes Forever to Make a Change, Kap. 8 How Do I
    Add a Feature?, Kap. 9 I Can't Get This Class into a Test Harness,
    Kap. 10 I Can't Run This Method in a Test Harness, Kap. 11 I Need to
    Make a Change. What Methods Should I Test?, Kap. 12 I Need to Make Many
    Changes in One Area, Kap. 13 I Need to Make a Change, but I Don't Know
    What Tests to Write, Kap. 14 Dependencies on Libraries Are Killing Me,
    Kap. 15 My Application Is All API Calls, Kap. 16 I Don't Understand the
    Code Well Enough to Change It, Kap. 17 My Application Has No Structure,
    Kap. 18 My Test Code Is in the Way, Kap. 19 My Project Is Not Object
    Oriented. How Do I Make Safe Changes?, Kap. 20 This Class Is Too Big
    and I Don't Want It to Get Any Bigger, Kap. 21 I'm Changing the Same
    Code All Over the Place, Kap. 22 I Need to Change a Monster Method and
    I Can't Write Tests for It, Kap. 23 How Do I Know That I'm Not Breaking
    Anything?, Kap. 24 We Feel Overwhelmed. It Isn't Going to Get Any
    Better)
  - Part III Dependency-Breaking Techniques (Kap. 25, Katalog von 24
    Techniken von Adapt Parameter bis Text Redefinition)
  - Appendix Refactoring (Extract Method), Glossary

## The Data Warehouse Toolkit (The Definitive Guide to Dimensional Modeling)
- **Autor:** Ralph Kimball, Margy Ross (3rd Edition 2013, Wiley)
- **Ordner:** `KI_und_Daten/`
- **Datei:** Kimball_The Data Warehouse Toolkit.pdf
- **Relevanz:** Referenzwerk der dimensionalen Modellierung (Fakten,
  Dimensionen, Star Schema) und damit die methodische Grundlage für einen
  eigenen Data Mart. Kap. 2 ist der Katalog aller Techniken zum Nachschlagen,
  Kap. 3 führt den vierstufigen Designprozess ein (Geschäftsprozess,
  Granularität, Dimensionen, Fakten). Direkt anschlussfähig sind Kap. 4
  Inventory (periodischer Snapshot, Bus-Matrix, Conformed Dimensions) für
  Bestandsauswertungen und die Materialdimension, Kap. 5 Procurement (Slowly
  Changing Dimensions) für Bestell- und Lieferantendaten, Kap. 6 Order
  Management (Kopf/Position, Accumulating Snapshot) für Auftragsdaten. Kap. 19
  bis 20 (34 ETL-Subsysteme, Vorgehen) als Prüfliste für die Ingest-Schicht.
  Kap. 16 schließt mit zehn typischen Modellierungsfehlern. Grenze: Stand
  2013, Kap. 21 (Big Data, Hadoop) ist veraltet, Kap. 8 bis 16 außer den
  genannten sind Branchenfallstudien ohne Fertigungsbezug.
- **Inhaltsverzeichnis:**
  - Kap. 1 Data Warehousing, Business Intelligence, and Dimensional
    Modeling Primer
  - Kap. 2 Kimball Dimensional Modeling Techniques Overview
  - Kap. 3 Retail Sales
  - Kap. 4 Inventory
  - Kap. 5 Procurement
  - Kap. 6 Order Management
  - Kap. 7 Accounting
  - Kap. 8 Customer Relationship Management
  - Kap. 9 Human Resources Management
  - Kap. 10 Financial Services
  - Kap. 11 Telecommunications
  - Kap. 12 Transportation
  - Kap. 13 Education
  - Kap. 14 Healthcare
  - Kap. 15 Electronic Commerce
  - Kap. 16 Insurance
  - Kap. 17 Kimball DW/BI Lifecycle Overview
  - Kap. 18 Dimensional Modeling Process and Tasks
  - Kap. 19 ETL Subsystems and Techniques
  - Kap. 20 ETL System Design and Development Process and Tasks
  - Kap. 21 Big Data Analytics

## Fundamentals of Data Engineering, Plan and Build Robust Data Systems
- **Autor:** Joe Reis, Matt Housley (1. Auflage 07/2022, O'Reilly)
- **Ordner:** `KI_und_Daten/`
- **Datei:** Reis_Fundamentals of Data Engineering.pdf
- **Relevanz:** Füllt die Lücke Data Engineering und Plattform-Architektur,
  Hauptquelle für den Aufbau einer eigenen Datenplattform neben Kimball. Kap.
  2 (Lebenszyklus mit den „Undercurrents" Data Management, DataOps,
  Orchestrierung) ist ein Ordnungsrahmen für die Verarbeitungsschicht. Kap. 3
  (gute Architektur, umkehrbare Entscheidungen) begründet etwa Parquet und
  DuckDB auf einem Netzlaufwerk statt eines Servers. Kap. 7 (Ingestion,
  Schemaänderung, Idempotenz) trägt Pull-Vertrag und Staging. Kap. 8 stellt
  Kimball neben Inmon und Data Vault und begründet so die Modellwahl. Anhang A
  erklärt Parquet. Grenze: durchgehend cloud-orientiert, für einen
  On-Premise-Fall ohne Server passen viele Werkzeugbeispiele nicht direkt.
- **Inhaltsverzeichnis:**
  - Part I Foundation and Building Blocks (Kap. 1 Data Engineering
    Described, Kap. 2 The Data Engineering Lifecycle, Kap. 3 Designing Good
    Data Architecture, Kap. 4 Choosing Technologies Across the Data
    Engineering Lifecycle)
  - Part II The Data Engineering Lifecycle in Depth (Kap. 5 Data Generation
    in Source Systems, Kap. 6 Storage, Kap. 7 Ingestion, Kap. 8 Queries,
    Modeling, and Transformation, Kap. 9 Serving Data for Analytics, Machine
    Learning, and Reverse ETL)
  - Part III Security, Privacy, and the Future of Data Engineering (Kap. 10
    Security and Privacy, Kap. 11 The Future of Data Engineering)
  - Anhang A Serialization and Compression Technical Details, Anhang B Cloud
    Networking

## Designing Data-Intensive Applications, The Big Ideas Behind Reliable, Scalable, and Maintainable Systems
- **Autor:** Martin Kleppmann (1. Auflage 03/2017, O'Reilly)
- **Ordner:** `KI_und_Daten/`
- **Datei:** Kleppmann_Designing Data-Intensive Applications.pdf
- **Relevanz:** Die technische Tiefe hinter den Entscheidungen beim Aufbau
  einer eigenen Datenplattform. Kap. 1 (Zuverlässigkeit, Wartbarkeit) liefert
  die Qualitätsziele. Kap. 3 (spaltenorientierte Speicherung, OLTP gegen
  Analytics) erklärt, warum Parquet und DuckDB für einen Data Mart passen.
  Kap. 4 (Encoding, Schema-Evolution) ist die Grundlage von
  Konsumentenverträgen. Kap. 8 (unzuverlässige Uhren, Leases, Fencing Tokens)
  begründet eine Sperrdatei mit Ablaufzeit beim Lauf auf mehreren Rechnern.
  Kap. 10 (Batch-Verarbeitung, unveränderliche Inputs, abgeleitete Daten) ist
  das Denkmodell einer Batch-Pipeline, Kap. 12 (Unbundling, Korrektheit über
  die ganze Kette) die Begründung, warum der Kern jederzeit aus dem
  Quellsystem neu baubar sein sollte. Kap. 5, 6, 9 und 11 (Replikation,
  Partitionierung, Konsens, Streaming) sind für kleine On-Premise-Fälle
  nachrangig. Ergänzt Reis/Housley um die Tiefe, die dort zugunsten der Breite
  fehlt. Das Glossar ist ein guter Einstieg in die Begriffe.
- **Inhaltsverzeichnis:**
  - Part I Foundations of Data Systems (Kap. 1 Reliable, Scalable, and
    Maintainable Applications, Kap. 2 Data Models and Query Languages,
    Kap. 3 Storage and Retrieval, Kap. 4 Encoding and Evolution)
  - Part II Distributed Data (Kap. 5 Replication, Kap. 6 Partitioning,
    Kap. 7 Transactions, Kap. 8 The Trouble with Distributed Systems, Kap. 9
    Consistency and Consensus)
  - Part III Derived Data (Kap. 10 Batch Processing, Kap. 11 Stream
    Processing, Kap. 12 The Future of Data Systems)
  - Glossary, Index

## Make It Stick: The Science of Successful Learning
- **Autor:** Peter C. Brown, Henry L. Roediger III, Mark A. McDaniel (2014),
  The Belknap Press of Harvard University Press
- **Ordner:** `Lernen_und_Wissensarbeit/`
- **Datei:** Brown_Make It Stick, The Science of Successful Learning.pdf
- **Relevanz:** Grundlage für das Lernsystem nach ALTER. Kap. 2 (Abruf) und
  Kap. 3 (Mischen und Verteilen der Übung) stützen die Wiederholungs-Engine
  und das Tagesbudget. Kap. 4 (erwünschte Schwierigkeiten) und Kap. 5
  (Illusion des Wissens) stützen Selbsttests und den Nachweis am Ende jedes
  Blocks. Kap. 8 fasst die Praxisregeln zusammen. Quelle des Frameworks
  ALTER_Lebenslanges_Lernen.
- **Inhaltsverzeichnis:**
  - Preface
  - 1 Learning Is Misunderstood
  - 2 To Learn, Retrieve
  - 3 Mix Up Your Practice
  - 4 Embrace Difficulties
  - 5 Avoid Illusions of Knowing
  - 6 Get Beyond Learning Styles
  - 7 Increase Your Abilities
  - 8 Make It Stick
  - Notes, Suggested Reading, Acknowledgments, Index

## Swadia, zwei Videos zum Selbststudium (ALTER und die drei Tore)
- **Autor:** Sandeep Swadia, YouTube (2026)
- **Ordner:** `Lernen_und_Wissensarbeit/`
- **Datei:** Swadia_Videos_Notizen.md (nicht mitgeliefert) (eigene Notizen mit Zeitmarken, kein
  Transkript)
- **Relevanz:** Herkunft der fünf Rollen des Frameworks
  ALTER_Lebenslanges_Lernen und der fünf Entscheidungen des Skills
  `/advisor`. Video 2 liefert mit den drei Toren ein Prüfraster für neue Werke
  und mit dem Entscheidungsjournal eine Übung zur Kalibrierung.
- **Inhaltsverzeichnis:**
  - Video 1 „Harvard in a Box“, 0:00 The university in a box, 2:41 Advisor,
    4:45 Actionable learning plans, 9:39 Librarian, 14:02 Tutor, 16:44 Editor,
    18:34 Roommate
  - Video 2 „The Only 7 Books You Need to Educate Yourself Like the Top 1%“,
    0:25 The Three Gates, 2:08 Fooled by randomness, 5:23 The proficiency
    prison, 8:26 Thinking in bets, 11:02 The intelligence trap

## Consulting Methodenkoffer
- **Autor:** Dr. Christopher Schulz / consulting-life.de
- **Datei:** Consulting_Life_Methodenkoffer.md (kein PDF, kuratierter Online-Index)
- **Relevanz:** Denkanstoß für die Methodenwahl in jedem Projekt
- **Inhaltsverzeichnis:** siehe 26 Kategorien direkt in der Datei

## The Official Cambridge Guide to IELTS
- **Autor:** Pauline Cullen, Amanda French, Vanessa Jakeman (2014, Cambridge
  University Press und Cambridge English Language Assessment), Student's Book
  with answers, Academic und General Training
- **Ordner:** `Sprachen/`
- **Datei:** Cullen_The Official Cambridge Guide to IELTS.pdf
- **Relevanz:** Hauptwerk für die Vorbereitung auf IELTS Academic. Die
  Kurzübersicht (S. 7 bis 9) nennt Aufgabentypen, Zeiten und
  Bewertungskriterien je Prüfungsteil. Die Probetests 1 bis 7 sind Academic, 8
  liefert den General-Training-Teil, für einen Startwert und für volle
  Probetests eignet sich einer davon. General Training (Kap. 8 Reading, Kap. 5
  Writing Task 1) braucht man für Academic nicht. Die DVD-ROM mit den
  Speaking-Videos liegt der PDF nicht bei.
- **Inhaltsverzeichnis:**
  - Introduction (S. 5), IELTS Summary (S. 7)
  - Listening skills (S. 13), 8 Units von Getting ready to listen bis
    Contrasting ideas
  - Reading skills (S. 42), 8 Units von Reading strategies bis General
    Training Reading
  - Writing (S. 91), 8 Units, Academic Task 1 (Charts, Vergleiche, Diagramme,
    Karten), General Training Task 1 (Brief), Task 2 (vorbereiten, Ideen
    ausdrücken, prüfen und korrigieren)
  - Speaking (S. 134), 4 Units, Part 1 bis 3 sowie Checking, correcting and
    assessing
  - Practice Tests 1 bis 8 (S. 154 bis 332)
  - Recording Scripts (S. 333), Answer Key (S. 366), Sample Answer Sheets
    (S. 397)

## Cambridge IELTS 19 Academic
- **Autor:** Cambridge University Press & Assessment (2024), Student's Book
  with Answers with Audio with Resource Bank, ISBN 978-1-009-45473-5
- **Ordner:** `Sprachen/`
- **Datei:** Cambridge University Press_IELTS 19 Academic.pdf
- **Relevanz:** echte Prüfungsaufgaben für volle Probetests (IELTS Academic)
  und für einen Startwert. Vier vollständige Tests, dazu Audioscripts,
  Lösungen und Musteraufsätze zum Abgleich der eigenen Writing-Antworten. Das
  Audio zu Listening fehlt in der PDF.
- **Inhaltsverzeichnis:**
  - Introduction (S. 4), Aufbau und Zeiten der vier Prüfungsteile
  - Test 1 (S. 10), Test 2 (S. 33), Test 3 (S. 55), Test 4 (S. 78)
  - Audioscripts (S. 99)
  - Listening and Reading answer keys (S. 120)
  - Sample Writing answers (S. 128)
  - Sample answer sheets (S. 139), Acknowledgements (S. 143)

## Hybrid make-to-stock and make-to-order systems, a taxonomic review
- **Autor:** Kay Peeters, Henny van Ooijen (2020), International Journal of
  Production Research 58(15), 4659 bis 4688
- **Ordner:** `Supply_Chain_und_Operations/`
- **Datei:** Peeters_Hybrid make-to-stock and make-to-order systems, a taxonomic review.pdf
- **Relevanz:** Überblicksarbeit zu hybriden MTS/MTO-Systemen mit einer
  eigenen Taxonomie (sequenziell, parallel, floating). Gute Einstiegsquelle,
  um Literatur zur Auftragsentkopplung und Produktionssteuerung einzuordnen,
  dazu Hinweise auf Industrieanwendungen und offene Forschungsfragen.
- **Inhaltsverzeichnis:**
  - 1 Introduction
  - 2 Hybrid production control (2.1 Definitions, 2.2 Examples of hybrid
    MTS/MTO systems)
  - 3 Review of literature on hybrid production control (3.1 Methodology,
    3.2 Sequential, 3.3 Parallel, 3.4 Floating hybrid production control)
  - 4 Research perspectives on hybrid production control (4.1 Hybrid
    MTS/MTO production control, 4.2 Production systems, 4.3 Further
    research)
  - 5 Industrial perspectives (5.1 Job shop, 5.2 Assembly line, 5.3
    Continuous production, 5.4 Managerial insights)
  - 6 Conclusions and future research

## On optimal dynamic pegging in rescheduling for new order arrival
- **Autor:** Shokraneh K. Moghaddam, Kazuhiro Saitou (2019), Computers &
  Industrial Engineering 136, 46 bis 56
- **Ordner:** `Supply_Chain_und_Operations/`
- **Datei:** Moghaddam_On optimal dynamic pegging in rescheduling for new order arrival.pdf
- **Relevanz:** Neuplanung bei neu eintreffenden Aufträgen, bei der
  Halbfertigware (WIP) anderen Aufträgen neu zugeordnet werden darf. Das
  MIP-Modell wird gegen zwei einfache Neuplanungsansätze verglichen, für
  große Fälle gibt es eine GA-Heuristik.
- **Inhaltsverzeichnis:**
  - 1 Introduction
  - 2 Literature review (2.1 Integrated production planning and scheduling,
    2.2 Dynamic scheduling and rescheduling)
  - 3 Optimization model (3.1 Assumptions)
  - 4 Results (4.1 Simple example, 4.2 Comparison cases, 4.3 Sensitivity
    analysis, 4.4 Mixed model production example)
  - 5 The heuristic algorithm based on GA (5.1 Representation, 5.2
    Evaluation function, 5.3 Selection, 5.4 Genetic operators, 5.5
    Algorithm, 5.6 Analysis of the results)
  - 6 Conclusion and future work

## A novel predictive-reactive rescheduling method for products assembly lines with optimal dynamic pegging
- **Autor:** Shokraneh K. Moghaddam, Kazuhiro Saitou (2022), Computers &
  Industrial Engineering 171, 108496
- **Ordner:** `Supply_Chain_und_Operations/`
- **Datei:** Moghaddam_A novel predictive-reactive rescheduling method with optimal dynamic pegging.pdf
- **Relevanz:** Fortsetzung von Moghaddam/Saitou (2019). Das MIP-Modell wird
  um prädiktiv-reaktive Neuplanung für zufällig eintreffende Aufträge
  erweitert und gegen den rein reaktiven Ansatz verglichen, mit
  Rechenzeitanalyse.
- **Inhaltsverzeichnis:**
  - 1 Introduction
  - 2 Literature review (2.1 Integrated production planning and scheduling,
    2.2 Predictive reactive rescheduling)
  - 3 Problem description and methodology (3.1 Assumptions, 3.2
    Mathematical model)
  - 4 Results (4.1 Predictive-reactive vs reactive-only scheduling with
    dynamic pegging, 4.2 Comparison scenarios, 4.3 Computational time
    analysis)
  - 5 Discussion and implications
  - 6 Conclusion and future research

## Making agency theory work for supply chain relationships, a systematic review across four disciplines
- **Autor:** Juri Matinheikki, Katri Kauppi, Alistair Brandon-Jones, Erik M.
  van Raaij (2022), International Journal of Operations & Production
  Management 42(13), 299 bis 334
- **Ordner:** `Supply_Chain_und_Operations/`
- **Datei:** Matinheikki_Making agency theory work for supply chain relationships.pdf
- **Relevanz:** Systematisches Review zur Agency-Theorie in
  Lieferkettenbeziehungen aus vier Fachgebieten. Liefert eine Typologie der
  Governance-Mechanismen (Informationstransfer, Zielangleichung,
  Integration, psychologische Einflussnahme) und eine Forschungsagenda.
- **Inhaltsverzeichnis:**
  - 1 Introduction
  - 2 Methods and materials (2.1 Theoretical premises, 2.2 Systematic
    literature review process)
  - 3 Summary of synthesis sample (3.1 Positivist agency theory versus
    principal-agent research, 3.2 Relationship types, 3.3 Methods
    employed, 3.4 Units of analysis, 3.5 Directionality of principal-agent
    relations)
  - 4 Governance mechanisms (4.1 Information transfer strategies, 4.2 Goal
    alignment, 4.3 Integration, 4.4 Psychological influence strategies)
  - 5 A typology of supply chain agency relationships
  - 6 Discussion (6.1 Future research agenda, 6.2 Theoretical
    contributions)
  - 7 Conclusions

## Agency Theory, An Assessment and Review
- **Autor:** Kathleen M. Eisenhardt (1989), Academy of Management Review
  14(1), 57 bis 74
- **Ordner:** `Supply_Chain_und_Operations/`
- **Datei:** Eisenhardt_Agency Theory, An Assessment and Review.pdf
- **Relevanz:** Klassische Grundlagenquelle zur Agency-Theorie mit Ansätzen
  zu Informationsasymmetrie, Risiko und Anreizen. Trennt die positivistische
  und die Principal-Agent-Linie und formuliert prüfbare Aussagen.
- **Inhaltsverzeichnis:** Die Überschriften sind im PDF nicht maschinenlesbar,
  die Gliederung folgt den vier Leitfragen der Einleitung.
  - Was ist Agency-Theorie (Überblick, zwei Forschungsrichtungen)
  - Was trägt sie zur Organisationstheorie bei
  - Ist sie empirisch belastbar
  - Welche Themen und Kontexte sind fruchtbar

## Human, technological and organizational aspects influencing the production scheduling process
- **Autor:** M. Berglund, J. Karltun (2007), International Journal of
  Production Economics 110, 160 bis 174
- **Ordner:** `Supply_Chain_und_Operations/`
- **Datei:** Berglund_Human, technological and organizational aspects influencing the production scheduling process.pdf
- **Relevanz:** Fallstudien zur Feinplanung in vier Holzverarbeitern. Zeigt,
  wie menschliche Fähigkeiten, technische Restriktionen und die
  Organisation (auch die informelle Autorität der Planer) das Ergebnis der
  Planung prägen.
- **Inhaltsverzeichnis:**
  - 1 Introduction
  - 2 Humans, technology and organization
  - 3 Method
  - 4 Company descriptions (4.1 Sawmill, 4.2 Parquet manufacturer, 4.3
    Furniture manufacturer, 4.4 House manufacturer)
  - 5 Findings (5.1 Human, 5.2 Technological, 5.3 Organizational aspects)
  - 6 Scheduling in an HTO-perspective (6.1 bis 6.3, je Aspekt)
  - 7 Conclusion

## Strategic positioning of the order penetration point
- **Autor:** Jan Olhager (2003), International Journal of Production
  Economics 85, 319 bis 329
- **Ordner:** `Supply_Chain_und_Operations/`
- **Datei:** Olhager_Strategic positioning of the order penetration point.pdf
- **Relevanz:** Beschreibt, welche Markt-, Produkt- und
  Produktionsfaktoren die Lage des Auftragsentkopplungspunkts bestimmen und
  wann er nach vorn oder zurück verschoben wird. Liefert ein Modell zur Wahl
  der Lieferstrategie (MTS, ATO, MTO, ETO).
- **Inhaltsverzeichnis:**
  - 1 Introduction
  - 2 Characteristics of the OPP
  - 3 Factors affecting the positioning of the OPP (3.1 Market-related,
    3.2 Product-related, 3.3 Production-related, 3.4 A conceptual factor
    impact model)
  - 4 The role of the OPP in a manufacturing strategy
  - 5 Forward and backward shifting
  - 6 Perspectives on the positioning of the OPP
  - 7 Discussion

## The role of the customer order decoupling point in production and supply chain management
- **Autor:** Jan Olhager (2010), Computers in Industry 61, 863 bis 868
- **Ordner:** `Supply_Chain_und_Operations/`
- **Datei:** Olhager_The role of the customer order decoupling point in production and supply chain management.pdf
- **Relevanz:** Überträgt den Entkopplungspunkt auf Lieferketten und
  Planungssysteme. Schlägt vor, vor und nach dem Punkt unterschiedliche
  Planungssysteme einzusetzen, gestützt auf eine Fallstudie und eine Umfrage
  unter 128 schwedischen Fertigern.
- **Inhaltsverzeichnis:**
  - 1 Introduction
  - 2 Related literature (2.1 The customer order decoupling point, 2.2
    Managerial differentiation in manufacturing planning and control, 2.3
    in supply chain design)
  - 3 Case study
  - 4 Survey findings (4.1 Supply chain design issues, 4.2 Manufacturing
    planning and control issues)
  - 5 Framework (5.2 Deployment of market requirements)
  - 6 Conclusion

## Combined make-to-order and make-to-stock in a food production system
- **Autor:** Chetan Anil Soman, Dirk Pieter van Donk, Gerard Gaalman (2004),
  International Journal of Production Economics 90, 223 bis 235
- **Ordner:** `Supply_Chain_und_Operations/`
- **Datei:** Soman_Combined make-to-order and make-to-stock in a food production system.pdf
- **Relevanz:** Literaturübersicht zu kombinierter MTO/MTS-Produktion mit
  Blick auf die Lebensmittelindustrie. Enthält ein hierarchisches
  Planungsrahmenwerk als Ausgangspunkt für Planungssysteme.
- **Inhaltsverzeichnis:**
  - 1 Introduction
  - 2 Literature review (2.1 MTO-MTS issues in the literature)
  - 3 Food production system characteristics (Anlage, Produkt, Prozess)
  - 4 MTO-MTS in food processing industry (4.1 MTO versus MTS decision,
    4.2 Production and inventory policy decisions, 4.3 Operational
    decisions, 4.4 Applicability of the MTO-MTS literature)
  - 5 Hierarchical planning framework
  - 6 Conclusions and future research

## Job Scheduling Algorithm for a Hybrid MTO-MTS Production Process
- **Autor:** Wojciech Danilczuk, Arkadiusz Gola, Patrik Grznar (2022), IFAC
  PapersOnLine 55-2, 451 bis 456
- **Ordner:** `Supply_Chain_und_Operations/`
- **Datei:** Danilczuk_Job Scheduling Algorithm for a Hybrid MTO-MTS Production Process.pdf
- **Relevanz:** Kurzer Algorithmus, der entscheidet, welche Komponenten auf
  Lager gefertigt werden, und die Aufträge so einplant, dass freie
  Kapazität in Schwachlastzeiten genutzt wird. Mit Zahlenbeispiel.
- **Inhaltsverzeichnis:**
  - 1 Introduction
  - 2 Characteristics of hybrid MTO-MTS production
  - 3 Job scheduling in hybrid production (3.1 Definition of the research
    problem, 3.2 Input data, 3.3 First stage, determination of eligible
    jobs, 3.5 Further iterations of the algorithm)
  - 4 Proof of concept

## Hybrid MTO-MTS production planning, an explorative study
- **Autor:** Bart Beemsterboer, Martin Land, Ruud Teunter (2016), European
  Journal of Operational Research 248, 453 bis 461
- **Ordner:** `Supply_Chain_und_Operations/`
- **Datei:** Beemsterboer_Hybrid MTO-MTS production planning, an explorative study.pdf
- **Relevanz:** Markov-Entscheidungsmodell für zwei Produkte (MTO und MTS)
  mit positiver Lieferzeit. Zeigt, dass die Entscheidung von Lagerbestand
  und Auftragsrückstand abhängen sollte, mit Einsparungen bis 65 Prozent
  gegenüber Strategien, die MTS oder MTO bevorzugen.
- **Inhaltsverzeichnis:**
  - 1 Introduction
  - 2 Literature review
  - 3 Model formulation (3.1 Production system, 3.2 Markov Decision
    Process)
  - 4 Policy structure
  - 5 Numerical comparison (5.1 Varying demand parameters, 5.2 Varying cost
    parameters)
  - 6 Conclusion

## ScienceDirect-Artikel zu Make-to-Order-Scheduling (Sammel-ZIP)
- **Autor:** verschiedene, abgerufen am 07.07.2026 über ScienceDirect
- **Ordner:** `Supply_Chain_und_Operations/`
- **Datei:** [21]_ScienceDirect_articles_07Jul2026_11-53-44.582.zip (nicht mitgeliefert)
- **Relevanz:** Sechs Artikel zu Planung und Terminierung in MTO-Umgebungen,
  ungeordnet gesammelt. Vor der Nutzung entpacken und die Artikel einzeln
  bewerten.
- **Inhaltsverzeichnis:**
  - Flow-shop optimization of hybrid make-to-order and make-to-stock (2021,
    Journal of Cleaner Production)
  - A hybrid algorithm for order acceptance and scheduling (2019, Computers
    & Industrial Engineering)
  - Manufacturing project scheduling considering human factors (2022,
    Applied Soft Computing)
  - Single-machine scheduling in make-to-order environments (2022,
    Computers & Industrial Engineering)
  - Order planning with an outsourcing strategy for a make-to-order
    manufacturer (2023, Computers & Industrial Engineering)
  - Manufacturing time estimation for offer pricing (2024, Engineering
    Applications of Artificial Intelligence)

## Supply chain management and advanced planning, basics, overview and challenges
- **Autor:** Hartmut Stadtler (2005), European Journal of Operational
  Research 163, 575 bis 588
- **Ordner:** `Supply_Chain_und_Operations/`
- **Datei:** Stadtler_Supply chain management and advanced planning.pdf
- **Relevanz:** Stellt das Haus des SCM und die Supply-Chain-Planungsmatrix
  vor und beschreibt die Module von APS (Demand, Network, Master,
  Production, Purchasing, Distribution, Transport) samt Schwächen.
- **Inhaltsverzeichnis:**
  - 1 Introduction
  - 2 Essence and scope of supply chain management (2.1 The house of SCM
    mit 2.1.1 Competitiveness and customer service bis 2.1.5 Information and
    communication technology, 2.2 Assigning contributions of this feature
    issue)
  - 3 Advanced planning systems (3.1 Modules von 3.1.1 Demand planning bis
    3.1.7 Transport planning, 3.2 Assigning contributions)
  - 4 The future of advanced planning (4.1 Modules, 4.2 Premises mit
    Uncertainty, 4.3 Seamless integration of business functions)
  - 5 Concluding remarks

## A hybrid multi-objective evolutionary algorithm for an adaptive flexible job-shop rescheduling problem
- **Autor:** Youjun An, Xiaohui Chen, Kaizhou Gao, Lin Zhang, Yinghe Li, Ziye
  Zhao (2023), Expert Systems with Applications 212, 118711
- **Ordner:** `Supply_Chain_und_Operations/`
- **Datei:** An_A hybrid multi-objective evolutionary algorithm for adaptive flexible job-shop rescheduling.pdf
- **Relevanz:** Neuplanung im Flexible Job Shop mit Auftragsannahme in
  Echtzeit und zustandsabhängiger Instandhaltung. Mehrzielmodell und
  evolutionärer Algorithmus mit Sensitivitätsanalysen.
- **Inhaltsverzeichnis:**
  - 1 Introduction
  - 2 Literature review and research gaps
  - 3 Problem description and mathematical model
  - 4 Proposed algorithm HMOEA
  - 5 Performance analysis of the CBPM policy
  - 6 Performance analysis of the HMOEA algorithm
  - 7 Rescheduling factors, scenarios and response indicators
  - 8 Sensitivity analysis on the adaptive rescheduling problem
  - 9 Conclusions and future work

## Case Study Research Design and Methods, Besprechung der 5. Auflage
- **Autor:** Trista Hollweck (2015), Canadian Journal of Program Evaluation
  30(1), Rezension von Robert K. Yin (2014), Sage
- **Ordner:** `Forschungsmethodik/`
- **Datei:** Hollweck_Case Study Research Design and Methods, Review.pdf
- **Relevanz:** Fünfseitige Rezension zu Yins Standardwerk für
  Fallstudienforschung. Fasst die sechs Schritte (Plan, Design,
  Vorbereitung, Datenerhebung, Analyse, Bericht), die Definition der
  Fallstudie und die Rolle von Logikmodellen zusammen. Ersetzt nicht das
  Buch selbst.
- **Inhaltsverzeichnis:** keines, es handelt sich um eine Rezension.

## Design and natural science research on information technology
- **Autor:** Salvatore T. March, Gerald F. Smith (1995), Decision Support
  Systems 15, 251 bis 266
- **Ordner:** `Forschungsmethodik/`
- **Datei:** March_Design and natural science research on information technology.pdf
- **Relevanz:** Zweidimensionales Rahmenwerk für IT-Forschung (Bauen,
  Bewerten, Theoretisieren, Rechtfertigen gegenüber Konstrukten, Modellen,
  Methoden, Instanziierungen). Grundlage für Design-Science-Argumentation.
- **Inhaltsverzeichnis:**
  - 1 Introduction
  - 2 Theoretical background
  - 3 A research framework in information technology (3.1 Research
    outputs, 3.2 Research activities, 3.3 Application to IT research)
  - 4 Discussion and prescriptions for IT research

## A Three Cycle View of Design Science Research
- **Autor:** Alan R. Hevner (2007), Scandinavian Journal of Information
  Systems 19(2), 87 bis 92
- **Ordner:** `Forschungsmethodik/`
- **Datei:** Hevner_A Three Cycle View of Design Science Research.pdf
- **Relevanz:** Beschreibt Design Science als Zusammenspiel von Relevance
  Cycle, Rigor Cycle und Design Cycle. Kurz und gut zitierbar, wenn ein
  Artefakt gebaut und im Einsatzfeld geprüft wird.
- **Inhaltsverzeichnis:**
  - 1 Design Science Research Cycles
  - 2 The Relevance Cycle
  - 3 The Rigor Cycle
  - 4 The Design Cycle
  - 5 Design as a Pragmatic Science

## Wharton Consulting Club Casebook 2017
- **Autor:** Wharton Consulting Club, Editorial Team (2017), University of Pennsylvania
- **Ordner:** `Consulting/`
- **Datei:** Wharton_Casebook 2017.pdf
- **Relevanz:** Übungssammlung mit 18 Fällen und kurzer Einführung in den
  Auswahlprozess der Beratungen, Fit- und Case-Interview. Dient der
  Vorbereitung auf Beratungsgespräche und als Fundus für
  Strukturierungsübungen. Die Einführung enthält den Ablauf eines Cases in
  vier Schritten.
- **Inhaltsverzeichnis:**
  - Einführung (Branchenüberblick, Ablauf eines Beratungsinterviews, Falltypen, Ablauf eines Cases)
  - 1 Unicloth (S. 9)
  - 2 Brazilian Highway Concessions (S. 18)
  - 3 Snacks Food Acquisitions (S. 27)
  - 4 US Manufacturing (S. 34)
  - 5 Chicago Parking Meters (S. 42)
  - 6 High Engineer Attrition at SLS Oil Gas Services (S. 55)
  - 7 Salt Lake City Airport (S. 68)
  - 8 Clothing Chain Acquisitions, Human Capital (S. 77)
  - 9 Pharma Outsourcing and Tech Adoption (S. 94)
  - 10 Mining Competitive Strategy (S. 111)
  - 11 Phighting Phillies (S. 121)
  - 12 Insurance for the underserved in India (S. 131)
  - 13 National Park Service (S. 139)
  - 14 Penn & Teller (S. 147)
  - 15 Wellington Equestrian Festival (S. 161)
  - 16 Medical Devices Co (S. 169)
  - 17 TV Screens (S. 176)
  - 18 Home Inspection Co (S. 191)

## MIT Management Consulting Casebook 2015
- **Autor:** The Consulting Club at MIT, herausgegeben von Jeremy David Curuksu (März 2015)
- **Ordner:** `Consulting/`
- **Datei:** MIT Sloan_Case Book 2015.pdf
- **Relevanz:** Casebook mit einer Anleitung, wie man eine eigene Fallstruktur als Issue Tree entwickelt (induktiv, hypothesengeleitet, MECE), dazu Referenzstrukturen und 10 Übungsfälle. Passt zu Abschnitt 3 der Kern-Regeln, weil es den Umgang mit fertigen Frameworks (anpassen statt unverändert übernehmen) ausdrücklich behandelt.
- **Inhaltsverzeichnis:**
  - 1 How to Develop a Tailored Case Structure (5 Schritte, Hypothesis generation, Client bias)
  - 2 High Level Case Structures (2.1 One-size-fits-all, 2.2 Profit framework, 2.3 Operations, 2.4 Growth, 2.5 Pricing, 2.6 Mergers & Acquisition, 2.7 New venture & Start-ups)
  - 3 Practice Cases (3.1 Lymphoma, 3.2 Coolarpess, 3.3 Travel Logistics, 3.4 Pharma+, 3.5 Video Interpreter, 3.6 Acquisition Railways, 3.7 Chemicals, 3.8 A Classic brainteaser, 3.9 Foodland Turnaround, 3.10 Coffee Shop)

## Case Interview Workbook (Accenture FY19)
- **Autor:** Accenture Strategy (2019)
- **Ordner:** `Consulting/`
- **Datei:** Accenture_Case Workbook FY19.pdf
- **Relevanz:** Kompakte Einführung (24 Seiten) in den Ablauf eines Case Interviews als strukturiertes Problemlösen, mit drei Falltypen und Beispiel-Frameworks. Kurzer Einstieg vor den umfangreicheren Casebooks.
- **Inhaltsverzeichnis:**
  - What is a Case Interview?
  - Common Misconceptions About Case Interviews
  - Case Interview Success Factors
  - The Case Interview Process, Structured Problem Solving (Clarify the Problem, Decompose the Problem, State Hypotheses and Develop, Test Hypotheses, Summarize and Communicate Findings)
  - Types of Cases ("The Great Unknown", "The Parade of Facts", "The Back of the Envelope")
  - Sample Frameworks and Application
  - Putting it Together

## BCG Online Case, Practice Case Med-Lines
- **Autor:** Boston Consulting Group (Vorbereitungsunterlage 2019, Copyright 2016)
- **Ordner:** `Consulting/`
- **Datei:** BCG_Online Case Med-Lines 2019.pdf
- **Relevanz:** Übungsfall für den 45-minütigen Online-Test von BCG mit 23 Multiple-Choice-Fragen zu Dokumenten (Fährbetreiber in Griechenland). Trainiert Zahlenverständnis, logisches Schließen und Rechnen ohne Tabellenkalkulation. Lösungen und Punktevergabe stehen am Ende.
- **Inhaltsverzeichnis:**
  - Instructions (Ablauf des Online-Cases, Punktelogik)
  - Case Briefing und Dokumente (Tourismus in der Ägäis, Flotte und Verkehrsdaten)
  - Questions 1 to 11
  - Questions 12 to 23
  - Answers

## The Fit Interview
- **Autor:** Oren Shur (Columbia Graduate Consulting Club, 17.07.2012)
- **Ordner:** `Consulting/`
- **Datei:** Shur_The Fit Interview.pdf
- **Relevanz:** Foliensatz (14 Seiten) zur Vorbereitung auf den Fit-Teil des
  Beratungsinterviews, mit STAR-Methode, einer Matrix aus Geschichten und
  Fragetypen und typischen Fehlern. Grundlage für eine eigene
  Geschichtenmatrix im Vorstellungsgespräch. Es ist ein Erfahrungsbericht
  eines Kandidaten, keine Methodenliteratur.
- **Inhaltsverzeichnis:**
  - Typical Interview Process, Purpose of Fit Interview, Focus Areas
  - Common Questions und Random Questions
  - Overall Strategy
  - The Fit Matrix
  - Telling the Story, STAR
  - Additional Prep Tips, Common Mistakes to Avoid
  - Questions and Group Practice

## Japanese Life Sciences Company Aligns Global Strategy with ASE and SAP S/4HANA
- **Autor:** Capgemini (Kundenfall, ohne Jahr)
- **Ordner:** `Transformation_OpEx_und_Change/`
- **Datei:** Capgemini_SAP S4HANA Case Study Life Sciences.pdf
- **Relevanz:** Vierseitiger Praxisfall zur Einführung eines globalen
  S/4HANA-Templates bei einem Life-Sciences-Hersteller (Balance aus globaler
  Standardisierung und regionaler Ausführung, Stammdaten-Governance,
  gemeinsame KPIs). Marketingnahe Herstellerquelle, als Praxisbeispiel zu
  lesen und nicht als Methodenbasis.
- **Inhaltsverzeichnis:** keines im PDF. Gliederung nach Zwischenüberschriften:
  - Understanding benefits of global standardization
  - Building an SAP S/4HANA-based global business platform aligned with strategic goals
  - Preparing for international implementation
  - Key business enablers of the revised S/4HANA design

## SAPIBP1 Documentation, Release 2508 (Planning Model Template)
- **Autor:** SAP, August 2025 (209 Seiten)
- **Ordner:** `Supply_Chain_und_Operations/`
- **Datei:** SAP_IBP 2508 SAPIBP1 Planning Model Template.pdf (PDF nicht mitgeliefert, SAP-vertraulich)
- **Relevanz:** Nachschlagewerk zum Standard-Planungsmodell SAPIBP1 von SAP
  IBP, Grundlage für den Einstieg in die IBP-Grundlagen. Das Dokument trägt
  einen SAP-Vertraulichkeitshinweis.
- **Inhaltsverzeichnis:**
  - What's New in 2508
  - General Remarks
  - Analytics and Alerts
  - Key Figure Overview
  - Master Data Type Overview
  - Planning Level Overview
  - General Planning Area Settings
  - Planning Operators
  - Changes in Previous Releases

## SAP S/4HANA Manufacturing for Planning & Scheduling, Implementation Guide (2023.5)
- **Autor:** SAP, Version 2023.5, DSC Edition (73 Seiten)
- **Ordner:** `Supply_Chain_und_Operations/`
- **Datei:** SAP_S4HANA DSC Edition PPDS Implementation Guide.pdf
- **Relevanz:** Customizing-Leitfaden für PP/DS im Side-by-Side-Betrieb eines
  DSC-Systems neben einem ERP-System. Es beschreibt nicht das embedded PP/DS,
  liefert aber Vokabular und Ablauf von Customizing und Stammdatenintegration.
- **Inhaltsverzeichnis:**
  - 1 Introduction (About this Document, Relevant SAP Notes, Naming Conventions)
  - 2 Prerequisites
  - 3 Customizing and Configuration (Settings in the ERP System, Settings in the PP/DS System, Customizing for Material Master Data in Both Systems)
  - 4 Setup and Integration of Master Data (Manual Creation in PP/DS, Master Data Integration Using Core Interface)
  - 5 Integration of Transactional Data
  - 6 Checks
  - 7 Specific Topics (Classes and Characteristics, Business Partners, Distributed Customer/Vendor ERP Systems, Subcontracting, Supported and Unsupported Scenarios, MRP Areas, Real-time Integration with SAP IBP, Segmentation, Periodic CIF Transfer, Multiple ERP Systems to a Single PP/DS System)

## SAP Integrated Business Planning: Functionality and Implementation (Leseprobe)
- **Autor:** Sandy Markin (laut PDF-Metadaten), SAP PRESS, Leseprobe mit 27 Seiten
- **Ordner:** `Supply_Chain_und_Operations/`
- **Datei:** Markin_SAP Integrated Business Planning, Leseprobe.pdf
- **Relevanz:** Leseprobe zu einem Einstiegswerk in SAP IBP. Das vollständige
  Buch liegt nicht vor.
- **Inhaltsverzeichnis:** keines auslesbar, das PDF besteht aus Bildseiten ohne Text. Autor und Inhalt vor dem Lesen am PDF prüfen.

## Die STAR Methode (Verhaltensbasierte Befragung)
- **Autor:** unbekannt, deutsche Übersetzung nach dem MIT Career Guide und der Drexel University (SCDC), 3 Seiten
- **Ordner:** `Consulting/`
- **Datei:** MIT Career Guide_STAR Methode Verhaltensinterview.pdf
- **Relevanz:** Merkblatt zu verhaltensbasierten Interviewfragen und zum
  STAR-Schema, mit einer Beispielantwort und Übungsfragen. Grundlage für
  Belege im Vorstellungsgespräch. Es ist ein Merkblatt und keine
  Methodenliteratur, ein Lehrbuch zur Gesprächsführung fehlt noch.
- **Inhaltsverzeichnis:**
  - Verhaltensbasierte Befragung (Behavioral Interviewing)
  - Die STAR-Methode mit Situation, Task, Action und Result
  - Beispiel einer Antwort nach der STAR-Methode
  - Beispiele für Verhaltensinterviewfragen

## MCI Winter School, The Consulting Profession (Folien Tag 1)
- **Autor:** KPMG Advisory GmbH Österreich, Vortrag am Management Center Innsbruck am 24.02.2025 (Seminarfolien, keine Primärquelle)
- **Ordner:** `Consulting/`
- **Datei:** KPMG_MCI Winter School 2025.pdf
- **Relevanz:** Einstieg in den Beratungsberuf aus der Sicht eines
  Beratungshauses. Beratertypen, Beratungsprozess, Lage der großen Häuser
  zwischen Strategie und Umsetzung, Alltag und Work-Life-Balance, Beratertypen
  nach einer Studie der Harvard Business Review, Einstiegsprozess und
  Case-Arten. Marktzahlen und Aussagen zu einzelnen Häusern stammen aus
  Sekundärquellen und sind vor Verwendung zu prüfen.
- **Inhaltsverzeichnis:** (nach der Agenda der Folien, ohne Seitenzahlen der Bibliothek)
  - Vorstellung und Einführung (S. 2 bis 9, Über das Haus)
  - Konzept und Funktion von Beratung (S. 10 bis 18, Definition, Geschichte in acht Stufen, Zweck, Missverständnisse)
  - Arten von Beratung (S. 19 bis 28, Beratertypen, Beratungshäuser von der Nische bis zum Komplettanbieter, Marktgröße, größte Anbieter)
  - Der Beratungsprozess (S. 29 bis 42, Prozessmodelle, Methoden, Agile, Design Thinking, Treiber des Wandels, Beratung 4.0)
  - Beratung als Beruf (S. 43 bis 48, Alltag, Work-Life-Balance, Beratertypen, gesuchte Profile, Bewerbungsprozess)
  - Cases (S. 49 und 50, Arten von Case-Interviews, Gruppenfallstudie)

## MCI Badge Consulting und Advisory, Übersicht
- **Autor:** Management Center Innsbruck, in Zusammenarbeit mit KPMG (Stand 21.11.2024, Datei vom Veranstalter)
- **Ordner:** `Consulting/`
- **Datei:** MCI_Overview Badge Consulting Advisory.pdf
- **Relevanz:** Aufbau des Badge, in dem die Winter School der Pflichtteil
  ist. Zeigt, was die vier Tage enthalten und welche Teile über die Winter
  School hinaus zum Badge gehören.
- **Inhaltsverzeichnis:**
  - S. 2 Aufbau (Winter School als Pflicht vor Ort, zwei von vier Wahlfächern online, Austausch mit MCI-Alumni)
  - S. 3 Winter School in vier Tagen (Beratungsberuf, Datenvisualisierung, Skill Set für Beratung in einer digitalen Welt, Präsentation und Storytelling, Case Cracking mit zwei Übungen, Escape Game)
  - S. 4 Wahlfächer (Slide Design, Methoden und Werkzeuge, Excel für Beratung, Agiles Projektmanagement)
