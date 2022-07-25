'''print('='*54)
print(' '*17, ' ANALISE DE LISTAS')
print('='*54)

valores = []

for c in range(0,5):
    n = int(input(f'Digite o número: '))
    if c == 0 or n > valores[-1]:
        valores.append(n)
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos,n)
                break
            pos += 1
print('-'*54)
print(f'Os valores digitados em ordem crescente foram {valores}')

print('='*54)
print(' '*17, ' ANALISE DE LISTAS')
print('='*54)

valores = []

for c in range(0,5):
    n = int(input('Digite um número: '))
    if c == 0 or n > valores[-1]:
        valores.append(n)
    else:
        pos = 0
        while pos <= len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                break
            pos += 1
print('-'*54)
print(f'Os números inseridos foram {valores}. ')'''

valores = []
for c in range(0,5):
    n = int(input('Digite um número: '))
    if c == 0 or n > valores[-1]:
        valores.append(n)
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                break
            pos += 1
print('-'*54)
print(f'Os valores inseridos foram {valores}. ')