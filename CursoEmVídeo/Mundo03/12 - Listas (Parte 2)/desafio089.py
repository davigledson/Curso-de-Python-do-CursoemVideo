lista=[]
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
print('No.   NOME         NOTAS      MEDIAS')

for numero in range(0,processo): #numero == posição dos dados
    print(f'{numero}      {listnome[numero]}        {listnotas[numero][0:2]}     {listmed[numero]}')

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
        print(f'As notas de {listnome[usu]} são {listnotas[usu][0:2]}')






