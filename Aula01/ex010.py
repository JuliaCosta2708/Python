n1 = int(input('Digite um número para ver sua tabuada: '))
cont = 1
print('-'*15)
while cont <= 10:
    tab = n1 * cont
    print('{:2}  x  {:2} = {:2}'.format(n1,cont,tab))
    cont += 1
print('-'*15)