'''
Abra um arquivo texto, calcule e escreva o número de caracteres, o número de linhas e o número de
palavras neste arquivo. Escreva também quantas vezes cada letra ocorre no arquivo (ignorando letras
com acento). Obs.: palavras são separadas por um caractere espaço ou nova linha.
'''

try:
    letras = {}
    file = open('dados.txt','r')
    carac = 0
    palavras = 0
    for nome in file:
        carac += len(nome.strip('\n'))
        palavras += len(nome.split())
        for l in nome.lower():
            if l.isalpha():
                letras[l] = letras.get(l,0) + 1
    print(f'No texto há {carac} caracteres')
    file.seek(0)
    texto = file.readlines()
    print(f'No texto há {len(texto)} linhas')
    print(f'No texto há {palavras} palavras')
    print(letras)
    file.close()
except:
    print('ERRO')