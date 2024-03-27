#Radar eletrônico com cobrança de multas
import time
velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7.00
    print('Você ultrapassou o limite da via! MULTADO:/')
    print('PROCESSANDO...')
    time.sleep(3)
    print('Sua multa será no valor de R${:.2f}'.format(multa))
else:
    print('Você está no limite da via! Continue... :)')