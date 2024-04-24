# A inserção de elementos pode ser utilizando o índice desejado:

M=[0]*2
for i in range(0,2):
    M[i]=[0]*3
    for j in range(0,3):
        M[i][j]=int(input("Informe o valor [{}][{}] -> ".format(i,j)))
print(M)

# Ou utilizando a função append().

M = []
for i in range(0,2):
    M.append([])
    for j in range(0,3):
        M[i].append(int(input("Informe o valor [{}][{}] -> ".format(i,j))))
print(M)

# Inserindo elementos aleatórios na matriz

from random import randint
M=[]
for i in range(0,2):
    M.append([])
    for j in range(0,3):
        M[i].append(randint(1,50))
print(M)
