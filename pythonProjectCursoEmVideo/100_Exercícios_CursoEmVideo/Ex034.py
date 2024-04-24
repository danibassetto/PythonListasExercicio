''' Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

s = float(input("Informe seu salário: "))
if s > 1250:
    ns = (10 / 100 * s) + s

else:
    ns = (15 / 100 * s) + s
print(f"Novo salário: R${ns:.2f}")