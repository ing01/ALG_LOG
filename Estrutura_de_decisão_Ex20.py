##Faça um programa que receba o salário inicial de um funcionário, calcule e mostre o novo salário, acrescido de bonificação e de auxílio escola.

##SALÁRIO	BONIFICAÇÃO
##Até 500,00	5% do salário
##Entre 500,00 e 1.200,00	12% do salário
##Acima de 1.200,00	Sem bonificação

##SALÁRIO	AUXÍLIO ESCOLA
##Até 600,00	150,00
##Acima de 600,00	100,00

##novo_salario = salario + bonificacao + auxílio escola

salario = float(input('Qual o salário? '))
if salario <= 500:
  bonifi = salario * 5/100
  print('A bonificação será de R$',bonifi)
elif salario > 500 and salario <=1200:
  bonifi = salario * 12/200
  print('A bonificação será de R$',bonifi)
elif salario > 1200:
  bonifi = 0
  print('Não há bonificação.')
  
if salario <= 600:
  aux = 150
  print('O auxílio escola será de R$',aux)
else:
  aux = 100
  print('O auxílio escola será de R$',aux)
novo_salario = salario + bonifi + aux
print('O novo salário será de R$',novo_salario)
