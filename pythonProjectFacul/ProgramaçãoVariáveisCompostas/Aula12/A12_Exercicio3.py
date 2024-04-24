''' Elabore um programa que leia uma matriz 5x5 e mostre os elementos do triângulo inferior esquerdo da matriz
(elementos abaixo da diagonal principal). '''

a = [0] * 5
print("Insira os elementos da matriz: ")
for i in range(5):
    a[i] = [0] * 5
    for j in range(5):
        a[i][j] = int(input())

print("Triângulo inferior esquerdo: ")
for i in range(5):
    for j in range(5):
        if i > j:
            print(a[i][j])


'''
OU
for i in range(1,5):
    for j in range(i):
        print(a[i][j])
'''