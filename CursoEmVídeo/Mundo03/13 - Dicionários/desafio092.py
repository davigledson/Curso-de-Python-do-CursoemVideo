dados={}
dados['nome']=input('Nome:')

ano_de_nasc=int(input('Ano de nascimento:'))

import datetime
atual=datetime.date.today().year
idade=atual - ano_de_nasc

dados['idade']=idade
ctps=int(input('Carteira de trabalho (0 não tem):'))
dados['CTPS']=ctps
if ctps != 0:

    ano_de_Contratacao=int(input('Ano de Contratação:'))
    dados['Ano de Contratação']=ano_de_Contratacao
    aposentadoria=ano_de_Contratacao+35

    dados['Salário']=float(input('Salário: R$'))
    dados['aposentadoria']=aposentadoria
print(dados)

for k,v in dados.items():
    print(f'{k} tem valor = {v}')