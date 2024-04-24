'''Elabore um algoritmo que leia um número inteiro de 3 algarismos e mostre cada número em separado. Por ex.,
considerando como numero lido: 372, o algoritmo deverá mostrar: Centena=3, Dezena = 7 e Unidade = 2. '''

num = int(input("Insira um número de até 3 algarismos: "))

c = num // 100
d = num % 100 // 10
u = num % 10
if num > 999 or num < 0:
    print("Número inválido!")
else:
    print(f"Centena: {c}\nDezena: {d}\nUnidade: {u}")

