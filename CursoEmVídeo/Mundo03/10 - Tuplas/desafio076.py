trupa=('Lapis',1.75,'Borracha',2,'Caderno',15.90,
       'Estojo',25,'Transferidor',4.20,'Compasso',9.99,'Mochila'
       ,120.32,'Canetas',22.30,'Livro',34.90)
print('-'*15,'LISTAGEM DE PREÇO','-'*15)
for pos in range(0,len(trupa),2):
    print(f'{trupa[pos]:.<30}...........R$ {trupa[pos+1]}')
print('-'*50)






