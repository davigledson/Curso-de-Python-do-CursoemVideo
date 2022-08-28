print('Gerador de PA')
print('='*20)

primeiro = int(input('Digite o 1° termo:'))
razao = int(input('Digite a Razão:'))
termo = primeiro
cont = 1
print(f'1° termo = {primeiro}')
while cont <= 9:
    termo += razao
    cont += 1

    print(f'{cont}° termo = {termo}')
