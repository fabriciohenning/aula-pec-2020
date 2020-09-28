# Em quanto tempo a população de um país ultrapassa a de outro?
pop_inicial_a = float(input('Informe a população do pais A: '))
pop_inicial_b = float(input('Informe a população do país B: '))
tempo = 0
pop_a = pop_inicial_a
pop_b = pop_inicial_b

if pop_inicial_a > pop_inicial_b:
    while not pop_a <= pop_b:
        tempo = tempo + 1
        pop_a += pop_a * 0.02
        pop_b += pop_b * 0.03
print(f'O tempo necessário para que a população do país B ultrapasse a do país A é de {tempo} anos')

if pop_inicial_a < pop_inicial_b:
    while not pop_a >= pop_b:
        tempo = tempo + 1
        pop_a += pop_a * 0.03
        pop_b += pop_b * 0.02
print(f'O tempo necessário para que a população do país A ultrapasse a do país B é de {tempo} anos')
