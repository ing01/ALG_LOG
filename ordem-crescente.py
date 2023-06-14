# Algoritmo que recebe três números DIFERENTES e mostra em ordem crescente. 

n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Informe o segundo número: '))
n3 = float(input('Informe o terceiro número : '))
if n1 < n2 and n1 < 13:
  if n2 < n3:
    print('A ordem crescente é:',n1,'-',n2,'-',n3)
  else:
    print('A ordem crescente é:',n1,'-',n3,'-',n2)
if n2 < n1 and n2 < n3:
  if n1 < n3:
    print('A ordem crescente é:',n2,'-',n1,'-',n3)
  else:
    print('A ordem crescente é:',n2,'-',n3,'-',n1)
if n3 < n1 and n3 < n2:
  if n1 < n2:
    print('A ordem crescente é:',n3,'-',n1,'-',n2)
  else:
    print('A ordem crescente é:',n3,'-',n2,'-',n1)
