pessoas = {'nome':'Davi','sexo':'muito','idade':19}
print(pessoas)
print(pessoas['nome'])
print(pessoas['sexo'])
print(pessoas['idade'])

print("=="*20)

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

print("=="*20)

print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos.')

print("=="*20)
for k in pessoas.keys():
    print(k)

print("=="*20)

for v in pessoas.values():
    print(v)

print("=="*20)

for k,v in pessoas.items():
    print(f'{k} = {v}')

print("=="*20)
#del pessoas['sexo'] deleta o sexo
pessoas['nome'] = 'Gledson'
pessoas['peso'] = 72 # adiciona o  peso
for k,v in pessoas.items():
    print(f'{k} = {v}')
