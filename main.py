import pygame
from pygame.locals import *

pygame.init()

screentest = pygame.display.set_mode((640, 480))
Booleen = True
while Booleen:
    for event in pygame.event.get():
        if event.type == QUIT:
            Booleen = False
pygame.quit()
