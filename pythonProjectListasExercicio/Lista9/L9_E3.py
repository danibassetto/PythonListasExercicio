'''Faça um programa em Python que implemente uma função INVERTE que receba um número
como parâmetro e retorne este número escrito ao contrário. Ex: 4312 → 2134. Peça um
número, chame a função e imprima o resultado.'''


def inverte(n):
    return str(n)[::-1]


n = int(input(f"Informe um número: "))
print(f"Inverso de {n} >> {int(inverte(n))}")

'''
# Podemos fazer a função utilizando variáveis como no inverte1 ou fazer
# direto em uma instrução apenas como no inverte2

def inverte1(n):
    invertido = str(n)
    invertido = invertido[::-1]
    n = int(invertido)
    return n

def inverte2(n):
    return int(str(n)[::-1])

num = int(input("Informe um número >> "))
inv = inverte2(num)
print(f"O número {num} inverido é {inv}")
'''