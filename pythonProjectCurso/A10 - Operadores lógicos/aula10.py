'''
Operadores lógicos
and (e)
or (ou)
not
in (estar naquilo)
not in (Não está naquilo)
'''

'''
(Verdadeiro E Verdadeiro) = Verdadeiro
(Verdadeiro E Falso) = Falso
(Falso E Falso) = Falso

(Verdadeiro OU Verdadeiro) = Verdadeiro
(Verdadeiro OU Falso) = Verdadeiro
(Falso OU Falso) = Falso

PensaR no not como um mentiroso, porque tudo que 
tem not junto é o contrário, por exemplo:
not False é True
not True é False
'''

nome = 'Danielle'
if 'u' in nome:
    print('Existe a letra U no seu nome.')
else:
    print('Não tem U no seu nome.')
print()
if 'e' not in nome:
    print('Não tem E no seu nome.')
else:
    print('Tem E no seu nome.')
print()

a = ''
b = 0
c = 2
d = 3

if not a:
    print('Por favor, preencha o valor de A.')
if not b:
    print('Por favor, preencha o valor de B.')
if not d > c: # inverte o valor, se retornaria verdadeiro, vai retornar falso
    print('D é maior que C.')
else:
    print('C é maior que D.')

