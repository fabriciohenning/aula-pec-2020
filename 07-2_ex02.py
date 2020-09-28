# Sequência de Fibonacci com n termos
num = int(input('Digite um valor maior que 2: '))
termo1 = 0
termo2 = 1
cont = 3
print(f'A sequência de Fibonacci com {num} termos é {termo1}, {termo2}', end='')
while cont <= num:
    termo3 = termo1 + termo2
    print(f', {termo3}', end='')
    termo1 = termo2
    termo2 = termo3
    cont += 1
