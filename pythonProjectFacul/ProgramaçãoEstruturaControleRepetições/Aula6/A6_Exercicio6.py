# Transformar inteiro decimal para binário

num = int(input('Digite o número inteiro que pretende converter para binário: '))
bin = 0
fator = 1
while num > 0:
    bin = bin + fator * (num % 2)
    fator *= 10
    num //= 2
print(f'Número binário:{bin}')

