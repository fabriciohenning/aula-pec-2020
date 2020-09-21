def menu():
    return '''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA'''


def main():
    print(menu())
    codigo = str(input('Digite o código do produto escolhido: ')).upper()[0]
    total = 0
    while True:
        if codigo == 'H':
            total += 5.50
            print(menu())
            codigo = str(input('Digite o código de outro produto mostrado na lista: ')).upper()[0]
        elif codigo == 'C':
            total += 6.80
            print(menu())
            codigo = str(input('Digite o código de outro produto mostrado na lista: ')).upper()[0]
        elif codigo == 'M':
            total += 4.50
            print(menu())
            codigo = str(input('Digite o código de outro produto mostrado na lista: ')).upper()[0]
        elif codigo == 'A':
            total += 7.00
            print(menu())
            codigo = str(input('Digite o código de outro produto mostrado na lista: ')).upper()[0]
        elif codigo == 'Q':
            total += 4.00
            print(menu())
            codigo = str(input('Digite o código de outro produto mostrado na lista: ')).upper()[0]
        elif codigo == 'X':
            break
        else:
            print('Opção inválida.')
            print(menu())
            codigo = str(input('Digite o código de outro produto mostrado na lista: ')).upper()[0]
    print('-=-' * 13)
    print(f'O TOTAL DO SEU PEDIDO É DE R$ {total:.2f}.')


if __name__ == '__main__':
    main()
