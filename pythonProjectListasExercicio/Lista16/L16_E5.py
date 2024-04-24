'''
Um anagrama é uma palavra que é feita a partir da transposição das letras de outra palavra. Por
exemplo, “Iracema” é um anagrama para “America”. Escreva um programa em Python que tenha
uma função que receba duas strings por parâmetro e decida se uma string é um anagrama de
outra string. A função deve considerar maiúsculas e minúsculas como sendo caracteres iguais, ou
seja, “a” = “A”. A função deve retornar True se uma string for anagrama da outra e False caso
contrário.
No programa principal, leia as duas strings e chame a função. Imprima se as duas strings são ou
não anagrama uma da outra.
'''


def anagrama(str1, str2):
    if len(str1) != len(str2):
        return False
    for letra in str1.upper():
        if letra not in str2.upper():
            return False
    return True


p1 = input('Informe a 1ª palavra >> ')
p2 = input('Informe a 2ª palavra >> ')
if anagrama(p1, p2):
    print(f'{p1} é um anagrama de {p2}')
else:
    print(f'{p1} não é um anagrama de {p2}')
