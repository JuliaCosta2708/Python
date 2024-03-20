frase = str(input('Digite uma frase: ')).lower().strip()
print('A letra "A" aparece {} vezes'.format(frase.count('a')))
print('A 1ª vez que a letra a aparece é {}'.format(frase.find('a')+1))
print('A última vez que a letra a aparece é {}'.format(frase.rfind('a')+1))