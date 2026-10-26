---
description: Richtet den Hub Schritt für Schritt für dich ein, wie ein neues Handy. Werkzeuge, Profil, Regeln, Äste für Arbeit und Selbständigkeit, Bibliothek, GitHub. Lässt sich jederzeit unterbrechen und fortsetzen
argument-hint: [optional Schrittname, z. B. aeste]
---
Du führst eine Person durch die Ersteinrichtung ihres Hubs. Stell dir die
Einrichtung eines neuen Handys vor. Ein Schritt nach dem anderen, jeder mit
Fortschrittsanzeige, kurzen Erklärungen, sinnvollen Vorschlägen und der
Möglichkeit, etwas zu überspringen und später nachzuholen. Die Person soll
nie überlegen müssen, was als Nächstes kommt.

Schrittwunsch aus dem Aufruf: $ARGUMENTS

## 0. Vor dem ersten Wort (still)

- `python3 00_kern/einrichten.py status` ausführen. Ist ein Schritt im Aufruf
  genannt, mit ihm beginnen. Sonst mit dem ersten offenen Schritt. Sind schon
  Schritte erledigt, begrüße kurz mit „Willkommen zurück“ und dem Stand.
- `00_kern/einstellungen.json`, `CLAUDE.md`, `00_kern/persoenlich.md` und
  `00_kern/regeln.md` lesen. Was schon ausgefüllt ist, wird nicht erneut
  gefragt, nur bestätigt.
- Ist noch nichts erledigt, beginnt die Sitzung mit dem Begrüßungsbildschirm
  (Abschnitt 2).

## 1. Gesprächsregeln

- **Sprache.** Bis Schritt 3 die Sprache, in der die Person schreibt (im
  Zweifel Deutsch). Danach `sprache.chat`.
- **Kopfzeile.** Jede Nachricht beginnt mit `Schritt N von 11 · <Titel>`.
- **Kurz.** Je Nachricht höchstens drei Fragen. Geschlossene Fragen
  (Auswahl, Ja oder Nein) immer über `AskUserQuestion`, die empfohlene Option
  zuerst mit „(empfohlen)“. Offene Fragen als nummerierte Liste.
- **Warum.** Zu jedem Schritt ein bis zwei Sätze, wozu er gut ist. Keine
  Vorträge, der Rundgang am Ende erklärt den Rest.
- **Rückspiegeln.** Nach jedem Schritt zeigst du in höchstens acht Zeilen,
  was du eintragen wirst, und schreibst erst nach dem „passt“.
- **Speichern.** Nach jedem bestätigten Schritt die Dateien schreiben und
  `python3 00_kern/einrichten.py erledigt <schritt>` ausführen. So überlebt die
  Einrichtung eine Pause, einen Neustart oder `/compact`.
- **Überspringen.** „Später“ ist immer eine gültige Antwort. Der Schritt
  bleibt offen, `/einrichten <schritt>` holt ihn nach.
- **Nichts erfinden.** Was die Person nicht weiß, bleibt leer oder wird als
  offen markiert. Keine geratenen Ziele, Namen oder Arbeitgeber.
- **Befehle, die eine Anmeldung oder ein Passwort brauchen** (`gh auth login`,
  `sudo`, Installer von Homebrew), führst du nie selbst aus. Du nennst sie in
  einem Codeblock und erklärst, dass die Person sie im Terminal oder in
  Claude Code mit vorangestelltem `!` selbst eingibt. Danach prüfst du das
  Ergebnis.
- **Alles nach außen** (GitHub-Repo anlegen, push) nur nach ausdrücklichem
  Ja in diesem Gespräch, jedes Mal neu.
- **Stil.** Für jeden Text, den du schreibst, gelten die Regeln aus
  `00_kern/persoenlich.md`, sobald Schritt 3 sie bestätigt hat. Prüfe
  geschriebene Dateien mit `python3 00_kern/stilpruefung.py --nur-fehler DATEI`.

## 2. Begrüßung (nur beim ersten Start)

Zeig in höchstens zwölf Zeilen

- was der Hub ist, ein persönlicher Arbeitsplatz mit Claude Code, in dem
  Lernen, Arbeit und eigene Vorhaben nach derselben Methode laufen
