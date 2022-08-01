soma=0
for c in range(1,11):
    n=int(input(f'Digite a {c}° nota da prova:'))
    soma+=n
print(f'A media da turma é {soma/10}')