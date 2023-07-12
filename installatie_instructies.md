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

Om de radar of compass in fullscreen te openen voeg je `fullscreen` toe aan het commando, bijvoorbeeld `python3 radar.py fullscreen`.

# Automatiseren van de progamma's op een raspberry pi
Als je in de homefolder (`/home/pi`) het `git clone` command uitvoert, komen de bestanden te staan in `/home/pi/bermuda`.

Installeer ook de `python3-sdl2` en `unclutter` packages: `sudo apt install python3-sdl2 unclutter`.

#### Via LXDE
Dit is de makkelijkste manier.

In het bestand `/etc/xdg/lxsession/LXDE-pi/autostart` kan je progamma's automatisch laten starten als de grafisch omgeving van de Raspberry Pi start.
Je kan het bestand via SSH bewerken met `sudo nano /etc/xdg/lxsession/LXDE-pi/autostart`.
Voeg daar bijvoorbeeld `@python3 /home/pi/bermuda/radar.py` om de radar automatisch te starten.

Zie [hier](https://forums.raspberrypi.com/viewtopic.php?t=294014) meer informatie.

Je kan de commando's die er al staan deactieveren met een `#`, waardoor de grafische omgeving van de pi niet volledig opstart.
Daarnaast kan je `unclutter` gebruiken om de cursor weg te halen.
Voorbeeld configuratie:
```SH
#@lxpanel --profile LXDE-pi
#@pcmanfm --desktop --profile LXDE-pi
#@xscreensaver -no-splash
@python3 /home/pi/bermuda/radar.py fullscreen
@unclutter -idle 0
```

#### Via systemd
Dit is hoe ik pipresents en dergelijken heb geconfigureerd automatisch te starten.

Je moet dan "service" bestanden toevoegen aan de `~/.config/systemd/user` folder voor elk progamma wat je automatisch wilt opstarten.

Ik heb al een aantal van deze bestanden gemaakt, en die zitten bij de rest van de code.
Je kan dan de `.service` bestanden kopieren naar `~/.config/systemd/user`.
Doe dat door `cp *.service ~/.config/systemd/user` uit te voeren binnen de `/home/pi/bermuda` folder.

Je kan dan bijvoorbeeld de radar starten met `systemctl --user start radar`. En zorgen dat de radar automatisch start met `systemctl --user enable radar`.

