'''
Faça um programa que gere uma matriz qualquer com números aletórios e uma função para
horizontalizar uma matriz. Objetivo: pegar uma matriz e retornar uma lista onde cada linha segue
a outra.
'''


# Código com loop tradicional
def horizontalizar_trad(matriz):
    flat = []
    for row in matriz:
        for x in row:
            flat.append(x)
    return flat


# Código com compreensão de listas
def horizontalizar_cl(matriz):
    return [x for row in matriz for x in row]


from random import randint

M = []
for i in range(5):
    M.append([])
    for j in range(5):
        M[i].append(randint(1, 20))
        print(f'{M[i][j]:3}', end='')
    print()

L = horizontalizar_cl(M)
print(L)

# Gerando a matriz e horizontalizando a matriz usando compreensão de lista
M = [[randint(1, 20) for i in range(5)] for j in range(5)]
print(M)
L = [M[i][j] for i in range(5) for j in range(5)]
# ou
L = [x for row in M for x in row]
print(L)
