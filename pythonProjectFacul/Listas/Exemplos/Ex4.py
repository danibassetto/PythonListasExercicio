from random import randint
L = []
for i in range(10):
    L.append(randint(1,20))

print(L)
L.insert(0,50)
print(L)
L += [51,52,53]
print(L)
L.extend([51,52,53])
print(L)

del L[0] #remove o elemento da posição passada dentro dos []
print(L)
n = L.pop() #remove o último elemento da lista ou da posição informada
print(L)
print(n)
L.remove(51) #remove por valor
print(L)