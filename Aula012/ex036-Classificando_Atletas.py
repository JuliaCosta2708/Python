from datetime import date
ano = int(input("Informe o ano de nascimento do atleta:"))
idade = date.today().year - ano
print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print('Atleta categoria MIRIM!')
elif idade <= 14:
    print('Atleta categoria INFANTIL!')
elif idade <= 19:
    print('Atleta categoria JÚNIOR')
elif idade <=25:
    print('Atleta categoria SÊNIOR!')
else: 
    print("Atleta categoria MASTER!")
