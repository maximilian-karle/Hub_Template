# Hub Template

Vorlage für einen persönlichen Hub mit Claude Code. Der Hub ist ein privates
Git-Repo, in dem Lernen, Arbeit und eigene Vorhaben nach derselben Methode
laufen. Er ist der Stamm mit Regeln, Bibliothek, Lernsystem und Werkzeugen.
An ihm hängen Äste, je ein eigenes privates Repo für die Arbeit beim
Arbeitgeber, für eine Selbständigkeit und für alles, was später dazukommt.

Nach dem Klonen führt `/einrichten` in elf Schritten durch die Einrichtung,
ungefähr wie bei einem neuen Handy. Rund 45 bis 60 Minuten mit Bewerbungsteil,
jederzeit unterbrechbar.

Wie du danach mit dem Hub arbeitest und lernst, erklärt das
[Handbuch](HANDBUCH.md), mit einem Beispiel von der ersten Aufgabe bis zur
Case Study, dem Lernsystem ALTER, deinem Rhythmus und einem Spickzettel.

## Schnellstart auf dem Mac

1. Auf GitHub oben rechts **Use this template** → **Create a new repository**,
   Name `Hub`, Sichtbarkeit **Private**. Der Hub enthält später Ziele,
   Profil und Bücher, er bleibt privat.
