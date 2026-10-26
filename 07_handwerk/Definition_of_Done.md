# Definition of Done je Ergebnistyp

Ein Ergebnis ist „berechnet“, sobald ein Zahlenwert vorliegt. Fertig ist es
erst, wenn die folgenden Punkte erfüllt sind.

## Analyse (etwa Cost-to-Serve, Reifegrad, Hochlauf, Szenario)

- [ ] Methodik in `methodology/*.md` dokumentiert (Formel, Datenquellen,
      Annahmen, Letzte Validierung)
- [ ] `/qa-check` gelaufen, keine offenen Befunde, oder offene Befunde
      bewusst akzeptiert und begründet
- [ ] Bei einer strategischen Empfehlung ist die Gegenposition durchdacht
      (Advocatus Diaboli)

## Dashboard

- [ ] Kennzahlen und Formeln dokumentiert (bei Power BI die DAX-Measures in
      `dashboards/dax_measures.md`, bei HTML-Dashboards im Builder)
- [ ] Datenquelle und Tabellenbeziehungen in `data_model_notes.md`
      nachvollziehbar
- [ ] Aktualisierungsrhythmus festgelegt (wer, wann, wie oft)
- [ ] Abgleich gegen die Rohdaten aus `data/output/` durchgeführt

## Pipeline-Umbau (Loader, Inputs, Logik ohne fachliche Änderung)

- [ ] Vor dem Umbau ist ein Referenzlauf eingefroren (Golden Master aus
      Ergebnistabelle, Inputs und deren Inhalts-Hashes)
- [ ] Der Lauf nach dem Umbau ist auf denselben Inputs zellgenau gegen die
      Referenz verglichen. Jede bewegte Zahl ist erklärt, sonst ist der
      Umbau nicht fertig
- [ ] Ein Gegentest belegt, dass der Vergleich eine absichtlich veränderte
      Zahl findet

## Bericht und Präsentation

- [ ] Struktur folgt `Praesentationsstandard.md`
- [ ] `/steering-prep` ergibt Go oder Conditional Go
- [ ] Anhang verweist auf `methodology/*.md`, statt Inhalte zu doppeln
- [ ] Jede Zahl trägt ihren Rechenweg (Formel und Inputs daneben oder im
      Rechenanhang)

Ein Ergebnis ohne erfüllte Checkliste gilt als Entwurf, gleich wie
überzeugend die Zahl wirkt.
