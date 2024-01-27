import pygame
from pygame.locals import *
from pygame.image import *
from pygame.transform import *

#imports and declarations:
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)



pygame.init()
#Check here to figure out how to fullscreen
w, h = 1000, 800
screen = pygame.display.set_mode((w, h))


center = w//2, h//2


pygame.display.set_caption("HackedMapper")



#------------------------------------
#map init
map = pygame.image.load('WorldMap.jpg')
map.convert()

rect1 = map.get_rect()
angle=0

map = pygame.transform.rotozoom(map, angle, 0.5)
rect1.center = w//2, h//2
rect1 = map.get_rect()
rect1.center = w//2, 550

#------------------------------------
#picture init
img = pygame.image.load('picture/Cityscape.jpeg')
img.convert()
rect2 = img.get_rect()
angle=0

img = pygame.transform.rotozoom(img, angle, 1.5)
rect2.center = w//2, h//2
rect2 = img.get_rect()
rect2.center = w//2,150


#Start display
screen.fill(GRAY)
screen.blit(map, rect1)
screen.blit(img, rect2)
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

pygame.quit()