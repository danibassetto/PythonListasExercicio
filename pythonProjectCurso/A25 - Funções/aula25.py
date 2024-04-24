'''
Funções - def em python (Parte 01)
'''

# quando utilizo função, se eu precisar mudar algo é só mudar dentro da função, facilita alterações e repetições de código
def funcao():
    print("Hello World")


funcao()
funcao()
funcao()
funcao()

print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")


# posso utilizar parâmetros e a funcao só será executada se eles forem preenchidos, lembrando que são enviados na ordem

def saudacao(msg):
    print(msg)


saudacao('Mensagem')
saudacao('Eu posso escrever o que eu quiser')
saudacao()
saudacao()


def saudacao2(msg, nome):
    print(msg, nome)


saudacao2('Oi', 'Dani')


def saudacao3(msg='Olá', nome='usuário'):  # parãmetro padrão para caso o usuário não informe
    print(msg, nome)


saudacao3()
saudacao3('Olá', 'Maria')
saudacao3(nome='Zezinho')


# geralmente não usamos print dentro de função

def ola(msg='Olá', nome='usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    return f'{msg} {nome}'


variavel = saudacao()
print(variavel)
