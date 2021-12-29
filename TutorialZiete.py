import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((800,800))
pygame.display.set_caption("Tutorial Siete")

Mi_imagen=pygame.image.load("Imagenes/pikachu.gif")
posX=randint(10,400)
posY= randint(10,200)

ventana.blit(Mi_imagen,(posX,posY))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:            
            pygame.quit()
            sys.exit()
    pygame.display.update()