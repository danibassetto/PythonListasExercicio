'''Elabore um algoritmo que leia uma frase e verifique se uma palavra existe na frase lida. '''

frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra: ")

if palavra in frase:
    print("Palavra existe na frase")
else:
    print("Palavra não existe na frase")