C = set()
C.add(1)
C.add(2)
C.add(3)
print(C)
C.add(1)
print(C)
C.add(5)
print(C)
C.add(4)
print(C)

D = set()
for i in range(10):
    D.add(i)
print(D)

'''
Podemos testar se um elemento faz parte de um conjunto usando o operador in do Python.
'''

if 1 in C:
   print("1 pertence a C")
else:
   print("1 não pertence a C")