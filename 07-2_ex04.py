# O número é primo ou não?
num = int(input('Digite um número: '))
divisores = 0
for c in range(1, num + 1):
    if num % c == 0:
        divisores += 1
if divisores == 2:
    print(f'{num} é um número primo.')
else:
    print(f'{num} não é um número primo.')