2. Werkzeuge installieren, falls noch nicht vorhanden. Homebrew von
   [brew.sh](https://brew.sh), danach

   ```bash
   brew install git gh python@3.12
   ```

3. Bei GitHub anmelden und den eigenen Hub klonen.

   ```bash
   gh auth login
   ```

   ```bash
   gh repo clone <dein-konto>/Hub ~/Hub
   ```

4. Claude Code im Ordner `~/Hub` öffnen (Desktop-App, Code-Tab, Ordner
   wählen, oder im Terminal `cd ~/Hub && claude`).
5. `/einrichten` eingeben. Ein Hinweis beim Sitzungsstart erinnert daran,
   solange die Einrichtung nicht abgeschlossen ist.

Wer die Vorlage direkt klont statt „Use this template“ zu nutzen, bekommt in
Schritt 10 der Einrichtung ein eigenes privates Repo angelegt.

## Was die Einrichtung abfragt

| Schritt | Inhalt |
|---|---|
| 1 Technik | git, GitHub CLI, Python, git-Identität, GitHub-Anmeldung |
| 2 Person | Name, Rolle, Ziele, wofür der Hub da sein soll |
| 3 Stil | Sprache, Schreibregeln ohne KI-Merkmale, Farbpalette, Kommunikation |
| 4 Arbeitsweise | Delegationsmodell, Qualitätsregeln, Git-Regeln |
| 5 Lernen | Kompetenzprofil mit Bereichen, Lernbudget, Trimesterstart |
| 6 Äste | Repos für Arbeit, Selbständigkeit und weitere, je mit Spur und Sprache |
| 7 Bibliothek | Themenordner für Fachbücher |
| 8 Karriere | Jobsuche, Lebenslaufdaten, Stil von Lebenslauf und Anschreiben, Probe-PDF |
| 9 Installieren | Regeln und Skills nach `~/.claude`, damit sie in jedem Ast gelten |
| 10 GitHub | eigenes privates Repo für den Hub, erster Commit |
| 11 Start | Rundgang und erste echte Aufgabe |

Alle Antworten landen in Dateien im Repo (`00_kern/einstellungen.json`,
`00_kern/persoenlich.md`, `00_kern/regeln.md`, `CLAUDE.md`,
`01_kompass/entwicklung/profil.md`, `05_werkstatt/karriere/Profil/`). Jeder Schritt lässt sich mit
`/einrichten <schritt>` erneut öffnen.

## Aufbau

```
Hub/                         privat, Stamm
├── 00_kern/                 Regeln, Einstellungen, Installskript, Skills für ~/.claude
├── 01_kompass/              Profil, Studienplan, Module, Aufnahmen
├── 02_bibliothek/           Fachbücher in Themenordnern, Literatur-Index
├── 03_projekte/             Lernprojekte und private Anliegen
├── 04_gedaechtnis/          Wiederholung nach SM-2, Karten, /heute
├── 05_werkstatt/            Case Studies, Karriere
├── 06_wissen/               eigene Frameworks, Verbindungen zwischen Fächern
├── 07_handwerk/             Projekt-Scaffold, Definition of Done, Deck und Dashboard
└── vorlagen/ast/            Vorlage für neue Äste

AT_<FIRMA>/                  privat, Ast Arbeit, Spur A
ST_<FIRMA>/                  privat, Ast Selbständigkeit, Spur U
<weitere>/                   beliebig viele, /ast-anlegen
```

Die Lernschleife läuft so.
`01_kompass → 02_bibliothek → 03_projekte und Äste → 04_gedaechtnis → 05_werkstatt → 06_wissen → 01_kompass`

Arbeitsdaten bleiben im Ast. In den Hub fließt nur Anonymisiertes über drei
feste Wege zurück, als Lernkarte, als Framework im Register oder als Case
Study.

## Befehle

| Befehl | Wofür |
|---|---|
| `/einrichten` | Ersteinrichtung, einzelne Schritte später erneut |
| `/ast-anlegen` | neuen Ast (eigenes Repo) an den Hub hängen |
| `/aufnahme` | neue Aufgabe aus einem Ast aufnehmen, Modul zuordnen |
| `/new-project` | Projekt im Hub oder Ast per Interview anlegen, mit Charter, Arbeitsplan, Lesepfad und eigenem `/xx-next` |
| `/advisor` | Durchlauf eines Moduls planen |
| `/alter` | nächste Tätigkeit im Lernsystem wählen und ausführen |
| `/heute` | tägliche Wiederholung der Karten |
| `/tutor`, `/editor`, `/roommate` | Verstehen prüfen, Ergebnis vorzeigbar machen, Fächer verbinden |
| `/weekly-review` | Wochenrückblick mit Lernteil |
| `/ast-stand` | lesen, was in einem Ast entstanden ist, ohne ihn zu klonen |
| `/add-literature` | neues Werk in den Literatur-Index |
| `/qa-check` | Plausibilität, Quellsystem gegen Gespräch, Ablauffrist der Annahmen |
| `/job-apply` | aus einer Stellenanzeige Lebenslauf und Anschreiben im eigenen Stil, mit Keyword-Abgleich und Lückenlog |
| `/learn-poster` | Hilfszettel A4 und Mind Map A3 zu einem Thema |
| `/framework-next` | Bibliothek Punkt für Punkt nach eigenen Frameworks durchsuchen |
| `security-audit` | Sicherheitsprüfung von Code (Skill, lädt bei Bedarf von selbst) |

## Zwei Rechner

Der Stand wandert über Git. Vor der Arbeit `git pull --ff-only`, danach
committen und pushen. Das Gedächtnis von Claude wandert nicht über Git,
dafür gibt es `python3 00_kern/gedaechtnis_sync.py export` (vor Arbeitsende,
mitcommitten) und `import` (nach dem Pull auf dem anderen Rechner).

## Vorlage aktualisieren

Neue Fassungen dieser Vorlage lassen sich übernehmen, ohne die eigenen
Inhalte zu verlieren. Einmalig die Vorlage als zweite Quelle eintragen.

```bash
git remote add vorlage https://github.com/maximilian-karle/Hub_Template.git
```

Danach `git fetch vorlage` und Claude bitten, die Änderungen aus
`vorlage/main` gezielt zu übernehmen. Eigene Dateien wie `einstellungen.json`,
`persoenlich.md` und `CLAUDE.md` bleiben dabei unangetastet.

## Voraussetzungen

Claude Code (Desktop-App oder CLI), git, GitHub CLI `gh`, Python ab 3.10.
Für Decks und Dashboards die Pakete aus `requirements.txt`.
