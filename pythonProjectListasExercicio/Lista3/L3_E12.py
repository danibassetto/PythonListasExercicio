# Bits Trocados

valor = int(input("Informe o valor em B$ "))
n50 = valor // 50
n10 = valor % 50 // 10
n5 = valor % 50 % 10 // 5
n1 = valor % 5
print("Cédulas entregues:")
if n50 > 0:
    print(f"{n50} notas de B$ 50,00")
if n10 > 0:
    print(f"{n10} notas de B$ 10,00")
if n5 > 0:
    print(f"{n5} notas de B$ 5,00")
if n1 > 0:
    print(f"{n1} notas de B$ 1,00")