chv = list()
expr = str(input('Digite a expressão: '))
for c in expr:
    if c == '(':
        chv.append('(')
    elif c == ')':
        if len(chv) > 0:
            chv.pop()
            break
        else:
            chv.append(')')
if len(chv) == 0:
    print('Sua expressão está correta. ')
else:
    print('Sua expressão está incorreta. ')