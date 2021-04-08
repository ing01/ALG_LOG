##Faça um programa que receba três números obrigatoriamente em ordem crescente e um quarto número que não siga essa regra. Mostre, em seguida, 
##os quatro números em ordem decrescente. Suponha que o usuário digitará quatro números diferentes.

1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o quarto número: '))
n3 = float(input('Digite o terceiro número: '))
n4 = float(input('Digite o quarto número: '))
if n4 > n3:
  print('A ordem decrescente é:',n4,'-',n3,'-',n2,'-',n1)
if n4 > n2 and n4 < n3:
  print('A ordem decrescente é:',n3,'-',n4,'-',n2,'-',n1)
if n4 > n1 and n4 < n2:
  print('A ordem decrescente é:',n3,'-',n2,'-',n4,'-',n1)
if n4 < n1:
  print('A ordem decrescente é:',n3,'-',n2,'-',n1,'-',n4)
