'''
Faça um programa em Python para gerar uma lista de 20 números aleatórios entre 1 e 50. Imprima a
lista. Após isto, deverá ser lido um número qualquer e verificar se esse número existe na lista ou não.
Se existir, gerar uma nova lista sem esse número (remova todas as ocorrências do número). Imprima
a nova lista
'''
import random

L = [0] * 20
for i in range(20):
    L[i] = random.randint(1,50)
print("Lista13 =", L)

x = int(input("Informe um número: "))

if x in L:
    for i in range(L.count(x)):
        L.remove(x)
    print("Lista13 após remoção =", L)
else:
    print("Valor não encontrado!")

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
