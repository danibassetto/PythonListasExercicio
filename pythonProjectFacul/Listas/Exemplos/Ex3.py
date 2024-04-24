from random import randint
L = []
for i in range(10):
    L.append(randint(1,20))

print(L)

for i in range(len(L)):
    print(i,L[i])

print('=' * 30)

for i,n in enumerate(L):
    print(i,n)