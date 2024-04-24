'''
Considere a função Comb(n,k), que representa o número de grupos distintos com k pessoas que
podem ser formados a partir de n pessoas. Por exemplo, Comb (4,3) = 4, pois com 4 pessoas (A,
B, C e D), é possível formar 4 diferentes grupos: ABC, ABD, ACD e BCD. Sabe-se:
Comb (n,k) = n se k==1
Comb (n,k) = 1 se k==n
Comb(n,k) = Comb(n-1, k-1) + Comb (n-1, k) caso contrário
Escreva um programa em Python com uma função recursiva para Comb (n,k).
'''


def comb(n, k):
    if k == 1:
        return n
    if k == n:
        return 1
    return comb(n - 1, k - 1) + comb(n - 1, k)


print("Informe dois valores para calcular o numero de grupos distintos (combinacao)")
a = int(input("1º valor: "))
b = int(input("2º valor: "))
print("A combinação é {}".format(comb(a, b)))
