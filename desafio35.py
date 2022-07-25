print('='*54)
print(' '*13, 'ANALISADOR DE TRIÂNGULOS')
print('='*54)
r1 = float(input('Digite o tamanho da primeira reta: '))
r2 = float(input('Digite o tamanho da segunda reta: '))
r3 = float(input('Digite o tamanho da terceira reta: '))
print('-'*54)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É POSSÍVEl formar um triângulo com os dados inseridos. ')
else:
    print('NÂO É POSSÍVEL formar um triângulo com os dados inseridos. ')


