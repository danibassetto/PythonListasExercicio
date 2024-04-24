'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três
listas geradas.'''

num = []
par = []
impar = []
while True:
    n = int(input("Informe um valor: "))
    num.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    resp = str(input("Deseja continuar? [S/N] "))
    if resp in "Nn":
        break
num.sort()
par.sort()
impar.sort()
print("Lista completa =", num)
print("Pares =",par)
print("Ímpar =",impar)

