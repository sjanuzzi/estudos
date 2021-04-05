#!/usr/bin/env /Library/Frameworks/Python.framework/Versions/3.8/bin/python3
from math import pi
import sys
import errno


ERRO = '\033[91m'
NORMAL = '\033[0m'


def help():
    print("Informe o numero do raio!")
    # sys.exit(1)


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
    elif not sys.argv[1].isnumeric():
        help()
        print(ERRO + "O raio tem que ser numerico", NORMAL)
        sys.exit(errno.EINVAL)
    else:
        raio = sys.argv[1]
        a = circulo(raio)
        print(a)


#print('nome do modulo ', __name__)
#print('nome do modulo ', __package__)
