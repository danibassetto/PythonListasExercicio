# Algoritmo para mostrar a tabuada de um número N qualquer lido pelo teclado

n = int(input('Digite a tabuada desejada: '))
cont = 1
while cont <= 10:
    r = n * cont  # r de resultado
    print(n,'x',cont,'=',r)
    cont += 1
