# Quadrantes

x = float(input('Digite a coordenada x do ponto: '))
y = float(input('Digite a coordenada y do ponto: '))
if x > 0 and y > 0:
    print('1º Quadrante')
elif x < 0 and y > 0:
    print('2º Quadrante')
elif x < 0 and y < 0:
    print('3º Quadrante')
elif x > 0 and y < 0:
    print('4º Quadrante')
else:
    print('Origem')