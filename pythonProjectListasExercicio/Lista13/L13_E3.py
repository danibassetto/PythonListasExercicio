'''
Faça um programa que peça um texto e uma função que remova todas as vogais do texto,
recebido por parâmetro. Objetivo: pegar uma ‘string’ como input e retornar uma ‘string’ sem as
vogais.
'''


def remove_vogal(txt):
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return "".join([letra for letra in txt if letra not in vogais])


txt = input("Informe um texto: ")
print(f"Texto sem vogal: {remove_vogal(txt)}")

'''
#Código com loop tradicional
def removendoVogais_trad(sentenca):
    vogais = 'aeiou'
    lista_filtrada = []
    for s in sentenca:
        if s not in vogais:
            lista_filtrada.append(s)
    return ''.join(lista_filtrada)

#Código com compreensão de listas
def removendoVogais_cl(sentenca):
   vogais = 'aeiou'
   return ''.join([s for s in sentenca if s not in vogais])

texto = input('Informe um texto -> ')
print(removendoVogais_cl(texto))
'''