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
    screen = pygame.display.set_mode((1288, 728), pygame.SCALED | pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((1288, 728), pygame.SCALED | pygame.RESIZABLE)

clock = pygame.time.Clock()
running = True
pygame.display.set_caption("PYLATRO")

fonte = pygame.font.Font("fontes/comicsans.ttf", 25)

# configs
carta_virada = globais.carta_parente_atras
num_cartas = 5


# Loop de jogo
while running:
    # eventos do pygame, inputs e tals
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Desenha a cor da tela no fundo
    screen.fill("black")

    # Lógica do jogo 
    


    # cartas dianteira baixo
    for i in range(num_cartas):
        screen.blit(carta_virada,(1100 - 6 * i,500 - 6 * i))
    funcoes.escrever(screen,
        f"{len(globais.cartas_atuais)}/{len(globais.cartas_atuais)}"
        ,fonte, (1165,460),
          centralizado=True,
          pixel_art = False
    )

    # renderização
    pygame.display.flip()
    clock.tick(60)  # FPS

pygame.quit()