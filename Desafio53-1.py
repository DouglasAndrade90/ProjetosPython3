frase = str(input('Digite uma frase para verificar se ela é Palindromo: ')).strip().upper()
divisao = frase.split()
junto = ''.join(divisao)
inverso = ''
print(junto)
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(inverso)
if inverso == junto:
    print(f'{frase}\033[1:36m É UM PALÍNDROMO.\033[m ')
else:
    print(f'{frase}\033[1;31m NÂO É UM PALÍNDROMO.\033[m ')