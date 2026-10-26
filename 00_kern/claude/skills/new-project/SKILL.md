---
name: new-project
argument-hint: [kurzname, optional]
description: Legt im Hub oder in einem Ast ein neues Projekt über ein geführtes Interview an. Claude fragt wie ein Berater Anlass, Ziele, Scope, Rollen, Termine, Daten, KPIs, Risiken, Vertraulichkeit und Arbeitsplan mit Lesepfad ab und baut daraus Charter, Arbeitsplan, Lesepfad, ADR-Ordner und ein eigenes /xx-next
---
Wir legen ein neues Projekt an. Ich soll meine Ideen nicht unsortiert
eingeben müssen. Du führst mich durch ein Interview, sortierst meine Antworten
und baust daraus Scaffold, Charter, Arbeitsplan, Lesepfad und Projekt-Kontext,
in jedem Repo im selben Schema. Chat auf Deutsch, die Sprache der Projektdoku
folgt dem Repo, außer ich lege in Block A etwas anderes fest. Für alles, was
entsteht, gelten die Schreibregeln aus `{{HUB}}/00_kern/regeln.md`.

Projektname aus dem Aufruf: $ARGUMENTS

## 0. Vorbereitung (still, ohne Rückfrage)

**Repo bestimmen** aus dem aktuellen Arbeitsverzeichnis.

| Repo | erkennbar an | Projektordner | Scaffold | Sprache der Doku |
|---|---|---|---|---|
| Hub | `00_kern/regeln.md`, `03_projekte/` | `03_projekte/<kurzname>/`, ohne Nummer, Kleinbuchstaben | `{{HUB}}/07_handwerk/project_scaffold/` | `sprache.hub` in `{{HUB}}/00_kern/einstellungen.json` |
| Ast | `ast.json` in der Wurzel | `<projektordner aus ast.json>/<kurzname>/` | `{{HUB}}/07_handwerk/project_scaffold/` | `sprache` aus `ast.json` |

Passt keine Zeile, frag einmal, wo das Projekt entstehen soll. Prüfe, dass der
Ordnername frei ist.

- **Im Hub** gehören Projekte für einen Arbeitgeber, die eigene Firma oder
  Kunden nicht hierher, sondern in den passenden Ast (Liste unter `aeste` in
  `{{HUB}}/00_kern/einstellungen.json`). Zeigt sich das im Interview, stopp und
  verweis auf `/aufnahme` im Hub.
- **In einem Ast** gelten zusätzlich dessen `CLAUDE.md` und die Dateien in
  `00_kontext/`. Liegen Daten dort schon zentral, liest das Projekt sie über
  Pfade und legt keine Kopie an.
- **Aufnahmeblatt suchen** unter `{{HUB}}/01_kompass/aufnahmen/` (Datei
  `*_<kurzname>.md`). Liegt eines vor, nenn es in drei Zeilen (Modul, Spur,
  Kern-Lesepfad) und füll daraus Block A bis C und G vor, ich bestätige oder
  korrigiere. Liegt keines vor und ist es ein Projekt in einem Ast,
  frag einmal, ob vorher `/aufnahme` im Hub laufen soll. Ohne Aufnahme gibt es
  keinen Kern-Lesepfad, dann stehen alle Abschnitte im Lesepfad des Projekts.
- Zusätzlich lesen: die `CLAUDE.md` des Repos (Projekttabelle),
  `{{HUB}}/07_handwerk/Definition_of_Done.md`,
  `{{HUB}}/00_kern/vertraulichkeit.md`, `{{HUB}}/06_wissen/frameworks/README.md`.
- Prüfen, ob es zum Thema schon Spuren im Repo gibt (Grep über die
  Projektordner, `*Backlog*`, Memory-Index). Fundstellen nennst du mir zu
  Beginn in zwei, drei Zeilen. Ich soll nichts erzählen müssen, was schon im
  Repo steht.

## 1. Interviewregeln

- **Ein Block pro Nachricht**, höchstens fünf Fragen. Geschlossene Fragen
  (Projekttyp, Rolle, Sprache, Vertraulichkeitsstufe) über `AskUserQuestion`,
  offene Fragen als nummerierte Liste im Chat.
- Nach jedem Block: **Rückspiegeln in maximal zehn Zeilen** („So habe ich es
  verstanden: …“), jede Aussage getaggt als `[Fakt]`, `[Hypothese]` oder
  `[offen]`. Ich korrigiere, dann erst der nächste Block.
- „Weiß ich nicht“ ist eine gültige Antwort: Sie wird zu einem offenen Punkt
  mit Owner (wer weiß es?) und Klärungsweg, nie zu einer geratenen Annahme.
- **Widerspruch statt Protokoll:** Wo eine Antwort gegen die Regeln unten
  verstößt (zwei „A“ in einer Zeile, Ziel nicht messbar, Rolle ohne Mandat),
  sagst du es direkt und schlägst eine Lösung vor.
- Blöcke, die für den Projekttyp nicht passen, überspringst du mit einem Satz
  Begründung. Nichts wird stillschweigend weggelassen.
