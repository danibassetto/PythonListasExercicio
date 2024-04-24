'''
reduce() – sua utilidade está na aplicação de uma função a todos os valores do conjunto, de forma a agregá-los todos em
um único valor. Por exemplo, para aplicar a operação de soma a todos os elementos de uma sequência, de forma que o
resultado final seja a soma de todos esses elementos, poderíamos fazer o seguinte:

É claro que, para realizar a soma de todos os elementos de uma sequência, é muito mais claro utilizarmos a função sum()

'''

from operator import add
from functools import reduce
valores = [1, 2, 3, 4, 5]

soma = reduce(add, valores)
print(soma)
print(sum(valores))
