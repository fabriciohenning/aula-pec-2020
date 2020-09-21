soma = 0
while True:
    n = int(input('Digite um número: '))
    if n != 0:
        soma += n
    if n == 0:
        break
print(f'A soma dos números digitados é {soma}.')
