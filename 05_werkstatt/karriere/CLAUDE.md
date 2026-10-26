# Karriere

Lädt, wenn in diesem Ordner gearbeitet wird. Zweck ist, von der
Stellenanzeige bis zur versandfertigen, auf die Anzeige zugeschnittenen
Bewerbung alles an einem Ort zu haben, dazu die laufende
Leistungsdokumentation für Gespräche und Verhandlungen.

Abgrenzung zu `../case_studies/`. Case Studies sind fertige, anonymisierte
Fallstudien. Hier liegt der Rohstoff davor (Profil, Leistungen) und die
Bewerbungen selbst.

## Aufbau

```
karriere/
├── CLAUDE.md
├── Profil/
│   ├── Master_CV_Daten.md          alle Fakten, einzige Quelle
│   ├── Nachweise_Index.md          was in jedem Nachweis steht
│   ├── Nachweise/                  Zeugnisse und Zertifikate als PDF, nur im privaten Repo
│   ├── Leistungsdokumentation.md   Ergebnisse nach STAR, vertraulich
│   ├── Zielfirmen_Praeferenzen.md  Rollen, Branchen, Region, Gehalt, Ausschlüsse
│   ├── Bewerbungsstil.md           Länge, Ton, Anrede, Wörter
│   ├── stil.json                   Schrift, Akzentfarbe, Foto, Seitenzahl für render.py
│   ├── cv_inhalt_basis.py          Basis für jede Bewerbung, aus Master_CV_Daten.md gebaut
│   ├── mappe.json                  welche Nachweise in welche Anlage
│   ├── Bewerbungsfoto.jpg          optional
│   └── Unterschrift.png            optional
└── Bewerbungen/
    ├── _Basis/                     gerenderte Basisfassung
    └── <Firma>_<Rolle>_<JJJJ-MM-TT>/
        ├── Stellenanzeige.md
        ├── Keyword_Matching.md
        ├── inhalt.py
        └── Lebenslauf_*.pdf, Anschreiben_*.pdf
```

## Grundsätze

- Jede Bewerbung wird zugeschnitten. Viele Firmen filtern per ATS nach den
  Wörtern der Anzeige, deshalb greift der Lebenslauf deren Formulierungen
  auf, wo die eigene Erfahrung sie deckt.
- Keine Erfindung. Was nicht belegt ist, kommt nicht hinein. Lücken werden
  offen benannt und ins `01_kompass/entwicklung/Skill_Gap_Log.md`
  eingetragen.
- Inhalte aus `Leistungsdokumentation.md` laufen vor der Übernahme durch die
  Prüfung nach `00_kern/vertraulichkeit.md`.
- Ablauf über `/job-apply`.
