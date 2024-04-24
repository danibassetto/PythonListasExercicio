'''Elaborar  um  programa  em Pythonpara  ler  somente  a  parte  numérica  da  placa  de  um  carro e
apresentar o dia do rodízio (em SP) para o mesmo (digitar apenas um número com 4 dígitos, fazer a validação).'''

placa = int(input('Informe a parte númerica da placa: '))
if placa > 9999:
    print('Placa inválida!')
else:
    ud = placa % 10
    if ud == 1 or ud == 2:
        print('Rodízio de segunda-feira')
    elif ud == 3 or ud == 4:
        print('Rodízio de terça-feira')
    elif ud == 5 or ud == 6:
        print('Rodízio de quarta-feira')
    elif ud == 7 or ud == 8:
        print('Rodízio de quinta-feira')
    else:
        print('Rodízio de sexta-feira')