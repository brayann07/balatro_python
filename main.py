# Descrição sobre o trabalho
""" 
REQUISITOS DO TRABALHO:
for ✅
while ✅
if 
elif
dicionarios ✅
funções ✅
menu interativo 
salvamento  
"""

# Bibliotecas/Imports
import pygame as pygame
lazy import arquivos_py.funcoes as funcoes
lazy import arquivos_py.classes as classes
lazy import arquivos_py.globais as globais

# Evento iniciais do PyGame 
pygame.init()

TESTE = False

if TESTE:
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((1288,728))

clock = pygame.time.Clock()
running = True
pygame.display.set_caption("PYLATRO")

carta1 = classes.Carta("A", "COPA", globais.sprites_cartas,(100, 100))
carta2 = classes.Carta("K", "ESPADA", globais.sprites_cartas,(300, 100))


# Loop de jogo
while running:
    # eventos do pygame, inputs e tals
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Desenha a cor da tela no fundo
    screen.fill("purple")

    # Lógica do jogo 

    carta1.desenhar(screen)
    carta2.desenhar(screen)

    # renderização
    pygame.display.flip()
    clock.tick(60)  # FPS

pygame.quit()