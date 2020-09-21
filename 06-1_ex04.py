digito = 0
num = int(input('Informe um número inteiro positivo qualquer: '))

while num > 0:
    digito = (digito * 10) + num % 10
    num //= 10

print(f'A sua forma invertida é {digito}.')
