print('='*54)
print(' '*17, 'CALCULADORA DE IMC')
print('='*54)
nome = str(input('Digite seu nome: ')).strip()
peso = float(input('Digite seu peso em KG: '))
altura = float(input('Digite sua altura: '))
imc = peso / altura ** 2
resultado = str(peso / altura ** 2)[:5]
if imc < 18.5:
    imc = '\033[1:32mABAIXO DO PESO\033[m'
elif imc > 18.5 and imc < 25:
    imc = 'com \033[1:34m PESO IDEAL\033[m'
elif imc == 25 or imc < 30:
    imc = 'com \033[1:32mSOBREPESO\033[m'
elif imc == 30 or imc < 40:
    imc = 'com \033[1:35mOBESIDADE\033[m'
else:
    imc = 'com \033[1:31mOBESIDADE MÓRBIDA\033[m'
print(f'Sr. {nome}, seu IMC é de {resultado} e você está {imc}. ')
