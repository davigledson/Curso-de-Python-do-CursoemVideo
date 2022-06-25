n1=float(input('qual é o preço do seu produto?'))
a=(n1*5/100)
a2=(n1-a)

b=(n1*10/100)
b2=(n1-b)


s=print(f'com o cupom de 5%, você tera um desconto de R${a:.2f}')
s2=print(f'ficando com o valor de R${a2:.2f}\n')

f=print(f'com o cupom de 10%, você tera um desconto de R${b:.2f}')
print(f'ficando com um valor de R${b2:.2f}\n')

#outra forma de fazer

c=n1-(n1*5/100)
print(f'na promoção de 5% de desconto, seu produto vai custa R${c}')