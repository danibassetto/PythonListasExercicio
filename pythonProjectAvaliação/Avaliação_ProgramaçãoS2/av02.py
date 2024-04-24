'''
Avaliação 02–Funções
GRUPO 12

Danielle Barros Bassetto RA: 629391
João Vitor Adonis RA: 590428
Matheus Henrique de Lima RA: 626732
'''


# função para validar a entrada
def validaEntrada(n):
    n = str(n)
    if len(n) == 4:
        for i in n:
            if n.count(i) > 3:
                return False
        return True
    else:
        return False


# função que retorna o número em ordem crescente
def crescente(n):
    n = str(n)
    lista = list(n)
    lista.sort()
    C = ''.join(lista)
    C = int(C)
    return C


# função que retorna o número em ordem decrescente
def decrescente(n):
    n = str(n)
    lista = list(n)
    lista.sort(reverse=True)
    D = ''.join(lista)
    D = int(D)
    return D


n = int(input())
resultado = n
if validaEntrada(n):
    while resultado != 6174:  # Enquanto o resultado não for 6174, irá realizar a subtração de Kaprekar
        print(resultado)
        resultado = decrescente(resultado) - crescente(resultado)
    print(resultado)