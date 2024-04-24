# Tabuleiro de xadrez

a = [0] * 8
for i in range(8):
    a[i] = [0] * 8
    for j in range(8):
        a[i][j] = (i+j) % 2
print("TABULEIRO: ")
for i in range(8):
    print(a[i])