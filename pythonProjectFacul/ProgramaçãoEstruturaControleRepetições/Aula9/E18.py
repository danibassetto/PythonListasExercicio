'''Elabore um algoritmo para mostrar na tela todos os anos que foram bissextos, partindo-se do ano 1 até o ano
atual (leia o ano atual). Um ano é bissexto se ele é múltiplo de 400 ou se ele é múltiplo de 4 e não é
múltiplo de 100. '''


ano = int(input('Digite um ano: '))
if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')