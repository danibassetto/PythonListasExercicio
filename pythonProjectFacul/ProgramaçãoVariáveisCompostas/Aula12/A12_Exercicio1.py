''' Elabore um programa que leia uma matriz 5x5 e calcule e mostre a diagonal secundária. '''

a = [0] * 5
print("Insira os elementos da matriz: ")
for i in range(5):
    a[i] = [0] * 5
    for j in range(5):
        a[i][j] = int(input())

print("Diagonal secundária: ")
for i in range(5):
    for j in range(5):
        if i + j == 4:
            print(a[i][j])

'''
OU
for i in range(5):
    print(a[i][4-i])
'''