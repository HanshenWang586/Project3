# Project4
# By Hanshen Wang, 11/18/2016

import pygame, sys
from pygame.locals import *
import random
import os
from pygame.locals import Rect, DOUBLEBUF, QUIT, K_ESCAPE, KEYDOWN, K_DOWN, \
    K_LEFT, K_UP, K_RIGHT, KEYUP, K_LCTRL, K_RETURN, FULLSCREEN

pygame.init()

XMax = 900
YMax = 600
crashed = False


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
# pygame.mixer.music.load(os.path.join("data","music.ogg"))

c1PosX = 500
c2PosX = 450
c3PosX = 400 
c1PosY = 0
c2PosY = 0
c3PosY = 0 
everything = pygame.sprite.Group()


class Drum1(pygame.sprite.Sprite):
	def __init__(self, c1Posx, c1PosY):
		super(Drum1, self).__init__()
		self.image = pygame.Surface((2, 2))
		self.rect = self.image.get_rect()
		pygame.draw.circle(self.image, lightred,(0,0),30)
		self.rect.center = (c1Posx, c1PosY)
		self.velocity = 1
		self.size = 1
		self.colour = lightred

	def accelerate(self):
		self.image = pygame.Surface((1, self.size))
		self.velocity += 1

	def update(self):

		c1Posx, c1PosY = self.rect.center
		c1PosX += self.velocity
		c1PosY -= int(self.velocity * 3)
		self.rect.center = c1Posx, c1PosY
		if c1PosY <= 0:
			self.kill()




while pygame.mixer.music.get_busy():
	time.Clock.tick(10)


def main():

	c1PosX = 500
	c2PosX = 450
	c3PosX = 400 
	c1PosY = 0
	c2PosY = 0
	c3PosY = 0 

	windowSurface = pygame.display.set_mode((XMax, YMax))
	pygame.display.set_caption('game')
	clock = pygame.time.Clock()
	empty = pygame.Surface((XMax, YMax))
	clock = pygame.time.Clock()
	drums = Drum1(100,100)
	crashed = False
	while (not crashed):
		windowSurface.fill(black)                              
		pygame.draw.line(windowSurface, maize, (150, 800),(400,0),5)
		pygame.draw.line(windowSurface, blue, (450, 800),(450,0),5)
		pygame.draw.line(windowSurface, pink, (750, 800),(500,0),5)
		pygame.draw.line(windowSurface, red, (0, 520),(900,520),3)
		pygame.draw.line(windowSurface, green, (0, 500),(900,500),3)
		drums.update()
		drums.accelerate()
		
		# c2 = pygame.draw.circle(windowSurface, mark,(c2PosX,c2PosY),30)
		# c3 = pygame.draw.circle(windowSurface, yellow,(c3PosX,c3PosY),30)
		# speed+= 0.01
		# c1PosX += int(velocity)
		# c2PosX += speed
		# c3PosX -= int(speed)

		# c1PosY += int(veloctiy * 3)
		# c2PosY += int(speed * 3)
		# c3PosY += int(speed * 3)
		# i -= 1
		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed = True
		if(c1PosY>520):
			c1PosX = 500
			c1PosY = 0
			continue

	pygame.time.wait(1000)

	while (True):
		clock.tick(30)
		screen = pygame.display.set_mode((XMax, YMax), DOUBLEBUF)
		windowSurface.fill(black)   
		everything.clear(screen, empty)
		everything.update()
		everything.draw(screen)
		pygame.display.flip()                           
		# c2 = pygame.draw.circle(windowSurface, mark,(c2PosX,c2PosY),30)
		# # speed+= 0.01

		# c2PosY += int(speed * 3)
		# # i -= 1
		# pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed = True
		if(c2PosY>520):
			c2PosX = 500
			c2PosY = 0
			continue
	
if __name__ == '__main__':
	main()

