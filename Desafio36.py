from time import sleep
print('='*54)
print(' '*16,'BANCO SANGUE-SUGA')
print('='*54)
print(' '*6,'Cálculo de Fincanciamento Habitacional')
print('-'*54)
valor_imovel = float(input('Digite o valor do imóvel desejado: R$ '))
salario = float(input('Digite o valor do seu salário mensal: R$ '))
periodo = int(input('Qual o prazo de pagamento (em meses): '))
if periodo < 12:
    periodo = periodo * 12
valor_parcela = valor_imovel / periodo
proporcao_salarial = (valor_parcela / salario) *100
print('.'*54)
print(' '*20, 'CALCULANDO')
print('.'*54)
sleep(3)
print('O valor da parcela será de R$ {:.2f}. '.format(valor_parcela))
if proporcao_salarial > 30:
    proporcao_salarial = '\033[1;31mNEGADA\033[m'
elif proporcao_salarial > 25 or proporcao_salarial == 30:
    proporcao_salarial = '\033[1;33mNECESSITA DE REVISÃO\033[m'
else:
    proporcao_salarial = '\033[1;32mAPROVADA\033[m'
print(f'Sua solicitação foi {proporcao_salarial} pelo banco emissor. ')
