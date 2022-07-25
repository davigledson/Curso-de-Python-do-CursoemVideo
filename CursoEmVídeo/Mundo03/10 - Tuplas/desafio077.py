palavras=('aprender','programar','linguagem','python','curso',
          'gratis','estudar','praticar','trabalhar','mercado','programador','futuro')

for p in palavras:
    print(f'\nna palavra {p} temos ',end='')
    for vogais in p:
        if vogais.lower() in 'aeiou':
            print(vogais,end=' ')



