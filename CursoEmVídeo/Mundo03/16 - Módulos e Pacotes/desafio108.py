

from utilidadesCeV import moeda
p=float(input('Digite o preço: R$'))
print(f'A medade de {p} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {p} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando {p} em 10% temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo {p} em 13% temos {moeda.moeda(moeda.diminuir(p, 13))}')