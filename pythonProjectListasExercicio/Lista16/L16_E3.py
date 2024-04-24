'''
Elabore um programa em Python com uma função que receba uma lista de 6 notas por parâmetro.
A função deve retornar a média desses valores, descontando a menor e a maior nota da lista.
Peça a entrada dos 6 valores, armazenando-os em uma lista, chame a função e imprima a média
'''


def calcMedia(notas):
    media = (sum(notas) - max(notas) - min(notas)) / (len(notas) - 2)
    return media


print('Informe 6 notas')
N = []
for i in range(6):
    N.append(float(input(f'Nota {i + 1} -> ')))
print(f'Média = {calcMedia(N)}')
