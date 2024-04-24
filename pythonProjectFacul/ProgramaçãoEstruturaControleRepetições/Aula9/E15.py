'''Elabore um algoritmo que leia dois valores x e y (inteiros) e calcule o valor de x elevado a y.
Considere a função abs(valor) que converte a variável valor para positivo caso seja negativa, pois 3 elevado a -2 é
igual a 1 dividido por 3 elevado a 2.'''

x = int(input("Digite a base X:"))
y = int(input("Digite o expoente Y:"))

r = 1
for i in range(abs(y)):
    r *= x

if y < 0:
    r = 1 / r

print("Resultado = ", r)

