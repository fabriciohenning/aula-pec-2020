# Valor das prestações sem juros
compra = float(input('Digite o valor da compra (R$): '))
for p in range(1, 25):
    prestacao = compra / p
    print(f'{p}x de R$ {prestacao:.2f}')
