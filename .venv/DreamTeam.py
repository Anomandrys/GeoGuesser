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
map = pygame.image.load('world-map-png-35416.png')

rect1 = map.get_rect()
angle=0

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

#------------------------------------
#score init
score = pygame.image.load('picture/New Piskel.png')
score.convert()
rect3 = score.get_rect()
angle=0

score = pygame.transform.rotozoom(score, angle, 6)
rect3.center = w//2, h//2
rect3 = img.get_rect()
rect3.center = w//3, 150

#------------------------------------
#Start display
screen.fill(GRAY)

bd = pygame.image.load('texture-1668079_1920.jpg')

screen.blit(bd, (0,0))
screen.blit(map, rect1)
screen.blit(img, rect2)
screen.blit(score, rect3)
pygame.display.update()


running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

        pos = pygame.mouse.get_pos()

        #if event.type == pygame.MOUSEBUTTONDOWN:
        if pos[0] >= 130 and pos[0] <= 870 and pos[1] >= 130 and pos[1] <= 780:
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("click")

pygame.quit()