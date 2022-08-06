lista=[]
nomepeso=[]
pesso=0
while True:
    nome=input('Nome:')
    peso=float(input('Peso:'))
    pesso+=1 #contador de pessoas

    lista.append(nome)
    lista.append(peso)

    nomepeso.append(lista[:])
    lista.clear()

    esc=' '
    while esc!='s' and esc!= 'n':
        esc=input('Quer Continuar?[S/N]').lower().strip()[0]
    if esc=='n':
        break

pesosoma=0
print(nomepeso)
for c in nomepeso:
    pesosoma+=c[1]



pesomedia=pesosoma/pesso #media de pesoa das pessoas

pessoas_mais_pesadas=[]
pessoas_mais_leves=[]


for p in nomepeso:
    if p[1]>pesomedia:
        pessoas_mais_pesadas.append(p[0])
    if p[1]<pesomedia:
        pessoas_mais_leves.append(p[0])

print('='*20,'PESADAS CADASTRADAS','='*20)
print(f'Numero de pessoas cadastradas: {pesso}')

print('='*20,'PESSOAS MAIS PESADAS','='*20)
print(f'Pessoas mais pesadas:{pessoas_mais_pesadas}')

print('='*20,'PESSOAS MAIS LEVES','='*20)
print(f'Pessoas mais leves: {pessoas_mais_leves}')
