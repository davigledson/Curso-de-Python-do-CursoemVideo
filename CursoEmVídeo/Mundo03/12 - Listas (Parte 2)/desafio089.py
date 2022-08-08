'''lista=[]
notas=[]
media=[]
contador=0
processo=0
while True:
    nome=input('Nome:')
    nota1=int(input('Nota 1:'))
    nota2=int(input('Nota 2:'))
    md=(nota1+nota2)/2

    lista.append(nome[:])

    media.append(md)
    notas.append(nota1)
    notas.append(nota2)

    notas.append(media[:])


    lista.append(notas[:])


    notas.clear()
    media.clear()

    processo+=1 #contador

    esc=' '
    while esc != 's' and esc != 'n':
        esc=input('Quer Continuar [S/N]:').lower().strip()[0]

    if esc =='n':
        break

print(f'LISTA COMPOSTA = {lista}')

listnome=[]
listnotas=[]
for c in lista:
    contador += 1

    if contador %2==1:
        listnome.append(c)
    else:
        listnotas.append(c)

listmed=[]
for m in listnotas:

    listmed.append(m[2])

print('='*20,'MEDIAS','='*20)
print(f'{"No.":<5}  {"NOME":<5}     {"NOTAS":<5}    {"MEDIAS":<5}')

for numero in range(0,processo): #numero == posição dos dados
    print(f'{numero}   {listnome[numero]}   {listnotas[numero][0:2]}    {listmed[numero]}')

from time import sleep
while True:


    usu=int(input('Mostrar as notas de qual aluno? (999 para interromper) '))
    if usu == 999:
        sleep(1)
        print('FINALIZANDO...')
        sleep(1)
        print('<<<<< VOLTE SEMPRE >>>>>')
        break
    if usu <processo:
        print(f'As notas de {listnome[usu]} são {listnotas[usu][0:2]}'''
ficha=list()
while True:
    nome=input('Nome:')
    nota1=float(input('Nota 1:'))
    nota2=float(input('Nota 2:'))
    media=(nota1+nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    resp=input('Quer Continuar?[S/N]:').lower().strip()[0]
    if resp in'Nn':
        break
print('='*30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*26)

for i,a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-=-'*35)
    ocp=int(input('Mostra qual nota? [999 interromper]'))
    if ocp ==999:
        print('FINALIZANDO')
        break
    if ocp<=len(ficha)-1:
        print(f'Notas de {ficha[ocp][0]} são {ficha[ocp][1]}')

print('<<<<< VOLTE SEMPRE >>>>>')










