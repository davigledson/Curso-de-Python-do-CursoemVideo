import random
print('Vamos brincar de pedra, papel e tesoura')
escolha=input('qual você escolhe?')
pedra=('pedra')
papel=('papel')
tesoura=('tesoura')
import time
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
time.sleep(1)

lis=(pedra,papel,tesoura)
resu=random.choice(lis)
print(resu)
if escolha !=pedra and escolha != papel and escolha != tesoura:
    print('Resposta invalida!')
elif escolha == resu:
    print(f' o resultado empatou! eu escolhi {resu}')
elif resu == pedra and escolha == papel:
    print(f'você Ganhou!, eu escolhi {resu}')
elif resu == papel and escolha == tesoura:
    print(f'Você Ganhou!, eu escolhi {resu}')
elif  resu == tesoura and escolha == pedra:
    print(f'Você Ganhou! eu escolhi {resu}')

elif resu == pedra and escolha==tesoura:
    print(f'Você Perdeu! eu escolhi {resu}')
elif resu == papel and escolha == pedra:
    print(f'Você Perdeu! eu escolhi {resu}')
elif resu == tesoura and escolha == papel:
    print(f'Você Perdeu! eu escolhi {resu}')