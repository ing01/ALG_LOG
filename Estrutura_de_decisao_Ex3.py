##Tendo como dados de entrada a altura e o sexo (M/F) de uma pessoa (M-masculino ou F-feminino), construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#homem: (72.7 * altura) - 58;
#mulher: (62.1 * altura) - 44.7

pessoa = input('Qual o seu sexo? ')
altura = float(input('Qual sua altura? '))
masculino = (72.7 * altura) - 58;
feminino = (62.1 * altura) - 44.7
if pessoa == feminino:
  print('Seu peso ideal é de',feminino,'kg.')
else:
  print('Seu peso ideal é de',masculino,'kg.')
