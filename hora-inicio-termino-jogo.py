# Algoritmo que receba a hora do início de um jogo e a hora do término mostrando a duração do jogo 
# (horas e minutos), sabendo que o tempo máximo de duração do jogo é de 24 horas e que ele pode começar 
# em um dia e terminar no dia seguinte.

horaInicio = int(input('Que horas começa o jogo?' ))
minutoInicio = int(input('Em quantos minutos começa o jogo? '))
horaFinal = int(input('Que horas termina o jogo? '))
minutoFinal = int(input('Em quantos minutos acaba o jogo? '))
if minutoInicio > minutoFinal:
    minutoFinal = minutoFinal + 60
    horaFinal = horaFinal - 1
if horaInicio > horaFinal:
    horaFinal = horaFinal + 24
minutoDura = minutoFinal - minutoInicio
horaDura = horaFinal - horaInicio
print('O jogo dura',horaDura,'horas e',minutoDura,'minutos.')
