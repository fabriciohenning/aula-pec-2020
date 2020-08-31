nome = str(input('Qual seu nome: '))
sexo = int(input('Informe seu sexo: (Digite 1 para masculino ou 2 para feminino) '))
if sexo == 1:
    print(f'Ilmo Sr. {nome}.')
elif sexo == 2:
    print(f'Ilma Sra. {nome}.')
else:
    print('Digite apenas 1 ou 2 para informar o sexo da pessoa.')
