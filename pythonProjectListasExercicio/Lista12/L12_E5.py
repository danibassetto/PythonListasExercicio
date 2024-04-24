'''
Defina a função media_digitos que recebe como argumento um número natural e devolve
a média dos seus dígitos.
'''

from operator import add
from functools import reduce


def digitos(n):
    lista = [int(num) for num in n]
    soma = reduce(add, lista)
    return soma / int(len(lista))


n = list(input("Informe um número: "))
print(f"Média de {[int(num) for num in n]} = {digitos(n)}")

'''
def media_digitos(N):
    digitos = list(map(int(str(num)))
    return sum(digitos) / len(digitos)
    
N = int(input("Informe um número: "))
print(f"Média dos digitos do número {N} = {media_digitos(N)}")
'''