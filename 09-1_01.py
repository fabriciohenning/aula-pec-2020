# função temp_maior retorna o índice da maior temperatura
def temp_maior(t1, e1, t2, e2):
    maior = 0
    if e1 == e2 == 'C' or e1 == e2 == 'F':
        if t1 > t2:
            maior = 0
        if t1 < t2:
            maior = 1
    if e1 == 'F' and e2 == 'C':
        t1 = (t1 - 32) * 5 / 9
        if t1 > t2:
            maior = 0
        if t1 < t2:
            maior = 1
    if e2 == 'F' and e1 == 'C':
        t2 = (t2 - 32) * 5 / 9
        if t2 > t1:
            maior = 1
        if t2 < t1:
            maior = 0
    return maior


def main():
    t1 = float(input('Primeira temperatura: '))
    e1 = input('Escala dessa temperatura: ').upper()[0]
    t2 = float(input('Segunda temperatura: '))
    e2 = input('Escala dessa temperatura: ').upper()[0]
    temperatura = [(t1, e1), (t2, e2)]
    maior = temp_maior(t1, e1, t2, e2)
    print(f'A maior temperatura é {temperatura[maior]}.')


if __name__ == '__main__':
    main()
