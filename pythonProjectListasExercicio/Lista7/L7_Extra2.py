'''
Na teoria dos sistemas, define-se como elemento minimax de uma matriz o menor
elemento da linha onde se encontra o maior elemento da matriz. Escreva um programa
em Python que gere uma matriz 10 X 10 de números aleatórios entre 1 e 99, imprima a
matriz e encontre seu elemento minimax, imprimindo-o e mostrando também sua
posição.
'''
from random import randint
menor = 100
m = []
for i in range(10):
    m.append([])
    for j in range(10):
        m[i].append(randint(1,99))
        if m[i][j] < menor:
            menor = m[i][j]
            linha = i
        print(f'{m[i][j]:02}', end=' ')
    print()

maior = 0
for j in range(10):
    if m[linha][j] > maior:
        maior = m[linha][j]
        coluna = j
print(f'Minimax = {maior}, na linha {linha} e coluna {coluna}')