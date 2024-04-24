''' Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros '''

preco = float(input("Preço da compra: R$ "))
print(''' FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão ''')
opcao = int(input("Qual forma deseja utilizar? "))

if opcao == 1:
    total = preco - (10 / 100 * preco)
elif opcao == 2:
    total = preco - (5 / 100 * preco)
elif opcao == 3:
    total = preco
    parcela = preco / 2
    print(f"Sua compra será parcelada em 2x de R${parcela:.2f}")
elif opcao == 4:
    total = preco + (20 / 100 * preco)
    parcela = total / 3
    print(f"Sua compra será parcelada em 3x de R${parcela:.2f}")
else:
    print("Forma de pagamento inválida!")
print("Total:", total)
