##Elabore um algoritmo que informando a idade de um nadador o mesmo terá condições de classificar em uma das seguintes categorias:
##infantil = 5 - 10 anos;
##juvenil = 11-17 anos;
##adulto = maiores de 18 anos.

idade = int(input('Digite sua idade: '))
if idade >= 5 and idade <= 10:
  print('Você pode se classificar para a categoria Infantil.')
elif idade >= 11 and idade <= 17:
  print('Você pode se classificar para a categoria Juvenil.')
elif idade >= 18:
  print('Você pode se classificar para a categoria Adulto.')
else:
  print('Você não pode se classificar para nenhuma categoria.')
