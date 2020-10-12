def soma_2temp(t1, t2, e1, e2):
    soma = 0
    if e1 == e2:
        soma = t1 + t2
    if e2 == 'C' and e1 == 'F':
        t1 = (t1 - 32) * 5 / 9
        soma = t1 + t2
    if e2 == 'F' and e1 == 'C':
        t1 = t1 * 9/5 + 32
        soma = (t1 + t2)
    return soma


def main():
    t1 = float(input('Primeira temperatura: '))
    e1 = input('Escala dessa temperatura: ').upper()[0]
    t2 = float(input('Segunda temperatura: '))
    e2 = input('Escala dessa temperatura: ').upper()[0]
    temperatura = [(t1, e1), (t2, e2)]
    soma = soma_2temp(t1, t2, e1, e2), e2
    print('A soma das temperaturas é {:.2f}.'.format(soma))


if __name__ == '__main__':
    main()
