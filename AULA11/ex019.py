import math
angulo = float(input('Digite o ângulo que você deseja saber: '))
seno = math.sin(math.radians(angulo))

cosseno = math.cos(math.radians(angulo))

tangente = math.tan(math.radians(angulo))

print('O ângulo de {} graus tem\n o seno de {:.2f}\n o cosseno de {:.2f}\n e a tangente de {:.2f}'.format(angulo, seno, cosseno, tangente))