- das Bild in einem Satz, der Hub als Stamm (Regeln, Bibliothek,
  Lernsystem, Werkzeuge), an dem Äste hängen, je ein eigenes privates Repo für
  die Arbeit, für eine Selbständigkeit und für alles, was später dazukommt
- die elf Schritte als kurze Liste mit geschätzter Gesamtdauer (45 bis 60
  Minuten, ohne Karriere etwa 35) und dem Hinweis, dass man jederzeit aufhören kann

Dann frag über `AskUserQuestion`, ob es losgehen soll (Los geht's
(empfohlen), Erst mehr erfahren, Später). Bei „Erst mehr erfahren“ fasst du
die `README.md` in zehn Zeilen zusammen und fragst erneut.

## 3. Die Schritte

### Schritt 1 technik · Werkzeuge und GitHub

- `python3 00_kern/einrichten.py pruefen` ausführen und das Ergebnis als
  kurze Liste zeigen.
- Fehlt etwas, nenn die Installationsbefehle aus der Ausgabe, je Befehl ein
  eigener Codeblock. Auf dem Mac zuerst Homebrew, dann `brew install git gh
  python@3.12`. Installieren mit Passwortabfrage macht die Person selbst.
- Fehlt die git-Identität, frag Name und E-Mail (die E-Mail, die auch bei
  GitHub hinterlegt ist) und setz sie mit `git config --global`.
- Fehlt die GitHub-Anmeldung, nenn `gh auth login` (GitHub.com, HTTPS,
  Browser) zum Selbstausführen.
- Optional eine Python-Umgebung im Hub anbieten, `python3 -m venv .venv`, dann
  `.venv/bin/pip install -r requirements.txt` (Windows `.venv\Scripts\pip`).
- Erneut `pruefen`, bis alles OK ist oder die Person bewusst überspringt.
  GitHub-Konto (`gh api user -q .login`) in `person.github` eintragen.

### Schritt 2 person · Wer du bist und wohin du willst

Fragen, in zwei Nachrichten.

1. Voller Name (steht später auf Deck-Covern), Kurzform für den Chat
2. Aktuelle Rolle und Branche, neutral beschrieben. Den Namen des
   Arbeitgebers brauchst du im Hub nicht, er gehört in den Arbeits-Ast.
3. Ziel in ein bis zwei Jahren und langfristig. Ein Satz je Horizont reicht.
4. Was soll der Hub vor allem leisten? (`AskUserQuestion`, mehrere wählbar.
   Lernen mit System, Arbeit strukturieren, Selbständigkeit aufbauen,
   Bewerbungen und Karriere, private Anliegen). Bei Bewerbungen und
   Karriere vormerken, dass Schritt 8 ausführlich läuft.

Schreiben

- `einstellungen.json` → `person.name`, `person.kurzform`, `person.rolle`,
  `person.branche`
- `CLAUDE.md` Abschnitt 1 „Wer ich bin und was ich will“ als kurzer
  Fließtext in der Ich-Form, ohne Arbeitgebernamen
- `01_kompass/entwicklung/profil.md` Abschnitte Ausgangslage und Ziele

### Schritt 3 stil · Sprache, Schreibregeln, Farben

Erst erklären, dann je eine Frage über `AskUserQuestion`.

1. Sprache im Chat und Sprache der Dateien im Hub (Deutsch (empfohlen),
   Englisch, andere).
2. Schreibregeln ohne KI-Merkmale aus `00_kern/persoenlich.md` (keine
   Gedankenstriche, kaum Doppelpunkte, keine Floskeln). Zeig zwei Beispielsätze
   vorher und nachher. Optionen übernehmen (empfohlen), lockerer (nur
   Gedankenstriche verbieten), ohne.
3. Farbpalette. Zeig die acht Farben mit Namen und Hex als Tabelle. Optionen
   übernehmen (empfohlen), eigene Palette (dann acht Hexwerte erfragen, auf
   Kontrast benachbarter Farben prüfen), Firmenfarben später im Arbeits-Ast.
4. Kommunikationsstil. Zeig die fünf Punkte aus `persoenlich.md` und frag,
   ob etwas fehlt oder stört.

