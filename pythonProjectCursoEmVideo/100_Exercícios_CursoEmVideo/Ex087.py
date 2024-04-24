''' Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''


spar = scol3 = maior = 0
m = [0] * 3
for i in range(3):
    m[i] = [0] * 3
    for j in range(3):
        m[i][j] = int(input(f"Digite um valor para [{i},{j}]: "))

for i in range(3):
    for j in range(3):
        print(f"{m[i][j]:02}", end=" ")
        if m[i][j] % 2 == 0:
            spar += m[i][j]
        if j == 2:
            scol3 += m[i][2]
        if i == 0:
            maior = m[1][j]
        elif m[1][j] > maior:
            maior = m[1][j]
    print()

print('Soma dos pares =',spar)
print('Soma da 3a coluna =', scol3)
print('Maior da 2a linha =',maior)