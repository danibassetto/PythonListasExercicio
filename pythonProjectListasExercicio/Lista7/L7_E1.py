''' Faça um programa em Python que leia uma matriz 2 x 3 de inteiros, imprima a matriz e a
soma de todos os elementos '''

'''
m = [0] * 2
print("Insira os elementos da matriz: ")
for i in range(2):
    m[i] = [0] * 3
    for j in range(3):
        m[i][j] = int(input())

soma = 0
for i in range(2):
    for j in range(3):
        print(f'{m[i][j]:02}', end=' ')
        soma += m[i][j]
    print()


print("Soma de todos elementos =",soma)
'''

mat = []
soma = 0
for i in range(2):
    mat.append([])
    for j in range(3):
        mat[i].append(int(input(f"[{i}][{j}] >> ")))
        soma += mat[i][j]

print("Números informados: ")
for i in range(2):
    for j in range(3):
        print(f"{mat[i][j]:3}",end="")
    print()
print(f"A soma de todos os números é {soma}")
