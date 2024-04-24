''' Elabore um programa em Python que gere uma matriz 4x6 e calcule e mostre a sua matriz
transposta equivalente. '''

from random import randint

print("="*30)
print("Matriz gerada")
print("="*30)
A = [0] * 4
for i in range(4):
    A[i] = [0] * 6
    for j in range(6):
        A[i][j] = randint(1,50)
        print(f"{A[i][j]:02}",end=" ")
    print()

print("="*30)
print("Matriz Transposta")
print("="*30)

B = [0] * 6
for i in range(6):
    B[i] = [0] * 4
    for j in range(4):
        B[i][j] = A[j][i]
        print(f"{B[i][j]:02}", end=" ")
    print()