# Sequência de Fibonacci

print('Sequência de Fibonacci')
n = int (input("Digite a qtd de valores para a serie de Fibonacci:"))
a = 1
b = 0
for i in range(n):
    c = a+b
    print(c)
    a = b
    b = c