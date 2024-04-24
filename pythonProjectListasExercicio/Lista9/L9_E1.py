'''Escreva um programa em Python que contenha uma função que peça um número e verifique se
é par ou ímpar. No principal, chame a função'''


def paridade(n):
    if n % 2 == 0:
        print("Par")
    else:
        print("Ímpar")


resp = 'S'
while resp in 'Ss':
    n = int(input("Informe um número: "))
    paridade(n)
    resp = input("Deseja continuar? [S/N] ")
    print("=-" * 20)

'''
def isParImpar():
    num = int(input('Informe um número >> '))
    if num % 2 == 0:
        print('PAR')
    else:
        print('ÍMPAR')

isParImpar()
'''
