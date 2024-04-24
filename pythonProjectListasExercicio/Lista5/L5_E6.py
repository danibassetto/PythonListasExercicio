'''
Faça um programa em Python que gere 10 elementos aleatórios (entre 1 e 50) armazenando na lista A e um valor x.
Criar o vetor B contendo os elementos do vetor A multiplicados por x. Imprima os dois vetores.
'''

import random

A = [0] * 10
for i in range(10):
    A[i] = random.randint(1,50)
print("A =",A)

x = int(input("Informe o valor que deseja multiplicar os elementos da lista A: "))

B = [0] * 10
for i in range(10):
    B[i] = A[i] * x
print("B =", B)


