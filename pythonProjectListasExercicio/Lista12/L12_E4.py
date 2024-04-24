'''
Defina a função prod_lista que recebe como argumento uma lista de números inteiros e
devolve o produto dos seus elementos.
'''

from functools import reduce
from operator import mul


def prod_lista(n):
    return reduce(mul, [int(num) for num in n])
    #return reduce(lambda x,y: x*y, n)


n = input("Informe os elementos de uma lista separados por espaço: ").split()
print(f"Produto dos elementos da lista informada: {prod_lista(n)}")