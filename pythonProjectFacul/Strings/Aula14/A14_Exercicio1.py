'''Elabore um algoritmo que leia um string e verifique se ela é palíndromo. Um palíndromo é uma palavra que se lida da
esquerda para a direita, ou vice versa, é idêntica. Veja alguns exemplos: “ARARA”, “REVER”, “OVO”, etc. '''

print("Digite uma palavra:")
p = input()
inv = p[::-1]
print("Palavra = ", p)
print("Invertida =", inv)
if p == inv:
    print("São palindromos!")
else:
    print("Não são palíndromos!")
