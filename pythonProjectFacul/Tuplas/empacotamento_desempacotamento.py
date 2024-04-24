'''
A operação de uma variável receber vários valores em uma mesma instrução chama-se empacotamento, onde é criada uma tupla.
'''

T = 100,200,300
print(T)

'''
Tuplas também podem ser utilizadas para desempacotar valores
'''

a, b = 10, 20
print(a)
print(b)

# Podemos trocar rapidamente os valores de variáveis com construções do tipo:
a, b = 10, 20
print("a = ",a)
print("b = ",b)

a, b = b, a
print("a = ",a)
print("b = ",b)

# As operações de empacotamento e desempacotamento também funcionam com listas.

a, b = [3,4]
print(a)
print(b)

# Podemos usar o * para indicar vários valores a desempacotar
*a, b = [1,2,3,4,5]
print("a = ",a)
print("b = ",b)
a, *b = [1,2,3,4,5]
print("a = ",a)
print("b = ",b)
