import random
from time import sleep
print('='*54)
print(' '*20, 'JOQUEMPÕ')
print('='*54)
jogador = int(input('''Digite sua jogada:
      (1) PEDRA:
      (2) PAPEL:
      (3) TESOURA: '''))
print('-'*54)
print('JO')
sleep(1)
print('QUEM')
sleep(1)
print('PÔ')
if jogador == 1:
    escolha = 'PEDRA'
elif jogador == 2:
    escolha = 'PAPEL'
elif jogador == 3:
    escolha = 'TESOURA'
else:
    print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE!')
print('-'*54)
print(f'Você escolheu: {escolha}')
lista = ['PEDRA', 'PAPEL', 'TESOURA']
random.shuffle(lista)
computador = random.choice(lista)
print(f'Computador: {computador}')
print('-'*54)
sleep(2)
if computador == 'PEDRA' and jogador == 3:
    print('\033[1:31mQUE PENA, VOCÊ PERDEU!\033[m')
elif computador == 'TESOURA' and jogador == 2:
    print('\033[1;31mQUE PENA, VOCÊ PERDEU!\033[m')
elif computador == 'PAPEL' and jogador == 1:
    print('\033[1;31mQUE PENA, VOCÊ PERDEU!\033[m')
elif jogador == 1 and computador == 'TESOURA':
    print('\033[1;34mPARABÉNS, VOCÊ VENCEU!\033[m')
elif jogador == 3 and computador == 'PAPEL':
    print('\033[1;34mPARABÉNS, VOCÊ VENCEU!\033[m')
elif jogador == 2 and computador == 'PEDRA':
    print('\033[1;34mPARABÉNS, VOCÊ VENCEU!\033[m')
else:
    print('EMPATE!')





