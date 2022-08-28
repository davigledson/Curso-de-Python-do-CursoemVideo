n1=float(input('quanto dinheiro você tem na carteira?'))
a=(n1/5.55)
print(f'com R${n1} você pode comprar US {a:.2f}')

#convertido em Euro:
print(f'com R${n1} você pode comprar EUR {n1/6.64:.2f}')

#convertido em iene japonês
print(f'com R$ {n1} você pode comprar JPY {n1/0.051:.2f}')

#de real par dolár
print(f'com {n1}R$ você pode compra US{n1*0.18}')