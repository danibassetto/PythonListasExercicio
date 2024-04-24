'''Elabore um algoritmo que leia um número inteiro e o inverta'''

num = int(input("Digite um número: "))
inv = 0
while num > 0:
    inv = inv * 10 + num % 10
    num //= 10
print("Valor invertido: ", inv)