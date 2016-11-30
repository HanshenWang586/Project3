# Project4
# By Hanshen Wang, 11/18/2016

import pygame, sys
from pygame.locals import *
import random
import os

pygame.init()

crashed = False
windowSurface = pygame.display.set_mode((900, 600))
pygame.display.set_caption('game')
clock = pygame.time.Clock()


brown=(190,128,0)
black=(0,0,0)
green=(0,128,10)
blue=(0,153,255)
mark=(0,102,204)
white=(255,255,255)
red=(255,0,10)
lightred=(255,0,50)
maize = (204,204,102)
pink = (255,102,204)
yellow=(255,255,0)


# pygame.mixer.init()
# pygame.mixer.music.load("music.ogg")





speed = 1


c1PosX = 500
c2PosX = 450
c3PosX = 400 

c1PosY = 0
c2PosY = 0
c3PosY = 0 






while pygame.mixer.music.get_busy():
	time.Clock.tick(10)

while not crashed:

	windowSurface.fill(black)                              # erase the entire display surface
	pygame.draw.line(windowSurface, maize, (150, 800),(400,0),5)
	pygame.draw.line(windowSurface, blue, (450, 800),(450,0),5)
	pygame.draw.line(windowSurface, pink, (750, 800),(500,0),5)
	pygame.draw.line(windowSurface, red, (0, 520),(900,520),3)
	pygame.draw.line(windowSurface, green, (0, 500),(900,500),3)

	c1 = pygame.draw.circle(windowSurface, lightred,(c1PosX,c1PosY),30)
	c2 = pygame.draw.circle(windowSurface, mark,(c2PosX,c2PosY),30)
	c3 = pygame.draw.circle(windowSurface, yellow,(c3PosX,c3PosY),30)
	# speed+= 0.01
	c1PosX += int(speed)
	# c2PosX += speed
	c3PosX -= int(speed)

	c1PosY += int(speed * 3)
	c2PosY += int(speed * 3)
	c3PosY += int(speed * 3)
	
	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True

pygame.quit()
quit()


