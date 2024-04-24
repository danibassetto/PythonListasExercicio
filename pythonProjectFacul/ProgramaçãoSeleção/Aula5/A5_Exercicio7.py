''' algoritmo que leia 3 valores inteiros (a, b e c) e os coloque em ordem crescente,
de modo que em A fique o menor valor, em B o valor intermediário e em C o maior valor. '''

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

if (a > b or a > c):
    if b < c:
        a,b = b,a
    else:
        a,c = c,a
if b > c:
    b,c = c,b
print()
print('A =',a,'B =',b,'C =',c)