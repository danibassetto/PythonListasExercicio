'''
Defina a função quadrados que recebe como argumento um número natural n devolve a lista
dos n primeiros quadrados perfeitos.
'''


def quadrados(n):
    return [elemento**2 for elemento in range(1,n+1)]


n = int(input("Informe um número: "))
print(f"Os {n} primeiros quadrados perfeitos são: {quadrados(n)}")
