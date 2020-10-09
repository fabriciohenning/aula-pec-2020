def ler_numeros(n):
    lista = []
    numero = 0
    for i in range(n):
        lista.append(float(input(f'Digite o {i+1}º número: ')))
    return lista

def main():
    n = int(input('Digite um número inteiro n para gerar uma lista com n posições: '))
    lista = ler_numeros(n)
    lista.sort(reverse=True)
    print(f'a) {lista}')
    lista = []

    for cont in range(n):
        if n == 0:
            print('SEM NOTAS')
        nota = float(input('Digite uma nota: '))
        lista.append(nota)
    print(f'A lista de notas é {lista} e sua média, {sum(lista) / len(lista)}.')

    lista = []
    cont_vogal = 0
    lista_consoante = []
    for cont in range(n):
        letra = str(input('Digite uma letra: '))[0]
        lista.append(letra)
        if letra in 'aeiou':
            cont_vogal += 1
        else:
            lista_consoante.append(letra)
    print(f'Foram lidas {cont_vogal} vogais.')
    print(f'As consoantes são {lista_consoante}.')


if __name__ == '__main__':
    main()
