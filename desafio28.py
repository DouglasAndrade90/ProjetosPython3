from random import randint
from time import sleep
computador = randint(0,5)
print('='*54)
print('\033[1;30;47mVou pensar em um número e você tenta adivinhar qual é:\033[m ')
print('='*54)
sleep(2)
print('PENSANDO... ')
sleep(3)
jogador = int(input('\033[1;30;47mDigite um número entre 0 e 5:\033[m '))
if jogador == computador:
    print('\033[1;33;46mVocê venceu! PARABÉNS!\033[m')
else:
    print('\033[1;31;40mVocê perdeu, eu pensei no número {} e não no {} \033[m'.format(computador, jogador))

















