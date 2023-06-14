# Algoritmo que define valores de X, Y e Z e define se eles podem ser os comprimentos dos lados de um triângulo e qual.
# Se eles não formarem um triângulo, exibe outra mensagem.

x = float(input('Digite um valor para X: '))
y = float(input('Digite um valor para y: '))
z = float(input('Digite um valor para z: '))
if x < y + z and y < x + z and z < x + y:
  if x == y and y == z:
    print('Triângulo equilátero.')
  elif x == y or x == z or y == z:
    print('Triângulo isósceles.')
  elif x != y and x != z and y != z:
    print('Triângulo escaleno.')
else:
  print('Essas medidas não formam um triângulo.')
