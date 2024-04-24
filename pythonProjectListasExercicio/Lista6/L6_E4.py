''' Faça um programa em Python que gere um vetor com N elementos e ordene utilizando o
método BubbleSort e pelo método sort. Faça a comparação de tempo para a ordenação
(imprima o tempo de ordenação de cada método) do mesmo conjunto de elementos.
Faça teste para vários valores de N. '''

import time, random

n = int(input("Informe o número de elementos que o vetor deve ter: "))
vai = int(input("Qual será o valor máximo de um elemento? "))
v = [] * n
V = [] * n
for i in range(n):
    num = random.randint(1, vai)
    v.append(num)
    V.append(num)

# Verificando tempo do sort
inicio = time.time()
v.sort()
print("Vetor sort =", v)
fim = time.time()
print(f"Tempo: {fim - inicio:.2f} s")

# Verificando tempo do bubble sort
inicio = time.time()
for i in range(n):
    for j in range(i+1, n):
        if V[i] > V[j]:
            V[i], V[j] = V[j], V[i]
print("Vetor bubble sort =", V)
fim = time.time()
print(f"Tempo: {fim - inicio:.2f} s")


'''
from random import randint
from time import time

N = int(input('Informe a quantidade de elementos >> '))
L = []
for i in range(N):
    L.append(randint(1,N))
M = L[:]

ini = time()
#bubbleSort
for i in range(N):
    for j in range(i+1,N):
        if L[i] > L[j]:
            L[i], L[j] = L[j], L[i]
fim = time()
print('Tempo de ordenação pelo BubbleSort >>',fim-ini)

ini = time()
M.sort()
fim = time()
print('Tempo de ordenação pelo sort() >>',fim-ini)
'''