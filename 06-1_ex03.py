maior = menor = 0
contador = 0
while True:
    n = int(input('Digite um número inteiro positivo: '))
    if n != 0:
        contador += 1
        if contador == 1:
            maior = n
            menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
    if n == 0:
        break
if contador >= 1:
    print(f'O maior e o menor, dentre todos os números, foram {maior} e {menor}, respectivamente.')
