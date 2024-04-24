''' Elabore um algoritmo que em uma matriz 8x8, leia as coordenadas iniciais de um Bispo do Xadrez e mostre os
possíveis movimentos. Para isso, crie a matriz toda zerada e coloque o valor 1 nos lugares possíveis de seus movimentos.'''

a = [0] * 8
for i in range(8):
    a[i] = [0] * 8

L = int(input("Digite a linha onde a torre está: "))
C = int(input("Digite a coluna onde a torre está: "))

for i in range(8):
    for j in range(8):
        if (i + j == L + C) or (i - j == L - C):
            a[i][j] = 1

print("Bispo: ")
for i in range(8):
    print(a[i])