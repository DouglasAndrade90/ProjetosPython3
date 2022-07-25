n = int(input('Digite um número inteiro: '))
print('''Selecione a base de conversão:
(1) para BINÁRIO
(2) para OCTAL
(3) para HEXADECIMAL''')
escolha = int(input('Sua escolha: '))
if escolha == 1:
    print(bin(n)[2:])
elif escolha == 2:
    print(oct(n)[2:])
elif escolha == 3:
    print(hex(n)[2:])
else:
    print('OPÇÃO INVÁLIDA. Tente novamente!')



