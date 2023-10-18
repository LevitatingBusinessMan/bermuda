#!/usr/bin/python
import pygame,math
import os
import sys

# Show mother ship
# with name, NSE
# add lines

pygame.init()
pygame.display.set_caption('Bermuda radar')

green = (0,255,0)

size = [1280,1024]
radar_radius = 400
if "fullscreen" in sys.argv:
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

current_scan_pos = -90 # in degrees

dots = [] # a list of dots, a dot is a tuple like: (x,y,size,timestamp)

trail_length = 250 #in degrees
line_multiplier = 1 #lines per degree
thickness = 9
max_green = 100 #where 255 makes it just as bright as the initial line

#precalculated data for performance
line_data = []
for i in range(360):
	x = math.cos(math.radians(i)) * radar_radius + size[0]/2
	y = math.sin(math.radians(i)) * radar_radius + size[1]/2
	line_data.append([x,y])

def draw():

		# draw tail
		for i in range(trail_length * line_multiplier):
			pos = current_scan_pos
			#x = math.cos(math.radians(pos-(i/line_multiplier))) * radar_radius + size[0]/2
			#y = math.sin(math.radians(pos-(i/line_multiplier))) * radar_radius + size[1]/2
			x, y = line_data[math.floor(pos-(i/line_multiplier))]

			pygame.draw.line(screen,(0,(1-i/(trail_length * line_multiplier))*max_green,0),[size[0]/2,size[1]/2],[x,y],thickness)

		#draw line
		x = math.cos(math.radians(current_scan_pos)) * radar_radius + size[0]/2
		y = math.sin(math.radians(current_scan_pos)) * radar_radius + size[1]/2

		#pygame.draw.aaline(screen,green,[size[0]/2,size[1]/2],[x,y],3)
		pygame.draw.line(screen,green,[size[0]/2,size[1]/2],[x,y],3)

		# draw circle
		pygame.draw.circle(screen,green,[size[0]/2,size[1]/2],radar_radius, 3)

		# draw range circles
		i = 0
		while i < radar_radius:
			i += (radar_radius/4)
			pygame.draw.circle(screen,green,[size[0]/2,size[1]/2],i, 1)

		# draw directional lines
		pygame.draw.line(screen, green, [size[0]/2,(size[1]/2) + radar_radius], [size[0]/2,(size[1]/2) - radar_radius])
		pygame.draw.line(screen, green, [(size[0]/2) - radar_radius, size[1]/2], [(size[0]/2) + radar_radius,size[1]/2])

#Main loop
while True:

	screen.fill((0,0,0))

	draw()

	pygame.display.update()

	current_scan_pos += 0.5

	if current_scan_pos == 360:
		current_scan_pos = 0

	clock.tick(60)
	
