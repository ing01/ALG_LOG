##Faça um programa que receba de um produto:
##o preço
##o tipo (A — alimentação; L — limpeza; e V — vestuário)
##a refrigeração (S — produto que necessita de refrigeração; e N — produto que não necessita de refrigeração).

##Suponha que haverá apenas a digitação de dados válidos e, quando houver digitação de letras, utilize maiúsculas. Calcule e mostre:
##O valor adicional
##O valor do imposto
##O preço de custo, ou seja, preço mais imposto. O desconto.
##O produto que não preencher nenhum dos requisitos a seguir terá desconto de 3%, caso contrário, 0 (zero).
##VALORES FIXOS PRÉ-ESTABELECIDOS

preco = float(input('Qual o preço do produto? '))
tipo = input('Qual o tipo do produto?''\n' 'A - Alimentação' '\n' 'L - Limpeza' '\n' 'V - Vestuário')
refrig = input('Selecione a opção que indica o tipo de refrigeração' '\n' 'S - Refrigeração necessária' '\n' 'N - Não precisa de refrigração')
if refrig == 'N':
  if tipo == 'A':
    if preco < 15:
      valor_adic = 2
    else: 
      valor_adic = 5
    if tipo == 'L':
      if preco < 10:
        valor_adic = 1.5
      else:
        valor_adic = 2.5
    if tipo == 'V':
      if preco < 30:
        valor_adic = 3
      else:
        valor_adic = 2.5
elif tipo == 'A':
  valor_adic = 8
  if tipo == 'L':
    valor_adic = 0
  if tipo == 'V':
    valor_adic = 0
print('O valor adicional do produto é de R$',valor_adic)
if preco < 25:
  imposto = 5/100 * preco
else: 
  imposto = 8/100 * preco

print('O valor do imposto é de R$',imposto)
pre_custo = preco + imposto
print('O preço de custo é de R$',pre_custo)

if tipo != 'A' and refrig != 'S':
  desconto = 3/100 * pre_custo
else: 
  desconto = 0
print('O desconto é de R$',desconto)

novo_preco = pre_custo + valor_adic - desconto
print('O novo preço é de R$',novo_preco)

if novo_preco <= 50:
  print('Barato.')
elif novo_preco < 100:
  print('Normal.')
else:
  print('Caro.')
