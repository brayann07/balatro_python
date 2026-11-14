import pygame

def linear(t):
    return t

def ease_out_cubic(t):
    return 1 - (1 - t) ** 3

def ease_in_out(t):
    return t * t * (3 - 2 * t)

def ease_out_back(t):
    c1 = 1.70158
    c3 = c1 + 1
    return 1 + c3 * (t - 1) ** 3 + c1 * (t - 1) ** 2


class Tween:
    def __init__(self, inicio, fim, duracao, easing=ease_out_cubic):
        self.posicao = isinstance(inicio, (tuple, list, pygame.Vector2))
        if self.posicao:
            self.inicio = pygame.Vector2(inicio)
            self.fim = pygame.Vector2(fim)
        else:
            self.inicio = inicio
            self.fim = fim
        self.duracao = duracao
        self.easing = easing
        self.tempo = 0
        self.terminou = False

    def atualizar(self, dt):
        self.tempo += dt
        t = min(self.tempo / self.duracao, 1)
        if t >= 1:
            self.terminou = True
        t = self.easing(t)
        if self.posicao:
            return self.inicio.lerp(self.fim, t)
        return self.inicio + (self.fim - self.inicio) * t