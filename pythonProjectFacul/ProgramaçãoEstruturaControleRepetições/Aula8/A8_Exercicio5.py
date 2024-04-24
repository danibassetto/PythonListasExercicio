'''
Algoritmo que leia um número inteiro e verifique se ele é ou não perfeito. Um número para ser perfeito deve ser igual a
soma de seus divisores, exceto ele próprio.
Ex: 6 é perfeito pois é == a  1 + 2 + 3 (soma de seus divisores)
'''

n = int(input("Informe o número que deseja saber se é perfeito: "))
soma = 0
for i in range(1, n//2 + 1):
    if n % i == 0:
        soma += i
if soma == n:
    print("Número perfeito!")
else:
    print("Número não perfeito!")