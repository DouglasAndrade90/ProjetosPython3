'''print('='*54)
print(' '*14, 'CALCULADORA DE FATORIAL')
print('='*54)

n = int(input('Digite um número qualquer: '))
c = n
f = 1
while c > 0:
   print(c, end= '')
   print(' x ' if c > 1 else ' = ', end= '')
   f = f * c
   c -= 1
print(f)'''

print('='*54)
print(' '*14, 'CALCULADORA DE FATORIAL')
print('='*54)
f = 1
n = int(input('Digite um número qualquer: '))
for c in range (n, 0, -1):
   print(c, end='')
   print(' x ' if c > 1 else ' = ', end='')
   f = f * c
print(f)
