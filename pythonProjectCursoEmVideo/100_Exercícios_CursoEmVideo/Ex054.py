''' Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
maioridade e quantas já são maiores. '''

from datetime import date
atual = date.today().year
tot_maior = 0
tot_menor = 0
for i in range(1,8):
	nascimento = int(input("Informe o ano que você nasceu: "))
	idade = atual - nascimento
	if idade >= 18:
		tot_maior += 1
	else:
		tot_menor += 1
print(f"Ao todo tivemos {tot_maior} pessoa(s) maior(es) de idade e {tot_menor} menor(es)")
