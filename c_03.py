# Limpando o terminal
import os

print('test')
g = input('Quer limpar?')

os.system('cls')

# Ex
lista = ['Maria', 'Helena', 'Luiz']
i = 0
for nome in lista:
    print(f'O nome é {nome} e o índice é {i}')
    i += 1

# Podemos pegar o resto da lista se queremos apenas um valor dela
nome1, *resto = ['Maria', 'Helena', 'Luiz'] # basta adicionar um * na frente da variável
nome1, *_ = ['Maria', 'Helena', 'Luiz']