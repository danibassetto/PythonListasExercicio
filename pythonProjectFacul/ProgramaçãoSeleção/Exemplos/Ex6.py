idade = int(input("Idade >> "))
if idade < 10:
    print('Criança')
else:
    if idade < 18:
        print('Adolescente')
    else:
        if idade < 60:
            print('Adulto')
        else:
            print('3ª idade')
print('FIM')