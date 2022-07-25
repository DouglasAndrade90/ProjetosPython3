menu = 0
s = 0
m = 0
maior = 0

while menu == 4 or menu != 5:
    print('=' * 54)
    print(' ' * 20, 'CALCULADORA')
    print('=' * 54)

    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    menu = int(input('''
    =====================
            MENU
    =====================
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR 
    ====================== '''))

    if menu == 1:
        print(' ')
        print('Você escolheu SOMAR. ')
        s = n1 + n2
        print(f'A soma entre {n1} e {n2} é \033[1;33m{s}\033[m.\n ')
        break


    if menu == 2:
        print('')
        print('Você escolheu MULTIPLICAR. ')
        m = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é \033[1;33m{m}.\033[m\n ')
        break


    if menu == 3:
        print('Você deseja saber qual é o MAIOR número inserido. ')
        if n1 > maior:
            maior = n1
        if n2 > maior:
            maior = n2
            print(f'O maior número inserido entre {n1} e {n2} é \033[1;33m{maior}\033[m\n ')
            break

    if menu == 5:
        print('-'*54)
        print(' '*14,'ENCERRADO PELO USUÁRIO')
        print('-'*54)

