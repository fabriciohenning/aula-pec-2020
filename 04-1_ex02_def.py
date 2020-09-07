def data_recente (d1, m1, a1, d2, m2, a2):
    if a1 > a2:
        return f'{d1}/{m1}/{a1}'
    elif a1 < a2:
        return f'{d2}/{m2}/{a2}'
    else:
        if m1 > m2:
            return f'{d1}/{m1}/{a1}'
        if m1 < m2:
            return f'{d2}/{m2}/{a2}'
        else:
            if d1 > d2:
                return f'{d1}/{m1}/{a1}'
            if d1 < d2:
                return f'{d2}/{m2}/{a2}'
            else:
                print(f'As duas datas são iguais!')


def main():
    d1 = int(input('Dia da primeira data, com dois dígitos: '))
    m1 = int(input('Mês da primeira data, com dois dígitos: '))
    a1 = int(input('Ano da primeira data, com quatro dígitos: '))
    d2 = int(input('Dia da segunda data, com dois dígitos: '))
    m2 = int(input('Mês da segunda data, com dois dígitos: '))
    a2 = int(input('Ano da segunda data, com quatro dígitos: '))
    recente = data_recente(d1, m1, a1, d2, m2, a2)
    print(f'A data mais recente é {recente}.')

if __name__ == '__main__':
        main()

