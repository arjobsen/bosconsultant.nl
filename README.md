# Arjen Bos - Curriculum Vitea
Als je dit leest heb je waarschijnlijk het GitHub-logo op mijn CV herkent en ben je geïnteresseerd in de hard-skills die ik te bieden heb.
* git
  * Bij ABN AMRO verzorgde ik het versiebeheer van ons team. Dit hield in dat ik de remote repo opzette en onderhield, toezag op juiste werkwijze en branchingstrategie en merge-conflicts oploste.
  * Veel van mijn persoonlijke projecten beheer ik met git. De repo's staan op GitHub, maar (helaas) de meeste zijn niet public.
* Python
  * Bij elk project gebruik ik wel [pandas-profiling](https://pypi.org/project/pandas-profiling/), zelfs al heeft het project verder niets met Python te maken. 
  * Voor data analyse zijn pandas, matplotlib en jupyter favoriete packages.
  * Automatiseren van processen doe ik o.a. met selenium, lxml, pathlib.
  * Mijn CV is ook gebouwd met Python! De code vind je in deze repo.
* Markdown


## Develop notes
### Todos
* Wordbreaks <wbr> in template als HTML doorzetten
* HTML naar PDF script
* Merge frontpage en trackrecord script of command (pdftk)

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
1) Open de HTML bestanden in een browser `firefox ./public/front_page.html`
1) Print deze als PDF in de print folder
1) Voeg de front page en track record samen `pdftk front_page.html.pdf track_record.html.pdf cat output CV\ Arjen\ Bos\.pdf`
