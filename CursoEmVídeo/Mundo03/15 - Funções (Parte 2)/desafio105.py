def notas(*notas,sit=False):
    """
    -> Função para analisar notas e situações de varios alunos
    :param notas: uma ou mais notas de varios alunos (aceita vários)
    :param sit:valor opcional, indicado se deve ou não adicionar a sotuação
    :return:dicionario com várias informações sobre a situação da turma
    """
    lista=[]
    soma=0
    for c in notas:
        soma+=c
        lista.append(c)



    dicionario= {'Quantidade de notas':len(lista) , 'Maior nota': max(lista),
                 'menor nota': min(lista), 'Media da turma': soma/len(lista)}
    if sit==True:
        media=soma/len(lista)
        if media>=7:
            dicionario['Situação']='Boa'
        elif media <7 and media>=6:
            dicionario['Situação'] = 'Razoavel'
        else:
            dicionario['Situação'] = 'Ruim'
    return dicionario

n=notas(9.5,6,8,sit=True)
print(n)