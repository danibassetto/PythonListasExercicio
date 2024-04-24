# Algoritmo que lê a idade de um nadador e determina sua categoria
i=int(input("Digite a idade do nadador: "))
if i<=8:
    print("Categoria Infantil A")
else:
    if i<13:
        print("Categoria Infantil B")
    else:
        if i<18:
            print("Categoria Juvenil A")
        else:
            if i<21:
                print("Categoria Juvenil B")
            else:
                print("Categoria Sênior")
print("FIM")
