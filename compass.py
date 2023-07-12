#!/usr/bin/python
import pygame
import math
import io
from random import random
import os

from osc4py3.as_eventloop import *
from osc4py3 import oscmethod as osm

OSC_PORT = 3333

bearing = 0
target_bearing = 0
rotate_speed = 18 # degrees per second
MAX_NATURAL_DEVIATION=2
NATURAL_DEVIATION_STEP=1
SECONDS_TILL_NATURAL_DEVIATION=2
natural_deviation = 0

osc_startup()
osc_udp_server("0.0.0.0", OSC_PORT, "compass")

print(f"OSCP server start op port {OSC_PORT}")
print("Pas de richting van de kompas aan via OSCP: /set_compass <richting> <snelheid>")

def set_compass(target, speed):
	print(f"Received set_compass: {target} {speed}")

	global target_bearing
	global rotate_speed
	target_bearing = int(target)
	rotate_speed = int(speed)

osc_method("/set_compass", set_compass)

pygame.init()
pygame.display.set_caption('Bermuda compass')

size = [800,600]
if os.environ.get("FULLSCREEN") == "1":
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

# cat compass.svg | sed s/#333333/#00ff00/ | sed s/#ffffff/#000000/ > compass_green.svg
svgfile = open("compass_green.svg", "r")
svg = svgfile.read()
compass = pygame.image.load(io.BytesIO(svg.encode()))

def draw():
	c_bearing = bearing + natural_deviation
	c_bearing = (360 + c_bearing if c_bearing < 0 else c_bearing) % 360
	
	screen.fill((0,0,0))
	rotated_compass = pygame.transform.rotate(compass, c_bearing).convert_alpha()
	#rotated_compass = pygame.transform.smoothscale(rotated_compass, (int(rotated_compass.get_width()*0.8),int(rotated_compass.get_height()*0.8)))
	#rotated_rect = rotated_compass.get_rect(center=(size[0]/2,size[1]/2))
	screen.blit(rotated_compass, rotated_compass.get_rect(center=(size[0]/2,size[1]/2)))
	#screen.blit(rotated_compass, rotated_rect)

	# Bearing text
	font = pygame.font.SysFont("Arial", 36)
	bearing_text = font.render(str(round(c_bearing)), True, (0,255,0))
	bearing_text_pos = (((screen.get_width() - bearing_text.get_rect().width) // 2),10)
	screen.blit(bearing_text, bearing_text_pos)

	pygame.display.flip()

frames_since_natural_deviation = 0
frames_since_rotation = 0

FPS = 30

while True:
	clock.tick(FPS)
	osc_process()
	draw()
	
	# Rotate to target
	if bearing != target_bearing:
		natural_deviation = 0

		if rotate_speed == 0:
			bearing = target_bearing

		frametime = (1/FPS)
		step = frametime * rotate_speed

		# calculate rotate direction
		diff = bearing - target_bearing
		if diff > 180:
			diff -= 360
		elif diff < -180:
			diff += 360

		#print(f"from {bearing} to {target_bearing}: {diff} (step {step})")

		if diff < 0:
			bearing += step
		else:
			bearing -= step

		if abs(diff) < step:
			bearing = target_bearing
		

	# Natural deviation
	else:
		if frames_since_natural_deviation / FPS >= SECONDS_TILL_NATURAL_DEVIATION:
			if round(random()):
				if abs(natural_deviation + NATURAL_DEVIATION_STEP) <= MAX_NATURAL_DEVIATION:
					natural_deviation += NATURAL_DEVIATION_STEP
			else:
				if abs(natural_deviation - NATURAL_DEVIATION_STEP) <= MAX_NATURAL_DEVIATION:
					natural_deviation -= NATURAL_DEVIATION_STEP	
			frames_since_natural_deviation = 0
			print(f"Current natural deviation: {natural_deviation}")
		else:
			frames_since_natural_deviation += 1
