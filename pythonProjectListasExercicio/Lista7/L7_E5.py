''' Faça um programa em Python que gere uma matriz 10 x 10 de inteiros entre 1 e 50,
imprima a matriz e o menor elemento de cada coluna.'''

from random import randint
m = [0] * 10
for i in range(10):
    m[i] = [0] * 10
    for j in range(10):
        m[i][j] = randint(1,50)
        print(f"{m[i][j]:02}", end=' ')
    print()

print("Menor de cada coluna: ")
for i in range(10):
    menor = 51
    for j in range(10):
        if m[j][i] < menor:  # m[j][i] significa que ele fixa o i e anda pelo j
            menor = m[j][i]
    print(f"{menor:02}", end=' ')