prnt = list()
expr = str(input('Digite uma expressão: '))
for c in expr:
    if c == '(':
        prnt.append('(')
    elif c == ')':
        if len(prnt) > 0 :
            prnt.pop()
            break
        else:
            prnt.append(')')
if len(prnt) == 0:
    print('Sua expressão está correta. ')
else:
    print('Sua expressão está incorreta. ')
