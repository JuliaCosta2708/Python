#Recebendo as informações para o calculo do IMC
altura = float(input("Informe sua altura (em metros): "))
peso = float(input('Informe seu peso em KG: '))
#Bloco 2 - Cálculo do IMC
imc = peso / (altura ** 2)
print('Seu IMC é {}'.format(imc))
#Bloco 3 - Condição para ver em qual categoria está o IMC 
if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal!')
elif 25 <= imc < 30:
    print("Você está com sobrepeso!")
elif 30 <= imc < 40:
    print('Você está com obesidade!')
else:
    print("Você está em obesidade morbida!")