import pygame
import sys
import random

pygame.init()

LARGURA, ALTURA = 800, 600
TAXA_FPS = 120
TEXTO = "TE FALEI CHINELÃO"
TEXTO2 = "EU TE AMO GREMIO"

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Teste Pygame")
clock = pygame.time.Clock()
fonte = pygame.font.SysFont("Arial", 50)

def nova_cor():
    return tuple(random.randint(0, 255) for _ in range(3))

texto = fonte.render(TEXTO, True, nova_cor())
rect = texto.get_rect(center=(LARGURA // 2, ALTURA // 2))

texto2 = fonte.render(TEXTO2, True, nova_cor())
rect2 = texto2.get_rect(center=(250, 200))

vel_x, vel_y = random.choice([-3, -2, 2, 3]), random.choice([-3, -2, 2, 3])
vel2_x, vel2_y = random.choice([-3, -2, 2, 3]), random.choice([-3, -2, 2, 3])

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    rect.x += vel_x
    rect.y += vel_y

    rect2.x += vel2_x
    rect2.y += vel2_y

    bateu_x = rect.left <= 0 or rect.right >= LARGURA
    bateu_y = rect.top <= 0 or rect.bottom >= ALTURA

    if bateu_x:
        vel_x *= -1
    if bateu_y:
        vel_y *= -1
    if bateu_x or bateu_y:
        texto = fonte.render(TEXTO, True, nova_cor())

    bateu2_x = rect2.left <= 0 or rect2.right >= LARGURA
    bateu2_y = rect2.top <= 0 or rect2.bottom >= ALTURA

    if bateu2_x:
        vel2_x *= -1
    if bateu2_y:
        vel2_y *= -1
    if bateu2_x or bateu2_y:
        texto2 = fonte.render(TEXTO2, True, nova_cor())

    if rect.colliderect(rect2):
        vel_x *= -1
        vel_y *= -1
        vel2_x *= -1
        vel2_y *= -1
        texto = fonte.render(TEXTO, True, nova_cor())
        texto2 = fonte.render(TEXTO2, True, nova_cor())

    tela.fill((0, 0, 0))
    tela.blit(texto, rect)
    tela.blit(texto2, rect2)
    pygame.display.flip()
    clock.tick(TAXA_FPS)

pygame.quit()
sys.exit()