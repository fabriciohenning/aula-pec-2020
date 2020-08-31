caractere = input('Digite um caractere qualquer: ')
if caractere.isnumeric():
    caractere = int(caractere)
    if 0 <= caractere <= 9:
        caractere = True
        print(caractere)
else:
    caractere = False
    print(caractere)
