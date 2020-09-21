salario = float(input('Salário inicial: '))
divida = float(input('Forneça o valor da dívida: '))
mes = 10
ano = 2016

while True:
    mes += 1
    divida = divida + 0.15 * divida
    if mes == 3:
        salario = salario + 0.05 * salario
    if mes > 12:
        mes = 1
        ano += 1
    if divida > salario:
        break
print(f'O valor da dívida irá superar o salário em {mes}/{ano}.')
