km=float(input('qual a quantidade de quilômetros percorrido?'))
dias=float(input('qual a quantidade de dias pelo quais ele foi alugado?'))

s = km * 0.15 + dias * 60
print(f'o valor total a pagar e de R${s}')