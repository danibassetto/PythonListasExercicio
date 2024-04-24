#  Elabore um algoritmo, usando a estrutura PARA, que calcule a soma de 10 números lidos pelo teclado.

soma = 0
for i in range(10):
    num = int(input(f'Insira o número {soma + 1}: '))
    soma += num
print(f'Soma: {soma}')