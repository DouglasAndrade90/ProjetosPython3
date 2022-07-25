from random import randint
from time import sleep
velocidade = randint(20,210)
print('='*51)
print(' '*20, 'DETRAN MG', ' '*20)
print('='*51)
print('Verificando a velocidade aferida... ')
print('CARREGANDO... ')
sleep(3)
print(velocidade, 'Km/h')
if velocidade > 80:
    multa = float(velocidade - 80) * 7
    print('Seu veículo foi multado! o valor da multa é de: R${}' .format(multa))
else:
    print('Você estava na adequada da rodovia. ')



