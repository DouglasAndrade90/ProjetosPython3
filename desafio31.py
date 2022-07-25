from time import sleep
print('='*52)
print(' '*18, 'VIAÇÃO JÁ FUI', ' '*20)
print('='*52)
cidade = str(input('Digite o nome da cidade desejada: ')).strip()
distancia = float(input('Digite a distância até {} Kms: '.format(cidade)))
print('-'*52)
print('Calculando valores... ')
print('-'*52)
sleep(3)
if distancia <=200:
    d = distancia * 0.50
    print('\033[1;30;41mO valor da passagem para {} é de: R$ {} \033[m'.format(cidade, d))
else:
    d1 = distancia * 0.45
    print('\033[7;4;30;41mO valor da passagem para {} é de: R$ {:.2f}\033[m '.format(cidade, d1))
