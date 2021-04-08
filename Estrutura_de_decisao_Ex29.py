##Faça um programa que:
##receba o valor do salário mínimo,
##o turno de trabalho (M — matutino; V — vespertino; ou N — noturno),
##a categoria (O — operário; G — gerente)
##número de horas trabalhadas no mês de um funcionário.
##Suponha a digitação apenas de dados válidos e, quando houver digitação de letras, utilize maiúsculas.

##Calcule e mostre:
##O coeficiente do salário
##O valor do salário bruto, ou seja, o número de horas trabalhadas multiplicado pelo valor do coeficiente do salário.
##O imposto
##A gratificação, de acordo com as regras a seguir. Se o funcionário preencher todos os requisitos a seguir, sua gratificação será de 50,00; caso contrário, será de 30,00.
##Auxilio alimentação, um terço do seu salário bruto; caso contrário, será de metade do seu salário bruto.
##O salário líquido, ou seja, salário bruto menos imposto mais gratificação mais auxílio alimentação.
##A classificação
##VALORES FIXOS PRÉ-ESTABELECIDOS

salario_min = float(input('Qual o valor do salário mínimo? '))
turno = input('Qual seu turno?' '\n' '1. Matutino' '\n' '2. Vespertino' '\n' '3. Noturno')
categoria = input('Qual a categoria?' '\n' '1. Operário' '\n' '2. Gerente')
numero_de_hr_trab = int(input('Quantas são as horas trabalhadas? '))

if turno == '1':
  coeficiente = 10/100 * salario_min
if turno == '2':
  coeficiente = 15/100 * salario_min
if turno == '3':
  coeficiente = 12/100 * salario_min

print('O coeficiente do salário é: ',coeficiente)

salario_bruto = numero_de_hr_trab * coeficiente

print('O salário bruto é de R$ ',salario_bruto)

if categoria == '1':
  if salario_bruto >= 300:
    imposto = 5/100 * salario_bruto
  else:
    imposto = 3/100 * salario_bruto 
if salario_bruto >= 400:
  imposto = 6/100 * salario_bruto
else:
  imposto = 4/100 * salario_bruto
 
print('O valor do impsto é de R$ ',imposto)
 
if turno == '1' and numero_de_hr_trab > 80:
  gratificacao = 50
else:
  gratificacao = 30
 
print('O valor da graficiação é de R$',gratificacao)
 
if categoria == '1' or coeficiente <= 25:
  auxilio = 1/3 * salario_bruto
else:
  auxilio = 1/2 * salario_bruto
 
print('O valor do auxílio é de R$ ',auxilio)
 
salario_liq = salario_bruto - imposto + gratificacao + auxilio
 
print('O salário líquido é de R$ ',salario_liq)
 
if salario_liq < 350:
  print('Mal Remunerado.')
elif salario_liq >= 350 and salario_liq <= 600:
  print('Normal.')
else:
  print('Bem remunerado.')
