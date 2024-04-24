# Programa para calcular as raízes de uma equação de segundo grau


a = float(input('Digite o coeficiente a: '))
b = float(input('Digite o coeficiente b: '))
c = float(input('Digite o coeficiente c: '))

print()

delta = (b ** 2) - 4 * a * c
raiz_delta = delta ** 0.5

if a == 0:
    print('Não é uma equação de segundo grau!')
else:
    if delta < 0:
        print('Não existe raiz real!')
    else:
        if delta == 0:
            x1 = (- b + raiz_delta) / (2 * a)
            x2 = (- b - raiz_delta) / (2 * a)
            print(f'Raiz única! (x1=x2)\n'
                  f'x1 = {x1:.2f}\n'
                  f'x2 = {x2:.2f}')
        else:
            x1 = (- b + raiz_delta) / (2 * a)
            x2 = (- b - raiz_delta) / (2 * a)
            print(f'Duas raízes\n'
                  f'x1 = {x1:.2f}\n'
                  f'x2 = {x2:.2f}')
print()
print('FIM')