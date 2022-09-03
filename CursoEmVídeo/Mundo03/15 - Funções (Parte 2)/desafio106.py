def titulo(titulo):

    con=len(titulo)+4
    print(f'~'*con)
    print(f'\033[;36;40m   {titulo}')
    print(f'~' * con)

def ajuda():
    while True:

        comando=input('\033[;30;46m Função ou Biblioteca>')
        titulo('SISTEMA DE AJUDA PyHelp')
        titulo(f'\033[;30;47m Acessando a função do {comando}')


        if comando =='fim':
            break

        help({comando})


ajuda()