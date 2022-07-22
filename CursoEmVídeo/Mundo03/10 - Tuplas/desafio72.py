lista='zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onde','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte'

num=int(input('Digite um numero entre 0 e 20:'))
while True:
    num=int(input('ERRO! Digite um numero entre 0 e 20:'))



    if  num <=20 and num>=0:
        break
print(f'Você digitou o numero {lista[num]}')