''' Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário
do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo
será negado. '''

casa = float(input("Valor da casa: R$ "))
s = float(input("Salário do comprador: R$ "))
anos = int(input("Quantos anos de financiamento? "))
prestacao = casa / (anos * 12)
minimo = s * 30 / 100
print(f"Para pagar uma casa de R$ {casa:.2f} em {anos} ano(s), a prestação será de R$ {prestacao:.2f}")
if prestacao <= minimo:
    print("Empréstimo pode ser CONCEDIDO")
else:
    print("Empréstimo NEGADO!")
