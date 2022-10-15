# Serena, Claire, Vanessa, Aditi
# 10/15/22
# CoFi Sym - Technica 2022

import pygame;
from pygame.locals import *

pygame.init()

# variables
x = 400
y = 50
money = 5000
weekCount = 1
window = 1
mouseX, mouseY = pygame.mouse.get_pos()

HEIGHT = 750
WIDTH = 1200

PERSON_HEIGHT = 100
PERSON_WIDTH = 50

# making window
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
    DISPLAY.fill(("white"))

#making person
def drawingPerson(x, y):
    pygame.draw.rect(DISPLAY, (14, 50, 107), (x, y, PERSON_WIDTH, PERSON_HEIGHT))

while True: # main game loop
    if(window == 1):
        drawBackground1()
        drawingPerson(x, y)
    elif(window == 2):
        drawBackground2()

    print(mouseX, mouseY)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT and x > 200:
                x -= 50
            elif event.key == K_RIGHT and x < WIDTH - PERSON_WIDTH:
                x += 50
            elif event.key == K_UP and y > 0:
                y -= 50
            elif event.key == K_DOWN:
                y += 50
            elif event.key == K_e:
                print("e")
                if(y == 200 and (x > 600 and x < 950)):
                    print("desk")
                    window = 2
            
    pygame.display.update()

