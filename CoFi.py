# Serena, Claire, Vanessa, Aditi
# 10/15/22
# CoFi Sym - Technica 2022

import pygame, random, time;
from pygame.locals import *

pygame.init()

# variables
x = 600
y = 300
money = 5000
weekCount = 1
wage = 15
tutorial = True

#status variables
health = 10
hunger = 10
energy = 10
grades = 5

#text variables
statusFont = pygame.font.Font('freesansbold.ttf', 15)
bigStatus = pygame.font.Font('freesansbold.ttf', 30)

#window varibles
window = 1
advice = 0

HEIGHT = 750
WIDTH = 1200

PERSON_HEIGHT = 100
PERSON_WIDTH = 50

# making window 1
pygame.init()
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cofi Sim")

def drawScreen():
    #drawing objectives window
    pygame.draw.rect(DISPLAY, "white", (0, 0, 200, HEIGHT))

    #drawing status display case
    pygame.draw.rect(DISPLAY, "white", (0, HEIGHT - 50, WIDTH, 50))

    #drawing screen (ref: 674 x 432)
    screenImg = pygame.image.load('assets/screen2.png').convert()
    DISPLAY.blit(screenImg, (200, 0))

#making first background
def drawBackground1():
    DISPLAY.fill((45, 20, 30))

    #drawing objectives window
    pygame.draw.rect(DISPLAY, "white", (0, 0, 200, HEIGHT))

    #drawing status display case
    pygame.draw.rect(DISPLAY, "white", (0, HEIGHT - 50, WIDTH, 50))

    #drawing bed
    pygame.draw.rect(DISPLAY, "green", (200, 0, 300, 450))
    bedImg = pygame.image.load('assets/bed.png').convert()
    DISPLAY.blit(bedImg, (200, 0))

    #drawing desk
    pygame.draw.rect(DISPLAY, (45, 20, 30), (600, 0, 350, 200))
    deskImg = pygame.image.load('assets/final-desk.png').convert()
    DISPLAY.blit(deskImg, (600, 0))

    #drawing chair
    pygame.draw.rect(DISPLAY, (45, 20, 30), (725, 200, 100, 100))
    chairImg = pygame.image.load('assets/chair.png')
    DISPLAY.blit(chairImg, (725, 175))

    #drawing fridge
    pygame.draw.rect(DISPLAY, (45, 20, 30), (200, 500, 200, 200))
    fridgeImg = pygame.image.load('assets/fridge.png')
    DISPLAY.blit(fridgeImg, (200, 500))

    #drawing door
    pygame.draw.rect(DISPLAY, (45, 20, 30), (WIDTH - 25, HEIGHT - 300, 25,  200))

    #drawing bookshelf
    pygame.draw.rect(DISPLAY, (45, 20, 30), (WIDTH - 200, 0, 200, 100))
    bookshelfImg = pygame.image.load('assets/bookshelf.png').convert()
    DISPLAY.blit(bookshelfImg, (WIDTH - 200, 0))

    #drawing door
    pygame.draw.rect(DISPLAY, (143, 86, 59), (WIDTH - 25, HEIGHT - 300, 25,  200))

#making second background
def drawBackground2():
    DISPLAY.fill((45, 20, 30))

    #creating a font object
    font = pygame.font.Font('fonts/Lato-Bold.ttf', 15)

    drawScreen()

    #drawing bill app (apps are separated by 20 px)
    billsAppImg = pygame.image.load('assets/billsApp.png').convert()
    DISPLAY.blit(billsAppImg, (383, 174))

    #implementing "Bills" text under bill app
    billText = font.render('Bills', True, "white")
    billRect = billText.get_rect()
    billRect.center = (418, 259)
    DISPLAY.blit(billText, billRect)
    
    #drawing insurance app (apps are separated by 20 px)
    insuranceAppImg = pygame.image.load('assets/insuranceApp.png').convert()
    DISPLAY.blit(insuranceAppImg, (473, 174))

    #implementing "Insurance" text under bill app
    billText = font.render('Insurance', True, "white")
    billRect = billText.get_rect()
    billRect.center = (508, 259)
    DISPLAY.blit(billText, billRect)

    #drawing stocks app (apps are separated by 20 px)
    stocksAppImg = pygame.image.load('assets/stocksApp.png').convert()
    DISPLAY.blit(stocksAppImg, (563, 174))

    #implementing "Stocks" text under bill app
    billText = font.render('Stocks', True, "white")
    billRect = billText.get_rect()
    billRect.center = (598, 259)
    DISPLAY.blit(billText, billRect)

