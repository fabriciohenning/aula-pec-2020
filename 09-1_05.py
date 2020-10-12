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
    mes_escolhido = int(input('Informe um mês [de 1 a 12]: '))
    print()
    populacao = int(input('Informe uma população para receber as cidades que\n'
                          'fazem aniversário no mês informado e com população maior: '))
    cidades = carrega_cidades()
    mes_extenso = 'JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO'
    print()
    print(f'CIDADES COM MAIS DE {populacao} HABITANTES E ANIVERSÁRIO EM {mes_extenso[mes_escolhido-1]}:')
    print()
    for uf, _, nome, dia, mes, pop in cidades:
        if mes == mes_escolhido and pop > populacao:
            print(f'{nome}({uf}) tem {pop} habitantes e faz aniversário em {dia} de {mes_extenso[mes_escolhido-1].lower()}.')


if __name__ == '__main__':
    main()
