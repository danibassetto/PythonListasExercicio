#algoritmo valores iguais, maior ou menor
n1=int(input("Digite um valor inteiro: "))
n2=int(input("Digite outro valor inteiro: "))
if (n1==n2):
    print("Valores iguais")
else:
    if n1>n2:
        print(f"O número {n1} é o maior")
    else:
        print(f"O número {n2} é o maior")
print("FIM")