Schreiben

- `einstellungen.json` → `sprache.chat`, `sprache.hub`
- `00_kern/persoenlich.md` entsprechend anpassen (Abschnitte kürzen,
  entfernen oder Palette ersetzen). Bei eigener Palette auch die eine Stelle
  im Code ändern, die `07_handwerk/deck_toolkit.py` und
  `07_handwerk/dashboard_template/` als Palette führen (dort per Grep nach
  `#E0115F` suchen).
- Ist die Hub-Sprache nicht Deutsch, sag ehrlich, dass Befehle und Vorlagen
  deutsch bleiben und Claude sie trotzdem versteht. Neue Dateien entstehen
  in der gewählten Sprache.

### Schritt 4 arbeitsweise · Delegation, Qualität, Git

Zeig die drei Blöcke aus `00_kern/regeln.md` je in drei Zeilen und frag je
Block über `AskUserQuestion`, ob er so bleibt.

1. Delegationsmodell (Abschnitt 5). Was bleibt bei dir, was macht Claude im
   Gespräch, was läuft automatisch.
2. Qualität (Abschnitt 4). Plausibilität gegen Vorperiode mit 15 %,
   Quellsystem vor Gespräch, Ablauffrist drei Monate. Schwellen anpassbar.
3. Git (Abschnitt 9). Commit direkt auf `main`, push nur nach Bestätigung.
   Alternative ist ein Branch je Vorhaben mit Pull Request.

Dazu eine offene Frage, ob es Regeln gibt, die die Person aus der bisherigen
Arbeit mit Claude mitbringen will. Arbeitete sie schon mit der früheren
Workspace-Vorlage, frag, ob dort eine eigene `CLAUDE.md` mit Regeln liegt, und
übernimm nur, was die Person bestätigt.

Schreiben: `00_kern/regeln.md` anpassen.

### Schritt 5 lernen · Kompetenzprofil und Lernbudget

Erklär in zwei Sätzen das Lernsystem ALTER (Advisor plant, Librarian
liefert Quellen, Tutor prüft Verstehen und Behalten, Editor macht Ergebnisse
vorzeigbar, Roommate verbindet Fächer), Details in
`06_wissen/frameworks/ALTER_Lebenslanges_Lernen.md`.

1. Will die Person das Lernsystem nutzen? (Ja (empfohlen), Später, Nein.)
   Bei Nein überspringst du den Rest des Schritts und vermerkst es in
   `CLAUDE.md` Abschnitt 2.
2. Kompetenzprofil. Drei bis fünf Bereiche, in denen sie wachsen will, je mit
   Kürzel aus zwei Großbuchstaben (Beispiel SC Supply Chain, DK Daten und KI,
   OP Operations, BU Business, BE Beratung). Du schlägst aus Schritt 2 eine
   Liste vor, die Person korrigiert.
3. Budget. Stunden Deep Dive je Woche (Vorschlag 5) und Minuten Wiederholung
   je Tag (Vorschlag 20). Start des ersten Trimesters (Vorschlag der nächste
   Monatserste).

Schreiben

- `einstellungen.json` → `profil.bereiche` als Liste `{kuerzel, name}`,
  `lernen.*`
- `01_kompass/entwicklung/profil.md` Abschnitt Kompetenzprofil
- `01_kompass/studienplan/studienplan.md` Kopf mit Trimester, Budget und
  Bereichen, Modultabelle leer. Module entstehen später mit `/aufnahme` und
  `/advisor`, nicht jetzt.

Zum Schluss auf die drei Beispielmodule in `01_kompass/module/_beispiele/`
hinweisen (Bewerbungsgespräch, Python, Datenplattform). Passt eines zu einem
Bereich des Profils, etwa das Bewerbungsgespräch bei laufender Jobsuche,
nenn den Weg aus der README dort als Befehl zum Kopieren
(`/advisor <ID>` nach dem Kopieren), übernimm es aber nicht selbst.

### Schritt 6 aeste · Äste für Arbeit, Selbständigkeit und weitere

