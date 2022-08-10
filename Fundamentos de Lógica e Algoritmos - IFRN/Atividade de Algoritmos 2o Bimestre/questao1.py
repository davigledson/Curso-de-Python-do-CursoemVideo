'''
Questão 1 - Faça um programa que pergunte o nome, calcule O nivel da procura de procura e o ranking
 de um pirata baseado na quantidade de ouro roubado e na quantidade de marinheiros derrotados

====RANKING DOS PIRATAS=====

- até 20 marinheiro derrotados - pirata normal
- + de 20 marinheiros até 100 marinheiros derrotados - pirata perigoso
- + de 100 até 300 marinheiros derrotados - Baroque Works
- + 300 até 700 marinheitos derrotados - Shinchibukai
- + de 700 marinheiros derrotados - Yonkou

=====NIVEIS DE PROCURA=====

- até 50 Kg de ouro - Procurado: Vivo
- + de 50 Kg á 100 Kg de ouro - procurado: morto
- + de 100 Kg de ouro - Procurado: vivo ou morto
'''
print('='*20,'SITE DO GOVERNO MUNDIAL','='*20)
nome=input('Digite o nome do pirata:')
quantidade_de_marinheiro=int(input('Digite a quantidade de marinheiros derrotados:'))
quantidade_de_ouro=float(input('Digite a quantidade de ouro roubado (Kg):'))

if quantidade_de_marinheiro <= 20 and quantidade_de_ouro<=50:
    print('='*5,f'{nome:^10}','='*5)
    print('=' * 5, 'Pirata Normal', '=' * 5)
    print('=' * 5, 'Procurado: Vivo', '=' * 5)
if quantidade_de_marinheiro <= 20 and 100>=quantidade_de_ouro>50:
    print('=' * 5, f'{nome:^10}', '=' * 5)
    print('=' * 5, 'Pirata Normal', '=' * 5)
    print('=' * 5, 'Procurado: Morto', '=' * 5)
if quantidade_de_marinheiro <= 20 and quantidade_de_ouro>100:
    print('=' * 5, f'{nome:^10}', '=' * 5)
    print('=' * 5, 'Pirata Normal', '=' * 5)
    print('=' * 5, 'Procurado: Vivo ou morto', '=' * 5)

if 20<quantidade_de_marinheiro<=100  and quantidade_de_ouro<=50:
    print('=' * 5, f'{nome:^10}', '=' * 5)
    print('=' * 5, 'Pirata perigoso', '=' * 5)
    print('=' * 5, 'Procurado: Vivo', '=' * 5)
if 20<quantidade_de_marinheiro<=100 and 100>=quantidade_de_ouro>50:
    print('=' * 5, f'{nome:^10}', '=' * 5)
    print('=' * 5, 'Pirata perigoso', '=' * 5)
    print('=' * 5, 'Procurado: Morto', '=' * 5)
if 20<quantidade_de_marinheiro<=100 and quantidade_de_ouro>100:
    print('=' * 5, f'{nome:^10}', '=' * 5)
    print('=' * 5, 'Pirata perigoso', '=' * 5)
    print('=' * 5, 'Procurado: Vivo ou morto', '=' * 5)

if 100<quantidade_de_marinheiro<=300  and quantidade_de_ouro<=50:
    print('=' * 5, f'{nome:^10}', '=' * 5)
    print('=' * 5, 'Pirata Baroque Works', '=' * 5)
    print('=' * 5, 'Procurado: Vivo', '=' * 5)
if 100<quantidade_de_marinheiro<=300 and 100>=quantidade_de_ouro>50:
    print('=' * 5, f'{nome:^10}', '=' * 5)
    print('=' * 5, 'Pirata Baroque Works', '=' * 5)
    print('=' * 5, 'Procurado: Morto', '=' * 5)
if 100<quantidade_de_marinheiro<=300 and quantidade_de_ouro>100:
    print('=' * 5, f'{nome:^10}', '=' * 5)
    print('=' * 5, 'Pirata Baroque Works', '=' * 5)
    print('=' * 5, 'Procurado: Vivo ou morto', '=' * 5)

if 300<quantidade_de_marinheiro<=700  and quantidade_de_ouro<=50:
    print('=' * 5, f'{nome:^10}', '=' * 5)
    print('=' * 5, 'Shinchibukai', '=' * 5)
    print('=' * 5, 'Procurado: Vivo', '=' * 5)
if 300<quantidade_de_marinheiro<=700 and 100>=quantidade_de_ouro>50:
    print('=' * 5, f'{nome:^10}', '=' * 5)
    print('=' * 5, 'Shinchibukai', '=' * 5)
    print('=' * 5, 'Procurado: Morto', '=' * 5)
if 300<quantidade_de_marinheiro<=700 and quantidade_de_ouro>100:
    print('=' * 5, f'{nome:^10}', '=' * 5)
    print('=' * 5, 'Shinchibukai', '=' * 5)
    print('=' * 5, 'Procurado: Vivo ou morto', '=' * 5)

if 700<quantidade_de_marinheiro  and quantidade_de_ouro<=50:
    print('=' * 5, f'{nome:^10}', '=' * 5)
    print('=' * 5, 'Yonkou', '=' * 5)
    print('=' * 5, 'Procurado: Vivo', '=' * 5)
if 700<quantidade_de_marinheiro and 100>=quantidade_de_ouro>50:
    print('=' * 5, f'{nome:^10}', '=' * 5)
    print('=' * 5, 'Yonkou', '=' * 5)
    print('=' * 5, 'Procurado: Morto', '=' * 5)
if 700<quantidade_de_marinheiro and quantidade_de_ouro>100:
    print('=' * 5, f'{nome:^10}', '=' * 5)
    print('=' * 5, 'Yonkou', '=' * 5)
    print('=' * 5, 'Procurado: Vivo ou morto', '=' * 5)