lista=[]
lista_de_jogadores=[]
dicionario={}
while True:

    jogador=input('Nome do Jogador:')
    dicionario['Jogador']=jogador

    partidas=int(input('Quantas Partidas ele Jogou:'))
    total_de_gols=0
    for c in range(1,partidas+1):
        qg=int(input(f'Quantidade de gol na partida {c}:'))

        lista.append(qg)
        total_de_gols += qg


    dicionario['Gols']=lista[:]
    dicionario['Total de Gols']=total_de_gols
    lista_de_jogadores.append(dicionario.copy())
    lista.clear()

    resp=input('Quer Continuar?[S/N]:').lower()[0]
    if resp == 'n':
        break
print('=-=-='*30)


print(lista_de_jogadores)

print('=-=-='*30)
print(f'        {"cod. nome"}       {"Gols"}     {"Total"}')
print('---'*30)
for pos,j in enumerate(lista_de_jogadores):
    print(f'{pos!s:<10s}{j["Jogador"]!s:<10s}{j["Gols"]!s:<10s}     {j["Total de Gols"]}')

usu=0
while True:
    usu=int(input('Mostrar dados de qual jogador? [999 stop]:'))
    if usu <= len(lista_de_jogadores)-1:
        print(f'-- LEVANTAMENTO DO JOGADOR: {lista_de_jogadores[usu]["Jogador"]}')
        for pos,val in enumerate(lista_de_jogadores[usu]['Gols']):
            print(f'    na partida {pos} ele fez {val} gols')



    if usu == 999:
        print('FINALIZANDO! VOLTE SEMPRE!')
        break
    if usu >len(lista_de_jogadores)-1:
        print('Jogador não encontrado!')
