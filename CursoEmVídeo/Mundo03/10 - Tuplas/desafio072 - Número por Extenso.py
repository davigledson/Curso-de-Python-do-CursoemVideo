lista='zero','um','dois','tres','quatro','cinco',\
      'seis','sete','oito','nove','dez',\
      'onde','doze','treze','quatorze','quinze'\
    ,'dezesseis','dezessete','dezoito','dezenove','vinte'

num=' '
while True:
    num=int(input('Digite um numero entre 0 e 20:'))

    if  0<=num<=20:
        break
    print('Tente novamente! ' ,end='')
print(f'Você digitou o numero {lista[num]}')