''' Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''

total = q1000 = menor = cont = 0
barato = ' '
while True:
	produto = str(input("Nome do produto: "))
	preco = float(input("Preço: R$"))
	cont += 1
	total += preco
	if preco > 1000:
		q1000 += 1
	if cont == 1:
		menor = preco
		barato = produto
	else:
		if preco < menor:
			menor = preco
			barato = produto
	resp = ' '
	while resp not in "SN":
		resp = str(input("Quer continuar? ")).strip().upper()[0]
	if resp == "N":
		break
print("PROGRAMA ENCERRADO")
print(f"Total: R${total:.2f}")
print(f"Temos {q1000} produtos custando mais de R$1000")
print(f"O pruduto mais barato é o {barato} que custa R${menor:.2f}")
