'''ajude jubileu a comer pipoca'''
resp=input('Voce gosta de pipoca?[S/N]:').lower()[0]
if resp =='s':
    manteiga=input('Pipoca quente na manteiga?[S/N]:').lower()[0]
    if manteiga=='s':
        print('(ง ͠° ͟ل͜ ͡°)ง')
        print(f'Final Feliz! Jubileu comeu pipoca quente na manteiga!')
    else:
        print('OK, Irei comer mesmo assim!')
        print('final neutro! Jubileu comeu pipoca mas sem manteiga!')
elif resp =='n':
    print('Final alternativo! jubileu tava sem fome!')