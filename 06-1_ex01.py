deposito_inicial = float(input('Qual o depósito inicial? '))
juros = float(input('Qual a taxa de juros ao ano? '))
deposito = deposito_inicial + deposito_inicial * (juros / 100)
anos = 1

while deposito < deposito_inicial * 2:
    deposito = deposito + deposito * (juros / 100)
    anos += 1

print(f'Em {anos}, o valor acumulado será o dobro do valor inicial.')

