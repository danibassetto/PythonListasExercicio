# Faça um programa que leia um ano qualquer e mostre se ele é bissexto
import datetime

ano = int(input("Que ano deseja analisar? "))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("ANO BISSEXTO!")
else:
    print("ANO NÃO BISSEXTO")
