#How to simulate animation

#required 
import pygame
import random
import os
pygame.init();

WIDTH = 800
HEIGHT = 800
#create colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#position vars
x_pos = 0
y_pos = 200
bg_x = 0
bg_y = -200
poop_x = random.randrange(0, WIDTH) 
poop_y = random.randrange(200, HEIGHT) 
print(poop_x)
print(poop_y)


#create a surface
gameDisplay = pygame.display.set_mode((800,600)) #initialize with a tuple

#lets add a title, aka "caption"
pygame.display.set_caption("Movement!")

def redraw():
	gameDisplay.fill(white)

pygame.display.update()		#only updates portion specified

bg = pygame.image.load(os.path.join('images', 'background.bmp'))
musher = pygame.image.load(os.path.join('images', 'musher.bmp'))
poop = pygame.image.load(os.path.join('images', 'poop.bmp'))


gameExit = False
while not gameExit:
	redraw()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
			x_pos -= 10
		if event.key == pygame.K_RIGHT:
			x_pos += 10
		if event.key == pygame.K_UP:
			y_pos -= 10
		if event.key == pygame.K_DOWN:
			y_pos += 10
	
	gameDisplay.blit(bg, (bg_x, bg_y))
	gameDisplay.blit(musher, (x_pos,y_pos))
	gameDisplay.blit(poop, (poop_x,poop_y))

	if x_pos>=WIDTH:
		poop_x = random.randrange(0, WIDTH) 
		poop_y = random.randrange(200, HEIGHT) 
		x_pos = 0
		if bg_x == 0:
			bg_x -=200
		else:
			bg_x = 0
	pygame.display.update()		




#required
pygame.quit()
quit()				#exits python