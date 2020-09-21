contador = 0
menor = maior = 0
soma_idades = 0
while True:
    idade = int(input('Digite a idade da pessoa: '))
    if idade != 0:
        contador += 1
        soma_idades += idade
        if contador == 1:
            menor = idade
            maior = idade
        else:
            if idade > maior:
                maior = idade
            if idade < menor:
                menor = idade
    if idade == 0:
        break

if contador != 0:
    print(f'Foi perguntada a idade de {contador} pessoas.')
    print(f'A idade média do grupo é {soma_idades / contador:.2f} anos.')
    print(f'A menor idade foi de {menor} anos.')
    print(f'A maior idade foi de {maior} anos.')
