'''
. Elabore um programa em Python com uma função que receba uma string por parâmetro,
contendo um número. A função deve retornar a soma dos algarismos desse número.
Peça a entrada da string contendo o número (como string), chame a função e imprima a soma.

'''


def somaAlg(numero):
    num = list(map(int, numero))
    return sum(num)


while True:
    N = input('Informe um número -> ')
    if not N.isdigit():
        print('Informe apenas números')
        continue
    print(f'A soma dos algarismos de {N} é {somaAlg(N)}')
    break
