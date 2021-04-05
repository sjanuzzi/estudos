

try:
    arquivo = open('pessoas.csv')
    for registro in arquivo:
        print('Nome {}, Idade {}'.format(*registro.strip().split(',')))
except IndexError:
    pass
finally:
    print('final')
    arquivo.close()


if arquivo.closed:
    print('Arquivo fechado')
