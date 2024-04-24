'''
Faça um programa em Python que gere 10 elementos aleatórios (entre 1 e 50) e ordene os números em ordem ascendente.
Imprima o vetor antes e após a ordenação. Pesquise sobre os métodos de ordenação.
'''

import random

print("ANTES DA ORDENAÇÃO: ")
L = [0] * 10
for i in range(10):
    L[i] = random.randint(1,50)
print("L =",L)

print("DEPOIS DA ORDENAÇÃO: ")
print("L =",sorted(L))  # USO DO SORTED PARA ORDENAR EM ORDEM CRESCENTE

''' 
OU Bubble Sort
for i in range(10):
    for j in range(i + 1, 10):
        if L[i] > L[j]:
            L[i], L[j] = L[j], L[i]
'''
