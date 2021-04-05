from random import randint


def sortear_dado():
    return randint(1, 6)


for valor in range(1, 7):
    if (valor % 2) == 1:
        continue

    if sortear_dado() == valor:
        print('Acertou', valor)
        break
else:
    print('Não acertou o numero')
