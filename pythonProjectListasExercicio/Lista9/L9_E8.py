'''
Faça um programa para entrar com a data de nascimento, data atual e mostrar a idade da pessoa.
Utilize as funções do exercício anterior para validar a entrada das datas.
'''
from datetime import datetime
from moduloData import validaEntrada, validaData


def entraData(texto):
    while True:
        d = input(f'Informe a data {texto} no formato dd/mm/aaaa >> ')
        if validaEntrada(d) and validaData(d):
            return d
        print('Data inválida, digite novamente...')


dN = entraData('de nascimento')
diaN, mesN, anoN = dN.split('/')
diaN, mesN, anoN = int(diaN), int(mesN), int(anoN)

dA = entraData('atual')
diaA, mesA, anoA = dA.split('/')
diaA, mesA, anoA = int(diaA), int(mesA), int(anoA)

'''
#Pegando a data atual do sistema
dA = datetime.today()
diaA, mesA, anoA = dA.day, dA.month, dA.year
'''

idade = anoA - anoN
if mesN > mesA:
    idade -= 1
elif mesN == mesA and diaN > diaA:
    idade -= 1
print(f'Você tem {idade} anos')
