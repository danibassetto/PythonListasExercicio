# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
v = 0
while True:
	jogador = int(input("Diga um valor "))
	computador = randint(0,10)
	total = jogador + computador
	tipo = ''
	while tipo not in "PI":
		tipo = str(input("Par ou ímpar? [P/I])).strip().upper()[0]
	print(f"Você jogou {jogador} e o compuador jogou {computador}. Total de {total}")
	print("DEU PAR!" if total % 2 == 0 else "DEU ÌMPAR!")
	if tipo == 'P'
		if total % 2 == 0:
			print("Você venceu!!")
			v += 1
		else:
			print("Você perdeu!")
			break
	elif tipo == "I":
		if total % 2 == 1:
			print("Você venceu!!")
			v += 1
		else:
			print("Você perdeu!!")
			break
print(f"GAME OVER! Você venceu {v} vezes!")
