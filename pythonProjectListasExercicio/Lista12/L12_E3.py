'''
Defina a função indices_pares que recebe como argumento uma lista de números
inteiros w e devolve a lista dos elementos de w em posições pares.
'''


def indices_pares(w):
    lista = [int(num) for num in w]
    return [num for num in lista if (lista.index(num) + 1) % 2 == 0]  # considerando que comece pela posição 1 e não 0


w = input("Informe números inteiros de uma lista separados por espaço: ").split()
print(f"Lista dos elementos informados em posições pares: {indices_pares(w)}")


'''
def indices_pares(w):
    #return [w[i] for  i in range(0, len(w), 2)]
    return [w[i] for i in range(len(w)) if i % 2 == 0]
    #return [num for num in w[::2]]
    #return [num for i, num in enumerate(w) if i % 2 == 0]
    

lista = [randint(1, 50) for i in range(10)]
print("Números gerados >>", lista)
print("Números das posições pares >>", indices_pares(lista))
'''