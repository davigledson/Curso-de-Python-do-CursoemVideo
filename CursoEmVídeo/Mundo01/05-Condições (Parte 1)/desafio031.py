n1=float(input('\033[4;33m qual a distância da viagem que o senhor deseja:'))
pre1=n1*0.50
pre2=n1*0.45
if n1<=200:
    print('por cada quilômetro será cobrado R$0.50 até 200Km')
    print(f'sua viagem custará R${pre1}')

else:
    print('para viagem maior que 200Km será cobrado R$0.45 por quilômetro')
    print(f'sua viagem custará R${pre2}')
