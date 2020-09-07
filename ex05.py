p = float(input('Qual o seu peso, em Kg? '))
a = float(input('Qual sua altura, em m? '))
imc = p / (a ** 2)
if imc < 18.5:
    print(f'Seu IMC é {imc:.0f}.\nAbaixo do peso.')
elif 18.5 <= imc < 25:
    print(f'Seu IMC é {imc:.0f}.\nPeso normal.')
elif 25 <= imc < 30:
    print(f'Seu IMC é {imc:.0f}.\nSobrepeso.')
elif 30 <= imc < 35:
    print(f'Seu IMC é {imc:.0f}.\nObeso leve.')
elif 35 <= imc < 40:
    print(f'Seu IMC é {imc:.0f}.\nObeso moderado.')
else:
    print(f'Seu IMC é {imc:.0f}.\nObeso mórbido.')
