# Matriz transposta

import random

a = [0] * 4
for i in range(4):
    a[i] = [0] * 6
    for j in range(6):
        a[i][j] = random.randint(1,99)
for i in range(4):
    print(*a[i])

T = [0] * 6
for i in range(6):
    T[i] = [0] * 4
    for j in range(4):
        T[i][j] = a[j][i]
print("Matriz transposta: ")
for i in range(6):
    print(*T[i])