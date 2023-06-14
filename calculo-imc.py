# Cálculo de IMC dado pela fórmula da OMS:
# IMC = peso / (altura)²

peso = float(input('Qual o seu peso? '))
altura = float(input('Qual sua altura? '))
IMC = peso / (altura) **2
if IMC <18.5:
  print('Você está abaixo do peso.')
elif IMC >=18.5 and IMC <=25:
  print('Você está no peso ideal.')
elif IMC >=25.1 and IMC <=30:
  print('Você está acima do peso.')
else: 
  print('Você está na condição de obesidade.')
