from random import randint
print('=' * 54)
print(' '*20, 'PAR ou ÍMPAR')
print('='*54)

s = 0
cont = 0
jogador = 0

while True:
    if jogador == 'PERDEU':
        break

    jogador = int(input('Digite um número para PAR ou ÍMPAR: '))

    if jogador % 2 == 0:
        escolhajogador = 'PAR'
    else:
         escolhajogador = 'ÍMPAR'
    print(f'Sua escolha é {escolhajogador} ')
    print('-'*30)

    computador = randint(0,999)

    if escolhajogador == 'PAR':
        escolhacomputador = 'ÍMPAR'
    else:
        escolhacomputador = 'PAR'

    print(f'Computador {computador} ')
    print(f'A escolha do computador é {escolhacomputador}')
    print('-'*30)

    s = computador + jogador
    print(f' O total foi {s}. ')
    if s % 2 == 0:
        s = 'PAR'
    else:
        s = 'ÍMPAR'
    print(f'O resultado foi {s}')
    print('-'*30)

    if s == escolhajogador:
        jogador = 'VENCEU'
        print('Parabéns, você VENCEU! ')
        cont += 1
        print('-'*30)
    else:
        jogador = 'PERDEU'

print(f'Que pena, você PERDEU!')
print(f'Mas venceu {cont} vezes' if cont > 0 else 'E não Venceu nenhuma vez. ')









