'''
Faça um programa em Python que gere 20 elementos aleatórios (entre 1 e 50) armazenando no vetor A e crie
outros 2 vetores B e C. O vetor B deve ter apenas os números pares e o vetor C deve conter apenas os números ímpares.
Imprima os três vetores.
'''

import random

A = [0] * 20
for i in range(20):
    A[i] = random.randint(1,50)
print("A =",A)

B = []
C = []
for i in A:
    if i % 2 == 0:  # Inserindo os valores pares em B
        B.append(i)
    else:           # Inserindo os valores ímpares em C
        C.append(i)
print("B =",B,"\nC =",C)

