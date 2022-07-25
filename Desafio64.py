print('='*54)
print(' '*20,' CALCULADORA ')
print('='*54)

cont = 0
n = 0
s = 0

while n != 999:
    n = int(input('Digite um número qualquer: '))
    if  n != 999:
        s = s + n
    cont += 1

print('-'*54)
print(f' Foram digitados {cont} números. ')
print(f'A soma dos valores inseridos é de {s}. ')
print('-'*54)
print(' '*19, ' FINALIZADO ')
