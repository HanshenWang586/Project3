#How to simulate animation

#required 
import pygame
import random
import os
pygame.init();

WIDTH = 800
HEIGHT = 800

clock = pygame.time.Clock()


#position vars
x_pos = 0
y_pos = 200
bg_x = 0
bg_y = -200
poop_x = random.randrange(0, WIDTH) 
poop_y = random.randrange(200, HEIGHT) 
print(poop_x)
print(poop_y)

musher = pygame.sprite.Sprite()
musher.image = pygame.image.load(os.path.join('images', 'musher.bmp'))
musher.rect = musher.image.get_rect()
musher.rect.move_ip(10,10)

poop = pygame.sprite.Sprite()
poop.image = pygame.image.load(os.path.join('images', 'poop.bmp'))
poop.rect = poop.image.get_rect()
poop.rect.move_ip(10,10)


#create a surface
gameDisplay = pygame.display.set_mode((800,600)) #initialize with a tuple

#lets add a title, aka "caption"
pygame.display.set_caption("Sprites!")

pygame.display.update()		#only updates portion specified

bg = pygame.image.load(os.path.join('images', 'background.bmp'))
musher = pygame.image.load(os.path.join('images', 'musher.bmp'))
poop = pygame.image.load(os.path.join('images', 'poop.bmp'))


gameExit = False
while not gameExit:
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

	if pygame.sprite.collide_rect(musher, poop):
		print("COLLISION!!!")

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