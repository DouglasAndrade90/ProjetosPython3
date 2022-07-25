from datetime import datetime
from datetime import date
descontoavista = 10
descontocartao = 5
preconormal = 0
juros = 0.2
print('='*54)
print(' '*20, 'LOJAS 250')
print('='*54)
datetime.now().time()
time = str(datetime.now().time())[:8]
print(date.today())
print(time)
print('-'*54)
valor = float(input('Digite o valor do produto: R$ '))
forma = int(input('''Selecione a forma de pagamento: 
        (1) À VISTA/DÉBITO
        (2) À VISTA 1X DIRETO NO CARTÂO
        (3) 2X NO CARTÃO
        (4) ACIMA DE 3X (com juros) 
        (5) CANCELAR '''))

if forma == 1:
    forma2 = 'À VISTA/DÉBITO'
    valorfinal = valor - valor * (descontoavista/100)
elif forma == 2:
    forma2 = 'À VISTA 1 X DIRETO NO CARTÂO DE CRÈDITO'
    valorfinal = valor - valor * (descontocartao/100)
elif forma == 3:
    forma2 = '2 X NO CARTÃO'
    valorfinal = valor
elif forma == 4:
    forma2 = 'ACIMA DE 3 X NO CARTÃO'
    valorfinal = valor + valor * juros
else:
    forma2 = 'FINALIZADO'

if forma == 1 or forma == 2:
    print('-'*54)
    print(' '*17, 'FORMA DE PAGAMENTO')
    print(forma2)
    print(' '*20, 'VALOR TOTAL')
    print(f'Valor', ('-'*20),f'{valor:.2f}')
    print(f'Desconto', ('-'*18), f'{valor - valorfinal:.2f}')
    print(f'Valor total:',('-'*13), f'{valorfinal:.2f}')
elif forma == 3:
    print('-' * 54)
    print(' ' * 17, 'FORMA DE PAGAMENTO')
    print(forma2)
    print(f'Valor', ('-'*20), f'{valor:.2f}')
    print('Valor da parcela',('-' * 9), f'{valor / 2:.2f}')
elif forma == 4:
    print('-' * 54)
    print(' ' * 17, 'FORMA DE PAGAMENTO')
    print(forma2)
    parcela = int(input('Digite a quantidade de parcelas: '))
    print(f'Valor',('-'*20), f'{valor:.2f}')
    print(f'Juros',('-'*21), f'{valor*juros:.2f}')
    print(f'Valor total',('-'*14), f'{valorfinal:.2f}')
    print(f'Valor da parcela',('-'*9),f'{valorfinal/parcela:.2f}')
else:
    print('\nLOJAS 250 AGRADECE A PREFERÊNCIA!!!')















