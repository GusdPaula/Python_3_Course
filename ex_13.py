# Exercício - Adiando execução de funções
# This is called closure
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    

    return interna


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

soma_final = soma_com_cinco(2)
multiplica_final = multiplica_por_dez(30)
print(multiplica_final)