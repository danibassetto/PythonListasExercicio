trab_laborat = float(input('Insira a nota do trabalho de laboratório: '))
avaliacao = float(input('Insira a nota da avaliação bimestral: '))
exame_final = float(input('Insira a nota do exame final: '))
print()
media = ((trab_laborat * 2) + (avaliacao * 3) + (exame_final * 5)) / 10

if (trab_laborat < 0 or trab_laborat > 10):
    print('Nota do trabalho do laboratório inválida!')
else:
    if (avaliacao < 0 or avaliacao > 10):
        print('Nota da avaliação inválida!')
    else:
        if (exame_final < 0 or exame_final > 10):
            print('Nota do exame final inválida!')
        else:
            if media >= 0 and media < 2.9:
                print(f'Aluno reprovado!\n'
                      f'Média final = {media}')
            else:
                if media >= 3 and media < 4.9:
                    print(f'Aluno de recuperação!\n'
                          f'Média final = {media}')
                else:
                    print(f'Aluno aprovado!\n'
                          f'Média final = {media}')
print()
print('FIM')