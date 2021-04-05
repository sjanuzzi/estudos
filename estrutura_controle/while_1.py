#!/usr/bin/env /Library/Frameworks/Python.framework/Versions/3.8/bin/python3

from random import randint


numero_informado = -1
numero_secreto = randint(0, 9)


while numero_informado != numero_secreto:
    numero_informado = int(input('Informe um numero secreto: '))

print('Número secreto {} foi encontrato'. format(numero_secreto))
