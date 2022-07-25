'''galera = [['João', 19], ['Maria', 33], ['Ana', 22] , ['Paulo', 53]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade. ')'''
totmaior = totmenor = 0
galera = []
dado = []
for c in range(0,3):
    dado.append(str(input('Digite o nome: ')))
    dado.append(int(input('Digite a idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade. ')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade. ')
        totmenor+=1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade. ')