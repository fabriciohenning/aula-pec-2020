num = int(input('Digite um número inteiro entre 100 e 999: '))
digito_par = 0
if 100 <= num <= 999:
    u = num // 1 % 10
    if u % 2 == 0:
        digito_par = digito_par + 1
    d = num // 10 % 10
    if d % 2 == 0:
        digito_par = digito_par + 1
    c = num // 100 % 10
    if c % 2 == 0:
        digito_par = digito_par + 1
    print(f'O número {num} tem {digito_par} digito(s) par(es).')
