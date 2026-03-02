import pygame
import sys

pygame.init()

# ===== TUPLAS =====
TAMANO_PANTALLA = (800, 600)
ANCHO, ALTO = TAMANO_PANTALLA

COLOR_FONDO = (0, 0, 0)
COLOR_OBJETOS = (255, 255, 255)

POSICION_INICIAL_BOLA = (390, 290)

pantalla = pygame.display.set_mode(TAMANO_PANTALLA)
pygame.display.set_caption("Ping Pong")

reloj = pygame.time.Clock()

# ===== OBJETOS =====
bola = pygame.Rect(POSICION_INICIAL_BOLA[0], POSICION_INICIAL_BOLA[1], 20, 20)
vel_x = 5
vel_y = 5

paddle_izq = pygame.Rect(20, 250, 10, 100)
paddle_der = pygame.Rect(770, 250, 10, 100)

# ===== LISTA =====
paddles = [paddle_izq, paddle_der]

vel_paddle = 7

# ===== DICCIONARIO =====
marcador = {
    "Izquierda": 0,
    "Derecha": 0
}

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

    # Movimiento de la bola
    bola.x += vel_x
    bola.y += vel_y

    # Rebote arriba y abajo
    if bola.top <= 0 or bola.bottom >= ALTO:
        vel_y = -vel_y

    # Rebote en paletas
    for paddle in paddles:
        if bola.colliderect(paddle):
            vel_x = -vel_x

    # Punto para derecha
    if bola.left <= 0:
        marcador["Derecha"] += 1
        bola.x, bola.y = POSICION_INICIAL_BOLA

    # Punto para izquierda
    if bola.right >= ANCHO:
        marcador["Izquierda"] += 1
        bola.x, bola.y = POSICION_INICIAL_BOLA

    # Dibujar
    pantalla.fill(COLOR_FONDO)

    for paddle in paddles:
        pygame.draw.rect(pantalla, COLOR_OBJETOS, paddle)

    pygame.draw.rect(pantalla, COLOR_OBJETOS, bola)

    texto1 = fuente.render(str(marcador["Izquierda"]), True, COLOR_OBJETOS)
    texto2 = fuente.render(str(marcador["Derecha"]), True, COLOR_OBJETOS)

    pantalla.blit(texto1, (350, 20))
    pantalla.blit(texto2, (430, 20))

    pygame.display.flip()
    reloj.tick(60)



