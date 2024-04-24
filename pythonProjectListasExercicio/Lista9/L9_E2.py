'''Escreva um programa em Python que implemente uma função potência, que receba uma base e
um expoente por parâmetro e retorne o valor da base elevada ao expoente. O expoente é sempre
maior ou igual a zero, e os números são sempre inteiros. Peça uma base e um expoente, chame a
função e imprima o resultado'''


def potencia(base, expo):
    p = 1
    for i in range(expo):
        p *= base
    return p


b = int(input("Informe uma base: "))
e = int(input("Informe um expoente: "))
print(f"Resultado da potencia: {potencia(b, e)}")

'''
def potencia(base, expo):
    p = 1
    for i in range(expo):
        p *= base
    return p

b = int(input('Base >> '))
e = int(input('Expoente >> '))
print(f'{b} elevado a {e} é igual a {potencia(b, e)}')
'''