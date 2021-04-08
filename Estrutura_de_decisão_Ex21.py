##Faça um programa que receba o valor do salário mínimo, o número de horas trabalhadas, o número de dependentes do funcionário e a quantidade de horas extras trabalhadas.
##Calcule e mostre o salário a receber do funcionário
##VALORES FIXOS PRÉ-ESTABELECIDOS

salario_min = float(input('Qual o valor do salário? '))
horas_trab = int(input('Quantas são as horas trabalhadas? '))
numeros_dep = int(input('Quantos são os dependentes? '))
horas_ex = int(input('Qual a quantidade de horas extras trabalhadas? '))
valor_hr = 1/5 * salario_min
salario_mes = horas_trab * valor_hr
valor_dep = 32 * numeros_dep
valor_hr_ex = horas_ex * (valor_hr + (valor_hr * 50/100))
salario_bruto = salario_mes + valor_dep + valor_hr_ex
if salario_bruto < 200:
  imposto = 0
elif salario_bruto >= 200 and salario_bruto <= 500:
  imposto = salario_bruto * 10 / 100
elif salario_bruto > 500:
  imposto = salario_bruto * 20 / 100
salario_liq = salario_bruto - imposto
if salario_liq <= 350:
  grat = 100
else:
  grat = 50
salario_receb = salario_liq + grat
print('O salário recebido pelo funcionário é de R$',salario_receb)
