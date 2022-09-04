def notas(*notas,sit=False):
    """
    -> Função para analisar notas e situações de varios alunos
    :param notas: uma ou mais notas de varios alunos (aceita vários)
    :param sit:valor opcional, indicado se deve ou não adicionar a sotuação
    :return:dicionario com várias informações sobre a situação da turma
    """

    dicionario= {'Quantidade de notas':len(notas) , 'Maior nota': max(notas),
                 'menor nota': min(notas), 'Media da turma': sum(notas)/len(notas)}
    if sit==True:
        media=sum(notas) / len(notas)
        if media>=7:
            dicionario['Situação']='Boa'
        elif media <7 and media>=6:
            dicionario['Situação'] = 'Razoavel'
        else:
            dicionario['Situação'] = 'Ruim'
    return dicionario

n=notas(9.5,6,8,sit=True)
n1=notas(5,6,8,7,4,6)
print(n)
print(n1)