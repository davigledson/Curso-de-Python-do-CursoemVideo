teste=list()
teste.append('davi')
teste.append(19)
print(teste)

galera=list()
galera.append(teste[:])
teste[0]='maria'
teste[1]=22
galera.append(teste[:])
print(galera)