expr=input('Digite a expressão:')
pilha=[]
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb ==')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
print(pilha)
if len(pilha) == 0:
    print('Sua expressão está valida!')
else:
    print('Sua expressaão está invalida!')