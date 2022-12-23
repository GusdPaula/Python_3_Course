# Funções

def multiplicacao(*args):

    total = 1

    for n in args:
        total *= n

    return total

def par_impar(valor):

    if valor % 2 == 0:
        return 'Valor é par.'

    else:
        return 'Valor é ímpar'


valor_final = multiplicacao(9, 3, 3)
print(f'O valor da multiplicação é: {valor_final}')
print(par_impar(valor_final))
