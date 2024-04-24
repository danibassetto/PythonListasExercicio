''' Faça  um  programa  que gere dois  conjuntos  de  números  inteiros  distintos  e  imprima  a intersecção  destes
dois  conjuntos  (os  números  presentes  em  ambos  os  conjuntos). Exemplo: Primeiro conjunto: 1 2 3 4 5 Segundo
conjunto: 2 5 7 1 9 18 Resultado: 1 2 5 5 '''


a = []
print("Informe os valores do conjunto A ou '#' para encerrá-lo: ")
while True:
    n = input()
    if n == '#':
        print("A =", a)
        break
    else:
        a.append(int(n))
b = []
print("Informe os valores do conjunto B ou '#' para encerrá-lo: ")
while True:
    n = input()
    if n == '#':
        print("B =", b)
        break
    else:
        b.append(int(n))

intersecao = []
if len(a) > len(b):
    for i in a:
        if i in b:
            intersecao.append(i)
else:
    for i in b:
        if i in a:
            intersecao.append(i)
print("Intersecção =", intersecao)

'''
from random import randint
a = []
b = []
c = []
while len(a) != 10:
    x = randint(1,20)
    if x not in a:
        a.append(x)
a.sort()
print(*a)

while len(b) != 10:
    x = randint(1,20)
    if x not in b:
        b.append(x)
b.sort()
print(*b)

for n in a:
    if n in b:
        c.append(n)
print(*c)
'''