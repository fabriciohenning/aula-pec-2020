cor = str(input('Cor do sinal de trânsito:\nDigite V, se verde; A, se amarelo ou E, se vermelho: ')).upper()
if cor == 'V':
    print('Siga.')
if cor == 'A':
    print('Atenção!')
if cor == 'E':
    print('Pare!')
