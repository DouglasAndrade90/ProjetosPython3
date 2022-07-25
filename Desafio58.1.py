from random import randint
print('='*54)
print(' '*17, 'JOGO DA ADIVINHAÇÃO')
print('='*54)
n = 0
cont = 0
lista = randint(0,10)

while n != lista:
    n = int(input('Digite o número de 0 a 10 que o computador escolheu: '))
    print('-'*54)
    print(f'Você escolheu: {n}')
    print(f'Computador: {lista}\n')


    if n != lista:
        print('\033[1:33mQUE PENA, VOCÊ PERDEU!\033[m ')
        print('-'*54)
        cont += 1

if n == lista:
    print('\033[1;36mPARABÉNS! VOCÊ VENCEU!\033[m ')
    print(f'Você errou {cont} vezes. ')
    print('-'*21, 'FINALIZADO', '-'*21)

