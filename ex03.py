num = int(input('Digite um número inteiro entre 10 e 99: '))
digito_impar = 0
if 10 <= num <= 99:
    u = num // 1 % 10
    if u % 2 != 0:
        digito_impar = digito_impar + 1
    d = num // 10 % 10
    if d % 2 != 0:
        digito_impar = digito_impar +1
    if digito_impar == 0:
        print('Nenhum dígito é ímpar.')
    elif digito_impar == 1:
        print('Apenas um dígito é ímpar.')
    elif digito_impar == 2:
        print('Os dois dígitos são ímpares.')
