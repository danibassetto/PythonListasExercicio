'''
Entrada de dados - Input
'''

'''nome = input('Qual o seu nome? ')
print(f'O usuário digitou {nome} e o tipo da variável é '
      f'{type(nome)}')  --> retorna como str, por isso não 
      daria pra fazer contas e então colocamos int ou float'''

nome=input('Qual seu nome? ')
idade=input('Qual sua idade? ')

ano_nascimento = 2022 - int(idade)

print()
print(f'{nome} tem {idade} anos. '
      f'{nome} nasceu em {ano_nascimento}')
print()

numero_1 = float(input('Digite um número: '))
numero_2 = float(input('Digite outro número: '))
print(numero_1 + numero_2)