# Matriz identidade

a = [0] * 5
for i in range(5):
    a[i] = [0] * 5
    for j in range(5):
        a[i][j] = int(input())

id = True
for i in range(5):
    for j in range(5):
        if (i == j and a[i][j] != 1) or (i != j and a[i][j] != 0):
            id = False
            break

if id:
    print("Matriz identidade")
else:
    print("Matriz não é identidade!")