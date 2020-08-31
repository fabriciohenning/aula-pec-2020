n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
m = (n1 + n2 + n3) / 3
print(f'A média das notas é {m:.2f}.')
if n3 > 8:
    m = m + 1
    if m > 10:
        m = 10
    print(f'A média final, com acréscimo, é {m:.2f}.')
