s = int(input('Qual o tempo de duração do evento nessa fábrica, em segundos? '))
h = s // 3600
m = (s % 3600) // 60
resto_s = (s % 3600) % 60
print(f'{s} segundos corresponde a {h}h:{m}m:{resto_s}s.')
