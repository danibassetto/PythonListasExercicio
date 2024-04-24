''' Algoritmo que leia um número inteiro e determine quantos algarismos ele possui '''

num = int(input("Digite um número: "))
alg = 0
while num > 0:
    alg += 1
    num //= 10
print("Total de algarismos: ",alg)