import pygame
import modulos.desenhar as renderizar
import modulos.configs as configuracoes

janela_atual = "inicio"

def inicio(tela):
   tela.fill(configuracoes.CORES.get("bg_inicio"))
   renderizar.retangulo(tela,"container",(120,30,20,30))

  

def jogo(tela):
    return


def runtime(tela):
    if janela_atual == "inicio":
        inicio(tela)
    else:
        jogo(tela)