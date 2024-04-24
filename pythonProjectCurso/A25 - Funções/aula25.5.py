"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz, se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro
da função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o número enviado.
"""
from random import randint


def n(valor):
    if valor % 3 == 5 and valor % 5 == 0:
        return f'fizzbuzz, {n} é divisível por 3 e 5'
    elif valor % 3 == 0:
        return f'fizz, {n} é divisível por 3'
    elif valor % 5 == 0:
        return f'buzz, {n} é divisível por 5'
    else:
        return n


for i in range(100):
    aleatorio = randint(0, 100)
    print(n(aleatorio))
