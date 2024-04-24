n1 = int(input('Insira um número inteiro: '))
n2 = int(input('Insira outro número inteiro: '))
if n1 > n2:
    print(f'{n1} é maior que {n2}\n'
          f'{n1} - {n2} = {n1 - n2}')
else:
    print(f'{n2} é maior que {n1}\n'
          f'{n2} - {n1} = {n2 - n1}')