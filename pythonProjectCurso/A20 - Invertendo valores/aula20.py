# Invertendo o valor de variáveis

x = 10  # Luiz
y = 'Luiz'  # 10

z = x
x = y
y = z

print(f'x = {x} e y = {y}')

''' ou

x, y = y, x

x = 10
y = 'Dani'
z = 'João'
x, y, z = z, x, y

print(f'x = {x}, y = {y} e z = {z}')
'''
