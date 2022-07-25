c = 1
s = 1
n = 0

while True:
    n = int(input('Digite um número: '))
    print('-'*30)
    if n < 0:
        break
    for c in range (1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-'*30)
print('PROGRAMA FINALIZADO! ')


