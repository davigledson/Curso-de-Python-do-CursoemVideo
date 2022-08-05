galera=list()
dado=list()

mai=men=0

for c in range(0,3):
    dado.append(input('nome:'))
    dado.append(int(input('idade:')))
    galera.append(dado[:]) #[:]CLIAR UMA COPIA DOS DADOS
    dado.clear()# EXCLUIR
print(galera)

for p in galera:
    if p[1]>21:
        print(f'{p[0]} é maior de idade!')
        mai+=1
    else:
        print(f'{p[0]} é menor de idade!')
        men+=1

print(f'total de maiores: {mai}')
print(f'total de menores: {men}')
