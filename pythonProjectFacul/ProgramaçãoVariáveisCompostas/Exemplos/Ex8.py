meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
print("Informe a data")
dia = int(input("Dia >> "))
mes = int(input("Mês >> "))
ano = int(input("Ano >> "))
print(f'{dia:02} de {meses[mes-1]} de {ano}')
