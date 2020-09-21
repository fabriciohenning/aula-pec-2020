nota = float(input('Nota do aluno: '))
while True:
    if nota < 0 or nota > 10:
        print('Nota inválida.')
        nota = float(input('Digite uma nota entre 0 e 10: '))
    elif nota >= 8.5:
        print('Conceito A.')
        break
    elif nota >= 7.0:
        print('Conceito B.')
        break
    elif nota >= 5.0:
        print('Conceito C.')
        break
    elif nota >= 4:
        print('Conceito D.')
        break
    else:
        print('Conceito E.')
        break
