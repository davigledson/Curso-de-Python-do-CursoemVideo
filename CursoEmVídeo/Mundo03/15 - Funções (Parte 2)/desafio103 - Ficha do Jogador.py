def ficha(nome_do_jogador='<Desconhecido>',gols='0'):

    tam=len(nome_do_jogador)
    if tam == 0:
        nome_do_jogador='<Desconhecido>'

    num=len(gols)
    if num==0:
        gols=0

    print(f'O jogador {nome_do_jogador} fez {gols} gols(s) no campeonato')


jogador=str(input('Jogador:'))
g=str(input('Quantidade de gols:'))

if g.isnumeric()==True:
    g=int(g)
ficha(jogador,g)



