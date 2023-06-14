# O algoritmo calcula valor de crédito especial a partir do saldo médio do usuário, de acordo com a tabela.
# Saldo médio de 0 a 200 =  nenhum crédito;
# de 201 a  400 = 20% do valor do saldo médio;
# de 401 a  600 = 30% do valor do saldo médio;
# acima de 601 = 40% do valor do saldo médio.

saldo = float(input('Qual o saldo médio? '))
if saldo >= 0 and saldo <= 200:
  print('O saldo médio é de,',saldo,'portanto, não receberá crédito.')
elif saldo >=201 and saldo <= 400:
  valor1 = saldo * 20/100
  print('O saldo médio é de,',saldo,'o valor do crédito recebido é de R$', valor1)
elif saldo >=401 and saldo <=600:
  valor2 = saldo * 30/100
  print('O saldo médio é de',saldo,'o valor do crédito recebido é de R$', valor2)
else:
  valor3 = saldo * 40/100
  print('O saldo médio é de',saldo,'o valor do crédito recebido é de R$', valor3)
