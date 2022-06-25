davi=input('primeiro aluno:')
gledson=input('segundo aluno:')
silva=input('terceiro aluno:')
bene=input('quarto aluno:')

import random

lista=[davi, gledson, silva, bene]
b=random.sample(lista, k=len(lista))

print(f'os alunos escolhidos na sequencia foram {b}')

#outra forma de fazer
from random import shuffle
shuffle(lista)
print('a ordem de apresentação será')
print(lista)
#Shuffle não mostra a lista numa ordem aleatória, ele altera a ordem dentro da lista