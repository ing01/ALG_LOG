##Faça um programa que mostre a data e a hora do sistema nos seguintes formatos: dia/mês/ano – mês por extenso e hora:minuto.

from datetime import datetime
hoje = datetime.now()
print ('Ano atual:',hoje.year)
print ('Mês:',hoje.month)
print ('Dia:',hoje.day)
print ('Hora:',hoje.hour)
print ('Minuto:',hoje.minute)
print ('Segundos:',hoje.second)
if hoje.month == 1:
    print(hoje.day,'/ janeiro /',hoje.year, hoje.hour,':',hoje.minute)
if hoje.month == 2:
    print(hoje.day,'/ fevereiro /',hoje.year, hoje.hour,':',hoje.minute)
if hoje.month == 3:
    print(hoje.day,'/ março /',hoje.year, hoje.hour,':',hoje.minute)
if hoje.month == 4:
    print(hoje.day,'/ abril /',hoje.year, hoje.hour,':',hoje.minute)
if hoje.month == 5:
    print(hoje.day,'/ maio /',hoje.year, hoje.hour,':',hoje.minute)
if hoje.month == 6:
    print(hoje.day,'/ junho /',hoje.year, hoje.hour,':',hoje.minute)
if hoje.month == 7:
    print(hoje.day,'/ julho /',hoje.year, hoje.hour,':',hoje.minute)
if hoje.month == 8:
    print(hoje.day,'/ agosto /',hoje.year, hoje.hour,':',hoje.minute)
if hoje.month == 9:
    print(hoje.day,'/ setembro /',hoje.year, hoje.hour,':',hoje.minute)
if hoje.month == 10:
    print(hoje.day,'/ outubro /',hoje.year, hoje.hour,':',hoje.minute)
if hoje.month == 11:
    print(hoje.day,'/ novembro /',hoje.year, hoje.hour,':',hoje.minute)
if hoje.month == 12:
    print(hoje.day,'/ dezembro /',hoje.year, hoje.hour,':',hoje.minute)
