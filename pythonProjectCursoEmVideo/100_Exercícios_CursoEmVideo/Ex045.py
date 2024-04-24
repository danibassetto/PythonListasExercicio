# Crie um programa que faça o computador jogar Jokenpô com você (PEDRA, PAPEL, TESOURA)

from random import randint
from time import sleep

#         0          1         2
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
print('''SUAS OPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
jogador = int(input("Qual é sua jogada? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
print('-=' * 15)
print(f"Computador jogou {itens[computador]}")
print(f"Jogador jogou {itens[computador]}")
print('-=' * 15)
if computador == 0:
    if jogador == 0:
        print("EMPATE!")
    elif jogador == 1:
        print("JOGADOR VENCEU!")
    elif jogador == 2:
        print("COMPUTADOR VENCEU!")
    else:
        print("JOGADA INVÁLIDA!")
elif computador == 1:
    if jogador == 0:
        print("COMPUTADOR VENCEU!")
    elif jogador == 1:
        print("EMPATE!")
    elif jogador == 2:
        print("JOGADOR VENCEU!")
    else:
        print("JOGADA INVÁLIDA!")
elif computador == 2:
    if jogador == 0:
        print("JOGADOR VENCEU!")
    elif jogador == 1:
        print("COMPUTADOR VENCEU!")
    elif jogador == 2:
        print("EMPATE!")
    else:
        print("JOGADA INVÁLIDA!")
