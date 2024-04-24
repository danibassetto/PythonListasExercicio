''' Faça um programa em Python que gere 10 números aleatórios (entre 1 e 50), armazene-os em uma lista.
Imprima os números e calcule quantos são números pares e quantos são números ímpares. '''

import random

L = [0] * 10
for i in range(10):
    L[i] = random.randint(1,50)
print(f"L = {L}")

par = 0
impar = 0
for i in L:
    if i % 2 == 0:
        par += 1
    else:
        impar += 1
print("Pares:",par,"\nÍmpares:",impar)