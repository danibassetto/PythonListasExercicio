# Número primo

num = int(input("Digite o número que deseja saber se é primo: "))
td = 2
for d in range(2, num // 2 + 1):
    if num % d == 0:
        td += 1
        break
if td == 2:
    print("É PRIMO")
else:
    print("NÃO É PRIMO")