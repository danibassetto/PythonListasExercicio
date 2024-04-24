''' Elabore um programa em Python que gere uma matriz aleatória (9x9), com números entre 0 e 10, imprima-a. Após, peça
o quadrante desejado e imprima os elementos desse quadrante. '''

from random import randint

from termcolor import colored

m = [0] * 9
for i in range(9):
    m[i] = [0] * 9
    for j in range(9):
        m[i][j] = randint(0,10)
        if i == 4 or j == 4:  # Criando a "divisão" entre os quadrantes
            print(colored(f"{m[i][j]:02}","blue"),end=" ")
        else:
            print(f"{m[i][j]:02}",end=" ")
    print()

while True:
    quadrante = int(input("\nInforme o quadrante [1-4] >> "))
    if quadrante in range(1,5):
        break
    print("Valor inválido!! Digite novamente...")

if quadrante == 1:
    for i in range(4):
        for j in range(4):
            print(f"{m[i][j]:02}", end=" ")
        print()
elif quadrante == 2:
    for i in range(4):
        for j in range(5,9):
            print(f"{m[i][j]:02}", end=" ")
        print()
elif quadrante == 3:
    for i in range(5,9):
        for j in range(4):
            print(f"{m[i][j]:02}", end=" ")
        print()
else:
    for i in range(5,9):
        for j in range(5,9):
            print(f"{m[i][j]:02}", end=" ")
        print()

''' 
from random import randint
from termcolor import colored

m = []
for i in range(9):
    m.append([])
    for j in range(9):
        m[i].append(randint(0,10))
        print(f'{m[i][j]:02}', end=' ')
    print()

while True:
    q = int(input('\nInforme o quadrante >> '))
    if 1 <= q <= 4:
        break
    print('Quadrante inválido. Digite um valor entre 1 e 4')

print()
if q == 1:
    for i in range(9):
        for j in range(9):
            if i < 4 and j < 4:
                print(colored(f'{m[i][j]:02}','red'), end=' ')
            else:
                print(f'{m[i][j]:02}', end=' ')
        print()
elif q == 2:
    for i in range(9):
        for j in range(9):
            if i < 4 and j > 4:
                print(colored(f'{m[i][j]:02}','red'), end=' ')
            else:
                print(f'{m[i][j]:02}', end=' ')
        print()
elif q == 3:
    for i in range(9):
        for j in range(9):
            if i > 4 and j < 4:
                print(colored(f'{m[i][j]:02}','red'), end=' ')
            else:
                print(f'{m[i][j]:02}', end=' ')
        print()
else:
    for i in range(9):
        for j in range(9):
            if i > 4 and j > 4:
                print(colored(f'{m[i][j]:02}','red'), end=' ')
            else:
                print(f'{m[i][j]:02}', end=' ')
        print()
'''