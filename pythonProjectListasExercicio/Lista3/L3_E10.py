# Jogo da Roleta (Simulador)

import random
resp = 'S'
while resp == 'S':
    valor_apostado = float(input('Valor da aposta: R$ '))
    numero_apostado = int(input('Valor a ser apostado [1 a 36]: '))

    x = random.randint(1,36)
    print(f'Número sorteado: {x}')
    print('-' * 50)

    if numero_apostado == x:
        valor_ganho = valor_apostado * 5
        print(f'Acertou a aposta!\nValor ganho: {valor_ganho}')
    elif x <= 12 and numero_apostado <= 12 or 13 <= x <= 24 and 13 <= numero_apostado <= 24 or 25 <= x <= 36 and 25 <= numero_apostado <= 36:
        valor_ganho = valor_apostado * 3
        print(f'Acertou a dúzia!\nValor ganho: {valor_ganho}')
    elif (x % 2 == 0) and (numero_apostado % 2 == 0) or (x % 2 != 0) and (numero_apostado % 2 != 0):
        valor_ganho = valor_apostado * 2
        print(f'Acertou a paridade!\nValor ganho: {valor_ganho}')
    else:
        print('Aposta perdida!')
    print('-' * 50)
    resp = input('Deseja apostar novamente? [S/N] ').upper()
    print()