''' Algoritmo que leia um número e  calcule a soma dos número menores ou iguais a ele, começando pelo 1. '''

num = int(input('Digite o último valor a ser somado: '))
cont = 1
soma = 0
while(cont <= num):
    soma += cont
    cont += 1
print('Soma =',soma)