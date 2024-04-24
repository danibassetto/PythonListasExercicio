# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma_idade = 0
mulheres_menos_vinte = 0
homem_mais_velho = 0
nome_hmais_velho = ''
for n in range(1, 5):
    print(f"---------- {n}° PESSOA ----------")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()
    soma_idade += idade
    if sexo == 'F':
        if idade < 20:
            mulheres_menos_vinte += 1
    if sexo == 'M':
        if n == 1:
            homem_mais_velho = idade
            nome_hmais_velho = nome
        if idade > homem_mais_velho:
            homem_mais_velho = idade
            nome_hmais_velho = nome
print()
media_idade = soma_idade / 4
print(f"Média das idades: {media_idade}\nNome do homem mais velho: {nome_hmais_velho}\nQuantidade de mulheres com menos "
      f"de 20 anos: {mulheres_menos_vinte}")
