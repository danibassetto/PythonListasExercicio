''' '''

import math

valor = input().split(" ")
a = int(valor[0])
b = int(valor[1])
c = int(valor[2])

maior = int((a + b + abs(a - b)) / 2)
resultado = int((maior + c + abs(maior - c)) / 2)

print(f"{resultado} eh o maior")