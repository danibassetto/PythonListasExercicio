'''
Uma biblioteca distribui um cartão magnético para que os alunos possam frequentá-la. A senha
inicial, enviada pelo correio, é gerada automaticamente a partir da data de nascimento do aluno
('dd/mm/aaaa') do seguinte modo:
dd+'$'+mm(invertido) + '#' + mm+'!'+dd(invertido) + '\'+aaaa
Exemplo:
Data de nascimento: 25/10/1995
25$01#10!52\1995
Escreva um programa em Python que tenha uma função que receba a data de nascimento por
parâmetro e retorne sua senha de acordo com as regras acima.
No programa principal, leia a data de nascimento (fazer a validação da data usando o módulo data
em anexo), chame a função e exiba a senha
'''

from moduloData import validaData, validaEntrada
def geraSenha(data):
    dia, mes, ano = data.split('/')
    senha = dia+'$'+mes[::-1]+'#'+mes+'!'+dia[::-1]+'\\'+ano
    return senha

while True:
    data = input("Entre com a data no formato dd/mm/aaaa >> ")
    if not validaEntrada(data):
        print('Formato inválido!! Digite novamente...')
    elif not validaData(data):
        print('Data inválida!! Digite novamente...')
    else:
        break

print(f"Sua senha é {geraSenha(data)}")