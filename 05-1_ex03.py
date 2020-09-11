soma = 0
for c in range(1, 101):
    n = int(input(f'Digite o {c}º número inteiro: '))
    soma += n
media = soma / c
print(f'O valor médio desses 100 números é {media:.2f}.')
