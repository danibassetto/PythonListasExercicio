'''
Faça um programa para simular um tradutor de palavras Português/Inglês – Inglês/Português.
Para isto crie um dicionário com duas palavras, uma para armazenar a palavra em português e a
outra para o inglês. Faça um laço para armazenar N palavras, informando as duas, após dê a opção
ao usuário escolher se ele quer entrar com uma palavra em inglês e saber a tradução ou viceversa. Faça uma busca da
palavra informada e a mostre na outra língua. Permita quantas consultas o usuário desejar.
'''

print('Vamos inserir as palavras no tradutor!! '
      'Insira as palavras em português e inglês')
tradutor = {}
while True:
    port = input('Português -> ').upper()
    if port not in tradutor:
        ingl = input('Inglês    -> ').upper()
        tradutor[port] = ingl
    else:
        print(f'{port} já se encontra no tradutor')
    r = input('Deseja inserir mais uma palavra? [S/N] -> ').upper()[0]
    if r != 'S':
        break

while True:
    print("=" * 40)
    print('TRADUTOR'.center(40))
    print("=" * 40)
    op = input('1. Português para Inglês\n'
               '2. Inglês para Português\n'
               '3. Sair\n'
               'Opção -> ')
    if op == '1':
        port = input('Português -> ').upper()
        if port in tradutor:
            print(f'{port} em inglês é {tradutor[port]}')
        else:
            print(f'{port} não se encontra no tradutor')
    elif op == '2':
        ingl = input('Inglês -> ').upper()
        if ingl in tradutor.values():
            for p in tradutor:
                if tradutor[p] == ingl:
                    print(f'{ingl} em português é {p}')
        else:
            print(f'{ingl} não se encontra no tradutor')
    elif op == '3':
        break
    else:
        print('Opção inválida!!')