'''Faça um programa em Python que gere uma matriz 10 x 10 de inteiros e crie funções para calcular
e retornar o maior elemento de uma determinada coluna (informada por parâmetro) e o menor
elemento de uma determinada linha (informada por parâmetro). Peça a coluna e a linha, chame
os respectivos métodos e mostre o resultado'''

import random
from random import randint


def geraMatriz():
    M = []
    for i in range(10):
        M.append([])
        for j in range(10):
            M[i].append(randint(1, 50))
    return M


def imprimeMatriz(M):
    for i in range(10):
        for j in range(10):
            print(f"{M[i][j]:3}", end="")
        print()


def maiorCol(M, c):
    maior = M[0][c]
    for i in range(1, 10):
        if M[i][c] > maior:
            maior = M[i][c]
    return maior


def menorLin(M, l):
    menor = M[l][0]
    for i in range(1, 10):
        if M[l][i] < menor:
            menor = M[l][i]
    return menor


mat = geraMatriz()
imprimeMatriz(mat)
while True:
    coluna = int(input("Informe a coluna para calcular o maior valor >> "))
    if coluna < 1 or coluna > 10:
        print("Valor inválido para coluna, informe no intervalo de 1 a 10")
    else:
        break
mc = maiorCol(mat, coluna - 1)
print(f"O maior valor da coluna {coluna} é {mc}")

while True:
    linha = int(input("Informe a linha para calcular o menor valor >> "))
    if linha < 1 or linha > 10:
        print("Valor inválido para linha, informe no intervalo de 1 a 10")
    else:
        break
