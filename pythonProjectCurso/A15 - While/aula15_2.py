#        Índices
#        0123456789.......................33
frase = 'o rato roeu a roupa do rei de roma'  # Iterável (percorre cada elemento)
tamanho_frase = len(frase)
print(tamanho_frase)
contador = 0
nova_string = ''

'''
while contador < tamanho_frase:
    print(frase[contador], contador)
    contador += 1
'''
input_do_usuario = input('Qual letra deseja colocar em maiúscula: ')

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    contador += 1
print(nova_string)