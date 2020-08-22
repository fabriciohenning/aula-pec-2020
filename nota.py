def desconto(dias):
    return dias * 5

d = int(input('Digite os dias de atraso: '))
desc = desconto(d)
print(f'Você deve descontar {desc} pontos da nota.')
