Simple Text Tool

Simple Text Tool är ett enkelt Pythonprogram som läser en textfil, analyserar innehållet
och räknar antal rader och ord. Resultatet skrivs ut i terminalen och sparas även i en fil.

Projektet är byggt med fokus på tydlig projektstruktur, versionshantering och isolerad miljö.

---

## Installation

1. Klona repot:
   git clone https://github.com/ilbron4/simple_text_tool.git

2. Gå in i projektmappen:
   cd simple_text_tool

3. Skapa en virtuell miljö:
   python -m venv .venv

4. Aktivera den virtuella miljön:

   Windows:
   .venv\Scripts\Activate

   Mac/Linux:
   source .venv/bin/activate

5. Installera beroenden:
   pip install -r requirements.txt

---

## Kör programmet

För att köra programmet, använd:

Windows:
py run.py

Alternativt:
python run.py

Programmet läser textfilen data/example.txt och skriver ut resultatet i terminalen.
Resultatet sparas även i output/result.txt.

---

## Projektstruktur (översikt)

- src/app innehåller applikationslogik, konfiguration och logger
- src/utils innehåller funktioner för filinläsning och databehandling
- data innehåller exempeldata
- output innehåller genererad output från programmet

---

## Funktionalitet

Programmet:
- läser textdata från fil
- bearbetar data genom att räkna rader och ord
- skriver resultat till terminal och fil

Projektet använder:
- klasser och funktioner i separata moduler
- konfigurationsfil för sökvägshantering
- egen logger
- Git med feature-branching
- virtuell miljö (venv)

