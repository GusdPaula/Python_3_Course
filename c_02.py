# Try and except
'''
numero = input('Digite um número: ')
try:
    numero_float = float(numero)
    print(f'O dobro de {numero} é {numero_float *  2}')
except:
    print('Isso não é um número.')

# As constante devem ser escritas com letras maiúsculas
# Devem ser evitadas várias condições no mesmo if
# O código precisa ser simples e legível

# While/ Else

string = 'Valor qualquer'

i = 0

while i < len(string):
    letra = string[i]

    print(letra)
    i += 1
else: # Se eu comando break for utilizado dentro do while, o else não é acionado
    print('Pronto')

'''

frase = 'O Python é uma linguagem de programação' \
        'multiparadigna.' \
        'Python foi criado por Guido Van Rossun'

print(frase.count('Python'))

i = 0 
maior_quant = 0
maior_letra = ''
while i < len(frase):
    letra_atual = frase[i]
    quantas_vezez_letra_apareceu = frase.count(letra_atual)

    if quantas_vezez_letra_apareceu > maior_quant and letra_atual != ' ':
        maior_quant = quantas_vezez_letra_apareceu
        maior_letra = letra_atual

    i += 1

print(f'A letra que mais apareceu foi {maior_letra}, pois apareceu {maior_quant}')