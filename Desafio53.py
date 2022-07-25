frase = str(input('Digite uma frase para verificar se é um Palíndromo: ')).strip().upper()
divisao = frase.split()
junto = ''.join(divisao)
inverso = junto[::-1]
print(junto)
print(inverso)
if inverso == junto:
    print(f'{frase}, \033[1:36m É UM PALÍNDROMO.\033[m ')
else:
    print(f'{frase}, \033[1:31m NÃO É UM PALÍNDROMO. \033[m')

