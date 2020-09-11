print('Programa que lê 100 números inteiros positivos e informa a quantidade de ímpares e pares.')
print('-'*90)
par = 0
impar = 0
for c in range(1, 101):
    n = int(input(f'Digite o {c}º número inteiro positivo: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print('-'*60)
print(f'Dentre esses 100 números, {par} são pares e {impar} são ímpares.')
