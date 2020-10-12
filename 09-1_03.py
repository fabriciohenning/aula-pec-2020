def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()
    return resultado


def main():
    dia_escolhido = int(input('Dia: '))
    mes_escolhido = int(input('Mês: '))
    cidades = carrega_cidades()
    mes_extenso = 'JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO'
    print(f'CIDADES QUE FAZEM ANIVERSÁRIO EM {dia_escolhido} DE {mes_extenso[mes_escolhido-1]}:')
    for uf, _, nome, dia, mes, _ in cidades:
        if dia_escolhido == dia and mes_escolhido == mes:
            print(f'{nome} ({uf})')


if __name__ == '__main__':
    main()
