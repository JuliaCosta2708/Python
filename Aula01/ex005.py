n1 = int(input('Digite um valor: '))
n2 = int(input('digite outro valor: '))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n a subtração é {}, \n o produto é {}, \n a divisão simples é {}'.format(s, sub, m, d), end= ' ')
print('A divisão inteira é {}, a potência é {}'.format(di, e))