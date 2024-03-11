import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hipo = math.hypot(co, ca)
print('A hipotenusa é {.:2f}'.format(hipo))
