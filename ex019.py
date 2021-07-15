from random import choice
print('Digite o nome dos participantes do sorteio:')
k2 = input('Nome 1:')
k1 = input('Nome 2:')
k3 = input('Nome 3:')
k4 = input('Nome 4:')
win = choice([k1, k2, k3, k4])
print('O ganhador foi {}'.format(win))
