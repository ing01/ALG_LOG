##Faça um programa que receba o salário base e o tempo de serviço de um funcionário.
##VALORES FIXOS PRÉ-ESTABELECIDOS

salario_base = float(input('Qual o salário base? '))
tempo = float(input('Qual o tempo de serviço do funcionário? '))
if salario_base < 200:
    imposto = 0
elif salario_base <= 450:
    imposto = 3/100 * salario_base
elif salario_base < 700:
    imposto = 8/100 * salario_base
else:
    imposto = 12/100 * salario_base
print('O valor do imposto é R$ ',imposto)
if salario_base > 500:
  if tempo <= 3:
    gratificacao = 20
  else:
    gratificacao = 30
if tempo <= 3:
    gratificacao = 23
elif tempo < 6:
    gratificacao = 35
else:
    gratificacao = 33
print('O valor da gratificação é de R$ ',gratificacao)
salario_liq = salario_base - imposto + gratificacao
print('O salário líquido é R$ ',salario_liq)
if salario_liq <= 350:
  print('Classificação A.')
elif salario_liq < 600:
  print('Classificação B.')
else:
  print('Classificação C.')
