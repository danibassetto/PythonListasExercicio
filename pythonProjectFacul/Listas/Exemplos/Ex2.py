from random import randint
L = []
for i in range(10):
    L.append(randint(1,20))

print(L)
print(L[:])
print(L[0:10])
print(L[:6])
print(L[1::2])
print(L[1:6:2])
print(L[::-1])