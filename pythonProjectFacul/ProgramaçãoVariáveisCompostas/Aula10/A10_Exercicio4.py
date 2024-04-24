'''Elabore um algoritmo que leia dois vetores de 10 valores cada e calcule o produto escalar entre eles:

	PE =  A[0]*B[0] + A[1]*B[1] + A[2]*B[2] + A[3]*B[3] + ... + A[9]*B[9]
'''

print('Insira os valores de A: ')
a = [0] * 10
for i in range(10):
    a[i] = int(input())
print('Insira os valores de B: ')
b = [0] * 10
for i in range(10):
    b[i] = int(input())
pe = 0
for i in range(10):
    pe += a[i] * b[i]
    print(pe, end=' ')
print("Produto escalar de A x B:",pe)