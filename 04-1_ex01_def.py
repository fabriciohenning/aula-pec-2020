# Cálculo da idade exata, em anos.
def idade_exata(dia, mes, ano, dia_atual, mes_atual, ano_atual):
    if mes < mes_atual:
        return (ano_atual - 1) - ano
    elif mes > mes_atual:
        return ano_atual - ano
    else:
        if dia < dia_atual:
            return (ano_atual - 1) - ano
        else:
            return ano_atual - ano

def main():
    dia_atual = int(input('Digite o dia atual: '))
    mes_atual = int(input('Digite o mês atual: '))
    ano_atual = int(input('Digite o ano atual: '))
    dia = int(input('Agora digite o dia do seu aniversário: '))
    mes = int(input('Digite o mês do seu aniversário: '))
    ano = int(input('Digite o ano do seu aniversário: '))
    idade = idade_exata(dia, mes, ano, dia_atual, mes_atual, ano_atual)
    print(f'Você tem {idade} anos de idade.')

if __name__ == '__main__':
    main()
