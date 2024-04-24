'''Elabore um algoritmo para calcular e mostrar a soma:
  S = 2 + 2^2 + 2^3 + 2^4 + 2^5 + ... + 2^10  '''
soma = 0
n = 1
while n <= 10:
    exp = 2 ** n
    soma += exp
    n += 1
print(f"Soma: {soma}")