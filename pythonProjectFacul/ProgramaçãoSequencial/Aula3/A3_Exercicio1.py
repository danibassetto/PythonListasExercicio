# salário fixo mais 4% de comissão
S=float(input("Informe o salário: "))
V=float(input("Informe o valor da venda: "))
C=0.04*V
SF=S+C
print(f"Comissão recebida: R${C} \nSalário final: R${SF}")