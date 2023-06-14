# Algoritmo que recebe nome e idade do usuário, verificando sua maioridade.
# Considera-se maior de idade uma pessoa com 18 anos ou mais.

pessoa = input('Qual é o seu nome? ')
idade = int(input('Qual a sua idade? '))
if idade >= 18:
  print(pessoa,'você tem',idade,'anos, então você é maior de idade.')
else:
  print(pessoa,'você tem',idade,'anos, então você não é maior de idade.')
