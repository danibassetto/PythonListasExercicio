"""
Analisador léxico com base no código em C - Aula 03

Caroline Ferreira dos Santos 630608
Danielle Barros Bassetto 629391
Jéssica Ferreira dos Santos 630616
"""


def is_letra(caractere):
    return caractere.lower() in letras


def is_digito(caractere):
    return caractere in digitos


def is_simbolo_especial(caractere):
    return caractere in simbolos_especiais


def is_simbolo_composto(token, proximo_caractere):
    composto_potencial = token + proximo_caractere
    for simbolo in simbolos_compostos:
        if composto_potencial == simbolo:
            return True
    return False


def is_palavra_reservada(token):
    return token in palavras_reservadas


def add_token(token, tipo):
    tokens.append({'token': token, 'tipo': tipo})


def analyze_token(token):
    if token:
        if is_palavra_reservada(token):
            add_token(token, 'Palavra Reservada')
        elif all(is_digito(c) for c in token):
            add_token(token, 'Número')
        elif is_letra(token[0]):
            add_token(token, 'Identificador')


letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']
digitos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos_especiais = ['.', ';', ',', '(', ')', ':', '+', '-', '<', '>', '=', '*', '%', '{', '}', '"']
simbolos_compostos = ['++', '--', '>=', '<=', '==', '!=', '+=', '-=', '*=', '/=', '%=']
palavras_reservadas = ['auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double', 'else', 'enum',
                       'extern', 'float', 'for', 'goto', 'if', 'int', 'long', 'register', 'return', 'short', 'signed',
                       'sizeof', 'static', 'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile',
                       'while', 'printf']

tokens = []

with open('arquivo-c.txt', 'r', encoding="utf8") as arquivo:
    for line in arquivo:
        linha = line.strip() + ' '
        token = ''
        i = 0
        while i < len(linha):
            caractere = linha[i]
            if caractere == ' ' or caractere in simbolos_especiais:
                analyze_token(token)
                token = ''
                if is_simbolo_especial(caractere):
                    if i + 1 < len(linha) and is_simbolo_composto(caractere, linha[i + 1]):
                        add_token(caractere + linha[i + 1], 'Símbolo Composto')
                        i += 1
                    else:
                        add_token(caractere, 'Símbolo Especial')
            else:
                token += caractere
            i += 1

for token_info in tokens:
    print(f"Token: {token_info['token']} Tipo: {token_info['tipo']}")
