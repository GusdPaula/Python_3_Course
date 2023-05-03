# Manipulando funções


'''
x = 1


def escopo():
    global x # Isso faz com que editemos a variável fora da função
    x = 10   # Porém é uma má prática... deixa o código confuso

    print(x)

    def outro_escopo():
        global x
        x = 11

        print(x)

    outro_escopo()


print(x)
escopo()
print(x)

'''

# CLOSURE E FUNÇÕES QUE RETORNAM OUTRA FUNÇÃO

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar # Não colocamos o parênteses aqui, isso faz com que o python salve o escopo

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

print(falar_boa_noite('Joao')) # Closure é este fechamento que permite a função ser executada
print(falar_bom_dia('Joao'))

for nome in ['Maria', 'Carlos', 'Yasmim', 'Anna']:
    print(falar_bom_dia(nome))
    
