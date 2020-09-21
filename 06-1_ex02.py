def media(soma, contador):
    return soma / contador


def main():
    print('Soma de uma quantidade indefinida de números.\n\nDigite 0 quando quiser encerrar o programa.')
    print('-'*43)
    soma = 0
    contador = 0
    while True:
        n = int(input('Digite um número inteiro positivo: '))
        if n != 0:
            soma += n
            contador += 1
        if n == 0:
            break

    if contador != 0:
        med = media(soma, contador)
        print(f'A média aritmética de todos os números lidos é {med}.')


if __name__ == '__main__':
    main()
