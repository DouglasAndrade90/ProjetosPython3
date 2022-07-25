n = 0
cont = 0
s = 0
while True:
    n = int(input('Digite um número, 999 para encerrar. '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'A soma de {cont} valores é de {s}. ')


