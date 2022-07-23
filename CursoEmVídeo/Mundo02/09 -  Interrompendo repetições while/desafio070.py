soma = p1000 = quant = menor = 0
qcont='nada'
barato=''
while True:

    nome = input('Digite o nome do produto:')
    preco = float(input('Digite o preço do produto:R$'))

    qcont=' '
    while qcont not in 'SsNn':
       qcont = input('Quer Continuar? [S/N]:').lower().strip()[0]

    soma += preco
    quant += 1


    if preco >= 1000:
        p1000 += 1

    if quant==1:
        menor=preco

    if quant==1 or preco<menor:
        menor=preco
        barato=nome

    if qcont == 'n':
        break
print(f'Total de gastos = R${soma:.2f}')
print(f'Produtos com mais de mil reais = {p1000}')
print(f'Produto mais barato = {barato} custando R${menor}')
print('FIM DO PROGRAMA')