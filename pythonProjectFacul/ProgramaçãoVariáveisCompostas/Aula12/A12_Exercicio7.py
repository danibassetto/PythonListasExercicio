# Verificar se uma matriz é simétrica ou não

print("Digite os valores da matriz: ")
a = [0] * 5
for i in range(5):
    a[i] = [0] * 5
    for j in range(5):
        a[i][j] = int(input())
for i in range(5):
    print(a[i])

sim = True
for i in range(5):
    for j in range(5):
        if a[i][j] != a[j][i]:
            sim = False
            break
if sim:
    print("Matriz simétrica!")
else:
    print("Matriz assimétrica!")