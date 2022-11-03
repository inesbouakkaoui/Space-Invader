# Space Invader in Pyhton (good luck to myself)
#test of comments
import pygame
import random

#Initialize pygame
pygame.init()

#Create game screen : ! 2 brackets because 2 variables (tuple) !
screen = pygame.display.set_mode((800,600))

#Background
background = pygame.image.load('background.jpg')

#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

#Player and its position
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

#Enemy and its position
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 40

def player(x,y) :
    screen.blit (playerImg, (x,y))
     
def enemy(x,y) :
    screen.blit (enemyImg, (x,y))

#Game Loop 
running = True

while running:

    #Screen color : RGB - Red, Green, Blue,
    screen.fill((0, 25, 51))

    #Include background in loop
    screen.blit(background, (0, 0))

#Allowing to close screen window
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
        
        #if keystroke is pressed check wether its right or left
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            
    
#Adding player movement
    playerX += playerX_change

#Enemy movement
    enemyX += enemyX_change

#Adding bounderies for player
    if playerX <=0:
        playerX = 0
    elif playerX >=736:
        playerX = 736

#Adding bounderies and variations for enemy movement
    if enemyX <=0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >=736:
        enemyX_change = -0.3
        enemyY += enemyY_change

    player(playerX,playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
