# Ordem crescente de 3 números
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
if n1 < n2 < n3:
    print(n1)
    print(n2)
    print(n3)
elif n1 < n3 < n2:
    print(n1)
    print(n3)
    print(n2)
elif n2 < n1 < n3:
    print(n2)
    print(n1)
    print(n3)
elif n2 < n3 < n1:
    print(n2)
    print(n3)
    print(n1)
elif n3 < n1 < n2:
    print(n3)
    print(n1)
    print(n2)
elif n3 < n2 < n1:
    print(n3)
    print(n2)
    print(n1)
