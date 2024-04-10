num = int(input("Digite o número decimal que precisa converter: "))
print('''Escolha uma das bases para fazer a conversão: 
[ 1 ] Decimal -> Binário
[ 2 ] Decimal -> Octal
[ 3 ]Decimal -> Hexadecimal''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('O número {} convertido em binário é: {}'.format(num, bin(num))) 
elif opcao == 2:
    print('O número {} convertido em octal é: {}'.format(num, oct(num)))
elif opcao == 3:
     print('O número {} convertido em hexadecimal é: {}'.format(num, hex(num)))
else:
    print("Opção inválida!")
