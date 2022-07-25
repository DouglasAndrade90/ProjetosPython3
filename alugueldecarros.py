dia = int(input('Quantos dias o carro foi alugado? '))
valor = float(input('Qual foi o valor da diária? R$ '))
km = float(input('Quantos kms o veículo percorreu? '))
preco = float(input('Digite o preço do km: R$ '))
vtotal = dia * valor + km * preco
print('O valor pago pelo aluguel de {} dias do veículo foi de: R${:.2f} '.format(dia,vtotal))