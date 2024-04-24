#Calculo do reajuste de salário
S=float(input("Insira seu salário: "))
R=float(input("Insira a porcentagem do reajuste: "))
Reaj=S+(S*R/100)
print(f"O salário reajustado é: R${Reaj:.2f}")
