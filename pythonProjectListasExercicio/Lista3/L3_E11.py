#Jogo Caça Níqueis

import random
resp = 'S'
while resp == 'S':
    valor_apostado = float(input('Digite o valor apostado: '))
    print('-' * 50)
    n1 = random.randint(1,99)
    print('Primeiro número sortedo:',n1)
    n2 = random.randint(1,99)
    print('Segundo número sorteado:',n2)
    n3 = random.randint(1,99)
    print('Terceiro número sorteado:',n3)
    print('-' * 50)

    if n1 != n2 != n3:
        print('GAME OVER: Perdeu a aposta!')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        valor_ganho = valor_apostado * 5
        print('Parabéns, dois números iguais!\n Valor final:', valor_ganho)
    elif n1 == n2 == n3:
        valor_ganho = valor_apostado * 100
        print('Parabéns, três números iguais!\n Valor final:', valor_ganho)
    print('-' * 50)
    resp = input('Deseja tentar novamente? [S/N] ').upper()
    print()
print('FIM')