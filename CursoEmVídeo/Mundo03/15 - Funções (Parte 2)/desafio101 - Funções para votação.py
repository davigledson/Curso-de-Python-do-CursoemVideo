def voto(ano):
    import datetime
    hoje = datetime.date.today().year
    s=hoje - ano
    if s>=18 and s<65:
         return 'VOTO OBRIGATORIO'
    if s>=16 or s>=65:
        return 'VOTO OPCIONAL'
    if s<16:
        return 'NÃO VOTA'




print('-'*40)
resp=int(input('Em que ano voce nasceu?'))
resultado=voto(resp)
print(resultado)
print('-'*40)
print(voto(resp))

print('-'*40)
voto(resp)

print('-'*40)
import datetime

print(f'com {datetime.date.today().year - resp} anos: {voto(resp)}')