n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
n3 = int(input('3º número: '))
n4 = int(input('4º número: '))
n5 = int(input('5º número: '))
media = (n1 + n2 + n3 + n4 + n5) / 5
print(f'A média desses números é {media:.2f}.')
print('São maiores que a média:')
if n1 > media:
    print(n1)
if n2 > media:
    print(n2)
if n3 > media:
    print(n3)
if n4 > media:
    print(n4)
if n5 > media:
    print(n5)
