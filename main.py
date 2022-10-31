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

#Game Loop + Allowing to close screen window
running = True

while running:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

    #Screen color : RGB - Red, Green, Blue,
    screen.fill((0, 25, 51))
    pygame.display.update()

