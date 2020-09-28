# A lebre e a tartaruga
vantagem = int(input('Quantos metros a tartaruga sai à frente? '))
distancia_t = vantagem
distancia_l = t = 0

while not distancia_l >= distancia_t:
    # A cada minuto, a tartaruga corre 1m e a lebre corre 10m:
    t += 1
    distancia_t += 1
    distancia_l += 10
print(f'Levará {t} minuto(s) até a lebre alcançar a tartaruga.')
