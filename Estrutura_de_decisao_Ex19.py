##Faça um programa que apresente o menu a seguir, permita ao usuário escolher a opção desejada, receba os dados necessários para executar a operação e mostre o resultado. 
##Verifique a possibilidade de opção inválida e não se preocupe com restrições, como salário negativo.

##Na opção 1: receber o salário de um funcionário, calcular e mostrar o valor do imposto usando as regras a seguir.
##SALÁRIO	PERCENTUAL DO IMPOSTO
##Menor que 500,00	5%
##De 500,00 (inclusive) a 850,00 (inclusive)	10%
##Acima de 850,00	15%

##Na opção 2: receber o salário de um funcionário, calcular e mostrar o valor do novo salário, usando as regras a seguir.
##SALÁRIO	AUMENTO
##Maior que 1.500,00	25,00
##De 750,00 (inclusive) a 1.500,00 (inclusive)	50,00
##De 450,00 (inclusive) a 750,00	75,00
##Menor que 450,00	100,00

##Na opção 3: receber o salário de um funcionário e mostrar sua classificação usando a tabela a seguir.
##SALÁRIO	CLASSIFICAÇÃO
##Até 700,00 (inclusive)	Mal remunerado
##Maiores que 700,00	Bem remunerado

salario = float(input('Qual o salário? '))
print('Menu de opções:''\n' '1. Imposto' '\n' '2. Novo salário' '\n' '3. Classificação')
op = int(input('Escolha uma opção: '))
if op == 1:
  if salario < 500:
    imposto = salario * 5/100
    print('O valor do imposto é de R$',imposto)
  if salario >= 500 and salario <= 850:
    imposto = salario * 10/100
    print('O valor do imposto é de R$',imposto)
  if salario > 850:
    imposto = salario * 15/100
    print('O valor do imposto é de R$',imposto)
if op == 2:
  if salario > 1500:
    aumento = salario + 25
    print('O valor do novo salário é de R$',aumento)
  if salario > 750 and salario <= 1500:
    aumento = salario + 50
    print('O valor do novo salário é de R$',aumento)
  if salario > 450 and salario <= 750:
    aumento = salario + 75
    print('O valor do novo salário é de R$',aumento)
  if salario < 450:
    aumento = salario + 100
    print('O valor do novo salário é de R$',aumento)
if op == 3:
  if salario <= 750:
    print('Mal remunerado.')
  else:
    print('Bem remunerado.')
