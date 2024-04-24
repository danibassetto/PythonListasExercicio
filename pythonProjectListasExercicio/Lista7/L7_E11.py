''' Faça um programa em Python que gere uma matriz M[10][10] com números aleatórios de 1
a 50 e copie para um vetor de 10 elementos, os números da diagonal principal. Imprima a
matriz e o vetor.'''

from random import randint

v = []
M = [0] * 10
for i in range(10):
    M[i] = [0] * 10
    for j in range(10):
        M[i][j] = randint(1,50)
        print(f"{M[i][j]:02}", end=" ")
    print()

print('-=' * 20)

#Imprimindo a Diagonal Principal
print("Diagonal Principal: ")
for i in range(10):
    v.append(M[i][i])
print(v)