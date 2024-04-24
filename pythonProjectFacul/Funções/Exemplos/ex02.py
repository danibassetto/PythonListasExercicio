"""Escreva uma função que ordene três números e os imprima em ordem crescente."""

from random import randint

a = int(input())
b = int(input())
c = int(input())


def ordena(a, b, c):
    if a > b:
        x = a
        a = b
        b = x
        # a,b = b,a
    if b > c:
        x = b
        b = c
        c = x
        # b,c = c,b
    if a > b:
        x = a
        a = b
        b = x
        # a,b = b,a


print("Números em ordem crescente: {} {} {}".format(a, b, c))

x = randint(1, 50)
y = randint(1, 50)
z = randint(1, 50)
ordena(x, y, z)
# chamando a função copm números aleatórios ordena(5, 18, 3)
# chamando a função com valores
x = int(input("Digite um número"))
y = int(input("Digite um número"))
z = int(input("Digite um número"))
ordena(x, y, z)
# chamando a função com valores digitados
