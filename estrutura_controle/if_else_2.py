#!/usr/bin/env /Library/Frameworks/Python.framework/Versions/3.8/bin/python3

def faixa_etaria(idade):
    if 0 < idade < 18:
        return 'Menor de Idade'
    elif idade in range(18, 50):
        return 'Adulto'
    elif idade in range(51, 100):
        return 'Maior idade'
    elif idade >= 100:
        return 'Centenário'
    else:
        return 'Data Inválida'


if __name__ == '__main__':
    for idade in (17, 25, 87, 113, -2):
        print(f'{idade}: {faixa_etaria(idade)}')
