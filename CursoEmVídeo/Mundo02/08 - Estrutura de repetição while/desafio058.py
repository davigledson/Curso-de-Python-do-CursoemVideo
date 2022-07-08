

import random

a=1
ale=random.randint(1,10)
while a != ale:
    a = int(input('Digite um numero entre 0 e 10:'))
    print('tente novamente')
    if a== ale:
        print(f'VOCÊ ACERTOU! eu pensei no {ale}')