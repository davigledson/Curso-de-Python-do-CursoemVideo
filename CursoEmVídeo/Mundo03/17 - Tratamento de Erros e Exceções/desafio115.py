from funções import funçoes_criadas_para_o_desafio115



arq='arquivo.txt'

if funçoes_criadas_para_o_desafio115.arquivoExiste(arq):
    print('Arquivo encontrado com suscesso!')
else:
    print('Arquivo não encontrado')
    funçoes_criadas_para_o_desafio115.criaarArquivo(arq)


while True:
    resposta = funçoes_criadas_para_o_desafio115.Menu([' Mostrar lista de pessoas cadastradas ',
                                                       ' Cadastrar uma nova pessoa'
                                                          , ' Sair do Sistema'])

    if resposta == 1:
        funçoes_criadas_para_o_desafio115.lerArquivo(arq)
    elif resposta == 2:
        print('--' * 20)
        nome = input('Nome:')
        idade = int(input('Idade:'))
        print('--' * 20)

    elif resposta == 3:
        print('--' * 20)
        print('Saindo... Volte sempre!')
        break
    else:
        print('\033[;31;58mErro! Digite uma opção valida\033[m')
