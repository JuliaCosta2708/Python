#Importando a biblioteca datetime para puxar o ano atual no sistema
from datetime import date

#Bloco 1 - Entrada de dados e calculo da idade
ano = int(input('Informe o ano que você nasceu:'))
genero = str(input('''Qual seu gênero: 
[feminino] 
[masculino] 
: '''))
idade = date.today().year - ano 

if genero == 'feminino':
    print('Seu alistamento não é obrigatório!')
else:
    #Infromando a idade do usuário
    print('Nascidos em {} tem {} anos no ano de {}'.format(ano, idade, date.today().year))
    #Bloco 2 - Condição
    if idade < 18:
        tempo = 18 - idade
        print('Ainda faltam {} anos para se alistar! Seu alistamento será em {}'.format(tempo, date.today().year + tempo ))
    elif idade > 18:
        tempo = idade - 18
        print('Já se passaram {} anos de se alistar! Foi no ano de {}'.format(tempo, date.today().year - tempo))
    else:
        print("Você deve se alistar nesse ano!")