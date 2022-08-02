
while True:
    nome = input('Digite o nome:')
    largura = float(input('Digite a largura:'))
    comp = float(input('Digite o comprimento:'))
    area=largura*comp
    print(f'A area do comodo {nome} é {area} cm²')

    esc=' '
    while esc not in "SsNn":
        esc=input('Quer Continuar [S/N]:').lower().strip()[0]

    if esc == 'n':
       break
