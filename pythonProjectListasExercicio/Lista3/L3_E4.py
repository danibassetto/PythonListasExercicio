salario = float(input('Insira seu salário: '))
prestacao_emprestimo = float(input('Insira a prestação do empréstimo: '))
if prestacao_emprestimo > (20/100) * salario:
    print('Empréstimo não concedido!')
else:
    print('Empréstimo concedido!')