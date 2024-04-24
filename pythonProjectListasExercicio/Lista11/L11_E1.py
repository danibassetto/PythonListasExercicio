'''
Faça um programa que gere uma lista de 20 números aleatórios entre 1 e 10. Leia um número x entre
1 e 10. Imprima a lista e mostre quantos números iguais a x tem na lista
'''
import random

L = [0] * 20
for i in range(20):
    L[i] = random.randint(1, 10)

x = int(input("Informe um número de 1 a 10: "))

print("Lista13 =", L)
print(f"Quantidade de número(s) {x}: {L.count(x)}")


'''
from random import randint
L = []
for i in range(20):
    L.append(randint(1,10))
print(L)
x = randint(1,10)
print(f'Há {L.count(x)} números {x} na lista')
'''