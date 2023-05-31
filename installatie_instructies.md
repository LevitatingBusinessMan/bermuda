# Python installeren
Installeer Python via: https://www.python.org/

Bij Windows zorg ervoor dat je `Add python.exe to PATH` aantikt bij de installatie.
![](https://i.imgur.com/DEOPocU.png)

# Bermuda bestanden downloaden
De bermuda python bestanden zijn te vinden op mijn GitHub: [LevitatingBusinessMan/bermuda](https://github.com/LevitatingBusinessMan/bermuda).

#### Zip-bestand
Zo kan je de meest recente versie downloaden als een ZIP-bestand.
![](https://i.imgur.com/sP2wlbY.png)

#### Terminal
Je kan de bestanden ook makkelijk via de terminal downloaden. Bijvoorbeeld handig op een Raspberry Pi. Je hebt dan [git](https://book.git-scm.com/) nodig. 

```SHELL
git clone https://github.com/LevitatingBusinessMan/bermuda.git
```
Dit vormt een folder genaamd "bermuda met de bestanden". In die folder kan je via `git pull origin master` zorgen dat je op de meest recente versie zit.

# Uitvoeren
### Terminal open in de bermuda folder op MacOS
Nadat je de bermuda bestanden gedownload hebt moet je ze uitvoeren. Het makkelijkst is om ze uit te voeren via je terminal. Daarvoor moet je de juiste folder openen in je terminal. Als je de `bermuda` folder uitgepakt hebt op je bureablad, kan je via Spotlight de Terminal open en `cd /Users/<gebruiker>/Desktop/bermuda` uitvoeren (`<gebruiker>` vervangen met je eigen username). Als je eenmaal in de juiste folder zit kan je met `ls` de python bestanden zien.

Er is ook een manier om dit knopje toe te voegen aan Finder. Zie https://stugon.com/open-terminal-in-current-folder-location-mac/.
![](https://i.imgur.com/lfdZ1nd.png)

### Packages installeren
De python progamma's gebruiken een paar python libraries. In de bermuda folder zit een lijst met nodige libraries in het bestand `requirements.txt`.  Je kan alle libraries tegelijk installeren via `pip3 install -r requirements.txt`.

![](https://i.imgur.com/fpxwMJb.png)

### Progamma's uitvoeren.

Je kan nu de progamma's uitvoeren via `python3 <bestandsnaam.py>`.
Er zijn nu 3 progamma's, `cli.py` (SHIP-OS), `radar.py` en `compass.py`.

Dus om de compass te starten moet je `python3 compass.py` uitvoeren.
