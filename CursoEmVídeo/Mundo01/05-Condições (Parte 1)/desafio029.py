n1=float(input(' Digite a velocidade do seu carro:'))
#('Se você ultrapassa velocidade de 80 km por hora  receberá \n '
      #'uma multa de R$7.00 por cada quilometro acima do limite ultrapassado')

if n1> 80:
    print('-=-'*20)
    print('\033[31m MULTADO! você ultrapassou o limite de velocidade de 80km/h')
    print('-=-'*20)
    a= (n1 -80) *7
    print('por cada quilometro acima do limite de velocidade será cobrado R$7.00')
    print(f'Sua multa será de R${a:.2f}')
else:  print('\033[32m Tenha um bom dia! Dirija com segurança!')
