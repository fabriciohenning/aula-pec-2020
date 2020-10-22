def media(nota1, nota2):
    return (nota1 + nota2) / 2


def main():
    alunos = {}

    while True:
        matricula = str(input('Matrícula: ')).strip()
        if matricula == '':
            break
        nome = str(input('Nome: ')).strip()
        nota1 = float(input('Primeira nota: '))
        nota2 = float(input('Segunda nota: '))
        m = media(nota1, nota2)
        aluno = (nome, nota1, nota2, m)
        alunos[matricula] = aluno

    while True:
        leitura = input('Informe uma matrícula para saber a média do respectivo aluno: ').strip()
        if leitura == '':
            break
        if leitura in alunos.keys():
            nome, nota1, nota2, m = alunos[leitura]
            print(f'{nome}: {m:.1f}')


if __name__ == '__main__':
    main()
