##Um supermercado deseja reajustar os preços de seus produtos usando o seguinte critério: o produto poderá ter seu preço aumentado ou diminuído.
##Faça um programa que receba o preço atual e a venda média mensal do produto, calcule e mostre o novo preço.

preco_atual = float(input('Qual o valor atual do produto? '))
media_mensal = float(input('Qual a média mensal que esse produto vende? '))
if media_mensal < 500 or preco_atual < 30:
  novo_preco = preco_atual + 10 / 100 * preco_atual
elif media_mensal >= 500 and media_mensal < 1200 or preco_atual > 30 and preco_atual < 80:
  novo_preco = preco_atual + 15 / 100 * preco_atual
elif media_mental >= 1200 or preco_atual >= 80:
  novo_preco = preco_atual + 20 / 100 * preco_atual
print('O novo preço do produto é R$',novo_preco)
