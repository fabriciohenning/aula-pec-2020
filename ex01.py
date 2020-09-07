pessoa = input('Nome da pessoa: ')
estado_civil = input('Estado civil da pessoa [C - para casado; S - para solteiro]: ').upper()
if estado_civil == 'C':
    conjuge = input('Nome do cônjuge: ')
    print(f'O total de caracteres nos nomes lidos é de {len(pessoa + conjuge)}.')
elif estado_civil == 'S':
    print(f'O total de caracteres no nome lido é de {len(pessoa)}.')
else:
    print('Digite apenas "C" ou "S" no estado civil.')
