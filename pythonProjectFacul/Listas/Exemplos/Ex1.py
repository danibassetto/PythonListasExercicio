from random import randint
L = []
for i in range(10):
    L.append(randint(1,20))
M = L.copy() #ou L[:]

print('L ->',L)
print('M ->',M)

L[0] = 50

print('L ->',L)
print('M ->',M)