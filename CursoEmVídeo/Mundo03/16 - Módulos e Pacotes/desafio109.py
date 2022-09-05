from utilidadesCeV import moeda
p=float(input('Digite o preço: R$'))
print(f'A medade de {p} é {moeda.metade(p, True)}')
print(f'O dobro de {p} é {moeda.dobro(p, rs=True)}')
print(f'Aumentando {p} em 10% temos {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo {p} em 13% temos {moeda.diminuir(p, 13, rs=True)}')