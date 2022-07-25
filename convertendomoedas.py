real = float(input('Digite o valor que possui em real: R$ '))
dolar = float(input('Digite a cotação do dolar hoje: $ '))
s = real / dolar
print('O valor que consegue comprar hoje são: $ {:.2f}'.format(s))