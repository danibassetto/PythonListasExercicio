'''
Entrada
A primeira linha contém um número N que representa quantas vezes seu amigo irá apertar algum
interruptor. Na linha seguinte seguirão N números, que pode ser 1, se o interruptor I1 foi apertado, ou 2,
se o interruptor I2 foi apertado.
Saída
Seu programa deve imprimir dois valores, em linhas separadas. Na primeira linha, imprima 1 se a lâmpada
A estiver acesa no final das operações e 0 caso contrário. Na segunda linha, imprima 1 se a lâmpada B
estiver acesa no final das operações e 0 caso contrário.
'''

N = int(input())
L = input().split()
A = False
B = False
for lamp in L:
    if lamp == '1':
        A = not(A)
    else:
        A = not(A)
        B = not(B)
if A:
    print('1')
else:
    print('0')
if B:
    print('1', end="")
else:
    print('0', end="")