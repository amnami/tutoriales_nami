import pygame, sys
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((800,800))
pygame.display.set_caption("Tutorial Seis ")

Mi_imagen=pygame.image.load("Imagenes/kitsune.png")
posX,posY= 130,70

"""
posX=130
posY=70
"""
ventana.blit(Mi_imagen,(posX,posY))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:            
            pygame.quit()
            sys.exit()
    pygame.display.update()