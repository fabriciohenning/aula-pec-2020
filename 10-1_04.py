texto = str(input('Digite um texto: ')).strip()
qtd_a = qtd_e = qtd_i = qtd_o = qtd_u = 0
vogais = {}
for c in texto:
    if c in 'aáàâãAÁÀÂÃ':
        qtd_a += 1
    if c in 'eéèêEÉÈÊ':
        qtd_e += 1
    if c in 'iíìîIÍÌÎ':
        qtd_i += 1
    if c in 'oóòôõOÓÒÔÕ':
        qtd_o += 1
    if c in 'uúùUÚÙ':
        qtd_u += 1
vogais['a'] = qtd_a
vogais['e'] = qtd_e
vogais['i'] = qtd_i
vogais['o'] = qtd_o
vogais['u'] = qtd_u
print(f"Quantidade de vogal a: {vogais['a']}")
print(f"Quantidade de vogal e: {vogais['e']}")
print(f"Quantidade de vogal i: {vogais['i']}")
print(f"Quantidade de vogal o: {vogais['o']}")
print(f"Quantidade de vogal u: {vogais['u']}")
