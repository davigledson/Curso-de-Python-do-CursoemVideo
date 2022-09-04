# from uteis import fatorial,dobro # pode ter imcompatibilidades com python ao importar assim,
# caso em seu programa tenha que importa muitas bibliotecas
import uteis

n=int(input('Digite um valor:'))

fat=uteis.fatorial(n)
print(f'o fatorial de {n} é {fat}')

print(uteis.dobro(n))