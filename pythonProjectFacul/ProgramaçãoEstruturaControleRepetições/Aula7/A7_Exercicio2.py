'''
Elabore um algoritmo que leia idades de um grupo de pessoas e, calcule e mostre a média
das idades lidas. O algoritmo deverá ser encerrado quando a idade lida for zero (0).
'''

soma = 0
tp = 0  # Total de pessoas
while True:
    id = int(input('Insira a idade ou 0 para encerrar: '))
    if id > 0:
        tp += 1
        soma += id
    else:
        break
if tp == 0:
    print('Não houve idades inseridas!')
else:
    M = soma / tp
    print('Média das idades =',M)