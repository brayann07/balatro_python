import pygame



def aperta_x_janela(running = False):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return False