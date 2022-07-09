tempo=int(input('quantos anos tem o seu carro?'))
if tempo <=3:
    print('seu carro é novo')
else:
    print('seu carro é velho')
print('---Fim---')

#condição simplificada
print('Carro novo'if tempo >=5 else 'Carro velho')
print('---Fim de novo---')

nome=input('Qual o  seu nome:')
if nome == 'Davi':
    print('Que nome lindo')
else:
    print('Que nome normal')
print(f'Bom dia, {nome}')

n1=float(input('Digite sua  primeira nota:'))
n2=float(input('Digite sua segunda nota:'))

resu=(n1 +n2) /2
print(f'Sua media foi {resu}')
if resu >=10:
    print('Parabens, você foi aprovado')
else:
    print('Meus pêsames, você foi reprovado')