# Algoritmo para ler uma matriz 5x5 e mostrar os elementos da diagonal principal.

a = [0] * 5
print("Digite os elementos da matriz:")
for i in range(5):
    a[i] = [0] * 5
    for j in range(5):
        a[i][j] = int(input())

print("Diagonal Principal:")
for i in range(5):
    for j in range(5):
        if i == j:
            print(a[i][j])

'''
ou 
for i in range(5):
    print(a[i][i])
'''