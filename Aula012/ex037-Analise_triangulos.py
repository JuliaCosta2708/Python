#Bloco 1- Informando os tamnahos das retas
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceito segmento: '))

#Bloco 2 - Condição primaria para saber se as retas podem ou não formar u triângulo
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segimentos acima PODEM formar um triângulo!", end='')
#Bloco 3 - If dentro do outro para verificar o tipo do teiêngulo, apenas se a condição anterior for vdd. end="" coloca o pirnt da condição que for verdadeir a jno final da primeira
    if r1 == r2 == r3:
        print('É um triângulo EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('É um triângulo ESCALENO!')
    else:
        print('É um triângulo ISÓCELES')
#Condição final da primeira condição
else: 
    print('Os segmentos NÃO PODEM formar um triângulo!')
