# Algoritmo que receba a altura e peso de uma pessoa. Mostra a classificação dessa pessoa.

altura = float(input('Qual sua altura? '))
peso = float(input('Qual seu peso? '))
if altura < 1.20:
  if peso <= 60:
    print('Sua classificação é A.')
  if peso > 60 and peso <= 90:
    print('Sua classificação é D.')
  if peso > 90:
    print('Sua classificação é G.')
if altura >= 1.20 and altura <= 1.70:
  if peso <= 60:
     print('Sua classificação é B.')
  if peso > 60 and peso <= 90:
    print('Sua classificação é E.')
  if peso > 90:
    print('Sua classificação é H.')
if altura > 1.70:
  if peso <= 60:
    print('Sua classificação é C.')
  if peso > 60 and peso <= 90:
    print('Sua classificação é F.')
  if peso > 90:
    print('Sua classificação é I.')
