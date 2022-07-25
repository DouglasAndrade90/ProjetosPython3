from random import randint

jogador = 0
cont = 0

while True:
    if jogador == 'PERDEU':
        break
    escolhajogador = str(input('Escolha PAR ou ÍMPAR: ')).strip().upper()
    print(f'Você escolheu {escolhajogador}')
    jogador = int(input('Digite o número que deseja jogar: '))
    print('-'*30)

    if escolhajogador == 'PAR':
        escolhacomputador = 'ÍMPAR'
    else:
        escolhacomputador = 'PAR'
    print(f'O computador fica com {escolhacomputador}')
    computador = randint(0,999)
    print(f'E jogou {computador} ')
    print('-'*30)

    s = computador + jogador
    if s % 2 == 0:
        s = 'PAR'
    else:
        s = 'ÍMPAR'
    print(f'O resultado foi {s}. ')

    if s == escolhajogador:
        jogador = 'VENCEU'
        cont += 1
        print('PARABÉNS, você venceu! ')
        print('-'*30)
    else:
        jogador = 'PERDEU'

print(f'Que pena, você perdeu! ')
print(f'Mas venceu {cont} vezes' if cont > 1 else 'E não venceu nenhuma vez. ')

