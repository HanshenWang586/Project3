# Project4
# By Hanshen Wang, 11/18/2016

import pygame, sys
from pygame.locals import *
import random

pygame.init()
crashed = False
windowSurface = pygame.display.set_mode((900, 600))
pygame.display.set_caption('game')

brown=(190,128,0)
black=(0,0,0)
green=(0,128,10)
blue=(0,102,204)
white=(255,255,255)
red=(255,0,10)
maize = (204,204,102)
pink = (255,102,204)



while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True

	pygame.draw.line(windowSurface, maize, (150, 800),(400,0),5)
	pygame.draw.line(windowSurface, blue, (450, 800),(450,0),5)
	pygame.draw.line(windowSurface, pink, (750, 800),(500,0),5)
	pygame.draw.line(windowSurface, red, (0, 520),(900,520),3)
	pygame.display.update()

pygame.quit()
quit()


