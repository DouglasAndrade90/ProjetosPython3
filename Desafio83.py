prnt = []

exp = str(input('Digite uma expressão: ')).strip().upper()
for c in exp:
    if c  == '(':
        prnt.append('(')
    elif c == ')':
        if len(prnt) > 0:
            prnt.pop()
        else:
            prnt.append(')')
            break
if len(prnt) == 0:
    print('Sua expressão está correta. ')
else:
    print('Sua expressão está incorreta. ')