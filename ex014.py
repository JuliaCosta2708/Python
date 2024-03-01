salario1 = float(input('Informe o salário antigo: R$'))
porcent = int(input('Qual será a porcentagem de reajuste: '))
aumento = salario1*porcent/100
novosal= salario1+aumento
print('O salário desse funcionário com {}% de aumento será de R${:.2f}'.format(porcent,novosal))