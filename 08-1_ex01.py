def ler_numeros(n):
    numeros = []
    for i in range(n):
        numeros.append(int(input(f'Digite o {i+1}º número: ')))
    return numeros


def main():
    numeros = ler_numeros(10)
    print(f'Os números da lista são {numeros}.')
    soma = 0
    mult = 1
    for c in numeros:
        soma = soma + c
        mult = mult * c
    print(f'A soma e a multiplicação desses 10 números são {soma} e {mult}, respectivamente.')


if __name__ == '__main__':
    main()
