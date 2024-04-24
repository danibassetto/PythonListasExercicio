''' Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
crescente. '''

numeros = list()  # Siginifica o mesmo que lista = []

while True:
    n = int(input("DIGITE UM VALOR: "))
    if n not in numeros:
        numeros.append(n)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor duplicado!")
    r = str(input("Quer continuar? [S/N] "))
    if r in "Nn":
        break

print("Lista =",sorted(numeros))
# Ou numeros.sort()