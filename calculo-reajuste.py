# Algoritmo que calcula reajuste de salário de acordo com o valor fornecido.
# Acima de R$500 = reajuste de 30%.

salario = float(input('Qual seu salário? '))
if salario <= 500:
    reajuste = salario + salario * 50/100
else:
    reajuste= salario + salario * 30/100
print('O seu salário reajustado é de R$',reajuste)
