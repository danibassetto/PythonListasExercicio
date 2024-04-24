''' Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
conversão: 1 para binário, 2 para octal e 3 para hexadecimal. '''

num = int(input("Digite um número inteiro: "))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL ''')
opcao = int(input("Sua opção: "))
if opcao == 1:
    print(f"{num} convertido para binário é {bin(num)}")
elif opcao == 2:
    print(f"{num} convertido para octal é {oct(num)}")
elif opcao == 3:
    print(f"{num} convertido para hexadecimal é {hex(num)}")
else:
    print("Opção inválida, tente novamente!")
