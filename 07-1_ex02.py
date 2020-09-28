# Poupança para comprar carro à vista
carro = float(input('Qual o valor do carro? '))

poupanca = 10000
mes = 0

while not poupanca >= carro:
    mes += 1
    carro += carro * 0.004
    poupanca += poupanca * 0.007
print(f'O dinheiro dessa aplicação será suficiente para comprar o carro à vista, em {mes} meses.')
