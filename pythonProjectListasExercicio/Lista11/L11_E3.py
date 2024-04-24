'''
Gere uma lista 20 números aleatórios entre 1 e 50 e mostre qual o maior valor da lista, o menor e a
média dos valores.
'''
import random

L = [0] * 20
for i in range(20):
    L[i] = random.randint(1,50)
print("Lista13 =", L)
print("Maior valor =", max(L))
print("Menor valor =", min(L))
print(f"Média dos valores = {(sum(L)/20)}")

'''
from random import randint
L = []
for i in range(20):
    L.append(randint(1,50))
L.sort()
print(L)
x = int(input('Informe um número -> '))
if x in L:
    for i in range(L.count(x)):
        L.remove(x)
    print(L)
else:
    print(f'O número {x} não pertence a lista')
'''