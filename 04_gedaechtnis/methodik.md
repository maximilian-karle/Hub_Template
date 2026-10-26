# Methodik Tagesbudget und Zufluss

Zu `heute.py`, `engine.py` und `alter.py`. Die Regeln stehen im Kopf von `heute.py`, hier
stehen die Annahmen dahinter, die Rechnung für die Obergrenze und die
Entscheidungen im Entwurf.

## Annahmen

Die Werte sind Startwerte für jeden neuen Hub. „Last Validated“ setzt der
Nutzer beim ersten Prüfen, ein leeres Feld heißt, der Wert ist noch nicht am
eigenen Verlauf geprüft.

| Annahme | Wert | Herkunft | Last Validated |
|---|---|---|---|
| Sekunden je Begriffskarte | 30 | Schätzung für einen kurzen Abruf, am eigenen Sitzungsverlauf prüfen | |
| Sekunden je Anwendungskarte | 60 | Schätzung, doppelt so lang wie ein Begriff | |
| Sekunden je Rechnungskarte | 90 | Schätzung, dreifach | |
| Tagesbudget | 15 bis 30 Minuten, Standard aus `lernen.wiederholung_min_tag` in `00_kern/einstellungen.json` (ohne Eintrag 20) | `01_kompass/lerngrundsaetze.md` | |
| Minimalbetrieb | 10 Minuten, nur Wiederholung | Grundsatz 4 in `01_kompass/lerngrundsaetze.md` | |
| Wiederholungen je neuer Karte in zwei Monaten | 4 | Intervalle 1, 6, 15, 38 bei durchweg richtiger Antwort | |
| Anteil aktiver Abschnitte am Neuen | 70 % | Setzung, Vorrang für den laufenden Stoff | |
| Aktiv heißt freigeschaltet vor weniger als | 14 Tagen | Schätzung, etwa ein Lesepfad-Abschnitt je Woche mit Nachlauf | |
| Bremse ab Wiederholungslast von | 1,5 Tagesbudgets | Setzung | |
| Mindestzufluss aus aktiven Abschnitten | 2 Karten | Schätzung | |
| Karte sitzt ab Intervall | 21 Tagen | Setzung, drei Wochen | |
| Wochenbudget Deep Dive | aus `lernen.deep_dive_h_woche` in `00_kern/einstellungen.json`, ohne Eintrag 5 Stunden | `01_kompass/lerngrundsaetze.md` | |
| Zielkorridor Abrufquote | 60 bis 70 % | Setzung. Eine höhere Quote heißt meist zu leichte Karten oder zu kurze Intervalle, eine tiefere zu viel Neues | |
| Bestehensschwelle Trimesterprüfung | 70 % | Schätzung, nach dem ersten Lauf prüfen | |
| Abstand der Messpunkte für den Rückstau-Trend | mindestens 6 Tage | Wochenrhythmus von `/weekly-review` | |
| Problemkarte (`alter.py`, Regel 2) | 2 Abrufe in Folge unter Note 3 | Setzung. Anki nennt solche Karten Leech, dort erst ab 8 Fehlern. Hier früher, weil die Karte zum Tutor führt und nicht gesperrt wird | |
| Illusion des Wissens (Regel 3) | 2 Abrufe in 14 Tagen mit Zuversicht ab 70 % und Note unter 3 | Setzung nach Make It Stick, Kap. 5 (Kalibrierung), die Schwellen stehen dort nicht | |
| Feynman mit Abstand (Regel 4) | Abschnitt mit mindestens 3 Karten, alle mit Intervall ab 21 Tagen | Schwelle „sitzt“ wie oben, Mindestzahl Setzung | |
| Wochenreview fällig | letzter Messpunkt 7 Tage alt | Wochenrhythmus | |

Die Schwellen für `alter.py` werden in den ersten Wochen geprüft. Feuert eine
Regel nie oder ständig, ist die Schwelle falsch gesetzt.

Die Werte ohne Messung werden nach den ersten vier Wochen gegen die Ist-Zeiten
und die Trefferquote aus dem Verlauf der Karten geprüft, danach steht das
Datum in „Last Validated“.

## Rechnung für die Obergrenze

