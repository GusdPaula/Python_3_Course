# Nonlocal and freevars

def fora(x):
    a = x

    def dentro():
        # Here you will be able to see that a is a freevar
        #print(dentro.__code__.co_freevars)

        return a

    return dentro

dentro1 = fora(10)

#print(dentro1())


def concatenar(string_inicial):
    valor_final = string_inicial

    def inter(valor_a_concatenar=''):
        # Now we will be able to modify this variable 
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    
    return inter

c = concatenar('a')
#print(c('b'))

################################################################


