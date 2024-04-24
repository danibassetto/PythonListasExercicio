''' Faça um programa em Python que gere uma matriz 5x5 com valores entre 1 e 50. Imprima a
matriz e troque uma linha por outra linha informada pelo usuário. Mostre a matriz após a
troca. '''
import random

print("--- MATRIZ ---")
m = [0] * 5
for i in range(5):
    m[i] = [0] * 5
    for j in range(5):
        m[i][j] = random.randint(1,50)
        print(f"{m[i][j]:02}", end=' ')
    print()

print()
print("Informe 2 linhas para efetuar a troca entre elas:")
while True:
    linha1 = int(input("Linha 1 >> "))
    if linha1 in range(5):  # Verificando se existe
        break
    print("Valor inválido! Informe uma linha de 0 a 4.")
while True:
    linha2 = int(input("Linha 2 >> "))
    if linha2 in range(5):  # Verificando se existe
        break
    print("Valor inválido!! Informe uma linha de 0 a 4.")

m[linha1], m[linha2] = m[linha2], m[linha1]  # Trocando as linhas!

print('=-' * 20)
print(f"Matriz com as linhas {linha1} e {linha2} trocadas")
for i in range(5):  # Imprimindo a nova matriz
    for j in range(5):
        print(f"{m[i][j]:02}", end = " ")
    print()


