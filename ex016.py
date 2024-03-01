km = float(input('Infome a kilometragem percorrida com o carro: '))
dias = int(input('Informe quantos dias o carro foi usado: '))
valor = (dias*60) +( km*0.15)
print('O valor total a pagar será de R${:.2f}'.format(valor))