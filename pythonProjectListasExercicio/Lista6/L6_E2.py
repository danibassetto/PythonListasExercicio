''' Faça um programa que gere dois conjuntos de números inteiros distintos e imprima a união destes
conjuntos (os números presentes em pelo menos um dos conjuntos).
Exemplo:
Primeiro conjunto: 1 2 3 4 5
Segundo conjunto: 2 5 7 1 9 18
Resultado: 1 2 3 4 5 7 9 18 6 '''

uniao = []
a = []
print("Informe os valores do conjunto A ou '#' para encerrá-lo: ")
while True:
    n = input()
    if n == '#':
        print("A =", a)
        break
    else:
        a.append(int(n))
        uniao.append(int(n))
print("-=-" * 20)
b = []
print("Informe os valores do conjunto B ou '#' para encerrá-lo: ")
while True:
    n = input()
    if n == '#':
        print("B =", b)
        break
    else:
        b.append(int(n))
print("-=-" * 20)
for i in b:
    if i not in a:
        uniao.append(i)
print("União =", uniao)

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

c = a[:]  # copiando a em c
for n in b:
    if n not in c:
        c.append(n)
c.sort()
print(*c)
'''