#!/usr/bin/env /Library/Frameworks/Python.framework/Versions/3.8/bin/python3
from math import pi
import sys
import errno


ERRO = '\033[91m'
NORMAL = '\033[0m'


def help():
    print("Informe uma Nota!")


def nota(valor):
    nota = float(valor)

    if nota > 10:
        return 'Nota inválida'
    elif nota >= 9.1:
        return 'Nota conceito é A'
    elif nota >= 8.1:
        return 'Nota conceito é A-'
    elif nota >= 7.1:
        return 'Nota conceito é B'
    elif nota >= 6.1:
        return 'Nota conceito é B-'
    elif nota >= 5.1:
        return 'Nota conceito é C'
    elif nota >= 4.1:
        return 'Nota conceito é C-'
    elif nota >= 3.1:
        return 'Nota conceito é D'
    elif nota >= 2.1:
        return 'Nota conceito é D-'
    elif nota >= 1.1:
        return 'Nota conceito é E'
    elif nota >= 0:
        return 'Nota conceito é E-'
    else:
        nota < 0
        return 'Nota inválida'


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
    else:
        valor = sys.argv[1]
        a = nota(valor)
        print(a)


#print('nome do modulo ', __name__)
#print('nome do modulo ', __package__)
