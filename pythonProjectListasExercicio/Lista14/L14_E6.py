'''
Para montar uma maratona de programação é necessário criar para cada problema os arquivos de
entrada e os arquivos de saída. Para cada entrada deve que ser criado n arquivos de entrada em uma
pasta input, com os nomes A_1, A_2, A_3,.., A_n, executados com a solução do problema gerando n
arquivos de saída em uma pasta output, com os nomes A_1, A_2, A_3, ..., A_n.
Faça um programa em Pyhton que gere 100 arquivos de entrada e de saída para o problema abaixo.
'''

from random import randint
# para criar pasta
import os

if not os.path.isdir("input"):
    os.mkdir("input")
if not os.path.isdir("output"):
    os.mkdir("output")

from random import randint

for i in range(1, 101):
    arq_in = 'input//A_' + str(i)
    f_in = open(arq_in, 'w')
    N = randint(1, 105)
    f_in.write("{}\n".format(N))
    for j in range(N):
        num = randint(1, 2)
        f_in.write("{} ".format(num))
    f_in.close()

for i in range(1, 101):
    arq_in = 'input//A_' + str(i)
    arq_out = 'output//A_' + str(i)
    f_in = open(arq_in, 'r')
    f_out = open(arq_out, 'w')

    N = int(f_in.readline())
    L = f_in.readline().split()
    A = False
    B = False
    for lamp in L:
        if lamp == '1':
            A = not (A)
        else:
            A = not (A)
            B = not (B)
    if A:
        f_out.write('1\n')
    else:
        f_out.write('0\n')
    if B:
        f_out.write('1')
    else:
        f_out.write('0')
    f_in.close()
    f_out.close()
