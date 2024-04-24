''' Faça um programa que gere duas sequências de números inteiros ordenados e imprima
uma sequência com os números ordenados das duas sequências anteriores. Você não
deve usar o método sort para o resultado.
Exemplo:
Primeira sequência: 1 3 5 5 7 9 10
Segunda sequência: 2 2 4 6 8 8 10
Resultado: 1 2 2 3 4 5 5 6 7 8 8 9 10 10 '''


a = []
print("Informe o número que deseja inserir ou '#' para encerrar: ")
while True:
    pos = 0
    n = input()
    if n == '#':
        print("A =", a)
        break
    elif len(a) == 0:
        a.append(int(n))
    else:
        if int(n) <= a[0]:
            a.insert(0, int(n))
        elif int(n) >= a[-1]:
            a.append(int(n))
        else:
            while a[pos] < int(n):
                pos += 1
            a.insert(pos, int(n))
b = []
print("Informe o número que deseja inserir ou '#' para encerrar: ")
while True:
    pos = 0
    n = input()
    if n == '#':
        print("B =", b)
        break
    elif len(b) == 0:
        b.append(int(n))
    else:
        if int(n) <= b[0]:
            b.insert(0, int(n))
        elif int(n) >= b[-1]:
            b.append(int(n))
        else:
            while b[pos] < int(n):
                pos += 1
            b.insert(pos, int(n))

sequencia = []
for i in a:
    sequencia.append(i)
for i in b:
    if len(sequencia) == 0:
        sequencia.append(i)
    else:
        if i <= sequencia[0]:
            sequencia.insert(0, i)
        elif i >= sequencia[-1]:
            sequencia.append(int(n))
        else:
            while sequencia[pos] < i:
                pos += 1
            sequencia.insert(pos, i)
print("Sequência A+B ordenada:", sequencia)

'''
from random import randint
a = []
b = []
c = []
while len(a) != 5:
    a.append(randint(1,20))
a.sort()
print(*a)

while len(b) != 5:
    b.append(randint(1,10))
b.sort()
print(*b)

i = 0
j = 0
while len(c) != 10:
    if i < 5 and j < 5:
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    else:
        if j == 5:
            c.append(a[i])
            i += 1
        elif i == 5:
            c.append(b[j])
            j += 1
print(*c)
'''