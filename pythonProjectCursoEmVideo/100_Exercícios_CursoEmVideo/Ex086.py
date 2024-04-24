''' Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre
a matriz na tela, com a formatação correta.'''

m = [0] * 3
for i in range(3):
    m[i] = [0] * 3
    for j in range(3):
        m[i][j] = int(input(f"Digite um valor: "))

for i in range(3):
    for j in range(3):
        print(f"{m[i][j]:02}", end=" ")
    print()

# ou
m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0,3):
    for j in range(0,3):
        m[i][j] = int(input(f"Digite um valor para [{i},{j}]: "))

for i in range(0,3):
    for j in range(0,3):
        print(f"{m[i][j]:02}", end=" ")
    print()