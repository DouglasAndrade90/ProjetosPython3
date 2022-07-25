soma = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        print(c)
        soma = soma + c
        cont = cont + 1
print(f'A soma de todos os {cont} itens é : {soma}.')

