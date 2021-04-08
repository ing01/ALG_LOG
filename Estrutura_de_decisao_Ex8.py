##A nota final de um estudante é calculada a partir de três notas atribuídas, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final.
##NOTA	PESO
##Trabalho de laboratório	2
##Avaliação semestral	3
##Exame final	5
##Faça um programa que receba as três notas, calcule e mostre a média ponderada e o conceito que segue a tabela
##MÉDIA PONDERADA	CONCEITO
##8,0 <= média <= 10	A
##7,0 <= média < 8,0	B
##6,0 <= média < 7,0	C
##5,0 <= média < 6,0	D
##0,0 <= média < 5,0	E
##media_ponderada = (nota_traballho * 2 + avaliacao_semestral * 3 + exame_final * 5) / 10

trabLab = float(input('Qual a nota do trabalho de laboratório? '))
avali = float(input('Qual a nota da avaliação bimestral? '))
exame = float(input('Qual a nota do exame final? '))
mediaPon = (trabLab * 2 + avali * 3 + exame * 5) / 10
if mediaPon >= 8.0 and mediaPon <=10:
  print('Sua nota final é A.')
elif mediaPon >= 7.0 and mediaPon < 8.0:
  print('Sua nota final é B.')
elif mediaPon >= 6.0 and mediaPon < 7.0:
  print('Sua nota final é C.')
elif mediaPon >= 5.0 and mediaPon < 6.0:
  print('Sua nota final é D.')
else:
  print('Sua nota final é E.')
