'''
Faça um programa em Python que gere 20 números aleatórios (entre 1 e 50), armazene-os em uma lista.
Imprima os números e imprima todos os números múltiplos de um número digitado pelo usuário.
'''
import random

n = int(input("Insira um número para encontrar seus múltiplos na lista: "))

L = [0] * 20
for i in range(20):
    L[i] = random.randint(1,50)
print("L =",L)

print()
print(f"Múltiplos de {n} encontrados: ", end='')
for i in L:
    if i % n == 0:
        print(i, end=' ')