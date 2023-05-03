# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]


first_list = ['Salvador', 'Ubatuba', 'Belo Horizonte']
second_list = ['BA', 'SP', 'MG', 'RJ']
or_result = [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper(list_1, list_2):
    '''
        Join two lists into one.
    
    '''

    result = []
    count = 0

    if len(list_1) < len(list_2):
        count = len(list_1)
    else:
        count = len(list_2)
    
    for i in range(count):
        one_tuple = (list_1[i], list_2[i])
        result.append(one_tuple)
    
    return result


result = zipper(first_list, second_list)
print(result)
print()
print(result == or_result)