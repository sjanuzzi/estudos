#!/usr/bin/env /Library/Frameworks/Python.framework/Versions/3.8/bin/python3


palavra = 'paralelepipedo'

for letra in palavra:
    print(letra, end=',')

aprovados = ['Anna', 'Saulo', 'Pedro']
for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    print(posicao + 1, nome)

dias_semana = ('Domingo', 'Segunda', 'Terça',
               'Quarta', 'Quinta', 'Sexta', 'Sabado')
for dia in dias_semana:
    print(f'Hoje é {dia}')

for letra in set('melhor'):
    print(letra)
