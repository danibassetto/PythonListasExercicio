#inserindo valores sobrepondo a posição
L = [0] * 5
for i in range(3):
    L[i] = int(input(f'{i+1}º valor >> '))
print('Valores >>',L)

#inserindo valores no final da lista com append
L = []
for i in range(5):
    L.append(int(input(f'{i+1}º valor >> ')))
print('Valores >>',L)

#inserindo valores aleatórios na lista om append
from random import randint
L = []
for i in range(5):
    L.append(randint(1,50))
print('Valores >>',L)