''' Elabore um programa que leia uma matriz 5x5 e mostre os elementos do triângulo inferior direito da matriz (elementos
abaixo da diagonal secundária).'''

a = [0] * 5
print("Insira os valores da matriz:")
for i in range(5):
    a[i] = [0] * 5
    for j in range(5):
        a[i][j] = int(input())
print("Triângulo inferior direito: ")
for i in range(1,5):
    for j in range(5-1,5):
        print(a[i][j])
