base = float(input('Base: '))
altura = float(input('Altura: '))
op = int(input('Escolha o polígono para cálculo da área\n'
               '1. Retângulo\n'
               '2. Triângulo\n'
               'Opção >> '))
if op != 1 and op != 2:
    print('Opção inválida!')
else:
    if op == 1:
        area = base * altura
        print('Área do retângulo:',area)
    else:
        area = (base * altura)/2
        print('Área do triângulo:',area)