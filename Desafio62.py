print('='*54)
print(' '*15, 'PROGRESSÃO ARITMÉTICA')
print('='*54)

pt = int(input('Digite o primeiro termo da progressão aritmética: '))
r = int(input('Digite a razão da progressão aritmética: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(pt, end= ' → ')
        pt += r
        cont += 1
    print('PAUSA')
    mais = int(input('Deseja mostrar mais quantos termos? Digite [0] para finalizar. '))
print(f' A Progressão Aritmética foi finalizada e foram mostrados {cont} termos. ')

