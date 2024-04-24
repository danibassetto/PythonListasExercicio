'''
While (enquanto) em python
utilizado para realizar ações enquanto
uma condição for verdadeira.
'''

'''while True:
    nome = input('Qual seu nome?')
    print(f'Olá {nome}!')'''


d = 0
while d <= 20:
    print(d)
    d = d + 1  # ou  += 1

print('Acabou') # Só será executada quando o while testar falso

print()

a = 0
while a < 10:
    if a == 3:
        a = a + 1
        continue  # Pula o 3

    print(a)
    a = a + 1
print('Acabou!')

print()

b = 0
while b < 10:
    if b == 3:
        b += 1
        break  # Termina no 2

    print(b)
    b += 1

print('Acabou!')

print()

x = 0


while x < 10:
    y = 0  # linha
    while y < 5:
        print(f'{x},{y}')
        y += 1
    x += 1
print('Acabou!')

print()

# Calculadora

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')


    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número.')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador inválido!')

    sair = input('Deseja sair? [s]im ou [n]ão: ')
    if sair == 's':
        break