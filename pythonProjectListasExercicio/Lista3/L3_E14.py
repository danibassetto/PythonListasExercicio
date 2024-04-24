# Jogo do bicho
from random import randint

print('Entre com os dois grupos da aposta')
dg1 = int(input('1º grupo da dupla de grupo [1 a 25] >> '))
dg2 = int(input('2º grupo da dupla de grupo [1 a 25] >> '))
if 1<=dg1<=25 and 1<=dg2<=25:
    m1 = randint(0,9999)
    m2 = randint(0,9999)
    m3 = randint(0,9999)
    m4 = randint(0,9999)
    m5 = randint(0,9999)
    g1 = (m1 - 1) % 100 // 4 + 1
    g2 = (m2 - 1) % 100 // 4 + 1
    g3 = (m3 - 1) % 100 // 4 + 1
    g4 = (m4 - 1) % 100 // 4 + 1
    g5 = (m5 - 1) % 100 // 4 + 1
    print('Milhares   Grupo')
    print(f'{m1:04}       {g1:02}')
    print(f'{m2:04}       {g2:02}')
    print(f'{m3:04}       {g3:02}')
    print(f'{m4:04}       {g4:02}')
    print(f'{m5:04}       {g5:02}')
    if dg1 in [g1,g2,g3,g4,g5] and dg2 in [g1,g2,g3,g4,g5]:
        print('GANHOU!!!')
    else:
        print('PERDEU!!!')
else:
    print('Algum grupo inválido!!')
