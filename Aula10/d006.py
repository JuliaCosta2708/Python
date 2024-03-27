salario = float(input('Qual é o sálario do funcionário: R$'))
if salario <= 1250:
    novo = salario + (salario*15/100)
else:
    novo = salario + (salario*10/100)
print('O novo slário será R${:.2f}'.format(novo))