import pygame, random, shutil, os
from pygame.locals import *
from pygame.image import *
from pygame.transform import *
import sys
import os

# imports and declarations:
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

TOTAL_ROUND = 10

# Check here to figure out how to fullscreen
w, h = 1000, 800
screen = pygame.display.set_mode((w, h))
center = w // 2, h // 2
pygame.display.set_caption("HackedMapper")
# ------------------------------------
# map init
map = pygame.image.load('world-map-png-35416.png')
rect1 = map.get_rect()
angle = 0
rect1.center = w // 2, h // 2
rect1 = map.get_rect()
rect1.center = w // 2, 550
# ------------------------------------
# picture init
img = pygame.image.load('picture/Cityscape.jpeg')
img.convert()
rect2 = img.get_rect()
angle = 0
img = pygame.transform.rotozoom(img, angle, 1.5)
rect2.center = w // 2, h // 2
rect2 = img.get_rect()
rect2.center = w // 2, 150


# ------------------------------------
# generate image
def generate_image():
    filename = img_list[right_count]
    img = pygame.image.load('picture/' + filename)

    if (right_count > (len(img_list) - 1)):
        filename = img_list[len(img_list) - 1]
    else:
        filename = img_list[right_count]

    dest = 350, 90
    screen.blit(bd, (0, 0))
    screen.blit(map, rect1)
    screen.blit(img, dest)
    pygame.display.update()


# ------------------------------------
# Start display
screen.fill(GRAY)
bd = pygame.image.load('texture-1668079_1920.jpg')
screen.blit(bd, (0, 0))
"""
screen.blit(map, rect1)
screen.blit(img, rect2)
pygame.display.update()
"""

# ----------------------------------------------
# Set up fonts and colors
font_size = 24  # Adjusted font size
font = pygame.font.Font(None, font_size)
text_color = pygame.Color('black')
text_color2 = pygame.Color('white')
input_box_color = pygame.Color('white')
border_color = pygame.Color('black')

# Create the input box
input_box = pygame.Rect(750, 100, 180, 100)
# Message to display
message = "Hello, SAMPLE"

# Create the message box
message_box = pygame.Rect(100, 100, 180, 100)
message_box2 = pygame.Rect(100, 100, 180, 100)  # if answer is correct
# Create the count box
count_box = pygame.Rect(750, 100, 180, 100)

answer_box = pygame.Rect(1000, 100, 180, 100)

intro_box = pygame.Rect(500, 500, 180, 100)

# list of insults
bad_answer = ["just a warm up, right?", 'nuh uh', "third time's a charm?", "is bad luck... or is there a trick?",
              "you really don't get it, do you?", "How you could that possibly go there", "truly extremely far off",
              "try again", "Yep keep guessing", "No way you just said that", "Some review required",
              'care to try again']

# scoreboard:
wrong_count = 0
right_count = 0
total_round_count = 0

# this is the message to be printed
count = "Your score is: " + str(right_count) + "/" + str(total_round_count)

answer = "FLORIDA!"

message2 = "Good!"

current_message = bad_answer[wrong_count % len(bad_answer)]

intro_text = "welcome :)"

correct = True
previously_correct = 0


# Main loop

# noinspection PyStatementEffect
def graphic_refresh():
    # Draw the input box
    if (wrong_count > (len(bad_answer) - 1)):
        message = bad_answer[(len(bad_answer) - 2)]
    else:
        message = bad_answer[wrong_count - 1]
    # pygame.draw.rect(screen, input_box_color, input_box)
    # pygame.draw.rect(screen, border_color, input_box, 2)

    # Render and display the text
    if not correct:
        text_surface = font.render(message, True, text_color)
        screen.blit(text_surface, (message_box.x + 5, input_box.y + 5))

    if correct:
        text_surface = font.render(message2, True, text_color)
        screen.blit(text_surface, (message_box2.x + 5, message_box2.y + 5))

    text_surface = font.render(count, True, text_color)
    screen.blit(text_surface, (count_box.x + 5, count_box.y - 5))

    if not correct:
        text_surface = font.render(answer, True, text_color)
        screen.blit(text_surface, (answer_box.x - 168, answer_box.y + 100))

    pygame.display.flip()


def clear_page(filename):
    screen.blit(bd, (0, 0))
    screen.blit(map, rect1)
    img=pygame.image.load('picture/'+filename)
    screen.blit(img, (350, 90))
    pygame.display.update()


def front_page():
    print("functionning")
    text_surface = font.render(intro_text, True, text_color2)
    screen.blit(text_surface, (intro_box.x, input_box.y))

source_dir = 'picture'
source_list = os.listdir(source_dir)
img_list = random.choices(source_list, k=len(source_list) - 1)
filename = img_list[right_count]


started = 0

while True:

    graphic_refresh()

    for event in pygame.event.get():

        if started == 0:
            front_page()
            if event.type == pygame.MOUSEBUTTONDOWN:
                started += 1

        elif started == 1:
            started += 1
            screen.blit(map, rect1)
            screen.blit(img, rect2)
            pygame.display.update()

            graphic_refresh()

        else:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            print(event)
            if event.type == pygame.QUIT:
                running = False
            pos = pygame.mouse.get_pos()
            if 300 <= pos[0] <= 315 and pos[1] >= 513 and pos[1] <= 530:
                if event.type == pygame.MOUSEBUTTONDOWN:

                    right_count += 1
                    previously_correct += 1
                    total_round_count += 1

                    filename=img_list[right_count]
                    clear_page(filename)

                    count = "Your score is: " + str(right_count) + "/" + str(total_round_count)
                    correct = True

            elif 300 > pos[0] or pos[0] < 315 or pos[1] < 513 or pos[1] > 530:
                if event.type == pygame.MOUSEBUTTONDOWN:

                    print("FLORIDA")

                    filename=img_list[right_count]
                    clear_page(filename)

                    if (wrong_count > (len(bad_answer) - 1)):
                        message = bad_answer[(len(bad_answer) - 2)]
                    else:
                        message = bad_answer[wrong_count]

                    wrong_count += 1
                    total_round_count += 1
                    count = "Your score is: " + str(right_count) + "/" + str(total_round_count)
                    correct = False

            # pygame.draw.rect(screen, input_box_color, input_box)
            # pygame.draw.rect(screen, border_color, input_box, 2)

        # Draw the input box
    if (wrong_count > (len(bad_answer) - 1)):
        message = bad_answer[(len(bad_answer) - 2)]
    else:
        message = bad_answer[wrong_count - 1]
    # pygame.draw.rect(screen, input_box_color, input_box)
    # pygame.draw.rect(screen, border_color, input_box, 2)

    text_surface = font.render(count, True, text_color)
    screen.blit(text_surface, (count_box.x + 5, input_box.y - 5))

    pygame.display.flip()

    if total_round_count == TOTAL_ROUND:
        # final print

        graphic_refresh()

        pygame.time.wait(1000)

        pygame.quit()
        sys.exit()

