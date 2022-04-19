# Arjen Bos - Curriculum Vitea
Als je dit leest heb je waarschijnlijk het GitHub-logo op mijn CV herkent en ben je geïnteresseerd in de hard-skills die ik te bieden heb.
* Python
  * Bij elk project gebruik ik wel [pandas-profiling](https://pypi.org/project/pandas-profiling/), zelfs al heeft het project verder niets met Python te maken. 
  * Voor data analyse zijn pandas, matplotlib en jupyter mijn favoriete packages.
  * Automatiseren van processen doe ik o.a. met selenium, lxml, pathlib.
  * Mijn CV is ook gebouwd met Python! De code vind je in deze repo in de folder cv.
* git
  * Bij ABN AMRO verzorgde ik het versiebeheer van ons team. Dit hield in dat ik de remote repository opzette en onderhield, toezag op juiste werkwijze en branchingstrategie en merge-conflicts oploste.
  * Veel van mijn persoonlijke projecten beheer ik met git. De repo's staan op GitHub, maar (helaas) de meeste zijn niet public.
  * Deze repo bevat de code van mijn website en mijn CV.
* Markdown
  * Documentatie, zoals deze README, schrijf ik het liefst in Markdown. Dat is gemakkelijk en duidelijk.

## Developers notes
### Todos
* Wordbreaks `<wbr>` in template als HTML doorzetten
    * Check yaml.safe_load() en/of jinja2 escapes
* Download PDF (en zwartwit PDF) optie onderin website CV
* Gebruik verschillende kleuren voor project voor freelance / EIFFEL en anderen
* Consistentie in datums / perioden van projecten

### Setup
1) Clone deze repo `git clone https://github.com/arjobsen/cv`
1) Opzetten virtual environment `python -m venv venv`
1) Activeer deze, zie [docs](https://docs.python.org/3/library/venv.html)
    * Op Linux met fish gebruik `source venv/bin/activate.fish`
1) Check eventueel met `which python`
1) Installeer requirements `pip install -r requirements.txt`

### Render templates naar HTML
1) Activeer de virtual environment
1) Run `python render.py`

### Prints
1) Gebruik de verborgen [Print pages 1 by 1] knop om de pagina's één voor één te printen.
1) Print deze als losse PDF in de print folder en noem ze print_1, print_2, etc.
1) Voeg de geprinte PDF's samen `pdftk (ls print_*) cat output CV\ Arjen\ Bos\.pdf`
