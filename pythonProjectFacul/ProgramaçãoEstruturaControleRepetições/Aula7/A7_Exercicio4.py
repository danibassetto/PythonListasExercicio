# Calculadora simples

while True:
    op = input('Digite a operação a ser realizada [+ - * /] ou # para encerrar: ')
    if op == '#':
        break
    else:
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite outro valor: '))
        if op == '+':
            r = n1 + n2
            print('Soma =',r)
        else:
            if op == '-':
                r = n1 - n2
                print('Subtração =',r)
            else:
                if op == '*':
                    r = n1 * n2
                    print('Multiplicação =',r)
                else:
                    if op == '/':
                        r = n1 / n2
                        print('Divisão =',r)
                    else:
                        print('Operação inválida!')
print('FIM')
