contatos = {}
numeracao = 0
quantidade = int(input('Digite a quantidade de contatos que deseja adicionar: '))

for cont in range(quantidade):
    nome = str(input('Nome: ')).strip()
    cidade = str(input('Cidade: ')).strip()
    estado = str(input('Estado: ')).strip()
    telefone = input('Telefone: ')
    numeracao += 1
    contato = nome, cidade, estado, telefone
    contatos[numeracao] = contato

for numeracao in contatos:
    nome, cidade, estado, telefone = contatos[numeracao]
    espacamento = 26 - len(cidade)
    print(f'{nome:25}{cidade}({estado}){espacamento * " "}{telefone}')
