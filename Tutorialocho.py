import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()
ventana=pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tutorial Ocho")

Mi_imagen=pygame.image.load("Imagenes/pikachu.gif")
posX=200
posy=100

velocidad=0.5
blanco=(255,255,255)
derecha=True

while True:
    ventana.fill(blanco)
    ventana.blit(Mi_imagen, (posX, posy))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    if derecha==True:
        if posX < 400:
            posX+=velocidad
        else:
            derecha=False
    else:
        if posX > 1:
            posX-=velocidad
        else:
            derecha=True

    pygame.display.update()
