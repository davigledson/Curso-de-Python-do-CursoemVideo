def area(a,b):
    print(f'A Área de um terreno {a}x{b} é {a*b}m²')
def mostralinha():
    print('--'*20)


mostralinha()
print('CONTROLE DE TERRENO')
mostralinha()
largura=float(input('Largura:'))
altura=float(input('Altura:'))
area(largura,altura)
