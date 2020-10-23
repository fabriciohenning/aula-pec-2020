contador = {}
for n in range(1000):
    ano = int(input('Digite o ano de nascimento: '))
    if ano in contador:
        contador[ano] = contador[ano] + 1
    else:
        contador[ano] = 1

anos_ordenados = tuple(contador.keys())
for ano in sorted(anos_ordenados):
    print(f'No ano de {ano} nasceram {contador[ano]} pessoa(s).')
