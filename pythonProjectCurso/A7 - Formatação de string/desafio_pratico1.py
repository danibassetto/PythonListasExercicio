nome = 'Danielle'
idade = 18
altura = 1.65
ano_atual = 2022
peso = 51.6
nascimento = ano_atual - idade
IMC = peso/(altura**2)

print(f'{nome} tem {idade} anos e {altura} de altura')
print(f'{nome} pesa {peso} e seu IMC é {IMC:.2f}')
print(f'{nome} nasceu em {nascimento}')