import pygame
import sys
from typing import Tuple

from osc4py3.as_eventloop import *
from osc4py3 import oscmethod as osm

pygame.init()
pygame.display.set_caption('Ship Information System')

GREEN = (0,255,0)
SIZE = [1280,1024]
FPS = 30
FONT_BIG = 	pygame.font.SysFont("Arial Bold", 130)
FONT_MEDIUM = 	pygame.font.SysFont("Arial Bold", 80)
FONT_SMALL = 	pygame.font.SysFont("Arial Bold", 37)

clock = pygame.time.Clock()

OSC_PORT = 3333
osc_startup()
osc_udp_server("0.0.0.0", OSC_PORT, "compass")

if "fullscreen" in sys.argv:
    screen = pygame.display.set_mode(SIZE, pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode(SIZE)

background = pygame.image.load("sos-labeled-NL.jpg")

class Status:
    def __init__(self):
        self.windrichting = "ZW"
        self.windkracht = 3
        self.snelheid = 11
        self.koers = 0
        self.gewenste_koers = 0
        self.latitude = 101010
        self.longitude = 232323
        self.autopilot = True
        self.foutmelding = "DIT IS EEN FOUTMELDING"
        self.kraan1 = 60
        self.kraan2 = 20
        self.kraan3 = 100

        # Zwart scherm
        self.black = False

status = Status()

def reset():
    global status
    status = Status()
osc_method("/reset", reset)

def black():
    global status
    status.black = True
osc_method("/black", black)

# ping?

#def set_language():
    # todo
#osc_method("/set_language", set_language)

def set_coords(latitude, longitude):
    global status
    status.latitude = latitude
    status.longitude = longitude
osc_method("/set_coordinates", set_coords)

def set_course():
    global status
    status.koers = koers
osc_method("/set_course", set_course)

def set_wanted_course():
    global status
    status.gewenste_koers = gewenste_koers
osc_method("/set_wanted_course", set_wanted_course)

# Dit is een kleine helper class
# om text gecentreerd te plaatsen
class Text:
    def __init__(self, text, loc, size = "big",  color = GREEN):
        [self.x, self.y] = loc
        if size == "big":
            font = FONT_BIG
        elif size == "small":
            font = FONT_SMALL
        else:
            font = FONT_MEDIUM

        if isinstance(text, int):
            text = str(text)

        self.txt = font.render(text, True, color)
        self.size = font.size(text)
    def draw(self, surface):
        x = self.x - (self.size[0] / 2.)
        y = self.y - (self.size[1] / 2.)
        surface.blit(self.txt, (x,y))

# Class voor de kraan levels
class Kraan:
    def __init__(self, percentage, loc):
        [x, y] = loc
        max_height = 470
        width = 80
        height = percentage / 100 * max_height
        self.rect = pygame.Rect(x, y + (max_height - height), width, height)

    def draw(self, surface):
        pygame.draw.rect(surface, GREEN, self.rect)

def draw():
    screen.blit(background, (0,0))
    if status.black:
        return

    # Windrichting
    Text(status.windrichting, (240, 125)).draw(screen)
    match status.windrichting:
        case "N":
            longtxt = "NOORD"
        case "NO":
            longtxt = "NOORD-OOST"
        case "O":
            longtxt = "OOST"
        case "ZO":
            longtxt = "ZUID-OOST"
        case "Z":
            longtxt = "ZUID"
        case "ZW":
            longtxt = "ZUID-WEST"
        case "W":
            longtxt = "WEST"
        case "NW":
            longtxt = "NOORD-WEST"

    Text(longtxt, (240, 184), "small").draw(screen)

    # Windkracht
    Text(status.koers, (440, 125)).draw(screen)

    # Snelheid
    Text(status.snelheid, (640, 125)).draw(screen)

    # Koers
    Text(status.koers, (940, 125)).draw(screen)

    # Gewenste koers
    Text(status.koers, (940, 325)).draw(screen)

    # Latitude
    Text(str(status.latitude).ljust(6, '0'), (960, 505), "medium").draw(screen)

    # Longitude
    Text(str(status.longitude).ljust(6, '0'), (960, 575), "medium").draw(screen)

    # Autopilot
    Text("AAN" if status.autopilot else "UIT", (945, 735)).draw(screen)

    # Foutmelding
    Text(status.foutmelding, (650, 940), "medium").draw(screen)

    # Kraan1
    Kraan(status.kraan1, (200,267)).draw(screen)
    Text(f"{status.kraan1} %", (240, 240), "small").draw(screen)

    # Kraan2
    Kraan(status.kraan2, (400,267)).draw(screen)
    Text(f"{status.kraan2} %", (440, 240), "small").draw(screen)

    # Kraan3
    Kraan(status.kraan3, (600,267)).draw(screen)
    Text(f"{status.kraan3} %", (640, 240), "small").draw(screen)


    pygame.display.flip()

while True:
    clock.tick(FPS)
    osc_process()
    draw()