| Wert | Formel und Eingaben | Ergebnis |
|---|---|---|
| Abrufe je neuer Karte im eingeschwungenen Kasten | 1 Erstkontakt + 4 Wiederholungen | 5 |
| Zeit je neuer Karte und Tag | 5 × 30 s | 150 s |
| Obergrenze bei 15 Min. | 900 s / 150 s | 6 Karten |
| Obergrenze bei 20 Min. | 1.200 s / 150 s | 8 Karten |
| Obergrenze bei 30 Min. | 1.800 s / 150 s | 12 Karten |
| Gegenprobe feste Teilung 50/50 bei 15 Min. | 450 s / 30 s = 15 neue Karten, Folgelast 15 × 4 × 30 s | 1.800 s Wiederholung je Tag, das Doppelte des Budgets |

Bei einer Trefferquote im Zielkorridor von 60 bis 70 % fallen Karten öfter
zurück, die Folgelast liegt eher bei sechs Wiederholungen je Karte. Dann trägt
der Kasten bei 15 Minuten nur vier neue Karten. Die Bremse fängt das ab.

## Entscheidungen im Entwurf

- **Ein Gedächtnis für alle Lernprojekte.** Jedes Lernprojekt des Hub legt
  seine Karten hier ab. Hat ein Lernprojekt eine eigene Engine (etwa eine
  Sprach-App), bleibt es draußen. Das steht dann im Studienplan
  `01_kompass/studienplan/studienplan.md`, und seine Zeit läuft nicht über
  `/heute`.
- **Drei Zustände statt einer Warteschlange.** Gesperrt, bereit, im Kasten.
  Freigeschaltet wird je Abschnitt, sobald er gelesen ist, nicht zufällig aus
  ungelesenem Stoff, weil Abruf auf Unbekanntem nichts misst. Der Vorrat
  bereiter Karten ist kein Rückstand und wird nirgends als solcher gezählt.
- **Wiederholung zuerst, gemischt über alle Projekte**, die am längsten
  überfälligen voran. Gemischtes und verteiltes Üben ist dem geblockten
  überlegen (Brown, Roediger, McDaniel, Make It Stick, Kap. 3).
- **Keine feste Teilung zwischen Wiederholung und Neuem.** Neues füllt den
  Rest, begrenzt durch die Obergrenze aus dem Gleichgewicht. Eine feste
  Teilung 50/50 ließe den Kasten in wenigen Wochen überlaufen (Rechnung oben).
- **Bremse mit Mindestzufluss.** Die Bremse hält die Last tragbar, der
  Mindestzufluss hält den laufenden Stoff in Bewegung, solange der Berg
  unter der Bremse liegt. Kontinuität im laufenden Stoff geht vor
  Vollständigkeit beim alten.
- **70/30 zwischen aktiven Abschnitten und Vorrat**, für Zeit und Anzahl.
  Der Vorrat wird zufällig gezogen, damit ältere Abschnitte nicht ewig liegen.
  Der Zufall ist je Tag fest. Was ein Anteil nicht braucht, geht an den
  anderen.
- **Ein Befehl für den Ablauf.** `alter.py` wählt die nächste Tätigkeit aus
  den Daten, damit Sokrates, Feynman und Editor nicht nur am Blockrand
  vorkommen, sondern immer dann, wenn die Karten eine Lücke zeigen.
  Behalten geht vor, dann Lücken im Verstehen (Problemkarte vor Illusion,
  weil eine Karte, die immer scheitert, den Kasten verstopft), dann der
  Abstandstest sitzender Abschnitte, dann der laufende Block, dann der
  Meilenstein, dann Neues. Ein Kern-Block, dessen Karten schon frei sind,
  überspringt Ausgangswert und Lesen, weil der Stoff gelesen ist.
- **Zurückgestellt statt Rückstand.** Was nicht in die Zeit passt, bleibt
  fällig und rückt nach. Die Ausgabe nennt es `zurueckgestellt`, `/heute`
  erwähnt es nicht (Grundsatz 5 in `01_kompass/lerngrundsaetze.md`, kein
  Schuldaufbau).

## Quellen

- Brown, Roediger, McDaniel, Make It Stick, Kap. 2 (Abruf), Kap. 3 (Mischen und
  Verteilen), Kap. 5 (Kalibrierung über die Zuversicht). Die Zeitkosten und
  Schwellen stammen nicht aus dem Werk, sie sind Setzungen und werden am
  eigenen Verlauf geprüft.
