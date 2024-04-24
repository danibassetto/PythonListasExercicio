'''
Formas de criar uma matriz
- M = [[1,2,3],[4,5,6]]
- M = [0] * 2
	for i in range(2):
	      M[i] = [0] * 3
            for j in range(3):
                 M[i][j] = 0
- M = [0] * 2
	M[0] = [0,0,0]
	M[1] = [0,0,0]

-----------------------------------------------------------------
                    DECLARAÇÃO DE MATRIZ:

<identificadorMatriz> = [ 0 ] * n
<identificadorMatriz>[ 0 ] =  [ 0 ] * m
<identificadorMatriz>[ 1 ] =  [ 0 ] * m
<identificadorMatriz>[ 2 ] =  [ 0 ] * m


<ident1> = [ 0 ] * n
<ident2> = [ 0 ] * n
<ident3> = [ 0 ] * n
<identificadorMatriz> = [<ident1>, <ident2>, <ident3>]


Exemplo:

matriz = [ 0 ] * 3
matriz [ 0 ] = [1,2,3,4,5]
matriz [ 1 ]  = [11,22,33,44,55]
matriz [ 2] = [111,222,333,444,555]

ou

matriz = [ 0 ] * 3
matriz [ 0 ] = [ 0 ] * 5
matriz [ 1 ]  = [ 0 ] * 5
matriz [ 2] =  [ 0 ] * 5



'''

M = [[1, 2, 3], [4, 5, 6]]
print(M)

M = [0] * 2
for i in range(2):
    M[i] = [0] * 3
    for j in range(3):
        M[i][j] = 0
print(M)

M = [0] * 2
M[0] = [0, 0, 0]
M[1] = [0, 0, 0]
print(M)

from random import randint

M = [0] * 5
for i in range(5):
    M[i] = [0] * 5
    for j in range(5):
        M[i][j] = randint(1,20)
        print(f'{M[i][j]:02}', end= ' ')
    print()

from termcolor import colored

M = []
for i in range(5):
    M.append([])
    for j in range(5):
        M[i].append(randint(1,20))
        print(f'{M[i][j]:02}', end= ' ')
    print()

print('Diagonal Principal')
for i in range(5):
    for j in range(5):
        if i == j:
            print(colored(f'{M[i][j]:02}','red'), end=' ')
        else:
            print(f'{M[i][j]:02}', end= ' ')
    print()