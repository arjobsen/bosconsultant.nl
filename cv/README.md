Voor het ontwerp van mijn CV gebruik ik HTML en CSS met [Tailwind](https://tailwindcss.com). En met Python en [Jinja](https://jinja.palletsprojects.com/) laad ik de data, zoals de projecten die ik uitgevoerd heb, in de templates.

Hier zijn de instructies om deze repo te klonen en het CV te renderen. Voer de `commando's` uit in een terminal zoals Git Bash. De code is vrij kopieerbaar, dus voel je vrij om dit voor eigen doeleinden te gebruiken.

### Eenmalige setup
1) Clone deze repo `git clone https://github.com/arjobsen/ahbos.nl`
1) Maak een Python virtual environment `python3 -m venv venv`
1) Activeer de venv, zie eventueel de [docs](https://docs.python.org/3/library/venv.html) welk commando geschikt is voor jouw computer
    * Op Windows met cmd gebruik `venv\Scripts\activate.bat`
    * Op Linux met fish gebruik `source venv/bin/activate.fish`
1) Check eventueel met `which python` (Linux) of `python` nu daadwerkelijk verwijst naar de zojuist aangemaakte venv
1) Installeer de vereiste packages `pip install -r requirements.txt`

### Templates met data render naar index.html
Ik gebruik Python en [Jinja](https://jinja.palletsprojects.com/) om data in mijn CV te laden.
1) Activeer de venv mocht die nog niet geactiveerd zijn
1) Navigeer naar de cv folder `cd cv`
1) Run `python render.py`

### Print de pagina's als PDF
1) Unhide de verborgen [Print pages 1 by 1] knop
  * Ga naar developer tools (F12 op Firefox)
  * Vind het eerste <div> onder <body> en uncheck de `display: none;` style
1) Klik op die knop om één voor één de pagina's te printen. Dit is nodig omdat portrait en landscape georiënteerde pagina's gebruikt worden.
1) Print deze als losse PDF in de /prints/pages folder en noem ze print_1.pdf, print_2.pdf, etc.
  * Wellicht moet je nog instellen om *geen* marges, headers en footers te printen en *wel* de background
  * Print de frontpage in portait modus en het trackrecord in landscape
1) Navigeer naar de prints folder `cd prints`
1) Voeg de geprinte PDF's samen `pdftk $(ls pages/*) cat output CV_Arjen_Bos.pdf`
  * Let op, [command substitution met fish](https://fishshell.com/docs/current/fish_for_bash_users.html#command-substitutions) gebruikt alleen de (haakjes), dus zonder $

### Todos
- [ ] Wordbreaks `<wbr>` in template als HTML doorzetten
    - [ ] Check yaml.safe_load() en/of jinja2 escapes
- [ ] Download PDF (en zwartwit PDF) optie onderin website CV
- [ ] Gebruik verschillende kleuren voor project voor freelance / EIFFEL en anderen
- [ ] Consistentie in datums / perioden van projecten
- [ ] Automatiseer het handmatige printproces
  - [ ] Ik heb al Python package html->pdf geprobeerd maar die pakt Tailwind niet goed mee
  - [ ] Het Firefox print venster lijkt niet goed automatiseerbaar, ook niet met Selenium
