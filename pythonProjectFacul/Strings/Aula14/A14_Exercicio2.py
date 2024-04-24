''' Elabore um programa, que leia um string e na sequência, um caractere. Verifique quantas vezes este caractere aparece
no string.  Faça isso, de forma iterativa e também, use o método “COUNT” do Python e teste-o. '''

frase = input("Digite uma frase: ")
letra = input("Digite uma letra: ")

c = 0
for i in range(len(frase)):
    if frase[i] == letra:
        c += 1

print("Existem", c, "letras", letra, "na frase", frase)

# OU

print("USANDO COUNT:", frase.count(letra))
