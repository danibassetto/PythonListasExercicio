'''Programa que peça o primeiro nome do usuário. Se o nome
tiver 4 letras ou menos, escreva que o nome é curto, se tiver entre
5 e 6, escreva que é normal e se for maior que 6, escreva que é grande'''

nome = input('Digite seu nome: ')
tamanho = len(nome)
if tamanho <= 4:
    print('Nome curto')
else:
    if tamanho <= 6:
        print('Nome normal')
    else:
        print('Nome grande')