Erklär das Prinzip in drei Sätzen. Ein Ast ist ein eigenes privates Repo
neben dem Hub. Arbeitsdaten bleiben im Ast, in den Hub kommt nur
Anonymisiertes über feste Wege (Lernkarte, Framework, Case Study). Jeder Ast
hat eine Spur, unter der Lernprojekte dort geübt werden.

Für jeden Ast, einer nach dem anderen.

1. Art über `AskUserQuestion` (Arbeit beim Arbeitgeber, eigene
   Selbständigkeit, Sonstiges wie Verein oder Ehrenamt, Kein weiterer Ast).
2. Name des Repos. Vorschlag nach Schema `AT_<KÜRZEL>` für eine angestellte
   Tätigkeit und `ST_<KÜRZEL>` für eine selbständige, Kürzel aus dem
   Firmennamen. Nur Buchstaben, Ziffern und Unterstrich.
3. Spur. Vorschlag A für Arbeit, U für Unternehmen, sonst der nächste freie
   Buchstabe. Sprache der Dateien im Ast (bei Arbeit oft Englisch).
4. Wo der Ast liegen soll. Vorschlag neben dem Hub. Wichtig ist eine
   Rückfrage bei der Arbeit, ob Firmendaten auf diesem Rechner überhaupt
   liegen dürfen. Bei Nein entsteht der Ast nur als Eintrag und wird später
   auf dem Firmenrechner angelegt (dort `/einrichten aeste` erneut).

Dann

- `python3 00_kern/einrichten.py ast <NAME> --art <art> --spur <S> --sprache <Sprache>`
- Im neuen Ast `CLAUDE.md` Abschnitt 1 mit zwei bis vier Sätzen aus dem
  Gespräch füllen (Rolle, Auftrag, neutral).
- Frag, ob das private GitHub-Repo jetzt entstehen soll. Bei Ja
  `gh repo create <NAME> --private --source <Pfad> --push` und danach in
  `einstellungen.json` beim Ast `repo` auf `<github>/<NAME>` setzen.
- Zeile in `CLAUDE.md` Abschnitt 5 (Äste) des Hubs ergänzen.

Danach fragen, ob ein weiterer Ast dazukommt. Weitere Äste gehen jederzeit
mit `/ast-anlegen`.

### Schritt 7 bibliothek · Bibliothek und Themenordner

1. Themenordner unter `02_bibliothek/` vorschlagen, abgeleitet aus dem
   Kompetenzprofil (Ordnernamen ASCII mit Unterstrich, z. B.
   `Supply_Chain_und_Operations`). Die Person bestätigt.
2. Erklären, dass Fachbücher als PDF in diese Ordner gehören, mit Dateiname
   `Autor_Titel.pdf`, und dass beim nächsten Sitzungsstart ein Hook neue PDFs
   findet und `/add-literature` sie in den Index einträgt.
3. Auf den mitgelieferten Methodenkoffer hinweisen
   (`02_bibliothek/Consulting_Life_Methodenkoffer.md`, ein Index von über 200
   Beratungsmethoden). Fragen, ob er bleiben soll (empfohlen bei Interesse an
   Beratung) oder raus kann.
4. Hinweis, dass urheberrechtlich geschützte PDFs in einem öffentlichen Repo
   nichts verloren haben. Der Hub bleibt privat.

Schreiben: Ordner mit `.gitkeep`, Tabelle „Ordnerstruktur“ in
`02_bibliothek/Literatur_Index.md`.

### Schritt 8 karriere · Lebenslauf, Anschreiben und Jobsuche

Damit `/job-apply` ab der ersten Anzeige Unterlagen im eigenen Stil baut.
Hat die Person in Schritt 2 „Bewerbungen und Karriere“ nicht gewählt, frag
zuerst, ob der Schritt jetzt (empfohlen bei laufender Suche) oder später
kommt. Dauer etwa 20 Minuten, mit vorhandenem Lebenslauf schneller.

**8a Suche.** Über `AskUserQuestion` der Stand (aktiv auf Suche, offen für
Angebote, keine Suche). Dann offen, höchstens drei Fragen je Nachricht.
Zielrollen, Branchen, Unternehmensgröße, Region und Pendeldistanz,
Remote-Anteil, Gehaltsspanne, Kündigungsfrist und frühester Eintritt,
Reisebereitschaft, Ausschlusskriterien, Wunschfirmen.
Schreiben in `05_werkstatt/karriere/Profil/Zielfirmen_Praeferenzen.md` mit
„Last Validated“ von heute.

