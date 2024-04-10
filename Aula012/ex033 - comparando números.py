numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))

if numero1 > numero2:
    print('O número {} é maior que o número {}'.format(numero1, numero2))
elif numero1 < numero2:
    print('O número {} é maior que o número {}'.format(numero2, numero1))
else:
    print('Os dois números são iguais')