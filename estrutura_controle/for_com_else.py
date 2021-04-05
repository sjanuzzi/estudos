PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}
textos = [
    'Saulo gosta de futebol e política',
    'a praia é divertida',
]


for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Texto não apropriado', intersecao)
    else:
        print('texto OK ')
