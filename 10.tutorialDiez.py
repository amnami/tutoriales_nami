import pygame
import sys
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tutorial Diez")

Mi_imagen = pygame.image.load("Imagenes/totoro_izquierda.png")
posX = 200
posy = 100

velocidad = 5
blanco = (255, 255, 255)
derecha = True

while True:
    ventana.fill(blanco)
    ventana.blit(Mi_imagen, (posX, posy))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                Mi_imagen = pygame.image.load(
                    "Imagenes/totoro_izquierda.png")
                posX -= velocidad
            elif event.key == K_RIGHT:
                Mi_imagen = pygame.image.load("Imagenes/totoro_derecha.png")
                posX += velocidad
        elif event.type == pygame.KEYUP:
            if event.key == K_LEFT:
                print("Tecla Izquierda Liberada")
            elif event.key == K_RIGHT:
                print("Tecla Derecha Liberada")

    posX, posY = pygame.mouse.get_pos()
    posX = posY - 100
    posX = posY - 50
    pygame.display.update()
