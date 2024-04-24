from random import randint
L = []
for i in range(10):
    L.append(randint(1,20))
print(L)
L.sort(reverse=True)
print(L)
L.reverse()
print(L)

M = sorted('RENATA',reverse=True)
print(M)