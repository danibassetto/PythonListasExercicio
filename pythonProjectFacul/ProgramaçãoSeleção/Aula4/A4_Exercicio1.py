#média entre 2 notas
n1=float(input("Digite a nota 1: "))
n2=float(input("Digite a nota 2: "))
med=(n1+n2)/2
if med>=7:
    print(f"Aprovado com média {med}")
else:
    print(f"reprovado com média {med}")