a = int(input('1º Valor: '))
b = int(input('2º Valor: '))
c = int(input('3º Valor: '))

#Verificação do menor número
menor = a
if b <a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#Verificação do maior número
maior = a 
if b > a and b > c:
    maior = b
if c>a and c>b:
    maior = c

print('O menor valor é ', menor)
print('O maior valor é ', maior)

