# Algoritmo que recebe gênero do usuário (M/F) e calcula seu peso ideal, utilizando as seguintes fórmulas:
# Masculino: (72.7 * altura) - 58; Feminino: (62.1 * altura) - 44.7

pessoa = input('Qual o seu sexo? ')
altura = float(input('Qual sua altura? '))
masculino = (72.7 * altura) - 58;
feminino = (62.1 * altura) - 44.7
if pessoa == feminino:
  print('Seu peso ideal é de',feminino,'kg.')
else:
  print('Seu peso ideal é de',masculino,'kg.')