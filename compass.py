#!/usr/bin/python
import pygame
import math
import io
from random import random

# receive heading and step speed, 0 is direct

pygame.init()
pygame.display.set_caption('Bermuda compass')

size = [800,600]
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

# cat compass.svg | sed s/#333333/#00ff00/ | sed s/#ffffff/#000000/ > compass_green.svg
svgfile = open("compass_green.svg", "r")
svg = svgfile.read()
compass = pygame.image.load(io.BytesIO(svg.encode()))

bearing = 0
target_bearing = 0
rotate_speed = 1
MAX_NATURAL_DEVIATION=3
NATURAL_DEVIATION_STEP=1

def draw():
	screen.fill((0,0,0))
	rotated_compass = pygame.transform.rotate(compass, bearing)
	screen.blit(rotated_compass, rotated_compass.get_rect(center=(size[0]/2,size[1]/2)))
	pygame.display.flip()

frames_since_natural_rotate=0
FRAMES_TILL_NATURAL_ROTATE=60

while True:
	clock.tick(60)
	draw()
	if frames_since_natural_rotate >= FRAMES_TILL_NATURAL_ROTATE:
		if round(random()):
			bearing += NATURAL_DEVIATION_STEP
		else:
			bearing -= NATURAL_DEVIATION_STEP
		frames_since_natural_rotate = 0
	else:
		frames_since_natural_rotate += 1
