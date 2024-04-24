''' Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso. '''

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opcao = 0
while opcao != 5:
    print('''[ 1 ] somar 
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    opcao = int(input(">>>>>> Qual é a sua opção? "))
    if opcao == 1:
        soma = n1 + n2
        print(f"SOMA = {soma}")
    elif opcao == 2:
        produto = n1 * n2
        print(f"MULTIPLICAÇÃO = {produto}")
    elif opcao == 3:
        if n1 > n2:
            print(f"Maior = {n1}")
        else:
            print(f"Maior = {n2}")
    elif opcao == 4:
        print("Informe os números novamente: ")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    elif opcao == 5:
        print("FIM")
    else:
        print("Opção inválida. Tente novamente!")
    print("=-" * 10)
