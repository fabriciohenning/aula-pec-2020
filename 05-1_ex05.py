# Maior número dentre 100 lidos
maior = 0
for n in range(1, 101):
    numero = int(input(f'Digite o {n}º número inteiro positivo: '))
    if maior < numero:
        maior = numero
print(f'O maior entre todos os números é {maior}.')