- **Zwischenstand sichern:** Ab Block A existiert der Projektordner. Nach jedem
  Block schreibst du die Antworten in `00_Charter/Setup_Interview.md`.
  So überlebt das Interview eine Pause oder `/compact`. Wird `/new-project`
  mit einem bestehenden Projektordner aufgerufen, liest du diese Datei und
  machst beim ersten offenen Block weiter.
- Termine sind Obergrenzen, gearbeitet wird so schnell wie möglich.

## 2. Die Blöcke

**A Anlass und Projekttyp**
- Projektname (kurz, ASCII für den Ordner; übertragbare Projekte allgemein
  benennen, der erste Fall wird Welle 1), Projekttyp: **Lernprojekt** (Können als
  Ziel, mit `lernlog.md`, Lehrplan über `/advisor`, Nachweis je Block, geübt in
  der Spur eines Asts oder an öffentlichen Daten) oder **Anliegen** (Ergebnis im eigenen Leben, Struktur des Scaffolds,
  fertig nach Definition of Done).
- Wer hat das Projekt ausgelöst, was ist der Anlass, welche Entscheidung ist
  schon gefallen?
- **Neustart oder Einstieg in ein laufendes Projekt?** Bei laufendem Projekt:
  Was ist erledigt, was weiß ich noch nicht? Dann ist die Charter ein
  Re-Baselining, und die Wissenslücken werden Interviewpartner in Block E.
- Sprache der Projektdoku und der Deliverables.
→ Danach: Scaffold kopieren (Abschnitt 3, Schritt 1) und Setup-Interview anlegen.

**B Ziele und Prioritäten**
- Maximal drei Ziele, jedes gegen SMART geprüft; ein nicht messbares Ziel
  formulierst du mit mir um.
- Rangfolge bei Zielkonflikten (z. B. Termintreue vor Qualität vor Kosten).
- Nicht-Ziele: was ausdrücklich nicht erreicht werden soll.

**C Scope und Schnittstellen**
- In und Out, also Produkte, Standorte, Prozesse, Kunden, Zeitraum.
- Schnittstellen zu bestehenden Projekten im Repo. Wer liefert wem Daten,
  wer ist Owner (welches Projekt ist die Single Source of Truth)?
- Übertragbarkeit: Was soll für spätere Fälle wiederverwendbar werden?

**D Meine Rolle und Governance**
- Meine Rolle: Projektleitung · Koordination mit Mandat · Workstream-Lead ·
  Zuarbeit. Welches Mandat habe ich (Planung, Steuerung, Budget, Eskalation)?
  Ist die Rolle noch offen, wird ihre Klärung ein offener Punkt mit Termin.
- Sponsor, Steering-Kadenz, Eskalationsweg.
- Einordnung nach `{{HUB}}/00_kern/regeln.md` Abschnitt 5 (Delegationsmodell): Was bleibt bei mir, was
  delegiere ich an Claude im Dialog, was wird automatisiert?

**E Team, Workstreams, Stakeholder**
- Workstreams ohne Überschneidung, je Workstream **genau ein Accountable**
  mit Namen (keine Abteilung). Zwei Namen in einer Zeile → aufteilen in A und
  R vorschlagen.
- Doppelrollen und Kopfmonopole sichtbar machen (eine Person hält mehrere A).
- Fehlende Köpfe und Know-how: Wer müsste dabei sein und ist es nicht?
  Betriebsrat, Kunde, Werk im Ausland, IT/Stammdaten prüfen.
- Interviewpartner für den Einstieg (bei laufendem Projekt Pflicht).

**F Termine, Meilensteine, Gates**
- Feste Termine und wer sie zugesagt hat.
- Meilensteine als Gates mit Kriterium, nicht nur mit Datum.
- Kritischer Pfad: Welcher Termin hängt an einer externen Partei?

**G Daten und Methoden**
- Datenquellen, also Exporte aus dem Quellsystem (ERP wie SAP, CRM,
  Buchhaltung), Interviews, Markt- und Fremddaten.
  Loader-Spalten werden später aus den echten Exporten übernommen, nie geraten.
- Methodencheck. Du gleichst mit `{{HUB}}/02_bibliothek/` (Index, Methodenkoffer falls vorhanden)
  und `{{HUB}}/06_wissen/frameworks/` ab und schlägst passende Methoden vor, mit Quelle und
  eigener Anpassung. Passt ein Framework „In trial“, nennst du es als Testfall.
  Fehlt im Hub etwas Wesentliches, sagst du es als Lücke.

**H Erfolgsmessung**
- KPIs auf drei Ebenen: Programmfortschritt · operative Wirkung · Ergebnis
  (Business Case). Je KPI: Definition, Quelle, Baseline, Ziel, Owner.
- Wann und wie wird nach Projektende nachgemessen?

**I Risiken und Annahmen**
- Top-Risiken mit Eintritt/Wirkung und Owner.
- Annahmen mit Quelle und „Last Validated“-Datum (Qualitätsstandard 3).

