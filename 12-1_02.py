from operator import itemgetter


def carregar(arquivo):
    linhas = []
    with open(arquivo) as f:
        f.readline()  # Descarta a primeira linha (cabeçalho do arquivo)
        for linha in f.readlines():
            data, abertura, alta, baixa, fechamento, volume = linha.strip().split(',')
            ano, mes, dia = data.split('-')
            linhas.append(
                {
                    "ano": int(ano),
                    "mes": int(mes),
                    "dia": int(dia),
                    "abertura": float(abertura),
                    "alta": float(alta),
                    "baixa": float(baixa),
                    "fechamento": float(fechamento),
                    "volume": int(volume),
                }
            )
    return linhas


def formatar_data(linha):
    meses = (
        'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
        'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
    )
    d, m, a, = linha['dia'], linha['mes'], linha['ano']
    return f'{d:0>2d} de {meses[m - 1]} de {a}'


def menor_preco(empresa):
    ordenado = sorted(empresa, key=itemgetter('fechamento'))
    return ordenado[0]['fechamento'], formatar_data(ordenado[0])


def main():
    # Carrega os dados da empresa a partir do arquivo .csv
    empresa = carregar(input())

    # Qual o menor preço de fechamento e a data em que ocorreu?
    fechamento, data = menor_preco(empresa)
    print(f'O menor preço no fechamento foi {fechamento:.2f} em {data}')


if __name__ == '__main__':
    main()