#draw square
def squareStat(x, y, stat, color):
    for i in range (stat):
        pygame.draw.rect(DISPLAY, color, (x + i * (25),  y,  25,  25))

#drawing labels
def write(x, y, words, color):
    text = statusFont.render(words, True, color)
    textRect = text.get_rect()
    textRect.center = (x, y)
    DISPLAY.blit(text, textRect)

def drawBackground3():
    DISPLAY.fill((0, 0, 0))
    drawScreen()

def drawBackground4():
    DISPLAY.fill((0, 0, 0))
    drawScreen()

def drawBackground5():
    DISPLAY.fill((0, 0, 0))
    drawScreen()
    
# fade to black, waits 2 seconds, fade back in
def sleep():
    fade = pygame.Surface((1200, 750))
    fade.fill((0,0,0))
    for alpha in range(300):
        fade.set_alpha(alpha)
        drawBackground1()
        drawPerson(300, 50)
        drawBlanket()
        DISPLAY.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)
    time.sleep(2)
    for alpha in range(255):
        fade.set_alpha(255 - alpha)
        drawBackground1()
        drawPerson(300, 50)
        drawBlanket()
        DISPLAY.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)
    
#drawing objectives
def drawObjectives():
    font = pygame.font.Font('fonts/Lato-Bold.ttf', 30)

    #Title
    objectivesText = font.render('Objectives', True, "black")
    objectivesRect = objectivesText.get_rect()
    objectivesRect.center = (100, 50)
    DISPLAY.blit(objectivesText, objectivesRect)

    #Task 1 - Study
    font2 = pygame.font.Font('fonts/Lato-Regular.ttf', 15)
    task1Text = font2.render('Study for 8 hours', True, 'black')
    DISPLAY.blit(task1Text, (49, 80))
    checkBox1 = pygame.image.load('assets/checkBox_unchecked.png')
    DISPLAY.blit(checkBox1, (29, 82))

    #Task 2 - Work
    font2 = pygame.font.Font('fonts/Lato-Regular.ttf', 15)
    task1Text = font2.render('Work', True, 'black')
    DISPLAY.blit(task1Text, (49, 110))
    checkBox2 = pygame.image.load('assets/checkBox_unchecked.png')
    DISPLAY.blit(checkBox2, (29, 112))

    #Task 3 - Bills
    font2 = pygame.font.Font('fonts/Lato-Regular.ttf', 15)
    task1Text = font2.render('Pay Bills on Computer', True, 'black')
    DISPLAY.blit(task1Text, (49, 140))
    checkBox3 = pygame.image.load('assets/checkBox_unchecked.png')
    DISPLAY.blit(checkBox3, (29, 142))

#making person
def drawPerson(x, y):
    pygame.draw.rect(DISPLAY, (14, 50, 107), (x, y, PERSON_WIDTH, PERSON_HEIGHT))

#drawing blanket
def drawBlanket():
    pygame.draw.rect(DISPLAY, "purple", (300, 354, 200, 96))
    blanketImg = pygame.image.load('assets/blanket.png')
    DISPLAY.blit(blanketImg, (200, 96))

