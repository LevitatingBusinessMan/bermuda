#!/usr/bin/python
import pygame,math

pygame.init()
pygame.display.set_caption('Bermuda radar')

green = (0,255,0)

size = [800,600]
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

current_scan_pos = -90 # in degrees

dots = [] # a list of dots, a dot is a tuple like: (x,y,size,timestamp)

def draw():

		# draw tail
		trail_length = 200 #in degrees
		line_multiplier = 1 #lines per degree
		thickness = 6
		max_green = 100 #where 255 makes it just as bright as the initial line

		for i in range(trail_length * line_multiplier):
			pos = current_scan_pos
			x = math.cos(math.radians(pos-(i/line_multiplier))) * 250 + 400
			y = math.sin(math.radians(pos-(i/line_multiplier))) * 250 + 300

			pygame.draw.line(screen,(0,(1-i/(trail_length * line_multiplier))*max_green,0),[400,300],[x,y],thickness)

		#draw line
		x = math.cos(math.radians(current_scan_pos)) * 250 + 400
		y = math.sin(math.radians(current_scan_pos)) * 250 + 300

		#pygame.draw.aaline(screen,green,[400,300],[x,y],3)
		pygame.draw.line(screen,green,[400,300],[x,y],3)

		# draw circle
		pygame.draw.circle(screen,green,[400,300],250, 3)

#Main loop
while True:

	screen.fill((0,0,0))

	draw()

	pygame.display.update()

	current_scan_pos += 0.5

	clock.tick(60)
	
