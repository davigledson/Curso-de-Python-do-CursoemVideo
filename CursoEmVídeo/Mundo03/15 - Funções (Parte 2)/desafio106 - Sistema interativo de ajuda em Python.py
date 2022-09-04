c=('\033[m', # 0 - sem cores
   '\033[0;30;41m', # 1 - vermelho
    '\033[0;30;42m',# 2 - verde
    '\033[0;30;43m',# 3 - amarelo
    '\033[0;30;44m',# 4 - azul
    '\033[0;30;45m',# 5 - roxo
    '\033[1;30;107m',# 6 - branco

   )
def titulo(titulo,cor=0):
    print(c[cor],end='')
    con=len(titulo)+4

    print(f'~'*con)
    print(f'  {titulo}')
    print(f'~' * con)
    print(c[0],end='')

def ajuda():
    while True:

        comando=input(f' Função ou Biblioteca>')
        titulo(f'SISTEMA DE AJUDA PyHelp',4)
        titulo(f' Acessando a função do {comando}',2)


        if comando =='fim':
            break
        print(f'{c[6]}',end='')
        help(comando)
        print(f'{c[0]}',end='')


ajuda()