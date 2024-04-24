tradutor = {}
try:
   f = open('palavras.txt', 'r')
   for line in f:
        port, ingl = line.split()
        tradutor[port] = ingl
except:
    print('Arquivo não encontrado!')

print(tradutor)

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