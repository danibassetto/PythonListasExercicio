'''
Faça um programa em Python que entre com uma fração (numerador e denominador) e converta
a fração para uma fração irredutível, ou seja, simplifique a fração pelo maior divisor comum.
Para isso faça uma função chamada ‘simplifica’ que recebe como parâmetro o numerador e o
denominador de uma fração. Esta função deve simplificar a fração recebida dividindo o
numerador e o denominador pelo maior fator possível. Por exemplo, a fração 36/60 simplifica
para 3/5 dividindo o numerador e o denominador por 12.
Peça a fração, chame a função e imprima a fração simplificada.
Obs.: Não precisa validar se a fração já é irredutível.
'''


def MDC(x, y):
    if y <= x and x % y == 0:
        return y
    if x < y:
        return MDC(y, x)
    return MDC(y, x % y)


def simplifica(num, den):
    mdc = MDC(num, den)
    num //= mdc
    den //= mdc
    return num, den


print("Informe o numerador e o denominado de um fração")
numerador = int(input("Numerador >> "))
denominador = int(input("Denominador >> "))
numS, denS = simplifica(numerador, denominador)
print(f"A fração {numerador}/{denominador} simplificada é {numS}/{denS}")