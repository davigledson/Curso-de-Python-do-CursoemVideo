from random import randint
#jeito que fiz
'''a=count=0
ale=randint(1,10)
while a != ale:
    a = int(input('Digite um numero entre 0 e 10:'))
    count+=1
    if ale<a:
        print('Menos, tente novamente')
    if ale>a:
        print('Mais, tente novamente')
    if a== ale:
        print(f'VOCÊ ACERTOU! eu pensei no {ale}')
print(f' voce acertou com {count} tentativas')'''

#jeito profissional
palpites=0
acertou= False
computador=randint(1,10)
while not acertou:
    jogador = int(input('Digite um numero entre 0 e 10:'))
    palpites += 1
    if jogador == computador:
        acertou = True
        print(f'VOCÊ ACERTOU! eu pensei no {computador}')
    else:
        if computador < jogador:
            print('Menos... Tente novamente')
        if computador > jogador:
            print('Mais... Tente novamente')


print(f'Voce acertou com {palpites} tentativas')