# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

s = float(input("Insira o seu salário: "))
ns = s + (15 / 100 * s)
print(f"O salário de R${s:.2f} foi reajustado para R${ns:.2f}!")