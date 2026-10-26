# Vertraulichkeit bei Case Studies und Rückfluss aus den Ästen

Gilt, sobald Inhalte aus einem Projekt in `05_werkstatt/case_studies/`
übertragen werden oder aus einem Ast über einen festen Weg in den Hub
zurückfließen (Lernkarte, Framework-Eintrag, Case Study). Gemeint ist alles,
was das Unternehmen oder den Auftraggeber verlässt, also
Bewerbungsunterlagen, Portfolio und externe Gespräche.

## Was NIE 1:1 übernommen wird

- Reale Namen von Lieferanten, Kunden und Partnern samt Konditionen
- Lohn- und Personalkosten (auch nicht aggregiert, wenn ein Rückschluss
  möglich ist)
- Interne Zielwerte und Budgetgrenzen im Original
- Namen einzelner Mitarbeitender aus Gesprächen (Rolle statt Name)
- Exakte Material- und Auftragsnummern aus dem Quellsystem (etwa SAP),
  Kundenaufträge und Vertragsdetails
- Der Name des Arbeitgebers oder Auftraggebers, solange er nicht
  ausdrücklich freigegeben ist (Branche und Größe statt Name)

## Wie stattdessen dargestellt wird

- Relative statt absolute Kennzahlen („−32 % Kosten“ statt „von X auf Y
  EUR“), außer das Unternehmen hat eine externe Nennung ausdrücklich
  freigegeben
- Rollenbezeichnung statt Klarname („Leitung Supply Chain“, „Einkauf“)
- Wo eine absolute Zahl fürs Verständnis nötig ist, als Bandbreite oder
  indexiert (Basis 100) statt als Originalwert

## Prüfpflicht

Entsteht aus einem Projekt ein Entwurf für eine Case Study oder einen
Rückfluss, prüft Claude ihn automatisch auf die Kategorien oben und markiert
sensible Stellen mit `[ANONYMISIEREN: ...]`, statt sie unkommentiert zu
übernehmen. Die finale Freigabe für die externe Nutzung liegt bei der
Person, nicht bei der automatischen Prüfung.
