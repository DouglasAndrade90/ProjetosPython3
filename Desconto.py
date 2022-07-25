p = float(input('Digite o preço atual do produto: R$ '))
i = float(input('Digite a taxa de desconto do produto: R$ '))
s = p - p * (i/100)
print('O valor final do produto será de: R$ ', s)