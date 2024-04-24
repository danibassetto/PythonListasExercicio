'''
                GRUPO 8
    Marllon Silva Araujo Coelho RA: 627021
    Matheus Henrique de Lima RA: 626732
    Cesar Augusto de Almeida RA: 626848
    Danielle Barros Bassetto RA: 629391
    Gabriel Barros de Melo Amorim RA: 574015
    João Vítor Adonis RA: 590428
'''

N = int(input())
superior = (10**N) - 1
inferior = (10**(N - 1))*2

L = []
for num in range(superior, inferior, -1):
    corte = num
    i = 0
    while i < N:
        superprimo = True
        j = 1
        while j < corte - 1:
            j += 1
            if (corte % j) == 0:
                superprimo = False
                break
        if not superprimo:
            break
        else:
            corte //= 10
        i += 1
    else:
        L.append(num)
L.sort()
for i in L:
    print(i)


'''
n = int(input())
l = []
for i in range(10**(n-1)*2, 10**n):
    num = i
    pd = num // 10**(n-1)
    if pd != 4 and pd != 6 and pd != 8 and pd != 9:
        while num != 0:
            primo = True
            for d in range(2,num//2+1):
                if num % d == 0:
                    primo = False
                    break
            if primo:
                num //= 10
            else:
                break
        if num == 0:
            l.append(i)
for sp in l:
    print(sp)
'''