import pygame
import modulos.configs as configuracoes

def retangulo(tela,cor,dimensoes,extras = {}):
    try:
        print(tela,configuracoes.CORES.get(cor),dimensoes)
        pygame.draw.rect(
            tela,
            configuracoes.CORES.get(cor) or (1,1,1),
            dimensoes,
            width = extras.get("espessura") or 0,
            border_radius= extras.get("borda") or 0,
            border_top_left_radius= extras.get("borda_cima_esquerda") or -1,
            border_top_right_radius= extras.get("borda_topo_direita") or -1,
            border_bottom_left_radius= extras.get("borda_baixo_esquerda") or -1, 
            border_bottom_right_radius= extras.get("borda_baixo_direita") or -1
        )
    except TypeError:
        print("Tu cagou alguma coisa")
