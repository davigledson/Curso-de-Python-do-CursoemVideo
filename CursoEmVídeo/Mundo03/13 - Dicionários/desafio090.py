dic={'Nome':'','Media':0}


nome=input('Nome:')
media=float(input(f'Media de {nome}:'))

dic['Nome']=nome
dic['Media']=media
if media <6:
    dic['Situação']='Reprovado'
else:
    dic['Situação']='Aprovado'

for k,v in dic.items():
    print(f'{k} e igual {v}')
