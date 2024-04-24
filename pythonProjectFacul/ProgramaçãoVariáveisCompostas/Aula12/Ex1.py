a = [0] * 5
print("Digite os elementos da matriz: ")
for i in range(5):
    a[i] = [0] * 5
    for j in range(5):
        a[i][j] = int(input())
print(a)