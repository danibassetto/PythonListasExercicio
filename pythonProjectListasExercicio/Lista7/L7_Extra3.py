'''
Faça um programa para gerar automaticamente números entre 1 e 75 de uma cartela
de bingo. Sabendo que cada cartela deverá conter 5 linhas de 5 números, cartelas nas
quais cada coluna contém 5 números e é associada a uma letra da palavra BINGO. Os
números são dispostos nas 5 colunas da cartela, divididos em grupos de 15 (por
exemplo, na coluna B só aparecerão os números de 1 a 15) . O ponto central é o coringa.
Gere estes dados de modo a não ter números repetidos dentro das cartelas. O
programa deve exibir na tela a cartela gerada.
'''

from random import randint
from termcolor import colored

bingo = []
ini = 1
fim = 15
for i in range(5):
    j = 0
    bingo.append([])
    while j < 5:
        x = randint(ini, fim)
        if x not in bingo[i]:
            bingo[i].append(x)
            j += 1
    ini += 15
    fim += 15

bingo[2][2] = colored('🍀','green')

print('\033[31;1m B  I  N  G  O\033[m')
for i in range(5):
    for j in range(5):
        print(f"{bingo[j][i]:2}",end=" ")
    print()