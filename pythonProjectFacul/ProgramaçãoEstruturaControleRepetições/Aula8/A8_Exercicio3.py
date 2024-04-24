# Divisores de um número

n = int(input("Informe o número que deseja saber os divisores: "))
print(f"Divisores de {n}: ")
for i in range(1, n+1):
    if (n % i == 0):
        print(i)