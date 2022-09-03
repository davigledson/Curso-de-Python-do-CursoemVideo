def ficha(nome_do_jogador,gols):
    num = str(gols)

    tam=len(nome_do_jogador)
    if tam == 0:
        nome_do_jogador='<Desconhecido>'


    quantidade_de_gols = len(num)
    if quantidade_de_gols == 0:
        gols = '0'
    print(f'O jogador {nome_do_jogador} fez {gols} gols(s) no campeonato')


jogador=input('Jogador:')
gol=input('Quantidade de gols:')
ficha(jogador,gol)



