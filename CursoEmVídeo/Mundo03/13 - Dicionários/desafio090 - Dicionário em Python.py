dic={}


nome=input('Nome:')
media=float(input(f'Media de {nome}:'))

dic['Nome']=nome
dic['Media']=media
if media >=7:
    dic['Situação']='Aprovado'
elif 5<=media<=6:
    dic['Situação']='Recuperação'

else:
    dic['Situação']='Reprovado'

print(dic)

for k,v in dic.items():
    print(f'{k} e igual {v}')
