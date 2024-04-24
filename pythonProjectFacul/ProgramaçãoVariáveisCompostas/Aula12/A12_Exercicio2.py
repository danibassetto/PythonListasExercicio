''' Elabore um programa que leia uma matriz 5x5 e mostre os elementos do triângulo superior direito da matriz
(elementos acima da diagonal principal). '''

a = [0] * 5
print("Insira os elementos da matriz: ")
for i in range(5):
    a[i] = [0] * 5
    for j in range(5):
        a[i][j] = int(input())

print("Triângulo superior direito: ")
for i in range(5):
    for j in range(5):
        if i < j:
            print(a[i][j])

'''
OU
for i in range(5):
    for j in range(i+1, 5):
        print(a[i][j])
'''