import pygame
import sys
import random

rojo = (255, 0, 0)
azul = (0, 0, 255)
amarillo = (255,225,0)
lila = (180, 27, 219)
morado = (200,50,110)



# Metodo random
rojo_aleatorio = random.randint(0, 255)
verde_aleatorio = random.randint(0, 255)
azul_aleatorio = random.randint(0, 255)
color_aleatorio = random.randint (0,255)

pygame.init()

ventana = pygame.display.set_mode((500, 500))

pygame.display.set_caption("El cuadrado que rebota")

clock = pygame.time.Clock()

XX = 300
MOVIMIENTO = 3

YY = 255
MOVIMIENTO_YY = 3

while 1:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(azul)

    XX = XX + MOVIMIENTO

    if XX >= 450:
        XX = 450
        MOVIMIENTO = -3
    elif XX <= 0:
        XX = 0
        MOVIMIENTO = 3
    
    YY = YY + MOVIMIENTO

    if YY >= 450:
        YY = 450
        MOVIMIENTO_YY= -3
    elif YY <= 0:
        YY = 0
        MOVIMIENTO_YY = 3


    pygame.draw.rect(ventana, morado , (XX,0, 50, 50))
    pygame.draw.rect(ventana, amarillo,(XX,450, 50, 50))
    pygame.draw.rect(ventana, rojo,(0, YY ,50, 50))
    pygame.draw.rect(ventana, lila,(450, YY ,50, 50))
    pygame.draw.rect(ventana, color_aleatorio , (200, 200 ,100, 100))
   
    pygame.display.flip()