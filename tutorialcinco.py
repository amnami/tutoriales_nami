import pygame,sys
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Tutorial Cinco")

pygame.draw.circle(ventana, (8, 70, 120,), (80, 90), 20)
pygame.draw.rect(ventana, (130,70,70),(0,0,100,50))
pygame.draw.polygon(ventana,(90,180,70),((80,90),(150,100),(40,80),(60,80)))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()