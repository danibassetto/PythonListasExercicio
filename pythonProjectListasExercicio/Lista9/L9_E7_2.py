from moduloData import validaEntrada, validaData

while True:
    d = input('Entre com a data no formato dd/mm/aaaa >> ')
    if validaEntrada(d):
        break
    print('Entrada no formato inválido!!')

if validaData(d):
    print('Data válida!!')
else:
    print('Data inválida!!')