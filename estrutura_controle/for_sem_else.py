PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')
textos = [
    'Saulo gosta de futebol e política',
    'a praia é divertida',
]


for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto não apropriado', palavra)
            found = True
            break

    if not found:
        print('texto OK ')
