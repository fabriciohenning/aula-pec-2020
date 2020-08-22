print('Quantos segundos se passaram desde a meia-noite?')
print()
h = int(input('Digite quantas horas se passaram (no formato de 24h): '))
m = int(input('Digite os minutos: '))
s = int(input('Digite os segundos:'))
s = h * 3600 + m * 60 + s
print(f'Passaram-se {s} segundos desde a meia-noite.')
