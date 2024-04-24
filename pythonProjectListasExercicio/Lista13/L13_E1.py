'''
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os
resultados em uma lista. Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um
vetor de contadores(1-6) e uma função para gerar números aleatórios, simulando os lançamentos
dos dados.
'''

from random import randint


def lançaDado():
    valores_lançamentos = [randint(1, 6) for i in range(100)]
    return valores_lançamentos


def contaValores(lista):
    for i in range(1, 7):
        print(f'o valor {i} foi sorteado {lista.count(i)} vezes')


def contaValoresDict(lista):
    d = {}
    for n in lista:
        d[n] = d.get(n, 0) + 1
    for n, qt in sorted(d.items()):
        print(f'o valor {n} foi sorteado {qt} vezes')


valores = lançaDado()
print(valores)
chama = contaValores(valores)
