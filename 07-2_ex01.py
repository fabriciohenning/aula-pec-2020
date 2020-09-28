# Fatorial de um número
n = int(input('Digite um número inteiro: '))
c = n
f = 1
for c in range(n, 1, -1):
    f *= c
    c -= 1
print(f'O fatorial de {n} é {f}.')
