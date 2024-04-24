''' Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

import random

computador = random.randint(0, 5)
n = int(input("Insira o número de 0 a 5 que você acha que eu pensei: "))
if computador == n:
    print("PARABÉNS, ERA ESSE MESMO!!")
else:
    print(f"QUE PENA, EU GANHEI! Havia pensado no número {computador}.")
