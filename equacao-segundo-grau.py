# Algoritmo que resolve equações do 2º grau.
# Fórmula: ax² + bx + c = 0

print('Observe a seguinte equação de segundo grau e insira os valores: ax² + bx + c = 0')
a = float(input('Qual o valor de "a"? '))
b = float(input('Qual o valor de "b"? '))
c = float(input('Qual o valor de "c"? '))
if A == 0:
  print('Estes valores não formam uma esquação de segundo grau.')
else:
  delta = (b ** 2) - (4 * a * c)
if delta < 0:
  print('Não existe raiz real.')
if delta == 0:
  print('Existe uma raiz real.')
  x1 = (- b) / (2 * a )
  print('O valor de x é:',x1)
if delta > 0:
  print('Existem duas raízes reais.')
  x1 = (- b) + delta / (2 * a)
  x2 = (+ b) + delta / (2 * a)
  print('O valor de x1 é: ',x1,'\n' 'O valor de x2 é: ', x2) 
