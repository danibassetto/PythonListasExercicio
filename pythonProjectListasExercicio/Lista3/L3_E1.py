# import math

n = int(input('Digite um número: '))
if n < 0:
    print('O número não é positivo!')
else:
    q = n ** 2
    r = n ** 0.5
    # r = math.sqrt(n)
    print(f'{n} ao quadrado = {q}\n'
          f'raiz quadrada de {n} = {r}')