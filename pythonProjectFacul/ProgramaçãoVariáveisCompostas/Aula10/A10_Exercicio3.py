'''Elabore um algoritmo que crie um vetor capaz de armazenar os 20 primeiros valores ímpares.'''

a = [0] * 20
imp = 1
for i in range(20):
    a[i] = imp
    imp += 2
print(a)

# OU
A = [0] * 20
for i in range(20):
    A[i] = 2*i+1
print(A)

#OU
B = [1]
for i in range(1,20):
    B.insert(i, A[i-1] + 2)
print(B)