# Faça um programa em Python que eleve um número qualquer a um outro, usando recursividade

def elevado(b, e):
    if e == 0:
        return 1
    return b * elevado(b, e - 1)


print("Informe a base e o expoente")
base = int(input("Base >> "))
expo = int(input("Expoente >> "))
print(f"{base} elevado a {expo} é igual a {elevado(base, expo)}")
