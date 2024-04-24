# Repetição para validação

num = 0
while num < 1 or num > 10:
    num = int(input("Informe um número de 1 a 10: "))
    if num < 1 or num >10:
        print('Número inválido, digite novamente...')
print(f'Número informado = {num}')

