#algoritmo comparação de valores

a=int(input("Digite o primeiro valor: "))
b=int(input("Digite o segundo valor: "))
c=int(input("Digite o terceiro valor: "))
if (a>b and a>c):
    print(f"Maior valor:{a}")
else:
    if (b>c):
        print(f"Maior valor:{b}")
    else:
        print(f"Maior valor:{c}")
print("FIM")