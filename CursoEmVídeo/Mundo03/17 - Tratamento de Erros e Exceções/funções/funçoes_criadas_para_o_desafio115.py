
def Titulo(txt):
    le = len(txt) + 32
    print('~' * le)
    print(f'                {txt}')
    print('~' * le)
def leiaint(num):
    while True:
        try:
            entrada=int(input(num))

        except KeyboardInterrupt:
            print('\033[;31;58mErro! Entrada de dados interrompida pelo usuario \033[m')
            return 0

        except (ValueError,TypeError):
            print('\033[;31;58mErro! Digite um numero inteiro valido\033[m')


        else:
            return entrada


def Menu(lista):

    Titulo('Menu principal')
    for p,c in enumerate(lista):
        print(f'\033[;33;58m{p+1} \033[;34;58m- {c}\033[m')
    opc=leiaint('\033[;33;58m Sua opção: \033[m')
    return opc