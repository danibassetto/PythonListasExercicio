''' Faça um programa em Python que gere uma matriz 10 x 10 de inteiros aleatórios entre 1 e
50, imprima a matriz e a média de todos os elementos. '''

import random

soma = 0
m = [0] * 10
for i in range(10):
    m[i] = [0] * 10
    for j in range(10):
        m[i][j] = random.randint(1, 50)
        soma += m[i][j]
        print(f'{m[i][j]:02}', end=' ')
    print()
print("Média de todos elementos:",soma/100)

