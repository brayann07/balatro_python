import pygame

# DEBUGS
TESTANDO = False

# JANELA E TALS
FPS = 60
RESOLUCAO_PADRAO = (1280,780)
ESCALA_GLOBAL_UI = 1.75
FONTES = {
    "texto_normal" : pygame.font.Font("fontes/comicsans.ttf",30),
    "texto_maiusculo" : pygame.font.Font("fontes/comicsans.ttf",50)
}
NOME_DA_JANELA = "PYLATRO!"
IMAGEM_JANELA = pygame.image.load("imagens/aafolou.jpg")

# UI
CORES = {
    "botao" : (215, 159, 236),
    "container" : (82, 0, 112),
    "bg_inicio" : "white"
}