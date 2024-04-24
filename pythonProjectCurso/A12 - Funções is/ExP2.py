'''Programa que pergunte a hora ao usuário e, baseando-se no
horário descrito exiba a saudação apropriada'''

horario = input('Digite um horário (0-23): ')
if horario.isdigit():
    horario = int(horario)
    if horario < 0 or horario > 23:
        print('Horário inválido')
    else:
        if horario <= 11:
            print('Bom dia!')
        else:
            if horario <= 17:
                print('Boa tarde!')
            else:
                print('Boa noite!')
else:
    print('Por favor, digite um horário entre 0 e 23')