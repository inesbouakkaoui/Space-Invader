# Space Invader in Pyhton (good luck à moi-même)
#test of comments
import pygame

#Initialize pygame
pygame.init()

#Create game screen : ! 2 brackets because 2 variables (tuple) !
screen = pygame.display.set_mode((800,600))

#Game Loop + Allowing to close screen window
running = True

while running:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
