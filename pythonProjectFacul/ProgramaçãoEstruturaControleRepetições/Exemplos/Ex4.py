# os três tipos de repetição

n = 1
while n <= 10:
    print(n, end=' ')
    n += 1
print()
n = 1
while True:
    if n <= 10:
        print(n, end=' ')
        n += 1
    else:
        break
print()
for n in range(10):  # Range = intervalo
    print(n, end=' ')
print()
for n in range(10, 0, -1):
    print(n, end=' ')  # O end é o que imprime após a impressão, se eu não colocar ele, ocorre pulo de linha