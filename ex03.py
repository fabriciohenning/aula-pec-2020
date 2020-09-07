n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
n3 = int(input('3º número: '))
n4 = int(input('4º número: '))
n5 = int(input('5º número: '))
maior = n1
if n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
    maior = n2
if n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
    maior = n3
if n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
    maior = n4
if n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
    maior = n5
print(f'Dentre os 5 números digitados, o maior é {maior};')
menor = n1
if n2 < n1 and n2 < n3 and n2 < n4 and n2 < n5:
    menor = n2
if n3 < n1 and n3 < n2 and n3 < n4 and n3 < n5:
    menor = n3
if n4 < n1 and n4 < n2 and n4 < n3 and n4 < n5:
    menor = n4
if n5 < n1 and n5 < n2 and n5 < n3 and n5 < n4:
    menor = n5
print(f'E dentre os mesmos números, o menor é {menor}.')
