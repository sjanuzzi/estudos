def soma(a, b):
    return a + b


def soma2(a, b, c):
    return a + b + c


def soma_n(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma


if __name__ == '__main__':
    print(soma(1, 2))
    print(soma2(1, 2, 3))
    print(soma_n(1, 2, 3, 4, 5, 6, 7, 8, 9))
    nums = (2, 1, 1)
    print(soma2(*nums))
