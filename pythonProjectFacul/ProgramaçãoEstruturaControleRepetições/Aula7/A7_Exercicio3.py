'''
Elabore um algoritmo, que simule um Caixa de supermercado. Para isso, leia preços e a quantidade comprada
de cada produto. Calcule  e mostre o total que o cliente gastou em sua compra. Encerrar o algoritmo
quando for digitado 0 para o preço.
'''

soma = 0
print('OBS: para encerrar a compra, dê enter e digite 0 no valor do produto')
while True:
    P = input('Produto: ')
    VP = float(input('Valor do produto: '))
    if VP > 0:
        Q = int(input('Quantidade: '))
        print(f'Produto: {P} Preço total: R${VP*Q:.2f}')
        soma += (VP * Q)
        print(50 * '-')
    else:
        break
print(50 * '-')
print(f'Total a pagar: R$ {soma:.2f}')