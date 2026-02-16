import pygame
import sys

pygame.init()

ANCHO = 800
ALTO = 600

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("")

reloj = pygame.time.Clock()

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

bola = pygame.Rect(390, 290, 20, 20)
vel_x = 5
vel_y = 5

paddle_izq = pygame.Rect(20, 250, 10, 100)
paddle_der = pygame.Rect(770, 250, 10, 100)

vel_paddle = 7

puntos_izq = 0
puntos_der = 0

fuente = pygame.font.Font(None, 50)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_w]:
        paddle_izq.y -= vel_paddle
    if teclas[pygame.K_s]:
        paddle_izq.y += vel_paddle

    if teclas[pygame.K_UP]:
        paddle_der.y -= vel_paddle
    if teclas[pygame.K_DOWN]:
        paddle_der.y += vel_paddle

    
    bola.x += vel_x
    bola.y += vel_y

    
    if bola.top <= 0 or bola.bottom >= ALTO:
        vel_y = -vel_y

    
    if bola.colliderect(paddle_izq) or bola.colliderect(paddle_der):
        vel_x = -vel_x

    
    if bola.left <= 0:
        puntos_der += 1
        bola.x = 390
        bola.y = 290

    if bola.right >= ANCHO:
        puntos_izq += 1
        bola.x = 390
        bola.y = 290

   
    pantalla.fill(NEGRO)

    pygame.draw.rect(pantalla, BLANCO, paddle_izq)
    pygame.draw.rect(pantalla, BLANCO, paddle_der)
    pygame.draw.rect(pantalla, BLANCO, bola)

    texto1 = fuente.render(str(puntos_izq), True, BLANCO)
    texto2 = fuente.render(str(puntos_der), True, BLANCO)

    pantalla.blit(texto1, (350, 20))
    pantalla.blit(texto2, (430, 20))

    pygame.display.flip()
    reloj.tick(60)



