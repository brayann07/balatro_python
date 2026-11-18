# Dias sem usar IA - 0 dias

# Bibliotecas/Imports
import pygame
lazy import modulos.configs as configuracoes
lazy import modulos.eventos as eventos
lazy import modulos.runtime as runtime

def iniciar():
    # init tem que ser chamado pra começar a biblioteca do pygame
    pygame.init()

    # configs globais declaradas no modulos/configs_pyg.py
    tela = pygame.display.set_mode(configuracoes.RESOLUCAO_PADRAO, pygame.SCALED | pygame.RESIZABLE) # Tamanho da janela
    pygame.display.set_caption(configuracoes.NOME_DA_JANELA) # nome da janela
    pygame.display.set_icon(configuracoes.IMAGEM_JANELA) # icone da janela
    clock = pygame.time.Clock()

    running = True
    while running:
        # ESSE EVENTO SEMPRE DEVE RODAR ANTES DE TUDO
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False


        # aqui a gente coloca nossa logica de jogo
        runtime.runtime(tela)
    
        # isso aqui basicamente é coisas do modulo do pygame
        pygame.display.flip()
        clock.tick(configuracoes.FPS)  

    # sempre bom garantir né...
    if running:
        running = False

    # acaba com os processos
    pygame.quit()

# sempre bom colocar um main pq eu sou tanso e fico rodando em outros arquivos sem querer
if __name__ == "__main__":
    iniciar()