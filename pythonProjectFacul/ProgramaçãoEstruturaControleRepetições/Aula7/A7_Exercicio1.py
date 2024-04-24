''' Elabore um algoritmo que leia  uma nota. Caso uma nota lida seja inválida,
emitir mensagem e repetir a entrada de dados. '''

while True:
    nota = float(input('Insira uma nota: '))
    if nota < 0 or nota > 10:
        print('Nota inválida!')
    else:
        print('Nota:',nota)
        break