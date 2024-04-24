'''
QUANTIDADE DE CARACTERES - LEN
já é retornado como int, o que possibilia contas diretas
'''

usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print('Você precisa digitar pelo menos 6 caracteres')
else:
    print('Você foi cadastrado no sistema.')
print()
string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')
print(f'A quantidade total de caracteres digitados foi {len(string1) + len(string2)}')
