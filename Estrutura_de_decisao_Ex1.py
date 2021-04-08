##Faça um algoritmo que calcule e exiba o salário reajustado de um funcionário de acordo com a seguinte regra: Salário até 500, reajuste de 50%;
##Salários maiores que 500, reajuste de 30%.

salario=float(input('Qual seu salário? '))
if salario <= 500:
    reajuste = salario + salario * 50/100
else:
    reajuste= salario + salario * 30/100
print('O seu salário reajustado é de R$',reajuste)