while True: # main game loop
    if(window == 1):
        drawBackground1()
        drawPerson(x, y)
        drawBlanket()
    elif(window == 2):
        drawBackground2()
    elif (window == 3):
        drawBackground3()
    elif (window == 4):
        drawBackground4()
    elif (window == 5):
        drawBackground5()

    #week label
    text = bigStatus.render("Week " + str(weekCount), True, "black")
    textRect = text.get_rect()
    textRect.center = (100, 50)
    DISPLAY.blit(text, textRect)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            print(x, y)
            if event.key == K_ESCAPE and window == 2:
                    window = 1
            elif event.key == K_ESCAPE and (window > 2 and window < 6):
                    window = 2
            if event.key == K_LEFT:
                if(x ==  WIDTH - 75):
                    x -= 25
                elif(x > 500 and y >= 200) or (x >= 1000) or (x > 400 and y >= 450) or (x == 550) or (y < 100 and x < 550 and x > 325): 
                    x -= 50
            elif event.key == K_RIGHT:
                if(x == WIDTH - 100 and y > HEIGHT - 400 and y < HEIGHT - 100) or (x == WIDTH - 75 and y < 400):
                    x+=25
                elif(y > HEIGHT - 50 and x < WIDTH - 100) or (x == 500) or (y >= 200 and y < HEIGHT - 350 and x < WIDTH - 50) or (x < 550 and x >= 300 and y < 100) or (y >= HEIGHT - 350 and y < HEIGHT - 50 and x < WIDTH-100) or ( x > 900 and y >= 100 and x <=  WIDTH - 100):
                    x += 50
            elif event.key == K_UP:
                if(y > 450) or (y > 200 and x >= 500) or ((x == 950 or x == 500 or x == 550) and y > 0) or (x > 950 and y > 100):
                    y -= 50
            elif event.key == K_DOWN:
                if (x <= WIDTH - 75 and x > 450 and y < HEIGHT - 150) or (x < 450 and y > 400 and y < HEIGHT - 150) or (x == 1150 and y < 350) or (x == 950) :
                    y += 50
            elif event.key == K_e:
                if(y == 200 and (x > 600 and x < 950) and window == 1):
                    window = 2
                    
                #making fridge interactive
                if(x == 400 and (y >= 500) and hunger < 10):
                   hunger += 1
                   money -= 5
                   energy -= 1
                   
                #making bookshelf interactive
                if(x >= 1000 and y == 100 and grades < 5):
                    energy -= 1
                    grades += 1
                    hunger -= 1
                    
                #making job
                if(x == 1125 and y > HEIGHT - 400):
                    energy -= 1
                    grades -= 1
                    hunger -= 1
                    health -= 1
                    money += 5 * wage

            #sleep
            if(x == 300):
                sleep()        
                x = 550
                y = 50
                weekCount += 1

                #randomizing two week situation
                grades -= 1
                energy = 10
                health -= random.randint(1,3)
                hunger -= random.randint(2,5)
                            
        elif (window == 2):
            #
            # CREATING BUTTONS -_-
            #
            if (event.type == pygame.MOUSEBUTTONDOWN):
                mouse = pygame.mouse.get_pos()
                print(str(mouse[0]) + ' ' + str(mouse[1]))
                if (383 <= mouse[0] and 453 >= mouse[0] and 174 <= mouse[1] and 244 >= mouse[1]): 
                    window = 3
                elif (473 <= mouse[0] and 543 >= mouse[0] and 174 <= mouse[1] and 244 >= mouse[1]):
                    window = 4
                elif (563 <= mouse[0] and 633 >= mouse[0] and 174 <= mouse[1] and 244 >= mouse[1]):
                    window = 5
                    
    #making status bars
    squareStat(50, HEIGHT - 37, health, "red")
    squareStat(350, HEIGHT - 37, hunger, "brown")
    squareStat(650, HEIGHT - 37, energy, "green")
    squareStat(950, HEIGHT - 37, grades, "blue")
    pygame.draw.rect(DISPLAY, "black", (1100, HEIGHT - 37, 80, 25))

    #making status names
    write(175, HEIGHT - 25, "health", "white")
    write(475, HEIGHT - 25, "hunger", "white")
    write(775, HEIGHT - 25, "energy", "white")
    write(1015, HEIGHT - 25, "grades", "white")
    write(1140, HEIGHT - 25, "$" + str(money), "white")

    #writing advice
    #1 = health, 2 = hunger,  3 = energy, 4 = grades, 5 = broke
    if(window == 1):
        if(advice == 1):
            write(100, 600, "Your health is slipping,", "black")
            write(100, 625, "health is more important", "black")
            write(100, 650, "than money or school!", "black") 
        elif(advice == 2):
            write(100, 600, "Your body is hungry,", "black")
            write(100, 625, "go eat something.", "black")
            write(100, 650, "Nothing can be more", "black")
            write(100, 675, "important than food", "black")
        elif(advice == 3):
            write(100, 600, "Your body is tired,", "black")
            write(100, 625, "you have to sleep", "black")
            write(100, 650, "Warning: your body will", "black")
            write(100, 675, "shut down soon.", "black")
        elif(advice == 4):
            write(100, 600, "Your grades are falling,", "black")
            write(100, 625, "money is now but", "black")
            write(100, 650, "education is the future!", "black")
        elif(advice == 5):
            write(100, 600, "Watch it, you're", "black")
            write(100, 625, "close to broke", "black")

    #checking if advice is needed
        if(health < 3):
            advice = 1
        elif(hunger < 3):
            advice = 2
        elif(energy < 3):
            advice = 3
        elif(grades < 2):
            advice = 4
        else:
            advice = 0
    
    pygame.display.update()
