# Introdução a formatação de strings

nome='Danielle'
idade=18
altura=1.65
e_maior= idade>=18
peso=51.6
IMC=peso/(altura**2)

print(nome, 'tem', idade, 'anos de idade e seu IMC é',IMC)
print(f'{nome} tem {idade} anos de idade e seu IMC é {IMC:.2f}')
print('{0} tem {1} anos de idade e seu IMC é {2:.2f}'.format(nome,idade,IMC))
print('{n} tem {i} anos de idade e seu IMC é {im:.2f}'.format(n=nome,i=idade,im=IMC))