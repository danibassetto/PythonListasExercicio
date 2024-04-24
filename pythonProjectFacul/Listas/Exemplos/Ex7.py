'''
Faça um programa em python que gere uma lista de 10 número aleatórios entre 1 e 50 e mostre quais são os dois maiores
valores da lista e suas posições originais
'''
import random

L = [0] * 10
for i in range(10):
    L[i] = random.randint(1, 50)
print("L =", L)

for i, n in enumerate(L):
    if n == max(L):
        print("Maior número:", n, "Posição:", i)
        L[i] = 0
        for i, n in enumerate(L):
            if n == max(L):
                print("Segundo maior número:", n, "Posição:", i)
            break

'''
from random import randint
L = []
for i in range(10):
    L.append(randint(1,20))
print(L)
M = L.copy()
pM = max(M)
M.remove(pM)
sM = max(M)
print(f'O 1º maior é {pM} na posição {L.index(pM)}')
print(f'O 2º maior é {sM} na posição {L.index(sM)}')

M = sorted(L)
pM = M[-1]
sM = M[-2]
print(f'O 1º maior é {pM} na posição {L.index(pM)}')
print(f'O 2º maior é {sM} na posição {L.index(sM)}')
'''

'''
import random

L = []

for i in range(10):
    L.append(random.randint(1, 50))

M = sorted(L)

print(L)

print(f"O primeiro maior: {M[-1]} na posição {L.index(M[-1])}")

print(f"O segundo maior: {M[-2]} na posição {L.index(M[-2])}")
'''