import arquivos_py.funcoes as func

# Sprites
carta_parente_atras = func.pegar_rect_especifico("imagens/cartas.png",0,0,71,95)
carta_parente_frente = func.pegar_rect_especifico("imagens/cartas.png",71,0,77,95)
sprites_cartas = func.carregar_sprites_valores()

# Configurações
coringas = {}
cartas_valores = {"A":  1, "2":  2, "3":  3, "4":  4, "5":  5, "6":  6,"7":  7, "8":  8, "9":  9, "10": 10,"J": 11, "Q":  12, "K":  13}

# Temporarios
cartas_atuais = {}
coringas_atuais = {}