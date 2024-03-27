"""nome = str(input('Qual é seu nome: '))
if nome == 'Julia':
    print('Que nome bonito!')
else:
    print('Seu nome é comum')
print('Bom dia, {}'.format(nome))"""

n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
media = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(media))

if media >= 6.00:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média está abaixo do esperado!')