'''
Faça um programa em Python que gere 20 números aleatórios (entre 1 e 50), armazene-os em uma lista.
Imprima os números e calcule a média apenas dos números pares.
'''
import random

L = [0] * 20
for i in range(20):
    L[i] = random.randint(1,50)
print("L =",L)

soma_pares = 0
pares = 0
print("Números pares da lista: ", end='')
for i in L:
    if i % 2 == 0:
        print(i, end=' ')
        soma_pares += i
        pares += 1

media = soma_pares / pares
print(f"\nMédia dos pares = {media:.2f}")