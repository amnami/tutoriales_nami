import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((800,800))
pygame.display.set_caption("Tutorial Siete ")

Mi_imagen=pygame.image.load("Imagenes/kitsune.png")
posX=randint