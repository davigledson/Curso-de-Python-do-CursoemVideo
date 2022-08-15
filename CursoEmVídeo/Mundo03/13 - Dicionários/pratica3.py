estados=dict()
brasil=list()

for c in range(0,3):
    estados['uf']=input('Unidade Federativa:')
    estados["sigla"]=input('Sigla do Estado:')
    brasil.append(estados.copy()) #em dicionarios para copiar não se usa o [:] igual em listas. se usar o copy()
print(brasil)

print('=='*20)

for e in brasil:
    print(e)

print('=='*20)

for e in brasil:
    for v,k in e.items():
        print(f'O campo {v} tem valor {k}.')
