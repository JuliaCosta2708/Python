#Código para calcular o preço de uma viagem por KM
import time
viagem = float(input('Qual será a distância da sua viagem em KM? '))
if viagem <= 200:
    preco = viagem * 0.50
    print('PROCESSANDO...')
    time.sleep(2)
    print('O valor da sua passangem será de R${}'.format(preco))
else:
    preco = viagem * 0.45
    print('PROCESSANDO...')
    time.sleep(2)
    print('O valor da sua passagem é de R${}'.format(preco))


#Outra forma de fazer
"""km = float(input('Qual será a distância da sua viagem em KM? '))
valor = km * 0.50 if km <= 200 else km * 0.45
print('O preço da sua passagem será de R${:.2f}'.format(valor))"""