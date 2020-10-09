numeros = []
par = []
impar = []
for i in range(4):
    numero = (int(input(f'Digite o {i+1}º número: ')))
    numeros.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
print(f'Lista dos 20 números: {numeros}.')
print(f'Lista dos números pares: {par}.')
print(f'Lista dos números ímpares: {impar}.')
