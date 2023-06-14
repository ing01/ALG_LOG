# Algoritmo que determina a data cronologicamente maior entre duas datas fornecidas pelo usuário.

dia1 = int(input('Insira um dia: '))
mes1 = int(input('Insira um mês (no formato numérico): '))
ano1 = int(input('Insira um ano: '))
dia2 = int(input('Insira um segundo dia: '))
mes2 = int(input('Insira um segundo mês: '))
ano2 = int(input('Insira um segundo ano: '))
if ano1 > ano2:
  print('A maior data é: ',dia1,'-',mes1,'-',ano1)
elif ano2 > ano1:
  print('A maior data é: ',dia2,'-',mes2,'-',ano2)
elif mes1 > mes2:
  print('A maior data é: ',dia1,'-',mes1,'-',ano1)
elif mes2 > mes1:
  print('A maior data é: ',dia2,'-',mes2,'-',ano2)
elif dia1 > dia2:
  print('A maior data é: ',dia1,'-',mes1,'-',ano1)
elif dia2 > dia1:
  print('A maior data é: ',dia2,'-',mes2,'-',ano2)
else:
  print('As datas são iguais!')
