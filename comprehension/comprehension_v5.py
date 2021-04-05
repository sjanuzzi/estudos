dicionario = {i: i * 2 for i in range(22) if i % 2 == 0}
print(dicionario)


for numero, dobro in dicionario.items():
    print(f'2x{numero} = {dobro}')
