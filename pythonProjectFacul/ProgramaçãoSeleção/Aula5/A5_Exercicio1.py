#  Algortimo de peso ideal
alt = float(input('Digite sua altura: '))
sexo = input('Insira seu sexo [F/M]: ').upper()[0]  # Coloco .upper pra não dar erro caso a pessoa digite minúsculo
if sexo != 'F' and sexo != 'M':
    print('Sexo inválido!')
else:
    if sexo == 'F':
        pi = 62.1 * alt - 44.7
        print(f'Peso ideal: {pi:.2f}')
    else:
        pi = 72.7 * alt - 58
        print(f'Peso ideal: {pi:.2f}')