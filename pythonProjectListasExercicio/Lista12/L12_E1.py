'''
Defina a função soma_nat que recebe como argumento um número natural n e devolve a
soma de todos os números naturais até n.
'''

from operator import add
from functools import reduce


def soma_nat(n):
    #return sum([elemento for elemento in range(n + 1)])
    return reduce(add, [elemento for elemento in range(n + 1)])


n = int(input("Informe um número: "))
print(f"Soma dos números de 0 a {n} = {soma_nat(n)}")