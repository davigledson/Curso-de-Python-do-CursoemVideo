ida=float(input('Digite sua idade:'))
if ida<=8:
    print(f'sua categoria será PRÉ-MIRIM')
if 8<ida<=11:
    print(f'sua categoria será MIRIM')
if 11<ida<=14:
    print(f'sua categoria será INFANTIL')
if 14<ida<=17:
    print(f'sua categoria será JUVENIL')
if 17<ida>=18:
    print(f'sua categoria será ADULTO')