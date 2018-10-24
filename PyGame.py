import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 600))

surf = pygame.Surface((50, 50))
surf.fill((255, 255, 255))
rect = surf.get_rect()

gameOn = True

while gameOn:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                gameOn = False
        elif event.type == QUIT:
            gameOn = True
    
    