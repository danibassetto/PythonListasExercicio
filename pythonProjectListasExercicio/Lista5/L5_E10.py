'''. Faça um programa em Python que gere 10 elementos aleatórios (entre 1 e 50) sem números repetidos.
Imprima o vetor.'''

import random
'''
L = [0] * 10
for i in range(10):
    L[i] = random.randint(1,50)
print(L)

x = set(L)  # set exclui os números iguais
print(x)

lista = list(range(1,50))
#                 lugar, quantidade 
L = random.sample(lista,10)   
print(L)
'''
L = []
while len(L) != 10:
    num = random.randint(1, 50)
    if num not in L:
        L.append(num)
print(L)
