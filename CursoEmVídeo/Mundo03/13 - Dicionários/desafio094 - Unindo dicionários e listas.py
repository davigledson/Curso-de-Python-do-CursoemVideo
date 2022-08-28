cont=0
dicionario={}
lista=[]


while True:

    nome=input('nome:')
    sexo=' '
    while sexo not in 'mf':
        sexo=input('Sexo [M/F]:').lower()[0]
    idade=int(input('Idade:'))

    dicionario['Nome']=nome
    dicionario['Sexo']=sexo
    dicionario['Idade']=idade
    lista.append(dicionario.copy())
    dicionario.clear()

    resp = ' '
    while resp not in 'sn':
        resp = input('Quer Continuar? [S/N]:').lower()[0]
    if resp == 'n':
        break


mulheres=[]
cont_idade=0
for pos,c in enumerate(lista):
    cont+=1
    if c['Sexo'] =='f':
        print(c['Nome'])
        mulheres.append(c['Nome'])
    cont_idade+=c['Idade']

media=cont_idade/len(lista)
idade_acima_da_media=[]

for pos,val in enumerate(lista):
    if val['Idade']>media:
        idade_acima_da_media.append(val)

print('-=-'*30)
print(f'O total de pessoas cadastradas na lista foi  de {cont} pessoas')
print(f'A media de idade das pessoas é {media} e a soma é {cont_idade}')
print(f'As mulheres cadastradas foram = {mulheres}')
print(f'A lista de pessoas com idade acima da media é ')

for c in idade_acima_da_media:
    print(f'    Nome = {c["Nome"]}   Idade = {c["Idade"]}  Sexo = {c["Sexo"]}')