'''Elabore um algoritmo para mostrar todos os números primos menores ou iguais a 1000.'''

print("Os dois primeiros primos são: 1 e 2")
for num in range (3,100, 2):
    td = 2
    for d in range(2,num//2):
        if num % d == 0:
            td += 1
            break
    if td==2:
        print(num)