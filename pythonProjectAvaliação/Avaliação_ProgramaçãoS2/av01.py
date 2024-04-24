'''
GRUPO 8
Danielle Barros Bassetto
César Augusto de Almeida
João Vitor Adonis
'''

texto = input().lower()

pontuacao = [".",  ",",  ":",  ";",  "!",  "?"]
for i in range(len(pontuacao)):
    texto = texto.replace(pontuacao[i], ' ')  # substituindo a pontuação por espaço

texto = texto.split()  # separando as palavras

palindromos = []
for i in texto:
    if i == i[::-1] and len(i) > 2 and i not in palindromos:  # verificando se a palavra já foi verificada/contabilizada e se é palíndromo
        palindromos.append(i)
        print(i, texto.count(i))