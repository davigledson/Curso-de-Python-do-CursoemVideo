'''Crie um programa que o usuário digite as notas de 10 alunos de uma turma. Depois
calcule e imprima a média das notas, a maior e a menor nota'''
lista=[]
sublista=[]

for c in range(1,6):
    nota1=float(input('Nota 1:'))
    nota2 = float(input('Nota 2:'))
    md=(nota1+nota2)/2

    sublista.append(nota1)
    sublista.append(nota2)
    sublista.append(md)
    lista.append(sublista.copy())
    sublista.clear()
print(lista)

print('n°   notas    media')
for pos,num in  enumerate(lista):
    print(f'{pos}   {num[0:2]}  {num[2]}')

    sublista.append(num[2])
print('==','MEDIAS','=='*20)
print(f'A menor media foi {min(sublista)}')
print(f'A maior media foi {max(sublista)}')

print('==','NOTAS','=='*20)
notas=[]
for n in lista:
    notas.append(n[0])
    notas.append(n[1])
print(f'A menor nota foi {min(notas)}')
print(f'A maior nota foi {max(notas)}')




