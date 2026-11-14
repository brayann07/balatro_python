import pygame

valor_global_escala = 2

def carregar_sprites_valores():
    sprites = {}
    caminho = "imagens/valores.png"
    linhas = 13
    colunas = 4
    ordem_valores = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    ordem_naipe = ["COPA","PAU","OURO","ESPADA"]

    sheet = pygame.image.load(caminho).convert_alpha()
    largura,altura = sheet.get_size()

    largura = largura // linhas
    altura = altura // colunas
    for l, naipe in enumerate(ordem_naipe):
        for c, valor in enumerate(ordem_valores):
            rect = pygame.Rect(c * largura, l * altura, largura, altura) 
            carta = sheet.subsurface(rect)
            carta = pygame.transform.scale(carta, (largura * valor_global_escala, altura * valor_global_escala))
            sprites[(valor, naipe)] = carta

    return sprites

def pegar_rect_especifico(caminho,x,y,largura,altura):
    sheet = pygame.image.load(caminho).convert_alpha()
    rect = pygame.Rect(x,y,largura,altura)    
    sprite = sheet.subsurface(rect)
    sprite = pygame.transform.scale(sprite,(largura * valor_global_escala, altura * valor_global_escala))
    return sprite


def escalar(sprite, fator):
    largura, altura = sprite.get_size()
    novo_tamanho = (int(largura * fator), int(altura * fator))
    return pygame.transform.scale(sprite, novo_tamanho)

def escrever(tela, texto, fonte, pos, cor="white", centralizado=False, pixel_art=True):
    surf = fonte.render(texto, not pixel_art, cor)
    rect = surf.get_rect(center=pos) if centralizado else surf.get_rect(topleft=pos)
    tela.blit(surf, rect)