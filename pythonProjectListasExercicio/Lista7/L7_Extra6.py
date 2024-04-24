# Exercício matriz caracol

n = int(input("Informe o tamanho da matriz >> "))

caracol = [0] * n
for i in range(n):
    caracol[i] = [0] * n

c = 1
ini = 0
fim = n
while c <= n**2: # enquanto o contador for menor que o len da matriz
    for i in range(ini, fim):  # esquerda para direita
        caracol[ini][i] = c
        c += 1
    for i in range(ini+1, fim):  # cima para baixo
        caracol[i][fim-1] = c
        c += 1
    for i in range(fim-2, ini-1, -1):  # direita para esquerda
        caracol[fim-1][i] = c
        c += 1
    for i in range(fim-2, ini, -1): # baixo para cima
        caracol[i][ini] = c
        c += 1
    ini += 1
    fim -= 1

for i in range(n):
    for j in range(n):
        print(f'{caracol[i][j]:3}', end=' ')
    print()
