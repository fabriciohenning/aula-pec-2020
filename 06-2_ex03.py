def menu():
    return 'OPÇÕES:\n1 - SAUDAÇÃO\n2 - BRONCA\n3 - FELICITAÇÃO\n0 - FIM'


def main():
    print(menu())
    opcao = int(input('Escolha uma das opções acima: '))
    while True:
        if opcao == 1:
            print('1 - Olá. Como vai?')
            print('-' * 18)
            print(menu())
            opcao = int(input('Escolha novamente outra das opções acima: '))
        elif opcao == 2:
            print('2 - Vamos estudar mais.')
            print('-'*23)
            print(menu())
            opcao = int(input('Escolha novamente outra das opções acima: '))
        elif opcao == 3:
            print('3 - Meus Parabéns!')
            print('-' * 18)
            print(menu())
            opcao = int(input('Escolha novamente outra das opções acima: '))
        elif opcao == 0:
            print('0 - Fim de serviço.')
            break
        else:
            print('Opção inválida.')
            print('-' * 15)
            print(menu())
            opcao = int(input('Escolha novamente outra das opções acima: '))


if __name__ == '__main__':
    main()