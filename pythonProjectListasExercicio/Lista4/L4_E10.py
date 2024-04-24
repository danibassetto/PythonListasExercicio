''' ler  2  valores,  calcular  e  escrever  a  soma  dos  inteiros  existentes entre os 2 valores
lidos (incluindo os valores lidos na soma). O programa deve validar que o 1º  valor  informado  seja
menor  que  o  2º  valor.  O  programa  deve  permitir  que  o  usuário possa executá-lo novamente. '''

resp = 'S'
while resp == 'S':
    v1 = int(input('Insira o primeiro valor: '))
    v2 = int(input('Insira o segundo valor: '))

    soma = 0
    if v1 <= v2:
        while v1 <= v2:
            soma = soma + v1
            v1 += 1
    else:
        print('ERRO: valor 1 deve ser menor que o valor 2!')
    print(f'Soma dos inteiros: {soma}')
    resp = input('Deseja executar novamente? [S/N] ').upper()[0]