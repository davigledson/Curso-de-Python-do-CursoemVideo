'''Um treinador de pokémon obteve um Kirlia e um Snorunt agora está ansioso para evoluí-los.
Crie um programa mostrando as limitações e possibilidades para tal.

[1] - Kirlia - nivel minimo de evolução = 30
a) caso o genero da Kirlia sejá femea, ela evoluira para um Gardevoir
b)caso o genero da Kirlia seja macho, ele evoluirá para um Gallade

[2] - Snornut - nivel minimo de evolução = 42
a) caso o genero do Snornut seja femea, ela evoluirá para Froslass
b) caso o genero do Snornut seja macho, ela evoluirá para Glalie
'''
print('[1] - Kirlia')
print('[2] - Snornut')
monster = int(input("Que pokémon você tem?"))
level = int(input("O nível dele?"))

if monster == 1 and level >= 30 or monster == 2 and level >= 42:
    print("Ele pode evoluir para duas formas.")
    print('[1] - femea')
    print('[2] - macho')

    gender =int(input("Qual o gênero dele?"))

    if monster == 1 and gender == 2:
        print("Com uma pedra aurora ele pode evoluir para Gallade. Sem a pedra será um Gardevoir.")
    elif monster == 1 and gender == 1:
        print("Sendo fêmea vai ser uma Gardevoir.")


    elif monster == 2 and gender == 1:
        print("Com uma pedra aurora, ela se tornará uma Froslass. Sem ela será uma Glalie.")

    else:
        print("Sendo macho, seu Snorunt será um Glailie ao evoluir")

else:
    print("Não pode evoluir.")
