times_do_brasileirao = 'Palmeiras','Corinthians','Atlético-MG','Fluminense','Athletico-PR',\
                       'Internacional','Flamengo','Bragantino','Santos','São Paulo','Ceará',\
                       'Botafogo','Avaí','Goiás','Cuiabá','Coritiba','América-MG','Atletico-GO'\
    ,'Fortaleza','Juventude'

print(f'os 5 primeiros da lista de classificação: {times_do_brasileirao[:5]}')
print('==='*60)
print(f'os 4 ultimos colocados são: {times_do_brasileirao[-4:]}')
print('==='*60)

print(f'o ordem de classificação do Internacional e o de {times_do_brasileirao.index("Internacional")+1}° colocado')# tbm pode ser assim com o ""
inter=times_do_brasileirao.index('Internacional')
print(f'o ordem de classificação do Internacional e o de {inter+1}° colocado')
print('==='*60)
print(f'A ordem alfabetica dos times do brasileirão = {sorted(times_do_brasileirao)}')