**J Vertraulichkeit und Case Study**
- Vertraulichkeitsstufe nach `{{HUB}}/00_kern/vertraulichkeit.md`; welche Daten dürfen nie ins
  Git (private Rohdaten liegen unter `data/input/`, gitignored)?
- Taugt das Projekt als Case Study (Situation, Task, Approach, Result)?
  Welche Zahl müsste am Ende stehen, damit es eine gute ist?

**K Arbeitsplan und Lesepfad**
- Aus Zielen (B) und Gates (F) die Arbeitspakete ableiten, je Paket Ergebnis
  („fertig, wenn“), Wer, Abhängigkeit, spätestens und LP.
- Spalte LP: Trägt ein Abschnitt des Kern-Lesepfads im Hub
  (`{{HUB}}/01_kompass/module/<Modul-ID>_<kurzname>/lesepfad.md`) das Paket, steht
  dessen ID (`<Modul-ID>-Knn`), der Text bleibt im Hub. Sonst schreibst du
  einen projektspezifischen Abschnitt `LP-nn` in `00_Charter/Lesepfad.md` nach
  der Vorlage, Seiten vorher im PDF der Bibliothek geprüft. Ohne passende
  Quelle steht „kein Eintrag“ mit Grund, die Lücke wird als Empfehlung
  genannt (Lesepfad-Regel in `{{HUB}}/00_kern/regeln.md`, Abschnitt 3).
- Je Designentscheidung ein ADR-Kandidat mit Literaturstelle, noch keine
  fertigen ADRs.
- Erklär-Check nach jedem Gate als eigene Zeile im Arbeitsplan.

## 3. Erzeugen (nach Block K, nach meinem „passt“)

1. Scaffold des Repos in den Projektordner kopieren (bereits nach Block A).
   Fehlen dort `00_Charter/Arbeitsplan.md`, `00_Charter/Lesepfad.md` oder
   `docs/adr/ADR-000_Vorlage.md`, kommen sie aus
   `{{HUB}}/07_handwerk/project_scaffold/`.
2. `00_Charter/Projektanforderungen.md` nach der Gliederung der Vorlage
   füllen, Executive Summary nach SCQA, jede Hypothese als solche markiert.
3. `00_Charter/Offene_Punkte.md`: alle `[offen]`-Punkte mit Owner, Klärungsweg
   und Zieltermin, sortiert nach Kritikalität.
4. `00_Charter/Arbeitsplan.md` und `00_Charter/Lesepfad.md` aus Block K,
   `docs/adr/` mit der Vorlage, die ADR-Kandidaten im Lesepfad.
5. Projekt-`CLAUDE.md` füllen: was das Projekt ist, Rolle, Governance,
   Datenquellen und Datenfallen, Sprache, Vertraulichkeit, Schnittstellen,
   Modul und Spur mit Verweis auf Aufnahmeblatt und Kern-Lesepfad.
6. `kpis/kpi_definitions.md` aus Block H; `methodology/Assumptions.md` aus
   Block I mit „Last Validated“.
7. Befehl `.claude/commands/<kurz>-next.md` im Repo aus der Vorlage
   `{{HUB}}/00_kern/claude/skills/new-project/next_vorlage.md`, Platzhalter
   ersetzt. Gibt es den Namen schon, schlag einen anderen vor.
8. Projekttabelle in der `CLAUDE.md` des Repos um eine Zeile ergänzen; im
   Hub bei einem Lernprojekt zusätzlich `lernlog.md` anlegen; bei
   zugeordnetem Framework dessen Testprojekt in
   `{{HUB}}/06_wissen/frameworks/README.md` und in der Framework-Datei
   eintragen.
9. Mit Aufnahmeblatt dort die Zeile „Status“ nachziehen (Ast angelegt am,
   Projektordner) und im Register `projekte.md` des Moduls die Spalte „Ort im
   Ast“. Nur der Status, keine Inhalte aus dem Ast.
10. Zum Schluss im Chat: Ordnerbaum, Executive Summary der Charter in fünf
    Zeilen, die drei dringendsten offenen Punkte, das erste Arbeitspaket mit
    seinem LP und der nächste Befehl (`/<kurz>-next`, im Hub danach
    `/advisor <Modul-ID>`). Kein Commit ohne meine Aufforderung.

## 4. Was du nicht tust

- Keine Inhalte erfinden, um Lücken zu füllen, die Lücke bleibt `[offen]`.
- Keine Stakeholder-Bewertung oder politische Einschätzung als Fakt in die
  Charter schreiben; das bleibt bei mir (`{{HUB}}/00_kern/regeln.md` Abschnitt 5 (Delegationsmodell)).
- Keine Emojis, echte Umlaute in deutschem Text.
- Keine Arbeitsdaten in den Hub, auch nicht ins Aufnahmeblatt.
- Den Kern-Lesepfad im Hub nicht aus dem Ast heraus ändern. Fehlt dort etwas,
  nennst du es als Vorschlag für `/aufnahme` oder `/advisor`.
