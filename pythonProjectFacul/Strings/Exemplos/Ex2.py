numero = input('Número >> ')
if numero.isdigit():
    numero = int(numero)
    print(f'O dobro de {numero} é {numero * 2}')
else:
    print('Valor inválido!!')
