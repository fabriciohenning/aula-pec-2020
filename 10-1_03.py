adultos = {}
menores = {}

# Lista que vai conter as chaves das pessoas menores de 18 anos
indices = []

for c in range(20):
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    CPF = str(input('CPF: ')).strip()
    pessoa = nome, idade
    adultos[CPF] = pessoa

for CPF in adultos:
    nome, idade = adultos[CPF]
    if idade < 18:
        menor = nome, idade
        menores[CPF] = menor
        indices.append(CPF)

for CPF in indices:
    del adultos[CPF]

print('========== MAIORES DE 18 ANOS ==========')
for CPF in adultos:
    nome, idade = adultos[CPF]
    print(f'{nome};{idade};{CPF}')

print('========== MENORES DE 18 ANOS ==========')
for CPF in menores:
    nome, idade = menores[CPF]
    print(f'{nome};{idade};{CPF}')