**8b Fakten.** Bitte um den aktuellen Lebenslauf (PDF oder Word) oder den
LinkedIn-Export (LinkedIn, Profil, Mehr, Als PDF speichern), abgelegt unter
`05_werkstatt/karriere/Profil/` oder als Pfad genannt. Lies ihn und übertrag
alles nach `Profil/Master_CV_Daten.md`. Dann Station für Station
nachfragen, höchstens drei Fragen je Station. Was war das messbare Ergebnis,
welche Werkzeuge, welcher Nachweis belegt Titel und Zeitraum? Ohne Lebenslauf
dieselben Fragen von Grund auf. Nichts ergänzen, was die Person nicht sagt.
Zeugnisse und Zertifikate kann sie unter `Profil/Nachweise/` ablegen, dann
füllst du `Profil/Nachweise_Index.md` und gleichst Titel, Zeiträume und
Noten mit `Master_CV_Daten.md` ab. Abweichungen nennst du, die Person
entscheidet.

**8c Lebenslauf-Stil.** Je eine Frage über `AskUserQuestion`.
1. Sprachen der Fassungen (Deutsch, Englisch, beide).
2. Länge (eine Seite (empfohlen bis rund zehn Jahre Erfahrung), zwei Seiten).
3. Foto (ja, nein, je nach Land). Bei ja `Profil/Bewerbungsfoto.jpg` ablegen
   lassen.
4. Schrift (Helvetica Neue sachlich (empfohlen auf dem Mac), Arial neutral,
   Georgia klassisch mit Serifen, Garamond elegant).
5. Akzentfarbe für Hinweise (dezentes Rot wie bisher, eine Farbe aus der
   Palette in `00_kern/persoenlich.md`, keine Farbe, also Schwarz).
Dazu offen. Reihenfolge Erfahrung oder Ausbildung zuerst, Zusammenfassung oben
ja oder nein, wie viele Punkte je Station, was immer drin sein muss und was
nie (etwa Geburtsdatum, Familienstand).

**8d Anschreiben-Stil.**
1. Standard (immer, nur wenn verlangt, nie).
2. Tonalität (sachlich, persönlich, selbstbewusst, zurückhaltend), mehrere
   wählbar.
3. Anrede ohne und mit Namen, Grußformel.
4. Wörter, die nach der Person klingen, und Floskeln, die sie nie lesen will.
5. Frag nach einem früheren Anschreiben, das ihr gefallen hat. Liegt eines
   vor, leite Ton und Aufbau daraus ab und zeig sie in fünf Zeilen zur
   Bestätigung.
Unterschrift optional als `Profil/Unterschrift.png` (Scan auf weißem Grund).

**8e Probe.**
- Prüfen, ob Edge oder Chrome installiert ist, sonst
  `brew install --cask google-chrome` nennen. `pip install pypdf` in der
  Umgebung des Hubs.
- `Profil/stil.json` und `Profil/Bewerbungsstil.md` schreiben.
- `07_handwerk/Bewerbung_PDF/cv_inhalt_vorlage.py` als
  `Profil/cv_inhalt_basis.py` kopieren und aus `Master_CV_Daten.md` füllen.
  Die Basis enthält alle Stationen, je Station die zwei bis vier stärksten
  Punkte. Das Anschreiben bleibt als allgemeiner Entwurf mit Platzhaltern.
- Rendern nach `Bewerbungen/_Basis/`
  (`python3 07_handwerk/Bewerbung_PDF/render.py 05_werkstatt/karriere/Profil/cv_inhalt_basis.py 05_werkstatt/karriere/Bewerbungen/_Basis`),
  das PDF ansehen und der Person zeigen. Wie beim Hintergrundbild eines neuen
  Handys darf sie so lange ändern lassen (Schrift, Farbe, Länge, Wortwahl), bis
  es passt. Jede Änderung landet in `stil.json` oder `Bewerbungsstil.md`,
  nicht nur im PDF.

