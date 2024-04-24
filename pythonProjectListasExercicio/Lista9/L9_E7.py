'''Faça um programa que leia uma data e determine se ela é válida, ou seja, verifique se o mês está
entre 1 e 12, e se o dia existe naquele mês. Note que Fevereiro tem 29 dias em anos bissextos, e
28 dias em anos não bissextos.'''


def validaEntrada(data):
    if len(data) != 10:
        return False
    if data[2] != '/' or data[5] != '/':
        return False
    if not data.replace('/', '').isdigit():
        return False
    return True


def isBissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        return True
    return False


def validaData(data):
    dia, mes, ano = data.split('/')
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
    if mes == 2:
        if isBissexto(ano):
            if 1 <= dia <= 29:
                return True
        else:
            if 1 <= dia <= 28:
                return True
    elif mes in [1, 3, 5, 7, 8, 10, 12]:
        if 1 <= dia <= 31:
            return True
    elif mes in [4, 6, 9, 11]:
        if 1 <= dia <= 30:
            return True
    return False


while True:
    d = input('Entre com a data no formato dd/mm/aaaa >> ')
    if validaEntrada(d):
        break
    print('Entrada no formato inválido!!')

if validaData(d):
    print('Data válida!')
else:
    print('Data inválida!')
