'''
Faça um programa que gere aleatoriamente duas listas de 10 posições (valores entre 1 e 50) e calcule
outra lista contendo, nas posições pares os valores da primeira lista e nas posições ímpares os valores
da segunda lista.
'''
import random


def geraLista():
    L = []
    for i in range(10):
        L.append(random.randint(1, 50))
    return L


a = geraLista()
b = geraLista()
c = []

print(a)
print(b)

for i in range(10):
    c.append(a[i])
    c.append(b[i])
print(c)
