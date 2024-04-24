'''Elabore um programa que leia uma matriz 5x5 e mostre os elementos do triângulo superior esquerdo da matriz (elementos
acima da diagonal secundária '''

a = [0] * 5
print("Insira os valores da matriz:")
for i in range(5):
    a[i] = [0] * 5
    for j in range(5):
        a[i][j] = int(input())
print("Triângulo superior esquerdo: ")
for i in range(4):
    for j in range(4-i):
        print(a[i][j])
