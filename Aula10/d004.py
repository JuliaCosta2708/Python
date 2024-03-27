#Código para verificar se o ano informado é bixesto
from datetime import date
ano = int(input('Informe o ano que quer analisar?(Coloque 0 se quiser saber sobre o ano atual... )'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: 
    print('O ano de {} é BISSEXTO!'.format(ano))
else:
    print('O ano de {} não é bissexto!'.format(ano))
