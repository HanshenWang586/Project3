import pygame, random
pygame.init()

screen = pygame.display.set_mode((640, 480))

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

class Circle1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(0)
        pygame.draw.circle(self.image, maize, (25, 25), 25, 0)
        self.rect = self.image.get_rect()
        self.velocity = 0

    def update(self):
        x = 150
        y = 0 + self.velocity
        self.velocity += 5
        self.rect.center = (x,y)


class Circle2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(0)
        pygame.draw.circle(self.image, blue, (25, 25), 25, 0)
        self.rect = self.image.get_rect()
        self.velocity = 0

    def update(self):
        x = 320
        y = 0 + self.velocity
        self.velocity += 5
        self.rect.center = (x,y)
        if(y>480):
            self.kill()


class Circle3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(0)
        pygame.draw.circle(self.image, lightred, (25, 25), 25, 0)
        self.rect = self.image.get_rect()
        self.velocity = 0

    def update(self):
        x = 490
        y = 0 + self.velocity
        self.velocity += 5
        self.rect.center = (x,y)

def main():
    pygame.display.set_caption("move the circle with the mouse")
    
    background = pygame.Surface(screen.get_size())
    background.fill(0)
    screen.blit(background, (0, 0))
    
    circle1 = Circle1()
    pygame.time.delay(100)
    circle2 = Circle2()
    circle3 = Circle3()
    allSprites = pygame.sprite.Group(circle1,circle2,circle3)
    
    #hide mouse
    pygame.mouse.set_visible(True)
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        pygame.draw.line(screen, maize, (150, 480),(150,0),5)
        pygame.draw.line(screen, blue, (320, 480),(320,0),5)
        pygame.draw.line(screen, pink, (490, 480),(490,0),5)
        pygame.draw.line(screen, red, (0, 450),(640,450),3)
        pygame.draw.line(screen, green, (0, 370),(640,370),3)
        
        allSprites.clear(screen, background)
        allSprites.update()
        # allSprites.draw(screen)
        
        pygame.display.flip()
        
    #return mouse
    pygame.mouse.set_visible(True)
    
if __name__ == "__main__":
    main()