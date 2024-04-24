# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for p in range(1,6):
	peso = float(input("Informe seu peso: "))
	if p == 1:		# para que seja atribuido o primeiro valor e na hora de verificar o menor, dar certo
		maior = peso
		menor = peso
	else:
		if peso > maior:
			maior = peso
		if peso < menor:
			menor = peso
print(f"Maior peso: {maior}Kg\nMenor peso: {menor}Kg")
