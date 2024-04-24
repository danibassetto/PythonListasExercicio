#Juntando dois dicionários
meus_contatos = {'Yan': '1234-5678', 'Pedro': '9999-9999',
                    'Ana': '8765-4321', 'João': '8887-7778'}

contatos_do_pedro = {'Yan': '1234-5678', 'Fernando': '4345-5434',
                        'Luiza': '4567-7654'}

for nome in contatos_do_pedro:
    meus_contatos[nome] = contatos_do_pedro[nome]

print(meus_contatos)

# ou
meus_contatos = {'Yan': '1234-5678', 'Pedro': '9999-9999',
                    'Ana': '8765-4321', 'João': '8887-7778'}

contatos_do_pedro = {'Yan': '1234-5678', 'Fernando': '4345-5434',
                        'Luiza': '4567-7654'}

meus_contatos.update(contatos_do_pedro)
print(meus_contatos)


meus_contatos_novo = {nome: '9' + meus_contatos[nome] for nome in meus_contatos}
print(meus_contatos_novo)
