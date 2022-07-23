print('-=-'*20)
print('VAMoS JOGAR PAR OU IMPAR')
print('-=-'*20)
vitorias=0

from random import randint

while True:
    pc = randint(1, 10)
    valor=int(input('digite um valor:'))
    esc=' '
    while esc not in 'pi':
        esc=input('PAR ou IMPAR? [P/I]:').lower()
    resu=(pc+valor)%2
    vitorias+=1
    print(f'eu escolhi {pc} e você {valor} deu {pc+valor}')

    if resu ==1 and esc =='i':
        print('IMPAR! VOCE GANHOU')
    if resu==0 and esc=='p':
        print('PAR! VOCE GANHOU!')
    if resu ==0 and esc=='i' or resu==1 and esc=='p':
        print('VOCE PERDEU!')
        break
print(f'seu total de vitorias consecutivas foi de {vitorias-1} vitorias')
