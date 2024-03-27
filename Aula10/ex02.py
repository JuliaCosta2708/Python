import random
import time
computador = random.randint(0, 5)

print('-=-'*20)
print('Tente adivinhar que número eu pensei entre (0,5)Tente adivinhar...')
print('-=-')
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
time.sleep(2)
if jogador == computador:
    print('PARABÉN!Você acertou:)')
else:
    print('Que pena :( o número era: {}'.format(computador))