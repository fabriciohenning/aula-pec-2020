# Preenchendo lista com zeros, de 1 a n, com valores lidos e com valores lidos em ordem inversa
n = int(input('Insira um número inteiro qualquer: '))
V = []

# a) Preenchendo lista com 0
for i in range(1, n+1):
    V.append(0)
print(f'a) {V}')
V = []

# b) Preenchendo lista com números de 1 a n
for i in range(1, n+1):
    V.append(i)
print(f'b) {V}')
V = []

# c) Preenchendo lista com valores inteiros lidos pelo teclado
for i in range(1, n+1):
    V.append(int(input(f'Digite o {i}º número inteiro: ')))
print(f'c) {V}')
V = []

# d) Preenchendo na ordem inversa com insert
for i in range(1, n+1):
    v_invert = int(input(f'Digite o {i}º número inteiro: '))
    V.insert(-i, v_invert)
print(f'd) {V}')
