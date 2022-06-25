davi=str(input('primeiro aluno:'))
gledson=str(input('segundo aluno:'))
silva=str(input('terceiro aluno:'))
bene=str(input('quarto aluno:'))

lista=[davi, gledson, silva, bene]

import random

s=random.choice(lista)
print(f'o aluno escolhido foi {s}')