import pygame
import random
import sys

pygame.init()
DIMENSIONS = 1350, 600
VENTANA = pygame.display.set_mode((DIMENSIONS[0], DIMENSIONS[1]))
pygame.display.set_caption("Carrera de Fórmula 1 - 2 Jugadores")

fondo = pygame.image.load("p4.jpg")
fondo = pygame.transform.scale(fondo,DIMENSIONS)

img1 = 0
img2 = DIMENSIONS[0]
fondo_velocidad = 5

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
GRIS = (100, 100, 100)


FUENTE = pygame.font.SysFont("Arial", 36)
RELOJ = pygame.time.Clock()


class Auto:
    def __init__(self, x, y, color):

        self.rect = pygame.Rect(x, y, 40, 80)
        self.color = color
        self.velocidad_x = 0
        self.velocidad_y = 0

    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.color, self.rect)

    def mover(self):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        self.rect.x = max(0, min(self.rect.x, DIMENSIONS[0] - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, DIMENSIONS[1] - self.rect.height))


class Obstaculo:
    def __init__(self, x, y, ancho, alto):
        self.rect = pygame.Rect(x, y, ancho, alto)

    def dibujar(self, ventana):
        pygame.draw.rect(ventana, GRIS, self.rect)


jugador1 = Auto(100, 200, ROJO)  
jugador2 = Auto(100, 350, AZUL)
  


obstaculos = [
    Obstaculo(400, 150, 30, 30),
    Obstaculo(500, 250, 30, 30),
    Obstaculo(600, 100, 30, 30),
    Obstaculo(550, 400, 30, 30),
    Obstaculo(450, 300, 30, 30)
]

carrera_en_curso = True
ganador = None

while carrera_en_curso:
    img1 -= fondo_velocidad
    img2 -= fondo_velocidad
    
    if img1 <= -DIMENSIONS[0]:  
        img1 = DIMENSIONS[0]  
    if img2 <= -DIMENSIONS[0]:  
        img2 = DIMENSIONS[0] 


    VENTANA.blit(fondo, (img1, 0))
    VENTANA.blit(fondo, (img2, 0))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif evento.type == pygame.KEYDOWN:
           
            if evento.key == pygame.K_w:
                jugador1.velocidad_y = -5
            elif evento.key == pygame.K_s:
                jugador1.velocidad_y = 5
            elif evento.key == pygame.K_a:
                jugador1.velocidad_x = -5
            elif evento.key == pygame.K_d:
                jugador1.velocidad_x = 5

           
            elif evento.key == pygame.K_UP:
                jugador2.velocidad_y = -5
            elif evento.key == pygame.K_DOWN:
                jugador2.velocidad_y = 5
            elif evento.key == pygame.K_LEFT:
                jugador2.velocidad_x = -5
            elif evento.key == pygame.K_RIGHT:
                jugador2.velocidad_x = 5

        elif evento.type == pygame.KEYUP:
            if evento.key in [pygame.K_w, pygame.K_s]:
                jugador1.velocidad_y = 0
            if evento.key in [pygame.K_a, pygame.K_d]:
                jugador1.velocidad_x = 0
            if evento.key in [pygame.K_UP, pygame.K_DOWN]:
                jugador2.velocidad_y = 0
            if evento.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                jugador2.velocidad_x = 0

   
    jugador1.mover()
    jugador2.mover()

   
    for obstaculo in obstaculos:
        obstaculo.dibujar(VENTANA)

   
    jugador1.dibujar(VENTANA)
    jugador2.dibujar(VENTANA)

    for obstaculo in obstaculos:
        if jugador1.rect.colliderect(obstaculo.rect):
            ganador = "Jugador 2 (Jugador 1 chocó)"
            carrera_en_curso = False
        elif jugador2.rect.colliderect(obstaculo.rect):
            ganador = "Jugador 1 (Jugador 2 chocó)"
            carrera_en_curso = False

    if jugador1.rect.x >= DIMENSIONS[0] - jugador1.rect.width:
        ganador = "Jugador 1"
        carrera_en_curso = False
    elif jugador2.rect.x >= DIMENSIONS[0] - jugador2.rect.width:
        ganador = "Jugador 2"
        carrera_en_curso = False

    pygame.display.update()
    RELOJ.tick(60)

VENTANA.fill(NEGRO)
texto = FUENTE.render(f"Ganador: {ganador}!", True, BLANCO)
VENTANA.blit(texto, (DIMENSIONS[0] // 2 - texto.get_width() // 2, DIMENSIONS[1] // 2))
pygame.display.update()
pygame.time.wait(4000)
pygame.quit()