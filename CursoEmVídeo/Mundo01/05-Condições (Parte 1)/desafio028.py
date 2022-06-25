print('-=-'*20)
print('Tente advinha que numero eu pensei entre 0 e 5 - Computador')
print('-=-'*20)
import random
lista=(0, 1, 2 ,3 ,4 ,5)

n2=random.choice(lista)

n3=random.randint(0,5) #outro jeito mais facil ussando o ''randint''

n1=int(input('Digite um numero entre 0 e 5:'))
import time

print('PROCESSANDO...')
time.sleep(3) #faz o computador ''dormi'' por algums segundos
if n1 == n3:
    print('\033[32m Parabens!, você acertou!')
else:
    print('\033[33m Que pena!, você errou')
print(f'Eu pensei no {n2}')