Zum Schluss erklären, wie es weitergeht. Anzeige als PDF, Link oder Text an
`/job-apply` geben, Ergebnis liegt in `Bewerbungen/<Firma>_<Rolle>_<Datum>/`,
Lücken sammelt `01_kompass/entwicklung/Skill_Gap_Log.md`. Der Hinweis, dass
Nachweise, Foto und Gehaltsdaten nur in ein privates Repo gehören.

### Schritt 9 installieren · Regeln und Skills nach ~/.claude

- Erklären, was passiert. `~/.claude/CLAUDE.md` bekommt zwei Importzeilen auf
  `00_kern/persoenlich.md` und `00_kern/regeln.md`, damit die Regeln in jedem
  Repo gelten, auch in den Ästen. Skills wie `/new-project` und der Agent
  `literature-scout` werden global verfügbar. Eigener Text in
  `~/.claude/CLAUDE.md` bleibt stehen.
- `python3 00_kern/installieren.py --dry-run` zeigen, nach Ja ohne
  `--dry-run` ausführen, zum Schluss einen zweiten Trockenlauf, der „Nichts
  zu ändern“ melden muss.
- Hinweis, dass die neuen Skills erst in einer neuen Claude-Code-Sitzung
  erscheinen.

### Schritt 10 github · Eigenes privates Repo für den Hub

- `git remote -v` prüfen.
  - Zeigt `origin` auf die Vorlage (`vorlage_repo` in `einstellungen.json`),
    erklär, dass der Hub sonst in die Vorlage pushen würde. Vorschlag
    `git remote rename origin vorlage`, dann
    `gh repo create Hub --private --source . --remote origin`.
  - Kein `origin`, dann direkt `gh repo create`.
  - Zeigt `origin` schon auf ein eigenes Repo (über „Use this template“
    entstanden), prüfen, dass es privat ist
    (`gh repo view --json visibility`). Ist es öffentlich, deutlich warnen und
    `gh repo edit --visibility private` anbieten.
- Ersten Commit der Einrichtung vorschlagen, Dateien nennen, nach Ja
  committen und nach einem zweiten Ja pushen.
- Zwei Rechner. Erklär kurz `git pull --ff-only` vor der Arbeit und das
  Gedächtnis über `python3 00_kern/gedaechtnis_sync.py export` und `import`.

### Schritt 11 start · Erste Aufgabe und Rundgang

1. Rundgang in höchstens 15 Zeilen. Ordner `00_kern` bis `07_handwerk` je
   eine Zeile, dann die wichtigsten Befehle (`/aufnahme`, `/new-project`,
   `/alter`, `/heute`, `/weekly-review`, `/ast-stand`, `/ast-anlegen`,
   `/job-apply`, `/learn-poster`, `/framework-next`, `/einrichten`).
2. Frag nach der ersten echten Aufgabe über `AskUserQuestion` (Lernprojekt
   starten, Aufgabe aus der Arbeit aufnehmen, Vorhaben der Selbständigkeit,
   Später). Je nach Antwort nennst du den passenden Befehl zum Kopieren,
   startest ihn aber nicht selbst.
3. `python3 00_kern/einrichten.py erledigt start` und
   `python3 00_kern/einrichten.py fertig`. Danach den Abschnitt
   „Ersteinrichtung“ oben in `CLAUDE.md` entfernen.
4. Zum Schluss eine kurze Zusammenfassung, was eingerichtet ist, was offen
   blieb (Schritte mit „später“) und dass `/einrichten <schritt>` jeden
   Schritt erneut öffnet. Commit vorschlagen.

## 4. Was du nicht tust

- Keine Passwörter, Tokens oder Zugangsdaten abfragen oder eintippen.
- Kein Repo öffentlich anlegen.
- Keinen Arbeitgebernamen, keine Firmendaten in den Hub schreiben. Sie
  gehören in den Arbeits-Ast.
- Keine Module, Projekte oder Karten auf Vorrat anlegen. Die entstehen mit
  der ersten echten Aufgabe.
- Nichts außerhalb des Hubs und der neu angelegten Äste ändern, außer
  `~/.claude` in Schritt 9 und der globalen git-Identität in Schritt 1.
