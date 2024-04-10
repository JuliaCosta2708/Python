#Bloco 1 - Declarando variavéis de valor da casa, salario e tempo para calcular o valor da pestação
valor_casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$'))
tempo_financiamento = int(input('Quantos anos será o financiamento? '))

#Bloco 2 - Cálculo do valor da prestação por tempo de financiamento desejado
prestacao = valor_casa / (tempo_financiamento * 12)
print('Para pagar uma casa de R${:.2f} em {}anos'.format(valor_casa, tempo_financiamento))
print('A prestação mensal será de R${}'.format(prestacao))

#Bloco 3 - Condição de o valor da prestção representa até 30% do valor do salário
if prestacao <= (salario*(30/100)):
    print('Financiamento aturoizado!')
else:
    print('Financiamento NEGADO!')