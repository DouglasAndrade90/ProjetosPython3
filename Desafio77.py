lista = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON','CURSO',
         'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR',
         'FUTURO' )

for vog in lista:
    print(f'\nNa palavra {vog.upper()} temos ', end= ' ')
    for letra in vog:
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')
