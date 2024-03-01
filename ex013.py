produto = float(input('Qual o valor do produto: R$'))
desconto = int(input('Qual a porcentagem de desconto: '))
valor = produto*desconto/100
new = produto-valor
print('O valor desse produto com desconto de {}% é de R${:.2f}'.format(desconto,new))