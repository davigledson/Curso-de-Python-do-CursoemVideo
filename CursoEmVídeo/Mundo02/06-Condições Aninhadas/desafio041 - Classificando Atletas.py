ida=int(input('Digite sua idade:'))
if ida <=9:
    print('você se encaixar  na categoria MIRIM ')
elif 14>=ida>9:
    print('você encaixar na categoria INFANTIL')
elif 19>=ida>14:
    print('você se encaixar na categoria JUNIOR')
elif 20>=ida>19:
    print('você se encaixar na categoria SÊNIOR')
elif ida>20:
    print('você se encaixar na categoria MASTER')
