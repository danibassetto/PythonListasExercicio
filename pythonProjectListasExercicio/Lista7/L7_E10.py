''' Escreva um programa em Python que gere uma matriz M[10][10] com números aleatórios
de 1 a 50, peça um número de uma linha qualquer, entre 0 e 9, e copie os elementos dessa
linha para um vetor. Imprima a matriz e o vetor. '''

from random import randint

print("Matriz gerada")
m = []
for i in range(10):
    m.append([])
    for j in range(10):
        m[i].append(randint(1,50))
        print(f"{m[i][j]:2}", end = " ")
    print()

# Pedindo o número e verificando o número inserido
while True:
    linha = int(input("Informe a linha [0 a 9] para fazer uma cópia >> "))
    if linha in range(10):
        break
    print("Número de linha inválida!! Digite um valor entre 0 e 9...")

#Cópia direta da linha da matriz para o vetor
v = m[linha][:]
print(v)

#Cópia de posição por posição da linha da matriz para o vetor
v = []
for i in range(10):
    v.append(m[linha][i])
print(v)




