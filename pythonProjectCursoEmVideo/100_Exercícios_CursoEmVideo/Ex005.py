# Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor

n = int(input("Digite um número: "))
a = n - 1
s = n + 1
print("Analisando o valor {}, seu antecessor é {} e seu sucessor é {}.".format(n, a, s))
# OU
print("Analisando o valor {}, seu antecessor é {} e seu sucessor é {}.".format(n, n-1, n+1))
