'''
Faça um programa que leia um arquivo que contenha as dimensões de uma matriz (linha e coluna), a
quantidade de posições que serão anuladas, e as posições a serem anuladas (linha e coluna). O
programa lê esse arquivo e, em seguida, produz um novo arquivo com a matriz com as dimensões
dadas no arquivo lido, e todas as posições especificadas no arquivo zeradas e o restante recebendo o
valor 1.
Ex: arquivo “matriz.txt”
3 3 2 /* 3 e 3 dimensões da matriz e 2 posições que serão anuladas*/
1 0
1 2 /*Posições da matriz que serão anuladas.
arquivo “matriz saida.txt”
saída:
1 1 1
0 1 0
1 1 1
'''

try:
    matriz = open('matriz.txt','r')
    line = matriz.readline()
    lin, col, pos = list(map(int, line.split()))
    M = [[1 for i in range(lin)] for j in range(col)]
    for i in range(pos):
        line = matriz.readline()
        l, c = list(map(int,line.split()))
        M[l][c] = 0
    matriz.close()
    matriz = open('matriz saida.txt','w')
    for i in range(lin):
        for j in range(col):
            matriz.write(f'{M[i][j]} ')
        matriz.write('\n')
    matriz.close()
except:
    print('ERRO')