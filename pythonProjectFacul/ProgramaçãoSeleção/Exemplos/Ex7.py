idade = int(input("Idade >> "))
if idade < 10:
    print('Criança')
elif idade < 18:
    print('Adolescente')
elif idade < 60:
    print('Adulto')
else:
    print('3ª idade')
print('FIM')