from datetime import datetime
datetime.now().time()
time = str(datetime.now().time())[:8]

print('='*54)
print(' '*17, ' BANCO SANGUE-SUGA')
print('='*54)

ced = 100
totalced = 0

valor = int(input('Digite o valor a ser sacado: R$ '))
total = valor
while True:
    if total >= ced:
        total -= ced
        totalced += 1

    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R$ {ced}. ')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totalced = 0
        if total == 0:
            break

print('-'*54)
print(' '*7, 'OBRIGADO POR UTILIZAR NOSSOS SERVIÇOS. ')
print(' '*12, 'AG. 171, Poços de Caldas - MG. ')
print(time)


