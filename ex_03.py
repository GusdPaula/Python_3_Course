nome = input('Qual o seu nome? ')

len_nome = len(nome)
indice = 0
new_nome = ''
letra = ''

while len_nome > indice:
    letra = nome[indice]
    new_nome += f'{letra}*'
    indice += 1

print(f'Pronto, {new_nome}')
