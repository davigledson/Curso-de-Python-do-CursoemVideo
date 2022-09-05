
def leiadinheieo(frase):

    while True:
        leia=input(frase)
        if '.' or ',' in leia:
            ponto=leia.index('.')
            virgula=leia.index(',')

        if leia.isnumeric():
            leia = float(leia)
            print(leia)

            break
        else:
            print(f'\033[;31;58m ERRO: {leia} é um preço invalido!\033[m')

leiadinheieo('Digite um valor:')

