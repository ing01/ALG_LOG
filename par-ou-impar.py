# Algoritmo que recebe um número inteiro e mostre uma mensagem indicando se este número é par ou ímpar e se é positivo ou negativo.

numero = int(input('Escreva um número inteiro: '))
resto = numero % 2
if resto == 0:
  print('Seu número é par.')
else:
  print('Seu número é ímpar.')
if numero >= 0:
  print('Seu número é positivo.')
else:
  print('Seu número é negativo.')
