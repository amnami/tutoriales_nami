import pygame, sys
from pygame.locals import *

Color=(255,140,60)
ColorDos=pygame.Color(255,120,9)

pygame.init()
ventana = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hola mundo de ana maria")

while True:
   ventana.fill(Color)
   for event in pygame.event.get():
      if event.type == QUIT:
         pygame.quit()
         sys.exit()

   
   pygame.display.update()