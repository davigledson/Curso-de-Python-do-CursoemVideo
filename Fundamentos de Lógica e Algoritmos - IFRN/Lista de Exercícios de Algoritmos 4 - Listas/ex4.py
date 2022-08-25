'''Crie um programa que cadastre os alunos de uma escola. Pergunte ao usuário o nome, o
curso e a série de um aluno. Salve esses 3 dados como uma (sub)lista e depois acrescente
esta (sub)lista em uma lista principal. O programa deve repetir quantas vezes o usuário
desejar. Ao finalizar os cadastros, imprima todos os alunos cadastrados.
'''
sublista=[]
lista=[]

resp='s'
while resp=='s':


    nome=input('Nome:')
    curso=input('Curso:')
    serie=int(input('Serie:'))
    sublista.append(nome)
    sublista.append(curso)
    sublista.append(serie)
    lista.append(sublista.copy())
    sublista.clear()
    resp=input('Qur Continuar?[S/N]:')
print(lista)
