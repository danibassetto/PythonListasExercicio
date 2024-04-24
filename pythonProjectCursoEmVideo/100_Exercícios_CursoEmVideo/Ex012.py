# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

p = float(input("Insira o preço do produto que deseja aplicar o desconto: "))
desc = (15/100) * p
np = p - desc
print(f"O valor inicial do produto era R${p:.2f} e com o desconto de R${desc:.2f} ficou R${np:.2f}!")