# Serena, Claire, Vanessa, Aditi
# 10/15/22
# CoFi Sym - Technica 2022

import pygame, random;
from pygame.locals import *

pygame.init()

# variables
x = 600
y = 300
money = 5000
weekCount = 1
health = 10
hunger = 10

window = 1
mouseX, mouseY = pygame.mouse.get_pos()

HEIGHT = 750
WIDTH = 1200

PERSON_HEIGHT = 100
PERSON_WIDTH = 50

PAYCHECK = 300

# making window 1
pygame.init()
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cofi Sim")

#making first background
def drawBackground1():
    DISPLAY.fill((45, 20, 30))

    #drawing objectives window
    pygame.draw.rect(DISPLAY, "white", (0, 0, 200, HEIGHT))

    #drawing status display case
    pygame.draw.rect(DISPLAY, "white", (0, HEIGHT - 50, WIDTH, 50))

    #drawing bed
    pygame.draw.rect(DISPLAY, "green", (200, 0, 300, 450))

    #drawing desk
    pygame.draw.rect(DISPLAY, "red", (600, 0, 350, 200))

    #drawing chair
    pygame.draw.rect(DISPLAY, "blue", (725, 200, 100, 100))

    #drawing fridge
    pygame.draw.rect(DISPLAY, "yellow", (200, 500, 200, 200))

    #drawing door
    pygame.draw.rect(DISPLAY, "purple", (WIDTH - 25, HEIGHT - 300, 25,  200))

    #drawing bookshelf
    pygame.draw.rect(DISPLAY, "orange", (WIDTH - 200, 0, 200, 100))

#making second background
def drawBackground2():
    DISPLAY.fill((45, 20, 30))

    #drawing objectives window
    pygame.draw.rect(DISPLAY, "white", (0, 0, 200, HEIGHT))

    #drawing status display case
    pygame.draw.rect(DISPLAY, "white", (0, HEIGHT - 50, WIDTH, 50))

    #drawing computer screen
    pygame.draw.rect(DISPLAY, "black", (200, 0, WIDTH - 200, HEIGHT - 25))
    pygame.draw.rect(DISPLAY, "grey", (300, 100, WIDTH - 400, HEIGHT - 225))

#making person
def drawPerson(x, y):
    pygame.draw.rect(DISPLAY, (14, 50, 107), (x, y, PERSON_WIDTH, PERSON_HEIGHT))

while True: # main game loop
    if(window == 1):
        drawBackground1()
        drawPerson(x, y)
    elif(window == 2):
        drawBackground2()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                print(x, y)
                if (y < 200 and x > 100) or (y > 200 and y < 400 and x > 500) or (y > 400 and x > 400):
                    x -= 50
            elif event.key == K_RIGHT:
                x += 50
            elif event.key == K_UP:
                y -= 50
            elif event.key == K_DOWN:
                y += 50
            elif event.key == K_e:
                if(y == 200 and (x > 600 and x < 950) and window == 1):
                    window = 2
            elif event.key == K_ESCAPE and window == 2:
                window = 1
    pygame.display.update()

