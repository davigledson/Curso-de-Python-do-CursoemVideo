#escreva um programa que converta uma temperatura em °C para °F
n1=float(input('digite a temperatura em °c:'))

#de celsios para fahrenheit
a=(n1*9)/5+32
print(f' a temperatura de {n1}°C convertida em °F, ficará {a:.1f}°F')

# de fahrenheit para celsius
n2=float(input('digite a temperatura em °F :'))
b=(n2-32)*5/9

print(f'a temperatura de {n2}°f convertida em celsius, ficará {b:.1f}°C')



