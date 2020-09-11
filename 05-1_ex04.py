# Sequência de 10 em 10, até 1000
for n in range(10, 1001, 10):
    if n != 1000:
        print(n, end=', ')
    else:
        print(n, end='.')
