#Bloco 1 - Declarando variáveis para nota
nota_1 = float(input('Informe a 1ª nota do aluno: '))
nota_2 = float(input('Informe a 2ª nota do aluno: '))
#Bloco 2 - Calculando a média
media = (nota_1 + nota_2)/2
print("A média do aluno é {:.1f}".format(media))
#Bloco 3 - Condição para aprovação
if media < 5.0:
    print('Aluno REPROVADO!')
elif 7 > media >= 5:
    print('Aluno em RECUPERAÇÃO!')
else:
    print('Aluno APROVADO!')