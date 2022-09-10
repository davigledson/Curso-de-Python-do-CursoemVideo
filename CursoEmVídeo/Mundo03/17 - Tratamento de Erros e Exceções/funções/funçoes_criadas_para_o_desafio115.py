
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

def arquivoExiste(nome):
    try:
        a=open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criaarArquivo(nome):
    try:
        a=open(nome,'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do aquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso! ')

def lerArquivo(nome):
    try:
        a=open(nome,'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        Titulo('PESSOAS CADASTRADAS')
        for linha in a:
            dado=linha.split(';')
            dado[1]=dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')






def cadastrar(arq,nome='desconhecido',idade=0):
    try:
        a=open(arq,'at')
    except:
        print('Houve um erro na criação do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()

