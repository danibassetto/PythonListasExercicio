'''
Faça um programa em Python que gere 20 números aleatórios (entre 1 e 50), armazene-os em uma lista.
Imprima os números e imprima todos os números múltiplos de 5.
'''
import random

L = [0] * 20
for i in range(20):
    L[i] = random.randint(1,50)
print("L =",L)

print("Múltiplos de 5: ", end='')
for i in L:
    if i % 5 == 0:
        print(i, end=' ')