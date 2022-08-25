'''Crie um programa que simule um painel eletrônico que organiza uma fila. O programa
exibe um menu com as seguintes opções: 1. Entrar na fila. / 2. Consultar a fila. / 3. Chamar
próximo da fila. Na opção 1, o usuário digita o nome da pessoa que está entrando no final
da fila. Na opção 2, o programa imprime a fila atual e diz *quantas pessoas há na fila*. Na
opção 3, o programa exibe uma mensagem chamando a pessoa da vez e remove seu nome
da fila. Se não houver pessoas na fila, mostre a mensagem "fila vazia"'''
fila=[]



while True:

    print('Selecione uma das opçoes abaixo:')
    print('[1] - entra na fila ')
    print('[2] - imprimir fila atual')
    print('[3] -  exibe uma mensagem chamando a pessoa da vez e remove seu nome da fila. ')
    print('[4] - sair do programa')
    resp=int(input('Selecione a opção:'))

    if resp==4:
        break

    if resp==1:
        print('-=-' * 20)
        usuario=input('Nome:')
        fila.append(usuario)
        print('-=-' * 20)
    if resp==2:
        print('-=-'*20)
        print(fila)
        print(f'Há {len(fila)} na fila!')
        print('-=-' * 20)

    if len(fila)==0 and len(fila)==0:
        print('-=-' * 20)
        print('FILA VAZIA')
        print('-=-' * 20)

    if len(fila)>=1 and resp==3:
        print('-=-' * 20)
        print(f'Chamando {fila[-1]}')
        print('-=-' * 20)
        fila.pop()



