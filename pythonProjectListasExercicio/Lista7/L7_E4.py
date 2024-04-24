''' Faça um programa em Python que gere uma matriz 10 x 10 de inteiros entre 1 e 50,
imprima a matriz e o menor elemento de cada linha '''

import random

m = [0] * 10
for i in range(10):
    menor = 50  # Vai checar a cada nova linha
    m[i] = [0] * 10
    for j in range(10):
        m[i][j] = random.randint(1, 50)
        if m[i][j] < menor:
            menor = m[i][j]
        print(f'{m[i][j]:02}', end=' ')
    print(f">> menor número: {menor}")

