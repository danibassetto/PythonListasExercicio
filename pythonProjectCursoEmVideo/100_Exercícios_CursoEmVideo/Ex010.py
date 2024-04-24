# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$1,00 = R$4,92

real = float(input("Quanto dinheiro você tem na carteira? "))
dolar = real / 4.92
print(f"Com R${real:.2f} você pode comprar US${dolar:.2f}")