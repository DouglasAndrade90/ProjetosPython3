lista = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON','CURSO',
         'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR',
         'FUTURO' )

for vog in lista:
    print(f'\Na palavra {vog.upper()} existem : ', end= ' ')
    for letra in vog:
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')