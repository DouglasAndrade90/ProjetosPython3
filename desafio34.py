from time import sleep
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m'}
print('='*54)
print(' '*10, 'TABELA DE AUMENTO DE SALÁRIO ')
print('=' *54)
sleep(2)
salario = float(input('Digite o valor do salário atual: R$ '))
print('-'*54)
print(' '*19, 'Calculando ')
print('-'*54)
sleep(2)
if salario >= 1250:
    aumento = salario * 0.10 + salario
else:
    aumento = salario * 0.15 + salario
print('O novo salário será de: R$ {} {:.2f}{}'.format('\033[1;30;43m',aumento, '\033[m'))