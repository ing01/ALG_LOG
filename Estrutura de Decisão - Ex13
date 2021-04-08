##Faça um programa que receba quatro valores: I, A, B e C. Desses valores, I é inteiro e positivo, A, B e C são reais. Escreva os números A, B e C obedecendo à tabela a seguir.
##Suponha que o valor digitado para I seja sempre um valor válido, ou seja, 1, 2 ou 3, e que os números digitados sejam diferentes um do outro.
##VALOR DE I	FORMA A ESCREVER
##1	A, B e C em ordem crescente.
##2	A, B e C em ordem decrescente
##3	O maior fica entre os outros dois números.

I = int(input('Digite um valor inteiro entre 1,2 e 3: '))
A = float(input('Digite o primeiro valor real: '))
B = float(input('Digite o segundo valor real: '))
C = float(input('Digite o terceiro valor real: '))
if I == 1:
  if A<B and A<C:
    if B<C:
      print('A ordem crescente dos números é:',A,'-',B,'-',C)
    else:
      print('A ordem crescebte dos números é:',A,'-',C,'-',B)
if B<A and B<C:
  if A<C:
    print('A ordem crescente dos números é:',B,'-',A,'-',C)
  else:
    print('A ordem crescente dos números é:',B,'-',C,'-',A)
if C<A and C<B:
  if A<B:
    print('A ordem crescente dos números é:',C,'-',A,'-',B)
  else:
    print('A ordem crescente dos números é:',C,'-',B,'-',A)
if I == 2:
  if A>B and A>C:
    if B>C:
      print('A ordem decrescente dos números é:',A,'-',B,'-',C)
    else:
      print('A ordem decrescente dos números é:',A,'-',C,'-',B)
if B>A and B>C:
  if A>C:
    print('A ordem decrescente dos números é:',B,'-',A,'-',C)
  else:
       print('A ordem decrescente dos números é:',B,'-',C,'-',A)
if C>A and C>B:
  if A>B:
    print('A ordem decrescente dos números é:',C,'-',A,'-',B)
  else:
    print('A ordem decrescente dos números é:',C,'-',B,'-',A)
if I == 3:
  if A>B and A>C:
    print('A ordem desejada é:',B,'-',A,'-',C)
  if B>A and B>C:
    print('A ordem desejada é:',A,'-',B,'-',C)
  if C>A and C>B:
    print('A ordem desejada é:',A,'-',C,'-',B)
