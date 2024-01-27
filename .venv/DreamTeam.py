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



map = pygame.image.load('WorldMap.jpg')
map.convert()
rect = map.get_rect()
angle=0

#map init
map = pygame.transform.rotozoom(map, angle, 0.4)
rect.center = w//2, h//2
rect = map.get_rect()
rect.center = w//2, 620

#

screen.fill(GRAY)
screen.blit(map, rect)
pygame.draw.rect(screen, RED, rect, 1)
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

pygame.quit()