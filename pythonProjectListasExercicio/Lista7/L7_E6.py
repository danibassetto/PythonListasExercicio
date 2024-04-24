''' Elabore um programa em Python que gere uma matriz 5x5 e calcule e mostre a diagonal
principal e a secundária '''

from random import randint

M = [0] * 5
for i in range(5):
    M[i] = [0] * 5
    for j in range(5):
        M[i][j] = randint(1,50)
        print(f"{M[i][j]:02}", end=" ")
    print()

#Imprimindo a Diagonal Principal
print("Diagonal Principal: ")
for i in range(5):
    print(f"{M[i][i]:2}", end=" ")

#Imprimindo a Diagonal Secundária
print("\nDiagonal Secundária: ")
for i in range(5):
    print(f"{M[i][4-i]:2}", end=" ")