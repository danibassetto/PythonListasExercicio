''' Faça um programa recursivo em Python para verificar se um determinado valor está contido em um vetor de 10 posições.
Gerar o vetor aleatoriamente. '''

from random import randint


def busca(l, elem):
    if l[0] == elem:
        return True
    if len(l) == 1:
        return False
    return busca(l[1:], elem)


L = []
for i in range(10):
    L.append(randint(1,30))
print(L)
x = randint(1, 30)
print("Número da busca >> ", x)
if busca(L, x):
    print(f"{x} pertence a lista")
else:
    print(f"{x} não pertence a lista")