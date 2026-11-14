import arquivos_py.globais as globais

class Carta:
    def __init__(self, valor, naipe, sprites, pos=(0, 0)):
        self.valor = valor
        self.naipe = naipe
        self.frente = sprites[(valor, naipe)]
        self.fundo = globais.carta_parente_frente
        self.rect = self.frente.get_rect(topleft=pos)


    def desenhar(self, tela):
       tela.blit(self.fundo, self.rect)
       tela.blit(self.frente, self.rect)