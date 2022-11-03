# Space Invader in Pyhton (good luck to myself)
#test of comments
import pygame

#Initialize pygame
pygame.init()

#Create game screen : ! 2 brackets because 2 variables (tuple) !
screen = pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

#Player and its position
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x,y) :
    screen.blit (playerImg, (x,y))

#Game Loop 
running = True

while running:

    #Screen color : RGB - Red, Green, Blue,
    screen.fill((0, 25, 51))

#Allowing to close screen window
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
        
        #if keystroke is pressed check wether its ight or left
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            
    
#Adding player image + movement
    playerX += playerX_change

#Adding bounderies
    if playerX <=0:
        playerX = 0
    elif playerX >=736:
        playerX = 736

    player(playerX,playerY)

    pygame.display.update()

