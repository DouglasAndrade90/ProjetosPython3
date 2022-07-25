print('='*54)
print(' '*12, 'CALCULADORA DE TRIÂNGULO')
print('='*54)
r1 = float(input('Digite a medida da primeira reta: '))
r2 = float(input('Digite a medida da segunda reta: '))
r3 = float(input('Digite a medida da tecerira reta: '))
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('\033[1:34mÉ possível formar um triângulo com as medidas informadas.\033[m ')
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('Este é um TRIÂNGULO EQUILÁTERO. ')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Este é um TRIÂNGULO ISÓSCELES. ')
    else:
        print('Esse é um TRIÂNGULO ESCALENO. ')
else:
    print('\033[1:31mNão é possível formar um triângulo com as medidas informadas.\033[m ')



