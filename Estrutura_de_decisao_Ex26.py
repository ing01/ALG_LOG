##Faça um programa que receba:
##O código de um produto comprado, supondo que a digitação do código do produto seja sempre válida, isto é, um número * inteiro entre 1 e 10.
##O peso do produto em quilos.
##O código do país de origem, supondo que a digitação do código seja sempre válida, isto é, um número inteiro entre 1 e 3.

##CÓDIGO DO PAÍS DE ORIGEM	IMPOSTO
##1	0%
##2	15%
##3	25%

##CÓDIGO DO PAÍS DO PRODUTO	IMPOSTO
##1 a 4	10
##5 a 7	25
##8 a 10	35

##Calcule e mostre:
##o peso do produto convertido em gramas;
##o preço total do produto comprado;
##valor do imposto, sabendo que ele é cobrado sobre o * preço total do produto comprado e dependendo país de origem;
##o valor total, preço total do produto mais imposto.

cod_prod = int(input('Qual o código do produto? '))
peso_kg = float(input('Qual o peso do produto? '))
codigo_pais = int(input('Qual o código do país de origem? '))
peso_gram = peso_kg * 1000
print('O peso em gramas do produto é: ',peso_gram,'kg.')
if cod_prod >= 1 and cod_prod <= 4:
  preco_gram = 10
if cod_prod >= 5 and cod_prod <= 7:
  peco_gram = 24
if cod_prod >= 8 and cod_prod <= 10:
  preco_gram = 35
preco_total = peso_gram * preco_gram
print('O preço total do produto é R$',preco_total)
if codigo_pais == 1:
  imposto = 0
if codigo_pais == 2:
  imposto = preco_total * 15 / 100
if codigo_pais == 3:
  imposto = preco_total * 25 / 100
print('O imposto é de: ',imposto)
valor_total = preco_total + imposto
print('O valor total do produto é de R$',valor_total)
